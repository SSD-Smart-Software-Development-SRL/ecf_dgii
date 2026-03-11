package dom.com.ssd.ecfx.client;

import dom.com.ssd.ecfx.client.api.*;
import dom.com.ssd.ecfx.client.model.*;

import java.util.List;
import java.util.UUID;

/**
 * High-level client for the ECF DGII API.
 *
 * <p>Provides {@link #sendEcf(String, ECF)} which automatically routes the ECF
 * to the correct endpoint based on its type, submits it, polls for completion,
 * and returns the final result.</p>
 *
 * <p>All raw generated API classes are also accessible via getters.</p>
 *
 * <pre>{@code
 * EcfClient client = new EcfClient.Builder()
 *     .baseUrl("https://api.prod.ecfx.ssd.com.do")
 *     .apiKey("your-jwt-token")
 *     .build();
 *
 * EcfResponse response = client.sendEcf("123456789", ecf);
 * }</pre>
 */
public class EcfClient {

    private static final String DEFAULT_ENV_VAR = "ECF_DGII_API_KEY";
    private static final long DEFAULT_POLLING_MAX_MS = 120_000L;
    private static final long DEFAULT_POLLING_INTERVAL_MS = 1_000L;
    private static final long MAX_POLLING_INTERVAL_MS = 5_000L;

    private final ApiClient apiClient;
    private final CompanyApi companyApi;
    private final EcfApi ecfApi;
    private final RecepcionApi recepcionApi;
    private final DgiiApi dgiiApi;
    private final ApiKeyApi apiKeyApi;
    private final long pollingMaxMs;
    private final long pollingIntervalMs;

    private EcfClient(Builder builder) {
        String apiKey = builder.apiKey;
        if (apiKey == null || apiKey.isEmpty()) {
            apiKey = System.getenv(DEFAULT_ENV_VAR);
        }

        this.apiClient = new ApiClient();
        if (builder.baseUrl != null && !builder.baseUrl.isEmpty()) {
            this.apiClient.setBasePath(builder.baseUrl);
        }
        if (apiKey != null && !apiKey.isEmpty()) {
            this.apiClient.setBearerToken(apiKey);
        }

        this.companyApi = new CompanyApi(this.apiClient);
        this.ecfApi = new EcfApi(this.apiClient);
        this.recepcionApi = new RecepcionApi(this.apiClient);
        this.dgiiApi = new DgiiApi(this.apiClient);
        this.apiKeyApi = new ApiKeyApi(this.apiClient);
        this.pollingMaxMs = builder.pollingMaxMs;
        this.pollingIntervalMs = builder.pollingIntervalMs;
    }

    /**
     * Sends an ECF, automatically routing by type, then polls until completion.
     *
     * @param rnc The company RNC
     * @param ecf The ECF document to send
     * @return The final EcfResponse when processing is complete
     * @throws EcfClientException if routing fails, polling times out, or DGII returns an error
     * @throws ApiException if the HTTP request fails
     */
    public EcfResponse sendEcf(String rnc, ECF ecf) throws EcfClientException, ApiException {
        if (ecf == null || ecf.getEncabezado() == null || ecf.getEncabezado().getIdDoc() == null) {
            throw new EcfClientException("ECF, encabezado, and idDoc must not be null");
        }

        TipoeCFType tipo = ecf.getEncabezado().getIdDoc().getTipoeCF();
        if (tipo == null) {
            throw new EcfClientException("tipoeCF must not be null in encabezado.idDoc");
        }

        // Step 1: Route and send
        EcfResponse initialResponse = routeAndSend(tipo, ecf);

        UUID messageId = initialResponse.getMessageId();
        if (messageId == null) {
            throw new EcfClientException("API returned null messageId");
        }

        // Step 2: Poll for completion
        return pollForCompletion(rnc, messageId);
    }

