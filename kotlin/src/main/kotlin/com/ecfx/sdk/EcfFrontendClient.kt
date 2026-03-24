package com.ecfx.sdk

import com.ecfx.sdk.api.CompanyApi
import com.ecfx.sdk.api.EcfApi
import com.ecfx.sdk.models.AllTipoECFTypes
import com.ecfx.sdk.models.CompanyResponse
import com.ecfx.sdk.models.EcfResponse
import com.ecfx.sdk.models.GetCompaniesLimitParameter
import com.ecfx.sdk.models.GetCompaniesPageParameter
import com.ecfx.sdk.models.PaginatedApiResultOfCompanyResponse
import com.ecfx.sdk.models.PaginatedApiResultOfEcfResponse
import com.ecfx.sdk.models.SearchEcfsAmountFromParameter
import kotlinx.coroutines.runBlocking
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import okhttp3.Response
import java.io.File
import java.time.OffsetDateTime
import java.util.Base64
import java.util.UUID
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey
import javax.crypto.spec.SecretKeySpec

/**
 * Configuration for the read-only frontend ECF client.
 *
 * @param getToken Required callback that fetches a fresh read-only token
 *   (e.g. calls your backend's `GET /ecf-token`).
 * @param cacheToken Optional callback to cache the token. Defaults to AES-encrypted file on disk.
 * @param getCachedToken Optional callback to retrieve a cached token. Defaults to reading from AES-encrypted file.
 * @param environment Target environment (`"test"`, `"cert"`, or `"prod"`). Defaults to `"test"`.
 * @param baseUrl Optional base URL override. Takes precedence over [environment].
 */
data class EcfFrontendClientConfig(
    val getToken: suspend () -> String,
    val cacheToken: suspend (String) -> Unit = DefaultTokenCache::cacheToken,
    val getCachedToken: suspend () -> String? = DefaultTokenCache::getCachedToken,
    val environment: String = "test",
    val baseUrl: String? = null,
)

/**
 * Default token cache that stores the token AES-encrypted on disk.
 */
internal object DefaultTokenCache {
    private val cacheFile = File(System.getProperty("user.home"), ".ecf-token-cache")
    private val keyFile = File(System.getProperty("user.home"), ".ecf-token-key")

    private fun getOrCreateKey(): SecretKey {
        if (keyFile.exists()) {
            val decoded = Base64.getDecoder().decode(keyFile.readText())
            return SecretKeySpec(decoded, "AES")
        }
        val key = KeyGenerator.getInstance("AES").apply { init(256) }.generateKey()
        keyFile.writeText(Base64.getEncoder().encodeToString(key.encoded))
        return key
    }

    fun cacheToken(token: String) {
        val cipher = Cipher.getInstance("AES")
        cipher.init(Cipher.ENCRYPT_MODE, getOrCreateKey())
        val encrypted = cipher.doFinal(token.toByteArray())
        cacheFile.writeText(Base64.getEncoder().encodeToString(encrypted))
    }

    fun getCachedToken(): String? {
        if (!cacheFile.exists()) return null
        return try {
            val cipher = Cipher.getInstance("AES")
            cipher.init(Cipher.DECRYPT_MODE, getOrCreateKey())
            val decoded = Base64.getDecoder().decode(cacheFile.readText())
            String(cipher.doFinal(decoded))
        } catch (_: Exception) {
            null
        }
    }
}

/**
 * Read-only frontend client for the ECF DGII API (Dominican Republic Electronic Fiscal Receipts).
 *
 * Provides only GET endpoints for querying and searching ECFs and companies.
 * This client does not support sending ECFs, managing companies, or any
 * write/delete operations.
 *
 * Token lifecycle is handled automatically:
 * - On each request, checks `getCachedToken()`. If null, calls `getToken()` then `cacheToken(token)`.
 * - On 401 responses, calls `getToken()` again, updates the cache, and retries the request.
 *
 * All methods are blocking (non-suspend) for convenient use in non-coroutine contexts.
 *
 * Usage:
 * ```kotlin
 * val client = EcfFrontendClient(EcfFrontendClientConfig(
 *     getToken = {
 *         val res = httpClient.get("https://my-backend/api/v1/ecf-token")
 *         res.body<TokenResponse>().apiKey
 *     },
 *     environment = "prod"
 * ))
 *
 * val ecfs = client.queryEcf("131880681", "E310000051630")
 * val company = client.getCompanyByRnc("131880681")
 * ```
 */
class EcfFrontendClient(private val config: EcfFrontendClientConfig) {

    private val resolvedBaseUrl: String = config.baseUrl ?: when (config.environment) {
        "test" -> Environment.TEST.url
        "cert" -> Environment.CERTIFICATION.url
        "prod" -> Environment.PRODUCTION.url
        else -> Environment.TEST.url
    }

    @Volatile
    private var currentToken: String? = null

    private val authenticatedClient: OkHttpClient = buildAuthenticatedClient()

    private val ecfApi: EcfApi = EcfApi(resolvedBaseUrl, authenticatedClient)

    private val companyApi: CompanyApi = CompanyApi(resolvedBaseUrl, authenticatedClient)

    /**
     * Query a specific ECF by RNC and eNCF.
     *
     * @param rnc The RNC (tax ID) of the company.
     * @param encf The eNCF (electronic fiscal receipt number).
     * @param includeEcfContent Whether to include the full ECF content in the response.
     * @return A list of matching [EcfResponse] objects.
     */
    fun queryEcf(
        rnc: String,
        encf: String,
        includeEcfContent: Boolean? = false,
    ): List<EcfResponse> = runBlocking {
        ecfApi.queryEcf(rnc, encf, includeEcfContent)
    }

