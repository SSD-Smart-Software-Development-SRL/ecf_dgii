using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using EcfDgii.Client.Generated;
using EcfDgii.Client.Generated.Models;
using Microsoft.Kiota.Http.HttpClientLibrary;

namespace EcfDgii.Client
{
    /// <summary>
    /// High-level client for the ECF DGII API.
    /// Provides both raw Kiota-generated endpoint access via <see cref="Api"/>
    /// and a simplified send-and-poll workflow via the typed <c>SendEcfAsync</c> overloads
    /// (one per e-CF type: 31, 32, 33, 34, 41, 43, 44, 45, 46, 47).
    /// </summary>
    public class EcfClient
    {
        private static readonly Dictionary<string, string> EnvironmentUrls = new Dictionary<string, string>
        {
            ["Test"] = "https://api.test.ecfx.ssd.com.do",
            ["Cert"] = "https://api.cert.ecfx.ssd.com.do",
            ["Prod"] = "https://api.prod.ecfx.ssd.com.do",
        };

        /// <summary>
        /// The underlying Kiota-generated API client for direct endpoint access.
        /// Use this for any raw API calls not covered by the high-level methods.
        /// </summary>
        public EcfApiClient Api { get; }

        /// <summary>
        /// Creates a new <see cref="EcfClient"/> with the specified options.
        /// </summary>
        public EcfClient(EcfClientOptions? options = null)
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

            Api = new EcfApiClient(adapter);
        }

        /// <summary>
        /// Creates a restricted, read-only <see cref="EcfFrontendClient"/> for frontend use.
        /// The returned client only exposes GET endpoints — no mutations.
        /// Uses callback-based token management with automatic 401 retry.
        /// </summary>
        /// <param name="options">Frontend client configuration with token callbacks.</param>
        /// <returns>A new <see cref="EcfFrontendClient"/> instance.</returns>
        public static EcfFrontendClient CreateFrontendClient(EcfFrontendClientOptions options)
        {
            return new EcfFrontendClient(options);
        }

        // ---------------------------------------------------------------------------
        // ECF send + poll — typed overloads, one per ECF type
        // ---------------------------------------------------------------------------

        /// <summary>Send a Factura de Crédito Fiscal Electrónica (e-CF 31) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf31ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.ThreeOne.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Factura de Consumo Electrónica (e-CF 32) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf32ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.ThreeTwo.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Nota de Débito Electrónica (e-CF 33) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf33ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.ThreeThree.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Nota de Crédito Electrónica (e-CF 34) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf34ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.ThreeFour.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Compras Electrónico (e-CF 41) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf41ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.FourOne.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Gastos Menores Electrónico (e-CF 43) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf43ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.FourThree.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Regímenes Especiales Electrónico (e-CF 44) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf44ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.FourFour.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Gubernamental Electrónico (e-CF 45) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf45ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.FourFive.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Comprobante de Exportaciones Electrónico (e-CF 46) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf46ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.FourSix.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        /// <summary>Send a Comprobante para Pagos al Exterior Electrónico (e-CF 47) and poll until completion.</summary>
        public Task<EcfResponse> SendEcfAsync(Ecf47ECF ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default)
            => SendInternalAsync(
                ecf.Encabezado?.Emisor?.RncEmisor,
                ecf.Encabezado?.IdDoc?.Encf,
                ct => Api.Ecf.FourSeven.PostAsync(ecf, cancellationToken: ct),
                pollingOptions,
                cancellationToken);

        private async Task<EcfResponse> SendInternalAsync(
            string? rnc,
            string? encf,
            Func<CancellationToken, Task<EcfResponse?>> postCall,
            PollingOptions? pollingOptions,
            CancellationToken cancellationToken)
        {
            if (string.IsNullOrWhiteSpace(rnc))
                throw new ArgumentException("ECF must have Encabezado.Emisor.RncEmisor");
            if (string.IsNullOrWhiteSpace(encf))
                throw new ArgumentException("ECF must have Encabezado.IdDoc.Encf");

            var postResponse = await postCall(cancellationToken).ConfigureAwait(false);

            if (postResponse?.MessageId == null)
                throw new InvalidOperationException("ECF submission did not return a message ID.");

            var result = await PollingHelper.PollUntilCompleteAsync(
                async () =>
                {
                    var responses = await Api.Ecf[rnc!][encf!].GetAsync(cancellationToken: cancellationToken).ConfigureAwait(false);
                    if (responses == null || responses.Count == 0)
                        throw new InvalidOperationException("No ECF response found for the given rnc/encf.");

                    return responses.FirstOrDefault(r => r.MessageId == postResponse.MessageId) ?? responses[0];
                },
                r => r.Progress == EcfProgress.Finished || r.Progress == EcfProgress.Error,
                pollingOptions,
                cancellationToken
            ).ConfigureAwait(false);

            if (result.Progress == EcfProgress.Error)
            {
                var message = result.Errors ?? result.Mensaje ?? "ECF processing failed";
                throw new EcfException(message, result);
            }

            return result;
        }
    }
}