    private EcfResponse routeAndSend(TipoeCFType tipo, ECF ecf) throws EcfClientException, ApiException {
        switch (tipo) {
            case FACTURA_DE_CREDITO_FISCAL_ELECTRONICA:
                return ecfApi.recepcionEcf31(ecf);
            case FACTURA_DE_CONSUMO_ELECTRONICA:
                return ecfApi.recepcionEcf32(ecf);
            case NOTA_DE_DEBITO_ELECTRONICA:
                return ecfApi.recepcionEcf33(ecf);
            case NOTA_DE_CREDITO_ELECTRONICA:
                return ecfApi.recepcionEcf34(ecf);
            case COMPRAS_ELECTRONICO:
                return ecfApi.recepcionEcf41(ecf);
            case GASTOS_MENORES_ELECTRONICO:
                return ecfApi.recepcionEcf43(ecf);
            case REGIMENES_ESPECIALES_ELECTRONICO:
                return ecfApi.recepcionEcf44(ecf);
            case GUBERNAMENTAL_ELECTRONICO:
                return ecfApi.recepcionEcf45(ecf);
            case COMPROBANTE_DE_EXPORTACIONES_ELECTRONICO:
                return ecfApi.recepcionEcf46(ecf);
            case COMPROBANTE_PARA_PAGOS_AL_EXTERIOR_ELECTRONICO:
                return ecfApi.recepcionEcf47(ecf);
            default:
                throw new EcfClientException("Unsupported ECF type: " + tipo);
        }
    }

    private EcfResponse pollForCompletion(String rnc, UUID messageId) throws EcfClientException, ApiException {
        long elapsed = 0L;
        long currentInterval = pollingIntervalMs;

        while (elapsed < pollingMaxMs) {
            try {
                Thread.sleep(currentInterval);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new EcfClientException("Polling interrupted", e, messageId.toString(), null);
            }
            elapsed += currentInterval;

            List<EcfResponse> responses = ecfApi.getEcfById(rnc, messageId, false);
            if (responses != null && !responses.isEmpty()) {
                EcfResponse response = responses.get(0);
                EcfProgress progress = response.getProgress();

                if (progress == EcfProgress.FINISHED) {
                    return response;
                }
                if (progress == EcfProgress.ERROR) {
                    String errorMsg = response.getErrors() != null ? response.getErrors() : "ECF processing failed";
                    throw new EcfClientException(errorMsg, null, messageId.toString(), response.getCodSec());
                }
            }

            // Exponential backoff up to MAX_POLLING_INTERVAL_MS
            currentInterval = Math.min(currentInterval * 2, MAX_POLLING_INTERVAL_MS);
        }

        throw new EcfClientException("Polling timed out after " + pollingMaxMs + "ms", null, messageId.toString(), null);
    }

    // --- Raw API accessors ---

    public CompanyApi getCompanyApi() { return companyApi; }
    public EcfApi getEcfApi() { return ecfApi; }
    public RecepcionApi getRecepcionApi() { return recepcionApi; }
    public DgiiApi getDgiiApi() { return dgiiApi; }
    public ApiKeyApi getApiKeyApi() { return apiKeyApi; }
    public ApiClient getApiClient() { return apiClient; }

    // --- Builder ---

    public static class Builder {
        private String baseUrl;
        private String apiKey;
        private long pollingMaxMs = DEFAULT_POLLING_MAX_MS;
        private long pollingIntervalMs = DEFAULT_POLLING_INTERVAL_MS;

        public Builder baseUrl(String baseUrl) {
            this.baseUrl = baseUrl;
            return this;
        }

        public Builder apiKey(String apiKey) {
            this.apiKey = apiKey;
            return this;
        }

        /** Maximum time to poll in milliseconds. Default: 120000 (2 minutes). */
        public Builder pollingMaxDurationMs(long ms) {
            this.pollingMaxMs = ms;
            return this;
        }

        /** Initial polling interval in milliseconds. Default: 1000 (1 second). Backs off exponentially to 5s. */
        public Builder pollingIntervalMs(long ms) {
            this.pollingIntervalMs = ms;
            return this;
        }

        public EcfClient build() {
            return new EcfClient(this);
        }
    }
}
