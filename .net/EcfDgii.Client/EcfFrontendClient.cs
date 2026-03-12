using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;
using EcfDgii.Client.Generated;
using EcfDgii.Client.Generated.Models;
using Microsoft.Kiota.Abstractions;
using Microsoft.Kiota.Http.HttpClientLibrary;

namespace EcfDgii.Client
{
    /// <summary>
    /// A restricted, read-only client for frontend use.
    /// Only exposes GET endpoints — no mutations, no raw API access.
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
        /// Creates a new <see cref="EcfFrontendClient"/> with the specified options.
        /// </summary>
        public EcfFrontendClient(EcfClientOptions? options = null)
        {
            var opts = options ?? new EcfClientOptions();

            var apiKey = opts.ApiKey
                ?? Environment.GetEnvironmentVariable("ECF_API_KEY")
                ?? throw new InvalidOperationException(
                    "API key is required. Set EcfClientOptions.ApiKey or the ECF_API_KEY environment variable.");

            var baseUrl = opts.BaseUrl
                ?? Environment.GetEnvironmentVariable("ECF_API_URL")
                ?? EnvironmentUrls[opts.Environment.ToString()];

            var authProvider = new BearerTokenAuthProvider(apiKey);
            var adapter = new HttpClientRequestAdapter(authProvider)
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
}
