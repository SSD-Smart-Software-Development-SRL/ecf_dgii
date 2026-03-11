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
    /// and a simplified send-and-poll workflow via <see cref="SendEcfAsync"/>.
    /// </summary>
    public class EcfClient
    {
        private static readonly Dictionary<string, string> EnvironmentUrls = new Dictionary<string, string>
        {
            ["Test"] = "https://api.test.ecfx.ssd.com.do",
            ["Cert"] = "https://api.cert.ecfx.ssd.com.do",
            ["Prod"] = "https://api.prod.ecfx.ssd.com.do",
        };

        private static readonly Dictionary<TipoeCFType, string> EcfTypeRouteMap = new Dictionary<TipoeCFType, string>
        {
            [TipoeCFType.FacturaDeCreditoFiscalElectronica] = "31",
            [TipoeCFType.FacturaDeConsumoElectronica] = "32",
            [TipoeCFType.NotaDeDebitoElectronica] = "33",
            [TipoeCFType.NotaDeCreditoElectronica] = "34",
            [TipoeCFType.ComprasElectronico] = "41",
            [TipoeCFType.GastosMenoresElectronico] = "43",
            [TipoeCFType.RegimenesEspecialesElectronico] = "44",
            [TipoeCFType.GubernamentalElectronico] = "45",
            [TipoeCFType.ComprobanteDeExportacionesElectronico] = "46",
            [TipoeCFType.ComprobanteParaPagosAlExteriorElectronico] = "47",
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

        // ---------------------------------------------------------------------------
        // ECF send + poll
        // ---------------------------------------------------------------------------

        /// <summary>
        /// Send an ECF and poll until processing completes.
        /// Automatically routes to the correct endpoint based on <c>ecf.Encabezado.IdDoc.TipoeCF</c>,
        /// then polls the status endpoint until progress is <c>Finished</c> or <c>Error</c>.
        /// </summary>
        /// <param name="ecf">The ECF document to send.</param>
        /// <param name="pollingOptions">Optional polling configuration.</param>
        /// <param name="cancellationToken">Cancellation token.</param>
        /// <returns>The final <see cref="EcfResponse"/> with a Finished status.</returns>
        /// <exception cref="EcfException">When the ECF processing finishes with an Error status.</exception>
        public async Task<EcfResponse> SendEcfAsync(
            ECF ecf,
            PollingOptions? pollingOptions = null,
            CancellationToken cancellationToken = default)
        {
            var tipoeCF = ecf.Encabezado?.IdDoc?.TipoeCF
                ?? throw new ArgumentException("ECF must have Encabezado.IdDoc.TipoeCF");

            string? route;
            if (!EcfTypeRouteMap.TryGetValue(tipoeCF, out route))
                throw new ArgumentException($"Unknown TipoeCF: {tipoeCF}");

            var rnc = ecf.Encabezado?.Emisor?.RncEmisor
                ?? throw new ArgumentException("ECF must have Encabezado.Emisor.RncEmisor");

            var encf = ecf.Encabezado?.IdDoc?.Encf
                ?? throw new ArgumentException("ECF must have Encabezado.IdDoc.Encf");

            // POST to the typed endpoint
            var postResponse = await PostEcfByRouteAsync(route, ecf, cancellationToken).ConfigureAwait(false);

            if (postResponse?.MessageId == null)
                throw new InvalidOperationException("ECF submission did not return a message ID.");

            // Poll until complete
            var result = await PollingHelper.PollUntilCompleteAsync(
                async () =>
                {
                    var responses = await Api.Ecf[rnc][encf].GetAsync(cancellationToken: cancellationToken).ConfigureAwait(false);
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

        private async Task<EcfResponse?> PostEcfByRouteAsync(string route, ECF ecf, CancellationToken cancellationToken)
        {
            switch (route)
            {
                case "31": return await Api.Ecf.ThreeOne.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "32": return await Api.Ecf.ThreeTwo.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "33": return await Api.Ecf.ThreeThree.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "34": return await Api.Ecf.ThreeFour.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "41": return await Api.Ecf.FourOne.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "43": return await Api.Ecf.FourThree.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "44": return await Api.Ecf.FourFour.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "45": return await Api.Ecf.FourFive.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "46": return await Api.Ecf.FourSix.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                case "47": return await Api.Ecf.FourSeven.PostAsync(ecf, cancellationToken: cancellationToken).ConfigureAwait(false);
                default: throw new ArgumentException($"Unsupported ECF route: {route}");
            }
        }
    }
}
