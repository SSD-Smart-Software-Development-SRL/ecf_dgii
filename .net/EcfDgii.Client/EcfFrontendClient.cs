using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using EcfDgii.Client.Generated;
using EcfDgii.Client.Generated.Models;
using Microsoft.Extensions.Caching.Distributed;
using Microsoft.Kiota.Abstractions.Authentication;
using Microsoft.Kiota.Http.HttpClientLibrary;

namespace EcfDgii.Client
{
    /// <summary>
    /// Configuration options for <see cref="EcfFrontendClient"/>.
    /// Uses callback-based token management with IDistributedCache.
    /// </summary>
    public class EcfFrontendClientOptions
    {
        /// <summary>
        /// REQUIRED. Callback to fetch a fresh token (e.g. calls your backend's /ecf-token endpoint).
        /// </summary>
        public Func<Task<string>> GetToken { get; set; } = null!;

        /// <summary>
        /// REQUIRED. The distributed cache instance to store the token.
        /// </summary>
        public IDistributedCache Cache { get; set; } = null!;

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
    /// Uses callback-based token management with automatic 401 retry via IDistributedCache.
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

        /// <summary>
        /// Creates a new <see cref="EcfFrontendClient"/> with callback-based token management.
        /// </summary>
        public EcfFrontendClient(EcfFrontendClientOptions options)
        {
            if (options.GetToken == null)
                throw new ArgumentNullException(nameof(options), "GetToken callback is required.");
            if (options.Cache == null)
                throw new ArgumentNullException(nameof(options), "Cache (IDistributedCache) is required.");

            var baseUrl = options.BaseUrl
                ?? System.Environment.GetEnvironmentVariable("ECF_API_URL")
                ?? EnvironmentUrls[options.Environment.ToString()];

            var authHandler = new TokenAuthHandler(options.GetToken, options.Cache);
            var httpClient = new HttpClient(authHandler);

            // We use AnonymousAuthenticationProvider because TokenAuthHandler handles the Authorization header
            var authProvider = new AnonymousAuthenticationProvider();
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
        public Task<List<EcfResponse>?> QueryEcfAsync(
            string rnc,
            string encf,
            bool? includeEcfContent = null,
            CancellationToken cancellationToken = default)
        {
            return _api.Ecf[rnc][encf].GetAsync(
                config =>
                {
                    config.QueryParameters.IncludeEcfContent = includeEcfContent;
                },
                cancellationToken);
        }

        /// <summary>
        /// Search ECF responses by RNC with optional filters.
        /// Maps to GET /ecf/{rnc}.
        /// </summary>
        public Task<PaginatedApiResultOfEcfResponse?> SearchEcfsAsync(
            string rnc,
            string[]? encfs = null,
            Guid?[]? ids = null,
            AllTipoECFTypes[]? tiposEcfs = null,
            bool? includeEcfContent = null,
            DateTimeOffset? fromFechaEmision = null,
            DateTimeOffset? toFechaEmision = null,
            string? amountFrom = null,
            string? amountTo = null,
            string? page = null,
            string? limit = null,
            CancellationToken cancellationToken = default)
        {
            return _api.Ecf[rnc].GetAsync(
                config =>
                {
                    config.QueryParameters.Encfs = encfs;
                    config.QueryParameters.Ids = ids;
                    config.QueryParameters.TiposEcfsAsAllTipoECFTypes = tiposEcfs;
                    config.QueryParameters.IncludeEcfContent = includeEcfContent;
                    config.QueryParameters.FromFechaEmision = fromFechaEmision;
                    config.QueryParameters.ToFechaEmision = toFechaEmision;
                    config.QueryParameters.AmountFrom = amountFrom;
                    config.QueryParameters.AmountTo = amountTo;
                    config.QueryParameters.Page = page;
                    config.QueryParameters.Limit = limit;
                },
                cancellationToken);
        }

        /// <summary>
        /// Search all ECFs across all companies.
        /// Maps to GET /ecf.
        /// </summary>
        public Task<PaginatedApiResultOfEcfResponse?> SearchAllEcfsAsync(
            string[]? encfs = null,
            Guid?[]? ids = null,
            AllTipoECFTypes[]? tiposEcfs = null,
            bool? includeEcfContent = null,
            DateTimeOffset? fromFechaEmision = null,
            DateTimeOffset? toFechaEmision = null,
            string? amountFrom = null,
            string? amountTo = null,
            string? page = null,
            string? limit = null,
            CancellationToken cancellationToken = default)
        {
            return _api.Ecf.GetAsync(
                config =>
                {
                    config.QueryParameters.Encfs = encfs;
                    config.QueryParameters.Ids = ids;
                    config.QueryParameters.TiposEcfsAsAllTipoECFTypes = tiposEcfs;
                    config.QueryParameters.IncludeEcfContent = includeEcfContent;
                    config.QueryParameters.FromFechaEmision = fromFechaEmision;
                    config.QueryParameters.ToFechaEmision = toFechaEmision;
                    config.QueryParameters.AmountFrom = amountFrom;
                    config.QueryParameters.AmountTo = amountTo;
                    config.QueryParameters.Page = page;
                    config.QueryParameters.Limit = limit;
                },
                cancellationToken);
        }

        /// <summary>
        /// Get an ECF by its message ID.
        /// Maps to GET /ecf/{rnc}/message/{id}.
        /// </summary>
        public Task<List<EcfResponse>?> GetEcfByIdAsync(
            string rnc,
            Guid id,
            bool? includeEcfContent = null,
            CancellationToken cancellationToken = default)
        {
            return _api.Ecf[rnc].Message[id].GetAsync(
                config =>
                {
                    config.QueryParameters.IncludeEcfContent = includeEcfContent;
                },
                cancellationToken);
        }

        // ---------------------------------------------------------------------------
        // Company queries
        // ---------------------------------------------------------------------------

        /// <summary>
        /// Get all companies with optional filters.
        /// Maps to GET /company.
        /// </summary>
        public Task<PaginatedApiResultOfCompanyResponse?> GetCompaniesAsync(
            string[]? rncs = null,
            string[]? names = null,
            string? page = null,
            string? limit = null,
            CancellationToken cancellationToken = default)
        {
            return _api.Company.GetAsync(
                config =>
                {
                    config.QueryParameters.Rncs = rncs;
                    config.QueryParameters.Names = names;
                    config.QueryParameters.Page = page;
                    config.QueryParameters.Limit = limit;
                },
                cancellationToken);
        }

        /// <summary>
        /// Get a single company by its RNC.
        /// Maps to GET /company/{rnc}.
        /// </summary>
        public Task<CompanyResponse?> GetCompanyByRncAsync(
            string rnc,
            CancellationToken cancellationToken = default)
        {
            return _api.Company[rnc].GetAsync(cancellationToken: cancellationToken);
        }
    }
}
