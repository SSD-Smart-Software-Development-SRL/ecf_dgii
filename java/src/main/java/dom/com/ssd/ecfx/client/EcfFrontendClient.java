package dom.com.ssd.ecfx.client;

import dom.com.ssd.ecfx.client.api.CompanyApi;
import dom.com.ssd.ecfx.client.api.EcfApi;
import dom.com.ssd.ecfx.client.model.*;

import java.util.Date;
import java.util.List;
import java.util.UUID;

/**
 * Restricted read-only client for the ECF DGII API, intended for frontend use.
 *
 * <p>Only exposes GET endpoints from the Company and ECF APIs.
 * No mutation, submission, or administrative operations are available.</p>
 *
 * <pre>{@code
 * EcfFrontendClient client = new EcfFrontendClient.Builder()
 *     .baseUrl("https://api.prod.ecfx.ssd.com.do")
 *     .apiKey("your-jwt-token")
 *     .build();
 *
 * List<EcfResponse> results = client.queryEcf("123456789", "E310000000001");
 * }</pre>
 */
public class EcfFrontendClient {

    private static final String DEFAULT_ENV_VAR = "ECF_DGII_API_KEY";

    private final ApiClient apiClient;
    private final CompanyApi companyApi;
    private final EcfApi ecfApi;

    private EcfFrontendClient(Builder builder) {
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
    }

    // --- ECF GET endpoints ---

    /**
     * Query a specific ECF by RNC and eNCF.
     *
     * @param rnc  The company RNC (required)
     * @param encf The eNCF identifier (required)
     * @return List of matching EcfResponse
     * @throws ApiException if the HTTP request fails
     */
    public List<EcfResponse> queryEcf(String rnc, String encf) throws ApiException {
        return ecfApi.queryEcf(rnc, encf, false);
    }

    /**
     * Query a specific ECF by RNC and eNCF, optionally including ECF content.
     *
     * @param rnc               The company RNC (required)
     * @param encf              The eNCF identifier (required)
     * @param includeEcfContent Whether to include the full ECF content in the response
     * @return List of matching EcfResponse
     * @throws ApiException if the HTTP request fails
     */
    public List<EcfResponse> queryEcf(String rnc, String encf, Boolean includeEcfContent) throws ApiException {
        return ecfApi.queryEcf(rnc, encf, includeEcfContent);
    }

    /**
     * Search ECFs for a specific company by RNC.
     *
     * @param rnc               The company RNC (required)
     * @param encfs             Filter by eNCFs (optional)
     * @param ids               Filter by IDs (optional)
     * @param tiposEcfs         Filter by ECF types (optional)
     * @param includeEcfContent Whether to include ECF content (optional, default false)
     * @param fromFechaEmision  Filter from emission date (optional)
     * @param toFechaEmision    Filter to emission date (optional)
     * @param amountFrom        Filter by minimum amount (optional)
     * @param amountTo          Filter by maximum amount (optional)
     * @param page              Page number (optional, default 1)
     * @param limit             Page size (optional, default 25)
     * @return Paginated ECF responses
     * @throws ApiException if the HTTP request fails
     */
    public PaginatedApiResultOfEcfResponse searchEcfs(
            String rnc,
            List<String> encfs,
            List<UUID> ids,
            List<AllTipoECFTypes> tiposEcfs,
            Boolean includeEcfContent,
            Date fromFechaEmision,
            Date toFechaEmision,
            SearchEcfsAmountFromParameter amountFrom,
            SearchEcfsAmountFromParameter amountTo,
            GetCompaniesPageParameter page,
            GetCompaniesLimitParameter limit) throws ApiException {
        return ecfApi.searchEcfs(rnc, encfs, ids, tiposEcfs, includeEcfContent,
                fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit);
    }

    /**
     * Search ECFs across all companies.
     *
     * @param encfs             Filter by eNCFs (optional)
     * @param ids               Filter by IDs (optional)
     * @param tiposEcfs         Filter by ECF types (optional)
     * @param includeEcfContent Whether to include ECF content (optional, default false)
     * @param fromFechaEmision  Filter from emission date (optional)
     * @param toFechaEmision    Filter to emission date (optional)
     * @param amountFrom        Filter by minimum amount (optional)
     * @param amountTo          Filter by maximum amount (optional)
     * @param page              Page number (optional, default 1)
     * @param limit             Page size (optional, default 25)
     * @return Paginated ECF responses
     * @throws ApiException if the HTTP request fails
     */
    public PaginatedApiResultOfEcfResponse searchAllEcfs(
            List<String> encfs,
            List<UUID> ids,
            List<AllTipoECFTypes> tiposEcfs,
            Boolean includeEcfContent,
            Date fromFechaEmision,
            Date toFechaEmision,
            SearchEcfsAmountFromParameter amountFrom,
            SearchEcfsAmountFromParameter amountTo,
            GetCompaniesPageParameter page,
            GetCompaniesLimitParameter limit) throws ApiException {
        return ecfApi.searchAllEcfs(encfs, ids, tiposEcfs, includeEcfContent,
                fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit);
    }

    /**
     * Get a specific ECF by RNC and message ID.
     *
     * @param rnc The company RNC (required)
     * @param id  The message UUID (required)
     * @return List of matching EcfResponse
     * @throws ApiException if the HTTP request fails
     */
    public List<EcfResponse> getEcfById(String rnc, UUID id) throws ApiException {
        return ecfApi.getEcfById(rnc, id, false);
    }

    /**
     * Get a specific ECF by RNC and message ID, optionally including ECF content.
     *
     * @param rnc               The company RNC (required)
     * @param id                The message UUID (required)
     * @param includeEcfContent Whether to include the full ECF content in the response
     * @return List of matching EcfResponse
     * @throws ApiException if the HTTP request fails
     */
    public List<EcfResponse> getEcfById(String rnc, UUID id, Boolean includeEcfContent) throws ApiException {
        return ecfApi.getEcfById(rnc, id, includeEcfContent);
    }

    // --- Company GET endpoints ---

    /**
     * Get companies with optional filters and pagination.
     *
     * @param rncs  Filter by RNCs (optional)
     * @param names Filter by names (optional)
     * @param page  Page number (optional, default 1)
     * @param limit Page size (optional, default 25)
     * @return Paginated company responses
     * @throws ApiException if the HTTP request fails
     */
    public PaginatedApiResultOfCompanyResponse getCompanies(
            List<String> rncs,
            List<String> names,
            GetCompaniesPageParameter page,
            GetCompaniesLimitParameter limit) throws ApiException {
        return companyApi.getCompanies(rncs, names, page, limit);
    }

    /**
     * Get a single company by its RNC.
     *
     * @param rnc The company RNC (required)
     * @return The company response
     * @throws ApiException if the HTTP request fails
     */
    public CompanyResponse getCompanyByRnc(String rnc) throws ApiException {
        return companyApi.getCompanyByRnc(rnc);
    }

    // --- Raw API accessors (read-only APIs only) ---

    public CompanyApi getCompanyApi() { return companyApi; }
    public EcfApi getEcfApi() { return ecfApi; }
    public ApiClient getApiClient() { return apiClient; }

    // --- Builder ---

    public static class Builder {
        private String baseUrl;
        private String apiKey;

        public Builder baseUrl(String baseUrl) {
            this.baseUrl = baseUrl;
            return this;
        }

        public Builder apiKey(String apiKey) {
            this.apiKey = apiKey;
            return this;
        }

        public EcfFrontendClient build() {
            return new EcfFrontendClient(this);
        }
    }
}
