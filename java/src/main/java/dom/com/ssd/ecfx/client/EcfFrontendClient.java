package dom.com.ssd.ecfx.client;

import dom.com.ssd.ecfx.client.api.CompanyApi;
import dom.com.ssd.ecfx.client.api.EcfApi;
import dom.com.ssd.ecfx.client.model.*;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.GeneralSecurityException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import java.util.function.Consumer;
import java.util.function.Supplier;

/**
 * Restricted read-only client for the ECF DGII API, intended for frontend use.
 *
 * <p>Only exposes GET endpoints from the Company and ECF APIs.
 * No mutation, submission, or administrative operations are available.</p>
 *
 * <p>Token management is handled automatically via callbacks:</p>
 * <ul>
 *   <li>{@code getToken} (required) — fetches a fresh token (e.g., from your backend)</li>
 *   <li>{@code cacheToken} (optional) — stores a token; defaults to AES-encrypted file in {@code ~/.ecf-dgii/}</li>
 *   <li>{@code getCachedToken} (optional) — reads the cached token; defaults to reading the encrypted file</li>
 * </ul>
 *
 * <pre>{@code
 * EcfFrontendClient client = new EcfFrontendClient.Builder()
 *     .getToken(() -> {
 *         // Call your backend to get a read-only token
 *         return fetchTokenFromBackend();
 *     })
 *     .environment("prod")
 *     .build();
 *
 * List<EcfResponse> results = client.queryEcf("123456789", "E310000000001");
 * }</pre>
 */
public class EcfFrontendClient {

    private static final String ECF_DIR = ".ecf-dgii";
    private static final String TOKEN_FILE = "cached-token.enc";
    private static final String KEY_FILE = "token.key";
    private static final String AES_ALGORITHM = "AES/GCM/NoPadding";
    private static final int GCM_IV_LENGTH = 12;
    private static final int GCM_TAG_LENGTH = 128;

    private static final Map<String, String> ENVIRONMENT_URLS = new HashMap<>();
    static {
        ENVIRONMENT_URLS.put("test", "https://api.test.ecfx.ssd.com.do");
        ENVIRONMENT_URLS.put("cert", "https://api.cert.ecfx.ssd.com.do");
        ENVIRONMENT_URLS.put("prod", "https://api.prod.ecfx.ssd.com.do");
    }

    private final ApiClient apiClient;
    private final CompanyApi companyApi;
    private final EcfApi ecfApi;
    private final Supplier<String> getToken;
    private final Consumer<String> cacheToken;
    private final Supplier<String> getCachedToken;

    private EcfFrontendClient(Builder builder) {
        if (builder.getToken == null) {
            throw new IllegalArgumentException("getToken callback is required");
        }

        this.getToken = builder.getToken;
        this.cacheToken = builder.cacheToken != null ? builder.cacheToken : defaultCacheToken();
        this.getCachedToken = builder.getCachedToken != null ? builder.getCachedToken : defaultGetCachedToken();

        this.apiClient = new ApiClient();
        if (builder.baseUrl != null && !builder.baseUrl.isEmpty()) {
            this.apiClient.setBasePath(builder.baseUrl);
        }

        this.companyApi = new CompanyApi(this.apiClient);
        this.ecfApi = new EcfApi(this.apiClient);
    }

    // --- Token management ---

    /**
     * Ensures a valid token is set on the API client.
     * Checks the cache first; if empty, fetches a new token and caches it.
     */
    private void ensureToken() {
        String token = getCachedToken.get();
        if (token == null || token.isEmpty()) {
            token = getToken.get();
            cacheToken.accept(token);
        }
        apiClient.setBearerToken(token);
    }

    /**
     * Refreshes the token by calling getToken, updating the cache and the API client.
     */
    private void refreshToken() {
        String token = getToken.get();
        cacheToken.accept(token);
        apiClient.setBearerToken(token);
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
        return queryEcf(rnc, encf, false);
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
        ensureToken();
        try {
            return ecfApi.queryEcf(rnc, encf, includeEcfContent);
        } catch (ApiException e) {
            if (e.getCode() == 401) {
                refreshToken();
                return ecfApi.queryEcf(rnc, encf, includeEcfContent);
            }
            throw e;
        }
    }

