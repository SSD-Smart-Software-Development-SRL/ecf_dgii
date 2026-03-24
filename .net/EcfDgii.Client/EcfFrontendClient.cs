using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using EcfDgii.Client.Generated;
using EcfDgii.Client.Generated.Models;
using Microsoft.Kiota.Abstractions;
using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Http.HttpClientLibrary;

namespace EcfDgii.Client
{
    /// <summary>
    /// Configuration options for <see cref="EcfFrontendClient"/>.
    /// Uses callback-based token management instead of a static API key.
    /// </summary>
    public class EcfFrontendClientOptions
    {
        /// <summary>
        /// REQUIRED. Callback to fetch a fresh token (e.g. calls your backend's /ecf-token endpoint).
        /// </summary>
        public Func<Task<string>> GetToken { get; set; } = null!;

        /// <summary>
        /// OPTIONAL. Callback to store a token in cache.
        /// Default: encrypts and writes to a file on disk using AES with an auto-generated key.
        /// </summary>
        public Func<string, Task>? CacheToken { get; set; }

        /// <summary>
        /// OPTIONAL. Callback to read a cached token.
        /// Default: reads from the encrypted file on disk.
        /// </summary>
        public Func<Task<string?>>? GetCachedToken { get; set; }

        /// <summary>
        /// Base URL override. Takes precedence over <see cref="Environment"/>.
        /// </summary>
        public string? BaseUrl { get; set; }

        /// <summary>
        /// Target environment. Defaults to <see cref="EcfEnvironment.Test"/>.
        /// </summary>
        public EcfEnvironment Environment { get; set; } = EcfEnvironment.Test;
    }

    /// <summary>
    /// A restricted, read-only client for frontend use.
    /// Only exposes GET endpoints — no mutations, no raw API access.
    /// Uses callback-based token management with automatic 401 retry.
    /// </summary>
    public class EcfFrontendClient
    {
        private static readonly Dictionary<string, string> EnvironmentUrls = new Dictionary<string, string>
        {
            ["Test"] = "https://api.test.ecfx.ssd.com.do",
            ["Cert"] = "https://api.cert.ecfx.ssd.com.do",
            ["Prod"] = "https://api.prod.ecfx.ssd.com.do",
        };

        private readonly EcfApiClient _api;
        private readonly TokenManager _tokenManager;

        /// <summary>
        /// Creates a new <see cref="EcfFrontendClient"/> with callback-based token management.
        /// </summary>
        public EcfFrontendClient(EcfFrontendClientOptions options)
        {
            if (options.GetToken == null)
                throw new ArgumentNullException(nameof(options), "GetToken callback is required.");

            var baseUrl = options.BaseUrl
                ?? System.Environment.GetEnvironmentVariable("ECF_API_URL")
                ?? EnvironmentUrls[options.Environment.ToString()];

            _tokenManager = new TokenManager(
                options.GetToken,
                options.CacheToken ?? DefaultFileCache.CacheToken,
                options.GetCachedToken ?? DefaultFileCache.GetCachedToken);

            var authHandler = new TokenAuthHandler(_tokenManager);
            var httpClient = new HttpClient(authHandler);

            var authProvider = new DynamicTokenAuthProvider(_tokenManager);
            var adapter = new HttpClientRequestAdapter(authProvider, httpClient: httpClient)
            {
                BaseUrl = baseUrl
            };

            _api = new EcfApiClient(adapter);
        }

        // ---------------------------------------------------------------------------
        // ECF queries
        // ---------------------------------------------------------------------------

        /// <summary>
        /// Query ECF responses by RNC and eNCF.
        /// Maps to GET /ecf/{rnc}/{encf}.
        /// </summary>
        /// <param name="rnc">The company RNC.</param>
        /// <param name="encf">The electronic fiscal receipt number.</param>
        /// <param name="includeEcfContent">Whether to include the full ECF content in the response.</param>
        /// <param name="cancellationToken">Cancellation token.</param>
        /// <returns>A list of matching <see cref="EcfResponse"/> objects.</returns>
        public async Task<List<EcfResponse>?> QueryEcfAsync(
            string rnc,
            string encf,
            bool? includeEcfContent = null,
            CancellationToken cancellationToken = default)
        {
            return await _api.Ecf[rnc][encf].GetAsync(
                requestConfiguration =>
                {
                    if (includeEcfContent.HasValue)
                    {
                        requestConfiguration.QueryParameters.IncludeEcfContent = includeEcfContent.Value;
                    }
                },
                cancellationToken).ConfigureAwait(false);
        }

