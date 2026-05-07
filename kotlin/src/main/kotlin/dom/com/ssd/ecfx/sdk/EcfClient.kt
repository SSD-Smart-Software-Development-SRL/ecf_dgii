package dom.com.ssd.ecfx.sdk

import dom.com.ssd.ecfx.sdk.apis.AprobacionComercialApi
import dom.com.ssd.ecfx.sdk.apis.CompanyApi
import dom.com.ssd.ecfx.sdk.apis.EcfApi
import dom.com.ssd.ecfx.sdk.apis.RecepcionApi
import dom.com.ssd.ecfx.sdk.models.Ecf31ECF
import dom.com.ssd.ecfx.sdk.models.Ecf32ECF
import dom.com.ssd.ecfx.sdk.models.Ecf33ECF
import dom.com.ssd.ecfx.sdk.models.Ecf34ECF
import dom.com.ssd.ecfx.sdk.models.Ecf41ECF
import dom.com.ssd.ecfx.sdk.models.Ecf43ECF
import dom.com.ssd.ecfx.sdk.models.Ecf44ECF
import dom.com.ssd.ecfx.sdk.models.Ecf45ECF
import dom.com.ssd.ecfx.sdk.models.Ecf46ECF
import dom.com.ssd.ecfx.sdk.models.Ecf47ECF
import dom.com.ssd.ecfx.sdk.models.EcfProgress
import dom.com.ssd.ecfx.sdk.models.EcfResponse
import kotlinx.coroutines.delay
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import java.util.UUID

/**
 * Configuration for the ECF DGII SDK client.
 *
 * @param baseUrl The base URL of the ECF API. Defaults to [Environment.TEST].
 * @param apiKey The JWT Bearer token for authentication. Falls back to `ECF_DGII_API_KEY` env var.
 * @param pollingIntervalMs Interval in milliseconds between polling attempts (default: 2000ms).
 * @param maxPollingAttempts Maximum number of polling attempts before timing out (default: 60).
 * @param httpClient Optional custom OkHttpClient instance (auth interceptor will be added).
 */
data class EcfClientConfig(
    val baseUrl: String = Environment.TEST.url,
    val apiKey: String = System.getenv("ECF_DGII_API_KEY") ?: "",
    val pollingIntervalMs: Long = 2000L,
    val maxPollingAttempts: Int = 60,
    val httpClient: OkHttpClient? = null,
)

/**
 * Predefined API environments for the ECF DGII API.
 */
enum class Environment(val url: String) {
    TEST("https://api.test.ecfx.ssd.com.do"),
    CERTIFICATION("https://api.cert.ecfx.ssd.com.do"),
    PRODUCTION("https://api.prod.ecfx.ssd.com.do"),
}

/**
 * Thrown when polling for ECF processing result exceeds the maximum attempts.
 */
class EcfPollingTimeoutException(
    val messageId: UUID,
    val lastProgress: EcfProgress,
    val attempts: Int,
) : RuntimeException(
    "ECF processing timed out after $attempts attempts. MessageId: $messageId, last progress: $lastProgress"
)

/**
 * Thrown when ECF processing results in an error from the API.
 */
class EcfProcessingException(
    val ecfResponse: EcfResponse,
) : RuntimeException(
    "ECF processing failed. MessageId: ${ecfResponse.messageId}, " +
        "errors: ${ecfResponse.errors}, mensaje: ${ecfResponse.mensaje}"
)

/**
 * High-level client for the ECF DGII API (Dominican Republic Electronic Fiscal Receipts).
 *
 * Provides all raw API endpoints via [company], [ecf], [recepcion], and [aprobacionComercial] properties,
 * plus typed [sendEcf] overloads (one per e-CF type: 31, 32, 33, 34, 41, 43, 44, 45, 46, 47)
 * that handle submission, polling, and error handling automatically.
 *
 * Usage:
 * ```kotlin
 * val client = EcfClient(EcfClientConfig(
 *     baseUrl = Environment.CERTIFICATION.url,
 *     apiKey = "your-jwt-token"
 * ))
 *
 * // High-level: send a typed ECF and poll until done
 * val result = client.sendEcf(ecf31Document)
 *
 * // Low-level: use raw API endpoints directly
 * val companies = client.company.getCompanies()
 * ```
 */
class EcfClient(private val config: EcfClientConfig) {

    private val authenticatedClient: OkHttpClient = buildAuthenticatedClient()

    /** Raw Company API endpoints. */
    val company: CompanyApi = CompanyApi(config.baseUrl, authenticatedClient)

    /** Raw ECF API endpoints (issuer side). */
    val ecf: EcfApi = EcfApi(config.baseUrl, authenticatedClient)

    /** Raw Recepcion API endpoints (receptor side). */
    val recepcion: RecepcionApi = RecepcionApi(config.baseUrl, authenticatedClient)

    /** Raw Aprobacion Comercial (ACECF) API endpoints. */
    val aprobacionComercial: AprobacionComercialApi = AprobacionComercialApi(config.baseUrl, authenticatedClient)

    // -------------------------------------------------------------------------
    // ECF send + poll — typed overloads, one per ECF type
    // -------------------------------------------------------------------------

    /** Send a Factura de Crédito Fiscal Electrónica (e-CF 31) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf31ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf31(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Factura de Consumo Electrónica (e-CF 32) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf32ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf32(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Nota de Débito Electrónica (e-CF 33) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf33ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf33(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Nota de Crédito Electrónica (e-CF 34) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf34ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf34(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Compras Electrónico (e-CF 41) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf41ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf41(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Gastos Menores Electrónico (e-CF 43) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf43ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf43(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Regímenes Especiales Electrónico (e-CF 44) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf44ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf44(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Gubernamental Electrónico (e-CF 45) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf45ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf45(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Comprobante de Exportaciones Electrónico (e-CF 46) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf46ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf46(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    /** Send a Comprobante para Pagos al Exterior Electrónico (e-CF 47) and poll until completion. */
    suspend fun sendEcf(
        ecf: Ecf47ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse = sendInternal(
        ecf.encabezado.emisor.rncEmisor,
        { this.ecf.recepcionEcf47(ecf) },
        pollingIntervalMs,
        maxPollingAttempts,
    )

    private suspend fun sendInternal(
        rnc: String,
        submit: suspend () -> EcfResponse,
        pollingIntervalMs: Long,
        maxPollingAttempts: Int,
    ): EcfResponse {
        val submitResponse = submit()
        return pollForResult(rnc, submitResponse.messageId, pollingIntervalMs, maxPollingAttempts)
    }

    private suspend fun pollForResult(
        rnc: String,
        messageId: UUID,
        pollingIntervalMs: Long,
        maxPollingAttempts: Int,
    ): EcfResponse {
        var lastProgress = EcfProgress.New

        for (attempt in 1..maxPollingAttempts) {
            delay(pollingIntervalMs)

            val responses = ecf.getEcfById(rnc, messageId, includeEcfContent = true)
            if (responses.isEmpty()) continue

            val response = responses.firstOrNull { it.messageId == messageId } ?: responses.first()
            lastProgress = response.progress

            when (response.progress) {
                EcfProgress.Finished -> return response
                EcfProgress.Error -> throw EcfProcessingException(response)
                EcfProgress.New,
                EcfProgress.Processing,
                EcfProgress.UploadedToDgii -> continue
            }
        }

        throw EcfPollingTimeoutException(messageId, lastProgress, maxPollingAttempts)
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
