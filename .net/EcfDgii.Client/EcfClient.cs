using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using EcfDgii.Client.Generated;
using EcfDgii.Client.Generated.Models;
using EcfDgii.Client.Generated.Company.Item.Certificate;
using Microsoft.Kiota.Abstractions;
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
        // ECF send + poll — Generic implementation with automatic routing
        // ---------------------------------------------------------------------------

        private static readonly Dictionary<TipoeCFType, string> RouteMap = new Dictionary<TipoeCFType, string>
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
        /// Send an ECF and poll until processing completes.
        /// Determines the correct endpoint from <c>ecf.Encabezado.IdDoc.TipoeCF</c>,
        /// posts the ECF, then polls until <c>Progress</c> is <c>Finished</c> or <c>Error</c>.
        /// </summary>
        /// <typeparam name="T">The ECF model type (must implement IEcfDocument).</typeparam>
        /// <param name="ecf">The ECF document to send.</param>
        /// <param name="pollingOptions">Optional polling configuration.</param>
        /// <param name="cancellationToken">Cancellation token.</param>
        /// <returns>The final <see cref="EcfResponse"/> after processing.</returns>
        public async Task<EcfResponse> SendEcfAsync<T>(T ecf, PollingOptions? pollingOptions = null, CancellationToken cancellationToken = default) where T : IEcfDocument
        {
            var doc = (IEcfDocument)ecf;
            var tipoeCF = doc.TipoeCF;

            if (tipoeCF == null || !RouteMap.TryGetValue(tipoeCF.Value, out var route))
            {
                throw new ArgumentException($"Unknown or missing TipoeCF: {tipoeCF}. Ensure Encabezado.IdDoc.TipoeCF is set correctly.");
            }

            return await SendInternalAsync(
                doc.RncEmisor,
                doc.Encf,
                ct => PostToRouteAsync(route, ecf, ct),
                pollingOptions,
                cancellationToken).ConfigureAwait(false);
        }

        private Task<EcfResponse?> PostToRouteAsync<T>(string route, T body, CancellationToken ct)
        {
            return route switch
            {
                "31" => Api.Ecf.ThreeOne.PostAsync((Ecf31ECF)(object)body!, cancellationToken: ct),
                "32" => Api.Ecf.ThreeTwo.PostAsync((Ecf32ECF)(object)body!, cancellationToken: ct),
                "33" => Api.Ecf.ThreeThree.PostAsync((Ecf33ECF)(object)body!, cancellationToken: ct),
                "34" => Api.Ecf.ThreeFour.PostAsync((Ecf34ECF)(object)body!, cancellationToken: ct),
                "41" => Api.Ecf.FourOne.PostAsync((Ecf41ECF)(object)body!, cancellationToken: ct),
                "43" => Api.Ecf.FourThree.PostAsync((Ecf43ECF)(object)body!, cancellationToken: ct),
                "44" => Api.Ecf.FourFour.PostAsync((Ecf44ECF)(object)body!, cancellationToken: ct),
                "45" => Api.Ecf.FourFive.PostAsync((Ecf45ECF)(object)body!, cancellationToken: ct),
                "46" => Api.Ecf.FourSix.PostAsync((Ecf46ECF)(object)body!, cancellationToken: ct),
                "47" => Api.Ecf.FourSeven.PostAsync((Ecf47ECF)(object)body!, cancellationToken: ct),
                _ => throw new NotSupportedException($"Route {route} is not supported.")
            };
        }

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

        // ---------------------------------------------------------------------------
        // Company operations
        // ---------------------------------------------------------------------------

        /// <summary>List companies with optional filters.</summary>
        public Task<PaginatedApiResultOfCompanyResponse?> GetCompaniesAsync(
            string[]? rncs = null,
            string[]? names = null,
            string? page = null,
            string? limit = null,
            CancellationToken ct = default)
        {
            return Api.Company.GetAsync(config =>
            {
                config.QueryParameters.Rncs = rncs;
                config.QueryParameters.Names = names;
                config.QueryParameters.Page = page;
                config.QueryParameters.Limit = limit;
            }, ct);
        }

        /// <summary>Get a company by RNC.</summary>
        public Task<CompanyResponse?> GetCompanyByRncAsync(string rnc, CancellationToken ct = default)
        {
            return Api.Company[rnc].GetAsync(cancellationToken: ct);
        }

        /// <summary>Create or update a company.</summary>
        public Task UpsertCompanyAsync(UpsertCompanyRequest body, CancellationToken ct = default)
        {
            return Api.Company.PutAsync(body, cancellationToken: ct);
        }

        /// <summary>Delete a company by RNC.</summary>
        public Task DeleteCompanyAsync(string rnc, CancellationToken ct = default)
        {
            return Api.Company[rnc].DeleteAsync(cancellationToken: ct);
        }

        // ---------------------------------------------------------------------------
        // Certificate operations
        // ---------------------------------------------------------------------------

        /// <summary>Get the current certificate for a company.</summary>
        public Task<List<CertificateResponse>?> GetCertificateAsync(string rnc, CancellationToken ct = default)
        {
            return Api.Company[rnc].Certificate.GetAsync(cancellationToken: ct);
        }

        /// <summary>Update a company's certificate.</summary>
        public async Task<Stream?> UpdateCertificateAsync(string rnc, Stream certificate, string password, CancellationToken ct = default)
        {
            using var ms = new MemoryStream();
            await certificate.CopyToAsync(ms, 8192, ct).ConfigureAwait(false);
            var body = new CertificatePutRequestBody
            {
                Certificate = ms.ToArray(),
                Password = password
            };

            return await Api.Company[rnc].Certificate.PutAsync(body, cancellationToken: ct).ConfigureAwait(false);
        }

        // ---------------------------------------------------------------------------
        // ECF query operations
        // ---------------------------------------------------------------------------

        /// <summary>Query ECFs by RNC and eNCF.</summary>
        public Task<List<EcfResponse>?> QueryEcfAsync(string rnc, string encf, bool? includeEcfContent = null, CancellationToken ct = default)
        {
            return Api.Ecf[rnc][encf].GetAsync(config =>
            {
                config.QueryParameters.IncludeEcfContent = includeEcfContent;
            }, ct);
        }

        /// <summary>Search ECFs for a specific RNC.</summary>
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
            CancellationToken ct = default)
        {
            return Api.Ecf[rnc].GetAsync(config =>
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
            }, ct);
        }

        /// <summary>Search all ECFs across all companies.</summary>
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
            CancellationToken ct = default)
        {
            return Api.Ecf.GetAsync(config =>
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
            }, ct);
        }

        /// <summary>Get a specific ECF by message ID.</summary>
        public Task<List<EcfResponse>?> GetEcfByIdAsync(string rnc, Guid id, bool? includeEcfContent = null, CancellationToken ct = default)
        {
            return Api.Ecf[rnc].Message[id].GetAsync(config =>
            {
                config.QueryParameters.IncludeEcfContent = includeEcfContent;
            }, ct);
        }

        // ---------------------------------------------------------------------------
        // Anulacion rangos
        // ---------------------------------------------------------------------------

        /// <summary>Request range annulment.</summary>
        public Task<RespuestaAnulacionRango?> AnulacionRangosAsync(string rnc, AnulacionRequest body, CancellationToken ct = default)
        {
            return Api.Ecf.Anularrango[rnc].PostAsync(body, cancellationToken: ct);
        }

        /// <summary>List annulments.</summary>
        public Task<PaginatedApiResultOfAnulacionListResponse?> ListAnulacionesAsync(
            ECFType[]? tipoEcf = null,
            string[]? rncs = null,
            DateTimeOffset? fechaDesde = null,
            DateTimeOffset? fechaHasta = null,
            string? page = null,
            string? limit = null,
            CancellationToken ct = default)
        {
            return Api.Ecf.Anulaciones.GetAsync(config =>
            {
                config.QueryParameters.TipoEcfAsECFType = tipoEcf;
                config.QueryParameters.Rncs = rncs;
                config.QueryParameters.FechaDesde = fechaDesde;
                config.QueryParameters.FechaHasta = fechaHasta;
                config.QueryParameters.Page = page;
                config.QueryParameters.Limit = limit;
            }, ct);
        }

        // ---------------------------------------------------------------------------
        // Firmar semilla
        // ---------------------------------------------------------------------------

        /// <summary>Sign a seed for a company.</summary>
        public Task<Stream?> FirmarSemillaAsync(string rnc, Stream xml, CancellationToken ct = default)
        {
            var body = new MultipartBody();
            body.AddOrReplacePart("xml", "application/xml", xml, "seed.xml");
            return Api.Ecf.FirmarSemilla[rnc].PostAsync(body, cancellationToken: ct);
        }

        // ---------------------------------------------------------------------------
        // Recepcion operations
        // ---------------------------------------------------------------------------

        /// <summary>Search ECF reception requests.</summary>
        public Task<PaginatedApiResultOfEcfReceptionRequestDto?> SearchEcfReceptionRequestsAsync(
            Guid?[]? messageIds = null,
            string[]? encfs = null,
            string[]? rncs = null,
            string? page = null,
            string? limit = null,
            CancellationToken ct = default)
        {
            return Api.Recepcion.GetAsync(config =>
            {
                config.QueryParameters.MessageIds = messageIds;
                config.QueryParameters.Encfs = encfs;
                config.QueryParameters.Rncs = rncs;
                config.QueryParameters.Page = page;
                config.QueryParameters.Limit = limit;
            }, ct);
        }

        /// <summary>Search ACECF reception requests.</summary>
        public Task<PaginatedApiResultOfAcecfReceptionRequestDto?> SearchAcecfReceptionRequestsAsync(
            string[]? encfs = null,
            Guid?[]? messageIds = null,
            string? page = null,
            string? limit = null,
            string[]? rncs = null,
            CancellationToken ct = default)
        {
#pragma warning disable CS0618
            return Api.Recepcion.Acecf.GetAsync(config =>
            {
                config.QueryParameters.Encfs = encfs;
                config.QueryParameters.MessageIds = messageIds;
                config.QueryParameters.Page = page;
                config.QueryParameters.Limit = limit;
                config.QueryParameters.Rncs = rncs;
            }, ct);
#pragma warning restore CS0618
        }

        /// <summary>Search ECF reception requests by RNC.</summary>
        public Task<PaginatedApiResultOfEcfReceptionRequestDto?> SearchEcfReceptionRequestsByRncAsync(
            string rnc,
            Guid?[]? messageIds = null,
            string[]? encfs = null,
            string? page = null,
            string? limit = null,
            CancellationToken ct = default)
        {
#pragma warning disable CS0618
            return Api.Recepcion.GetAsync(config =>
            {
                config.QueryParameters.Rncs = new[] { rnc };
                config.QueryParameters.MessageIds = messageIds;
                config.QueryParameters.Encfs = encfs;
                config.QueryParameters.Page = page;
                config.QueryParameters.Limit = limit;
            }, ct);
#pragma warning restore CS0618
        }

        /// <summary>Get a specific ECF reception request by RNC and messageId.</summary>
        public Task<EcfReceptorDto?> GetEcfReceptionRequestAsync(string rnc, Guid messageId, CancellationToken ct = default)
        {
#pragma warning disable CS0618
            return Api.Recepcion[messageId][rnc].GetAsync(cancellationToken: ct);
#pragma warning restore CS0618
        }

        /// <summary>Get a specific ACECF reception request by messageId.</summary>
        public Task<Stream?> GetAcecfReceptionRequestAsync(Guid messageId, CancellationToken ct = default)
        {
            return Api.Recepcion.Acecf[messageId].GetAsync(cancellationToken: ct);
        }

        /// <summary>Send aprobacion comercial (ACECF) for a given ECF reception messageId.</summary>
        public Task<Stream?> AprobacionComercialAsync(Guid messageId, SendAcecfRequest body, CancellationToken ct = default)
        {
            return Api.Recepcion[messageId].Acecf.PostAsync(body, cancellationToken: ct);
        }

        // ---------------------------------------------------------------------------
        // DGII operations
        // ---------------------------------------------------------------------------

        /// <summary>Consulta directorio - listado.</summary>
        public Task<List<Directorio>?> ConsultaDirectorioListadoAsync(string rnc, CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Consultadirectorio.Listado.GetAsync(cancellationToken: ct);
        }

        /// <summary>Consulta directorio - obtener directorio por RNC.</summary>
        public Task<Directorio?> ConsultaDirectorioPorRncAsync(string rnc, string queryRnc, CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Consultadirectorio.ObtenerDirectorioPorRnc.GetAsync(config =>
            {
                config.QueryParameters.RNC = queryRnc;
            }, ct);
        }

        /// <summary>Consulta estado.</summary>
        public Task<RespuestaConsultaEstado?> ConsultaEstadoAsync(
            string rnc,
            string rncEmisor,
            string ncfElectronico,
            string rncComprador,
            string codigoSeguridad,
            CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Consultaestado.Estado.GetAsync(config =>
            {
                config.QueryParameters.RncEmisor = rncEmisor;
                config.QueryParameters.NcfElectronico = ncfElectronico;
                config.QueryParameters.RncComprador = rncComprador;
                config.QueryParameters.CodigoSeguridad = codigoSeguridad;
            }, ct);
        }

        /// <summary>Consulta resultado.</summary>
        public Task<RespuestaConsultaTrackId?> ConsultaResultadoAsync(string rnc, string trackId, CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Consultaresultado.Estado.GetAsync(config =>
            {
                config.QueryParameters.TrackId = trackId;
            }, ct);
        }

        /// <summary>Consulta RFCE.</summary>
        public Task<RespuestaConsultaRFCE?> ConsultaRFCEAsync(
            string rnc,
            string rncEmisor,
            string encf,
            string codSeguridadECF,
            CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Consultarfce.Consulta.GetAsync(config =>
            {
                config.QueryParameters.RNCEmisor = rncEmisor;
                config.QueryParameters.ENCF = encf;
                config.QueryParameters.CodSeguridadECF = codSeguridadECF;
            }, ct);
        }

        /// <summary>Consulta timbre.</summary>
        public Task<RespuestaConsultaTimbre?> ConsultaTimbreAsync(
            string rnc,
            string rncemisor,
            string encf,
            string montototal,
            string codigoseguridad,
            CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Consultatimbre.GetAsync(config =>
            {
                config.QueryParameters.Rncemisor = rncemisor;
                config.QueryParameters.Encf = encf;
                config.QueryParameters.Montototal = montototal;
                config.QueryParameters.Codigoseguridad = codigoseguridad;
            }, ct);
        }

        /// <summary>Consulta timbre FC.</summary>
        public Task<RespuestaConsultaTimbre?> ConsultaTimbreFCAsync(
            string rnc,
            string rncemisor,
            string encf,
            string montototal,
            string codigoseguridad,
            CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Consultatimbrefc.GetAsync(config =>
            {
                config.QueryParameters.Rncemisor = rncemisor;
                config.QueryParameters.Encf = encf;
                config.QueryParameters.Montototal = montototal;
                config.QueryParameters.Codigoseguridad = codigoseguridad;
            }, ct);
        }

        /// <summary>Consulta track IDs.</summary>
        public Task<RespuestaConsultaTrackId?> ConsultaTrackIdAsync(string rnc, string rncEmisor, string encf, CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Consultatrackids.Consulta.GetAsync(config =>
            {
                config.QueryParameters.RncEmisor = rncEmisor;
                config.QueryParameters.Encf = encf;
            }, ct);
        }

        /// <summary>Estatus servicios - obtener estatus.</summary>
        public Task<List<RespuestaEstatusServicio>?> EstatusServiciosAsync(string rnc, CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Estatusservicios.ObtenerEstatus.GetAsync(cancellationToken: ct);
        }

        /// <summary>Estatus servicios - obtener ventanas de mantenimiento.</summary>
        public Task<RespuestaVentanaDeMantenimiento?> VentanasMantenimientoAsync(string rnc, CancellationToken ct = default)
        {
            return Api.Dgii[rnc].Estatusservicios.ObtenerVentanasMantenimiento.GetAsync(cancellationToken: ct);
        }

        // ---------------------------------------------------------------------------
        // ApiKey operations
        // ---------------------------------------------------------------------------

        /// <summary>Create a new API key.</summary>
        public Task<Token?> CreateApiKeyAsync(NewCompanyApiKey body, CancellationToken ct = default)
        {
            return Api.ApiKey.PostAsync(body, cancellationToken: ct);
        }
    }
}
