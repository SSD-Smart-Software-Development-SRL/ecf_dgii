using System;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Caching.Distributed;

namespace EcfDgii.Client
{
    /// <summary>
    /// HTTP delegating handler that handles token retrieval, caching, and 401 retries.
    /// </summary>
    internal sealed class TokenAuthHandler : DelegatingHandler
    {
        private readonly Func<Task<string>> _getToken;
        private readonly IDistributedCache _cache;
        private readonly string _cacheKey = "ecf_dgii_token";
        private readonly SemaphoreSlim _semaphore = new SemaphoreSlim(1, 1);

        public TokenAuthHandler(Func<Task<string>> getToken, IDistributedCache cache)
            : base(new HttpClientHandler())
        {
            _getToken = getToken ?? throw new ArgumentNullException(nameof(getToken));
            _cache = cache ?? throw new ArgumentNullException(nameof(cache));
        }

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var token = await GetOrRefreshTokenAsync(forceRefresh: false).ConfigureAwait(false);
            request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);

            var response = await base.SendAsync(request, cancellationToken).ConfigureAwait(false);

            if (response.StatusCode == HttpStatusCode.Unauthorized)
            {
                token = await GetOrRefreshTokenAsync(forceRefresh: true).ConfigureAwait(false);
                
                // Clone the request for retry
                using var retryRequest = await CloneRequestAsync(request).ConfigureAwait(false);
                retryRequest.Headers.Authorization = new AuthenticationHeaderValue("Bearer", token);

                response.Dispose();
                response = await base.SendAsync(retryRequest, cancellationToken).ConfigureAwait(false);
            }

            return response;
        }

        private async Task<string> GetOrRefreshTokenAsync(bool forceRefresh)
        {
            if (!forceRefresh)
            {
                var cachedToken = await _cache.GetStringAsync(_cacheKey).ConfigureAwait(false);
                if (!string.IsNullOrEmpty(cachedToken))
                    return cachedToken!;
            }

            await _semaphore.WaitAsync().ConfigureAwait(false);
            try
            {
                // Double-check after acquiring lock
                if (!forceRefresh)
                {
                    var cachedToken = await _cache.GetStringAsync(_cacheKey).ConfigureAwait(false);
                    if (!string.IsNullOrEmpty(cachedToken))
                        return cachedToken!;
                }

                var newToken = await _getToken().ConfigureAwait(false);
                await _cache.SetStringAsync(_cacheKey, newToken, new DistributedCacheEntryOptions
                {
                    AbsoluteExpirationRelativeToNow = TimeSpan.FromHours(1) // Default buffer
                }).ConfigureAwait(false);

                return newToken;
            }
            finally
            {
                _semaphore.Release();
            }
        }

        private static async Task<HttpRequestMessage> CloneRequestAsync(HttpRequestMessage original)
        {
            var clone = new HttpRequestMessage(original.Method, original.RequestUri);

            if (original.Content != null)
            {
                var content = await original.Content.ReadAsByteArrayAsync().ConfigureAwait(false);
                clone.Content = new ByteArrayContent(content);
                if (original.Content.Headers.ContentType != null)
                    clone.Content.Headers.ContentType = original.Content.Headers.ContentType;
            }

            foreach (var header in original.Headers)
                clone.Headers.TryAddWithoutValidation(header.Key, header.Value);

            return clone;
        }
    }
}
