package dom.com.ssd.ecfx.sdk

import dom.com.ssd.ecfx.sdk.infrastructure.Serializer
import dom.com.ssd.ecfx.sdk.models.DgiiSubmissionState
import dom.com.ssd.ecfx.sdk.models.EcfProgress
import dom.com.ssd.ecfx.sdk.models.EcfResponse

/**
 * DGII's result is not confirmed yet ([DgiiSubmissionState.PendingReconciliation]).
 * Keep polling; do not resend the document or reuse its eNCF.
 */
val EcfResponse.isPendingReconciliation: Boolean
    get() = dgiiSubmissionState == DgiiSubmissionState.PendingReconciliation

/**
 * DGII confirmed it has no record of the document ([DgiiSubmissionState.NotReceived]):
 * it was not accepted, the eNCF was not used and the same eNCF may be submitted again.
 */
val EcfResponse.canResubmit: Boolean
    get() = dgiiSubmissionState == DgiiSubmissionState.NotReceived

/**
 * True when polling should stop: never while pending reconciliation, always when not received,
 * otherwise when [EcfResponse.progress] is `Finished` or `Error`. Null states fall back to progress.
 */
val EcfResponse.isTerminal: Boolean
    get() = when {
        isPendingReconciliation -> false
        canResubmit -> true
        else -> progress == EcfProgress.Finished || progress == EcfProgress.Error
    }

/**
 * Makes the shared JSON parser tolerate values added to the API after this SDK was built:
 * an unknown enum value in an optional field (e.g. a new `dgiiSubmissionState`) decodes as
 * null instead of failing the whole response. Skipped if the app already configured
 * [Serializer] itself.
 */
internal object EcfJsonDefaults {
    init {
        runCatching {
            val custom = Serializer.kotlinxSerializationJsonConfiguration
            Serializer.kotlinxSerializationJsonConfiguration = {
                coerceInputValues = true
                custom()
            }
        }
    }

    fun install() = Unit
}