        /// <summary>
        /// Search ECF responses by RNC with optional filters.
        /// Maps to GET /ecf/{rnc}.
        /// </summary>
        /// <param name="rnc">The company RNC.</param>
        /// <param name="page">Page number for pagination.</param>
        /// <param name="limit">Number of results per page.</param>
        /// <param name="fromFechaEmision">Filter by emission date (from).</param>
        /// <param name="toFechaEmision">Filter by emission date (to).</param>
        /// <param name="amountFrom">Filter by minimum amount.</param>
        /// <param name="amountTo">Filter by maximum amount.</param>
        /// <param name="includeEcfContent">Whether to include the full ECF content in the response.</param>
        /// <param name="cancellationToken">Cancellation token.</param>
        /// <returns>A paginated result of <see cref="EcfResponse"/> objects.</returns>
        public async Task<PaginatedApiResultOfEcfResponse?> SearchEcfsAsync(
            string rnc,
            string? page = null,
            string? limit = null,
            DateTimeOffset? fromFechaEmision = null,
            DateTimeOffset? toFechaEmision = null,
            string? amountFrom = null,
            string? amountTo = null,
            bool? includeEcfContent = null,
            CancellationToken cancellationToken = default)
        {
            return await _api.Ecf[rnc].GetAsync(
                requestConfiguration =>
                {
                    requestConfiguration.QueryParameters.Page = page;
                    requestConfiguration.QueryParameters.Limit = limit;
                    requestConfiguration.QueryParameters.FromFechaEmision = fromFechaEmision;
                    requestConfiguration.QueryParameters.ToFechaEmision = toFechaEmision;
                    requestConfiguration.QueryParameters.AmountFrom = amountFrom;
                    requestConfiguration.QueryParameters.AmountTo = amountTo;
                    requestConfiguration.QueryParameters.IncludeEcfContent = includeEcfContent;
                },
                cancellationToken).ConfigureAwait(false);
        }

        /// <summary>
        /// Get an ECF by its message ID.
        /// Maps to GET /ecf/{rnc}/message/{id}.
        /// </summary>
        /// <param name="rnc">The company RNC.</param>
        /// <param name="id">The message ID (GUID).</param>
        /// <param name="includeEcfContent">Whether to include the full ECF content in the response.</param>
        /// <param name="cancellationToken">Cancellation token.</param>
        /// <returns>A list of matching <see cref="EcfResponse"/> objects.</returns>
        public async Task<List<EcfResponse>?> GetEcfByIdAsync(
            string rnc,
            Guid id,
            bool? includeEcfContent = null,
            CancellationToken cancellationToken = default)
        {
            return await _api.Ecf[rnc].Message[id].GetAsync(
                requestConfiguration =>
                {
                    if (includeEcfContent.HasValue)
                    {
                        requestConfiguration.QueryParameters.IncludeEcfContent = includeEcfContent.Value;
                    }
                },
                cancellationToken).ConfigureAwait(false);
        }

        // ---------------------------------------------------------------------------
        // Company queries
        // ---------------------------------------------------------------------------

        /// <summary>
        /// Get all companies with optional filters.
        /// Maps to GET /company.
        /// </summary>
        /// <param name="page">Page number for pagination.</param>
        /// <param name="limit">Number of results per page.</param>
        /// <param name="rncs">Filter by specific RNCs.</param>
        /// <param name="names">Filter by company names.</param>
        /// <param name="cancellationToken">Cancellation token.</param>
        /// <returns>A paginated result of <see cref="CompanyResponse"/> objects.</returns>
        public async Task<PaginatedApiResultOfCompanyResponse?> GetCompaniesAsync(
            string? page = null,
            string? limit = null,
            string[]? rncs = null,
            string[]? names = null,
            CancellationToken cancellationToken = default)
        {
            return await _api.Company.GetAsync(
                requestConfiguration =>
                {
                    requestConfiguration.QueryParameters.Page = page;
                    requestConfiguration.QueryParameters.Limit = limit;
                    requestConfiguration.QueryParameters.Rncs = rncs;
                    requestConfiguration.QueryParameters.Names = names;
                },
                cancellationToken).ConfigureAwait(false);
        }

