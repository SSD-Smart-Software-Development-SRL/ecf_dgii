package dom.com.ssd.ecfx.sdk

import dom.com.ssd.ecfx.sdk.api.CompanyApi
import dom.com.ssd.ecfx.sdk.api.EcfApi
import dom.com.ssd.ecfx.sdk.api.RecepcionApi
import dom.com.ssd.ecfx.sdk.models.ECF
import dom.com.ssd.ecfx.sdk.models.EcfProgress
import dom.com.ssd.ecfx.sdk.models.EcfResponse
import dom.com.ssd.ecfx.sdk.models.TipoeCFType
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
 * Provides all raw API endpoints via [company], [ecf], and [recepcion] properties,
 * plus a convenient [sendEcf] method that handles ECF type routing, submission,
 * polling, and error handling automatically.
 *
 * Usage:
 * ```kotlin
 * val client = EcfClient(EcfClientConfig(
 *     baseUrl = Environment.CERTIFICATION.url,
 *     apiKey = "your-jwt-token"
 * ))
 *
 * // High-level: send ECF with automatic routing and polling
 * val result = client.sendEcf(ecfDocument)
 *
 * // Low-level: use raw API endpoints directly
 * val companies = client.company.getCompanies()
 * ```
 */
class EcfClient(private val config: EcfClientConfig) {

    private val authenticatedClient: OkHttpClient = buildAuthenticatedClient()

    /** Raw Company API endpoints. */
    val company: CompanyApi = CompanyApi(config.baseUrl, authenticatedClient)

    /** Raw ECF API endpoints. */
    val ecf: EcfApi = EcfApi(config.baseUrl, authenticatedClient)

    /** Raw Recepcion API endpoints. */
    val recepcion: RecepcionApi = RecepcionApi(config.baseUrl, authenticatedClient)

    /**
     * Sends an ECF to the DGII, automatically routing it to the correct endpoint
     * based on the ECF type (tipoeCF) in the document header, then polls until
     * processing is complete and returns the final result.
     *
     * This method encapsulates:
     * - **Routing**: Determines the correct `/ecf/{type}` endpoint from `encabezado.idDoc.tipoeCF`
     * - **Submission**: Sends the ECF to the API
     * - **Polling**: Repeatedly checks the processing status using the returned message ID
     * - **Error handling**: Throws [EcfProcessingException] on processing errors,
     *   [EcfPollingTimeoutException] on timeout
     *
     * @param ecfDocument The ECF document to send.
     * @param pollingIntervalMs Override the default polling interval for this call.
     * @param maxPollingAttempts Override the default max polling attempts for this call.
     * @return The final [EcfResponse] with the DGII processing result.
     * @throws EcfProcessingException if the ECF processing fails.
     * @throws EcfPollingTimeoutException if polling exceeds the maximum attempts.
     */
    suspend fun sendEcf(
        ecfDocument: ECF,
        pollingIntervalMs: Long = config.pollingIntervalMs,
        maxPollingAttempts: Int = config.maxPollingAttempts,
    ): EcfResponse {
        val tipoEcf = ecfDocument.encabezado.idDoc.tipoeCF
        val rnc = ecfDocument.encabezado.emisor.rncEmisor

        val submitResponse = routeAndSubmit(tipoEcf, ecfDocument)
        val messageId = submitResponse.messageId

        return pollForResult(rnc, messageId, pollingIntervalMs, maxPollingAttempts)
    }

    private suspend fun routeAndSubmit(tipoEcf: TipoeCFType, ecfDocument: ECF): EcfResponse {
        return when (tipoEcf) {
            TipoeCFType.FacturaDeCreditoFiscalElectronica -> ecf.recepcionEcf31(ecfDocument)
            TipoeCFType.FacturaDeConsumoElectronica -> ecf.recepcionEcf32(ecfDocument)
            TipoeCFType.NotaDeDebitoElectronica -> ecf.recepcionEcf33(ecfDocument)
            TipoeCFType.NotaDeCreditoElectronica -> ecf.recepcionEcf34(ecfDocument)
            TipoeCFType.ComprasElectronico -> ecf.recepcionEcf41(ecfDocument)
            TipoeCFType.GastosMenoresElectronico -> ecf.recepcionEcf43(ecfDocument)
            TipoeCFType.RegimenesEspecialesElectronico -> ecf.recepcionEcf44(ecfDocument)
            TipoeCFType.GubernamentalElectronico -> ecf.recepcionEcf45(ecfDocument)
            TipoeCFType.ComprobanteDeExportacionesElectronico -> ecf.recepcionEcf46(ecfDocument)
            TipoeCFType.ComprobanteParaPagosAlExteriorElectronico -> ecf.recepcionEcf47(ecfDocument)
        }
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

            val response = responses.first()
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