    /**
     * Search ECFs for a specific company by RNC.
     *
     * @param rnc The company RNC (required)
     * @return Paginated ECF responses
     * @throws ApiException if the HTTP request fails
     */
    public PaginatedApiResultOfEcfResponse searchEcfs(String rnc) throws ApiException {
        return searchEcfs(rnc, null, null, null, false, null, null, null, null, null, null);
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
        ensureToken();
        try {
            return ecfApi.searchEcfs(rnc, encfs, ids, tiposEcfs, includeEcfContent,
                    fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit);
        } catch (ApiException e) {
            if (e.getCode() == 401) {
                refreshToken();
                return ecfApi.searchEcfs(rnc, encfs, ids, tiposEcfs, includeEcfContent,
                        fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit);
            }
            throw e;
        }
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
        ensureToken();
        try {
            return ecfApi.searchAllEcfs(encfs, ids, tiposEcfs, includeEcfContent,
                    fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit);
        } catch (ApiException e) {
            if (e.getCode() == 401) {
                refreshToken();
                return ecfApi.searchAllEcfs(encfs, ids, tiposEcfs, includeEcfContent,
                        fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit);
            }
            throw e;
        }
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
        return getEcfById(rnc, id, false);
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
        ensureToken();
        try {
            return ecfApi.getEcfById(rnc, id, includeEcfContent);
        } catch (ApiException e) {
            if (e.getCode() == 401) {
                refreshToken();
                return ecfApi.getEcfById(rnc, id, includeEcfContent);
            }
            throw e;
        }
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
        ensureToken();
        try {
            return companyApi.getCompanies(rncs, names, page, limit);
        } catch (ApiException e) {
            if (e.getCode() == 401) {
                refreshToken();
                return companyApi.getCompanies(rncs, names, page, limit);
            }
            throw e;
        }
    }

    /**
     * Get a single company by its RNC.
     *
     * @param rnc The company RNC (required)
     * @return The company response
     * @throws ApiException if the HTTP request fails
     */
    public CompanyResponse getCompanyByRnc(String rnc) throws ApiException {
        ensureToken();
        try {
            return companyApi.getCompanyByRnc(rnc);
        } catch (ApiException e) {
            if (e.getCode() == 401) {
                refreshToken();
                return companyApi.getCompanyByRnc(rnc);
            }
            throw e;
        }
    }

    // --- Raw API accessors (read-only APIs only) ---

    public CompanyApi getCompanyApi() { return companyApi; }
    public EcfApi getEcfApi() { return ecfApi; }
    public ApiClient getApiClient() { return apiClient; }

    // --- Default encrypted file-based token cache ---

    private static Path ecfDir() {
        return Paths.get(System.getProperty("user.home"), ECF_DIR);
    }

    private static SecretKey loadOrCreateKey() {
        Path keyPath = ecfDir().resolve(KEY_FILE);
        try {
            if (Files.exists(keyPath)) {
                byte[] keyBytes = Base64.getDecoder().decode(
                        new String(Files.readAllBytes(keyPath), StandardCharsets.UTF_8).trim());
                return new SecretKeySpec(keyBytes, "AES");
            }
            Files.createDirectories(ecfDir());
            KeyGenerator keyGen = KeyGenerator.getInstance("AES");
            keyGen.init(256);
            SecretKey key = keyGen.generateKey();
            Files.write(keyPath, Base64.getEncoder().encode(key.getEncoded()));
            return key;
        } catch (IOException | GeneralSecurityException e) {
            throw new RuntimeException("Failed to load or create encryption key at " + keyPath, e);
        }
    }