        /// <summary>
        /// Get a single company by its RNC.
        /// Maps to GET /company/{rnc}.
        /// </summary>
        /// <param name="rnc">The company RNC.</param>
        /// <param name="cancellationToken">Cancellation token.</param>
        /// <returns>The <see cref="CompanyResponse"/> for the given RNC.</returns>
        public async Task<CompanyResponse?> GetCompanyByRncAsync(
            string rnc,
            CancellationToken cancellationToken = default)
        {
            return await _api.Company[rnc].GetAsync(cancellationToken: cancellationToken).ConfigureAwait(false);
        }
    }

    // ---------------------------------------------------------------------------
    // Token management infrastructure
    // ---------------------------------------------------------------------------

    /// <summary>
    /// Manages token lifecycle: caching, retrieval, and refresh.
    /// </summary>
    internal sealed class TokenManager
    {
        private readonly Func<Task<string>> _getToken;
        private readonly Func<string, Task> _cacheToken;
        private readonly Func<Task<string?>> _getCachedToken;
        private readonly SemaphoreSlim _semaphore = new SemaphoreSlim(1, 1);

        public TokenManager(
            Func<Task<string>> getToken,
            Func<string, Task> cacheToken,
            Func<Task<string?>> getCachedToken)
        {
            _getToken = getToken;
            _cacheToken = cacheToken;
            _getCachedToken = getCachedToken;
        }

        /// <summary>
        /// Gets a valid token, using cache first. If no cached token, fetches a new one.
        /// </summary>
        public async Task<string> GetValidTokenAsync()
        {
            var cached = await _getCachedToken().ConfigureAwait(false);
            if (!string.IsNullOrEmpty(cached))
                return cached;

            return await RefreshTokenAsync().ConfigureAwait(false);
        }

        /// <summary>
        /// Forces a token refresh: calls GetToken and updates the cache.
        /// Thread-safe — only one refresh runs at a time.
        /// </summary>
        public async Task<string> RefreshTokenAsync()
        {
            await _semaphore.WaitAsync().ConfigureAwait(false);
            try
            {
                var token = await _getToken().ConfigureAwait(false);
                await _cacheToken(token).ConfigureAwait(false);
                return token;
            }
            finally
            {
                _semaphore.Release();
            }
        }
    }

    /// <summary>
    /// Kiota authentication provider that resolves the token dynamically via <see cref="TokenManager"/>.
    /// </summary>
    internal sealed class DynamicTokenAuthProvider : IAuthenticationProvider
    {
        private readonly TokenManager _tokenManager;

        public DynamicTokenAuthProvider(TokenManager tokenManager)
        {
            _tokenManager = tokenManager;
        }

        public async Task AuthenticateRequestAsync(
            RequestInformation request,
            Dictionary<string, object>? additionalAuthenticationContext = null,
            CancellationToken cancellationToken = default)
        {
            var token = await _tokenManager.GetValidTokenAsync().ConfigureAwait(false);
            request.Headers.Remove("Authorization");
            request.Headers.Add("Authorization", $"Bearer {token}");
        }
    }

    /// <summary>
    /// HTTP delegating handler that retries on 401 by refreshing the token.
    /// </summary>
    internal sealed class TokenAuthHandler : DelegatingHandler
    {
        private readonly TokenManager _tokenManager;

        public TokenAuthHandler(TokenManager tokenManager)
            : base(new HttpClientHandler())
        {
            _tokenManager = tokenManager;
        }

