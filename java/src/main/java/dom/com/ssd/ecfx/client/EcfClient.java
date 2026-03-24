package dom.com.ssd.ecfx.client;

import dom.com.ssd.ecfx.client.api.*;
import dom.com.ssd.ecfx.client.model.*;

import java.util.List;
import java.util.UUID;


/**
 * High-level client for the ECF DGII API.
 *
 * <p>Provides overloaded {@code sendEcf} methods for each ECF type (Ecf31ECF, Ecf32ECF, etc.)
 * which automatically submit, poll for completion, and return the final result.</p>
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

    // --- Type-specific sendEcf overloads ---

    /** Sends a Factura de Crédito Fiscal Electrónica (e-CF 31). */
    public EcfResponse sendEcf(String rnc, Ecf31ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf31(ecf));
    }

    /** Sends a Factura de Consumo Electrónica (e-CF 32). */
    public EcfResponse sendEcf(String rnc, Ecf32ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf32(ecf));
    }

    /** Sends a Nota de Débito Electrónica (e-CF 33). */
    public EcfResponse sendEcf(String rnc, Ecf33ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf33(ecf));
    }

    /** Sends a Nota de Crédito Electrónica (e-CF 34). */
    public EcfResponse sendEcf(String rnc, Ecf34ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf34(ecf));
    }

    /** Sends a Compras Electrónico (e-CF 41). */
    public EcfResponse sendEcf(String rnc, Ecf41ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf41(ecf));
    }

    /** Sends a Gastos Menores Electrónico (e-CF 43). */
    public EcfResponse sendEcf(String rnc, Ecf43ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf43(ecf));
    }

    /** Sends a Regímenes Especiales Electrónico (e-CF 44). */
    public EcfResponse sendEcf(String rnc, Ecf44ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf44(ecf));
    }

    /** Sends a Gubernamental Electrónico (e-CF 45). */
    public EcfResponse sendEcf(String rnc, Ecf45ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf45(ecf));
    }

    /** Sends a Comprobante de Exportaciones Electrónico (e-CF 46). */
    public EcfResponse sendEcf(String rnc, Ecf46ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf46(ecf));
    }

    /** Sends a Comprobante para Pagos al Exterior Electrónico (e-CF 47). */
    public EcfResponse sendEcf(String rnc, Ecf47ECF ecf) throws EcfClientException, ApiException {
        return sendAndPoll(rnc, ecfApi.recepcionEcf47(ecf));
    }

    private EcfResponse sendAndPoll(String rnc, EcfResponse initialResponse) throws EcfClientException, ApiException {
        UUID messageId = initialResponse.getMessageId();
        if (messageId == null) {
            throw new EcfClientException("API returned null messageId");
        }
        return pollForCompletion(rnc, messageId);
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

    /**
     * Creates a new {@link EcfFrontendClient.Builder} for constructing a read-only frontend client.
     *
     * @return A new EcfFrontendClient builder
     */
    public static EcfFrontendClient.Builder frontendBuilder() {
        return new EcfFrontendClient.Builder();
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
