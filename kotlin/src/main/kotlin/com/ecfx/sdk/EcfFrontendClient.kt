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
import java.time.OffsetDateTime
import java.util.UUID

/**
 * Read-only frontend client for the ECF DGII API (Dominican Republic Electronic Fiscal Receipts).
 *
 * Provides only GET endpoints for querying and searching ECFs and companies.
 * This client does not support sending ECFs, managing companies, or any
 * write/delete operations.
 *
 * All methods are blocking (non-suspend) for convenient use in non-coroutine contexts.
 *
 * Usage:
 * ```kotlin
 * val client = EcfFrontendClient(EcfClientConfig(
 *     baseUrl = Environment.CERTIFICATION.url,
 *     apiKey = "your-jwt-token"
 * ))
 *
 * val ecfs = client.queryEcf("123456789", "E310000000001")
 * val company = client.getCompanyByRnc("123456789")
 * ```
 */
class EcfFrontendClient(private val config: EcfClientConfig) {

    private val authenticatedClient: OkHttpClient = buildAuthenticatedClient()

    private val ecfApi: EcfApi = EcfApi(config.baseUrl, authenticatedClient)

    private val companyApi: CompanyApi = CompanyApi(config.baseUrl, authenticatedClient)

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
        val baseClient = config.httpClient ?: OkHttpClient()
        return baseClient.newBuilder()
            .addInterceptor(Interceptor { chain ->
                val request = chain.request().newBuilder()
                    .header("Authorization", "Bearer ${config.apiKey}")
                    .build()
                chain.proceed(request)
            })
            .build()
    }
}
