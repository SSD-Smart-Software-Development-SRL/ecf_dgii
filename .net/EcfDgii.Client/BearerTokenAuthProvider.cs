using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Kiota.Abstractions;
using Microsoft.Kiota.Abstractions.Authentication;

namespace EcfDgii.Client
{
    /// <summary>
    /// A simple authentication provider that attaches a static JWT Bearer token.
    /// </summary>
    internal sealed class BearerTokenAuthProvider : IAuthenticationProvider
    {
        private readonly string _token;

        public BearerTokenAuthProvider(string token)
        {
            _token = token ?? throw new ArgumentNullException(nameof(token));
        }

        public Task AuthenticateRequestAsync(
            RequestInformation request,
            Dictionary<string, object>? additionalAuthenticationContext = null,
            CancellationToken cancellationToken = default)
        {
            request.Headers.Add("Authorization", $"Bearer {_token}");
            return Task.CompletedTask;
        }
    }
}