        protected override async Task<HttpResponseMessage> SendAsync(
            HttpRequestMessage request, CancellationToken cancellationToken)
        {
            var response = await base.SendAsync(request, cancellationToken).ConfigureAwait(false);

            if (response.StatusCode == HttpStatusCode.Unauthorized)
            {
                // Refresh the token
                var newToken = await _tokenManager.RefreshTokenAsync().ConfigureAwait(false);

                // Clone the request with the new token and retry
                using var retryRequest = await CloneRequestAsync(request).ConfigureAwait(false);
                retryRequest.Headers.Authorization =
                    new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", newToken);

                response.Dispose();
                response = await base.SendAsync(retryRequest, cancellationToken).ConfigureAwait(false);
            }

            return response;
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

    /// <summary>
    /// Default file-based token cache using AES encryption.
    /// Stores the encrypted token and a per-machine key in the user's local app data folder.
    /// </summary>
    internal static class DefaultFileCache
    {
        private static readonly string CacheDir = Path.Combine(
            System.Environment.GetFolderPath(System.Environment.SpecialFolder.LocalApplicationData),
            "EcfDgii");

        private static readonly string TokenPath = Path.Combine(CacheDir, ".ecf_token");
        private static readonly string KeyPath = Path.Combine(CacheDir, ".ecf_key");

        public static async Task CacheToken(string token)
        {
            Directory.CreateDirectory(CacheDir);

            byte[] key;
            byte[] iv;

            if (File.Exists(KeyPath))
            {
                var keyData = await ReadAllBytesAsync(KeyPath).ConfigureAwait(false);
                key = new byte[32];
                iv = new byte[16];
                Buffer.BlockCopy(keyData, 0, key, 0, 32);
                Buffer.BlockCopy(keyData, 32, iv, 0, 16);
            }
            else
            {
                key = new byte[32];
                iv = new byte[16];
                using (var rng = RandomNumberGenerator.Create())
                {
                    rng.GetBytes(key);
                    rng.GetBytes(iv);
                }
                var keyData = new byte[48];
                Buffer.BlockCopy(key, 0, keyData, 0, 32);
                Buffer.BlockCopy(iv, 0, keyData, 32, 16);
                await WriteAllBytesAsync(KeyPath, keyData).ConfigureAwait(false);
            }

            var plainBytes = Encoding.UTF8.GetBytes(token);
            byte[] encrypted;

            using (var aes = Aes.Create())
            {
                aes.Key = key;
                aes.IV = iv;
                using var encryptor = aes.CreateEncryptor();
                encrypted = encryptor.TransformFinalBlock(plainBytes, 0, plainBytes.Length);
            }

            await WriteAllBytesAsync(TokenPath, encrypted).ConfigureAwait(false);
        }

        public static async Task<string?> GetCachedToken()
        {
            if (!File.Exists(TokenPath) || !File.Exists(KeyPath))
                return null;

            try
            {
                var keyData = await ReadAllBytesAsync(KeyPath).ConfigureAwait(false);
                var key = new byte[32];
                var iv = new byte[16];
                Buffer.BlockCopy(keyData, 0, key, 0, 32);
                Buffer.BlockCopy(keyData, 32, iv, 0, 16);

                var encrypted = await ReadAllBytesAsync(TokenPath).ConfigureAwait(false);

                using var aes = Aes.Create();
                aes.Key = key;
                aes.IV = iv;
                using var decryptor = aes.CreateDecryptor();
                var plainBytes = decryptor.TransformFinalBlock(encrypted, 0, encrypted.Length);

                return Encoding.UTF8.GetString(plainBytes);
            }
            catch
            {
                // Corrupted cache — treat as missing
                return null;
            }
        }

        private static async Task<byte[]> ReadAllBytesAsync(string path)
        {
            using var fs = new FileStream(path, FileMode.Open, FileAccess.Read, FileShare.Read, 4096, useAsync: true);
            var bytes = new byte[fs.Length];
            await fs.ReadAsync(bytes, 0, bytes.Length).ConfigureAwait(false);
            return bytes;
        }

        private static async Task WriteAllBytesAsync(string path, byte[] data)
        {
            using var fs = new FileStream(path, FileMode.Create, FileAccess.Write, FileShare.None, 4096, useAsync: true);
            await fs.WriteAsync(data, 0, data.Length).ConfigureAwait(false);
        }
    }
}