    /**
     * Search ECFs for a specific company by RNC.
     *
     * @param rnc The RNC (tax ID) of the company.
     * @param encfs Filter by specific eNCF numbers.
     * @param ids Filter by specific ECF IDs.
     * @param tiposEcfs Filter by ECF types.
     * @param includeEcfContent Whether to include the full ECF content in the response.
     * @param fromFechaEmision Filter by emission date (from).
     * @param toFechaEmision Filter by emission date (to).
     * @param amountFrom Filter by amount (from).
     * @param amountTo Filter by amount (to).
     * @param page Page number for pagination.
     * @param limit Number of results per page.
     * @return A paginated result of [EcfResponse] objects.
     */
    fun searchEcfs(
        rnc: String,
        encfs: List<String>? = null,
        ids: List<UUID>? = null,
        tiposEcfs: List<AllTipoECFTypes>? = null,
        includeEcfContent: Boolean? = false,
        fromFechaEmision: OffsetDateTime? = null,
        toFechaEmision: OffsetDateTime? = null,
        amountFrom: SearchEcfsAmountFromParameter? = null,
        amountTo: SearchEcfsAmountFromParameter? = null,
        page: GetCompaniesPageParameter? = null,
        limit: GetCompaniesLimitParameter? = null,
    ): PaginatedApiResultOfEcfResponse = runBlocking {
        ecfApi.searchEcfs(
            rnc, encfs, ids, tiposEcfs, includeEcfContent,
            fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit
        )
    }

    /**
     * Search ECFs across all companies.
     *
     * @param encfs Filter by specific eNCF numbers.
     * @param ids Filter by specific ECF IDs.
     * @param tiposEcfs Filter by ECF types.
     * @param includeEcfContent Whether to include the full ECF content in the response.
     * @param fromFechaEmision Filter by emission date (from).
     * @param toFechaEmision Filter by emission date (to).
     * @param amountFrom Filter by amount (from).
     * @param amountTo Filter by amount (to).
     * @param page Page number for pagination.
     * @param limit Number of results per page.
     * @return A paginated result of [EcfResponse] objects.
     */
    fun searchAllEcfs(
        encfs: List<String>? = null,
        ids: List<UUID>? = null,
        tiposEcfs: List<AllTipoECFTypes>? = null,
        includeEcfContent: Boolean? = false,
        fromFechaEmision: OffsetDateTime? = null,
        toFechaEmision: OffsetDateTime? = null,
        amountFrom: SearchEcfsAmountFromParameter? = null,
        amountTo: SearchEcfsAmountFromParameter? = null,
        page: GetCompaniesPageParameter? = null,
        limit: GetCompaniesLimitParameter? = null,
    ): PaginatedApiResultOfEcfResponse = runBlocking {
        ecfApi.searchAllEcfs(
            encfs, ids, tiposEcfs, includeEcfContent,
            fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit
        )
    }

    /**
     * Get a specific ECF by RNC and message ID.
     *
     * @param rnc The RNC (tax ID) of the company.
     * @param id The message ID (UUID) of the ECF.
     * @param includeEcfContent Whether to include the full ECF content in the response.
     * @return A list of matching [EcfResponse] objects.
     */
    fun getEcfById(
        rnc: String,
        id: UUID,
        includeEcfContent: Boolean? = false,
    ): List<EcfResponse> = runBlocking {
        ecfApi.getEcfById(rnc, id, includeEcfContent)
    }

    /**
     * Get a paginated list of companies.
     *
     * @param rncs Filter by specific RNCs.
     * @param names Filter by company names.
     * @param page Page number for pagination.
     * @param limit Number of results per page.
     * @return A paginated result of [CompanyResponse] objects.
     */
    fun getCompanies(
        rncs: List<String>? = null,
        names: List<String>? = null,
        page: GetCompaniesPageParameter? = null,
        limit: GetCompaniesLimitParameter? = null,
    ): PaginatedApiResultOfCompanyResponse = runBlocking {
        companyApi.getCompanies(rncs, names, page, limit)
    }

    /**
     * Get a specific company by RNC.
     *
     * @param rnc The RNC (tax ID) of the company.
     * @return The [CompanyResponse] for the given RNC.
     */
    fun getCompanyByRnc(rnc: String): CompanyResponse = runBlocking {
        companyApi.getCompanyByRnc(rnc)
    }

    private fun buildAuthenticatedClient(): OkHttpClient {
        val baseClient = OkHttpClient()
        return baseClient.newBuilder()
            .addInterceptor(Interceptor { chain ->
                val token = resolveToken()
                val request = chain.request().newBuilder()
                    .header("Authorization", "Bearer $token")
                    .build()
                val response = chain.proceed(request)

                // On 401, refresh the token and retry once
                if (response.code == 401) {
                    response.close()
                    val freshToken = refreshToken()
                    val retryRequest = chain.request().newBuilder()
                        .header("Authorization", "Bearer $freshToken")
                        .build()
                    return@Interceptor chain.proceed(retryRequest)
                }

                response
            })
            .build()
    }

    /**
     * Resolve the current token: check cache first, fetch if needed.
     */
    private fun resolveToken(): String {
        currentToken?.let { return it }

        return runBlocking {
            val cached = config.getCachedToken()
            if (cached != null) {
                currentToken = cached
                cached
            } else {
                val fresh = config.getToken()
                config.cacheToken(fresh)
                currentToken = fresh
                fresh
            }
        }
    }

    /**
     * Force-refresh the token by calling getToken(), update cache.
     */
    private fun refreshToken(): String {
        return runBlocking {
            val fresh = config.getToken()
            config.cacheToken(fresh)
            currentToken = fresh
            fresh
        }
    }
}