    private static Consumer<String> defaultCacheToken() {
        return token -> {
            try {
                SecretKey key = loadOrCreateKey();
                byte[] iv = new byte[GCM_IV_LENGTH];
                new SecureRandom().nextBytes(iv);

                Cipher cipher = Cipher.getInstance(AES_ALGORITHM);
                cipher.init(Cipher.ENCRYPT_MODE, key, new GCMParameterSpec(GCM_TAG_LENGTH, iv));
                byte[] encrypted = cipher.doFinal(token.getBytes(StandardCharsets.UTF_8));

                // Prepend IV to ciphertext
                byte[] combined = new byte[iv.length + encrypted.length];
                System.arraycopy(iv, 0, combined, 0, iv.length);
                System.arraycopy(encrypted, 0, combined, iv.length, encrypted.length);

                Path tokenPath = ecfDir().resolve(TOKEN_FILE);
                Files.createDirectories(ecfDir());
                Files.write(tokenPath, Base64.getEncoder().encode(combined));
            } catch (IOException | GeneralSecurityException e) {
                throw new RuntimeException("Failed to cache token", e);
            }
        };
    }

    private static Supplier<String> defaultGetCachedToken() {
        return () -> {
            Path tokenPath = ecfDir().resolve(TOKEN_FILE);
            if (!Files.exists(tokenPath)) {
                return null;
            }
            try {
                SecretKey key = loadOrCreateKey();
                byte[] combined = Base64.getDecoder().decode(
                        new String(Files.readAllBytes(tokenPath), StandardCharsets.UTF_8).trim());

                byte[] iv = new byte[GCM_IV_LENGTH];
                System.arraycopy(combined, 0, iv, 0, GCM_IV_LENGTH);
                byte[] encrypted = new byte[combined.length - GCM_IV_LENGTH];
                System.arraycopy(combined, GCM_IV_LENGTH, encrypted, 0, encrypted.length);

                Cipher cipher = Cipher.getInstance(AES_ALGORITHM);
                cipher.init(Cipher.DECRYPT_MODE, key, new GCMParameterSpec(GCM_TAG_LENGTH, iv));
                byte[] decrypted = cipher.doFinal(encrypted);
                return new String(decrypted, StandardCharsets.UTF_8);
            } catch (IOException | GeneralSecurityException e) {
                // If decryption fails (corrupted file, wrong key), return null to trigger fresh fetch
                return null;
            }
        };
    }

    // --- Builder ---

    public static class Builder {
        private String baseUrl;
        private Supplier<String> getToken;
        private Consumer<String> cacheToken;
        private Supplier<String> getCachedToken;

        /**
         * Sets the base URL directly.
         *
         * @param baseUrl The full API base URL
         * @return this builder
         */
        public Builder baseUrl(String baseUrl) {
            this.baseUrl = baseUrl;
            return this;
        }

        /**
         * Sets the environment, which determines the base URL.
         * Valid values: "test", "cert", "prod".
         *
         * @param environment The environment name
         * @return this builder
         * @throws IllegalArgumentException if environment is not recognized
         */
        public Builder environment(String environment) {
            String url = ENVIRONMENT_URLS.get(environment);
            if (url == null) {
                throw new IllegalArgumentException(
                        "Unknown environment: " + environment + ". Valid values: test, cert, prod");
            }
            this.baseUrl = url;
            return this;
        }

        /**
         * Sets the callback to fetch a fresh token (REQUIRED).
         * This is typically a call to your backend's token endpoint.
         *
         * @param getToken supplier that returns a fresh JWT token
         * @return this builder
         */
        public Builder getToken(Supplier<String> getToken) {
            this.getToken = getToken;
            return this;
        }

        /**
         * Sets the callback to cache a token (OPTIONAL).
         * Default: AES-encrypted file stored in {@code ~/.ecf-dgii/}.
         *
         * @param cacheToken consumer that stores the token
         * @return this builder
         */
        public Builder cacheToken(Consumer<String> cacheToken) {
            this.cacheToken = cacheToken;
            return this;
        }

        /**
         * Sets the callback to read a cached token (OPTIONAL).
         * Default: reads from AES-encrypted file in {@code ~/.ecf-dgii/}.
         * Should return null if no cached token is available.
         *
         * @param getCachedToken supplier that returns the cached token or null
         * @return this builder
         */
        public Builder getCachedToken(Supplier<String> getCachedToken) {
            this.getCachedToken = getCachedToken;
            return this;
        }

        public EcfFrontendClient build() {
            return new EcfFrontendClient(this);
        }
    }
}
