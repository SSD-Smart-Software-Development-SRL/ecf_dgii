package dom.com.ssd.ecfx.client;

import dom.com.ssd.ecfx.client.model.DgiiSubmissionState;
import dom.com.ssd.ecfx.client.model.EcfProgress;
import dom.com.ssd.ecfx.client.model.EcfResponse;

/**
 * Helpers to interpret {@link EcfResponse#getDgiiSubmissionState()} together with
 * {@link EcfResponse#getProgress()}.
 *
 * <ul>
 *   <li>{@code PendingReconciliation}: DGII's result is not confirmed yet. Keep polling; do not
 *       resend the document or reuse its eNCF.</li>
 *   <li>{@code NotReceived}: DGII confirmed it has no record of the document. Final, not accepted;
 *       the same eNCF may be submitted again as a new request.</li>
 * </ul>
 *
 * <p>A null or unknown ({@code UNKNOWN_DEFAULT_OPEN_API}) state falls back to {@code progress}.</p>
 */
public final class EcfStatus {

    private EcfStatus() {
    }

    /** True while DGII's result is unconfirmed: keep polling and never resend or reuse the eNCF. */
    public static boolean isPendingReconciliation(EcfResponse response) {
        return response != null && response.getDgiiSubmissionState() == DgiiSubmissionState.PENDING_RECONCILIATION;
    }

    /** True when DGII has no record of the document, so the same eNCF may be submitted again. */
    public static boolean canResubmit(EcfResponse response) {
        return response != null && response.getDgiiSubmissionState() == DgiiSubmissionState.NOT_RECEIVED;
    }

    /** True when polling should stop (finished, error or not received; never while pending reconciliation). */
    public static boolean isTerminal(EcfResponse response) {
        if (response == null || isPendingReconciliation(response)) {
            return false;
        }
        if (canResubmit(response)) {
            return true;
        }
        EcfProgress progress = response.getProgress();
        return progress == EcfProgress.FINISHED || progress == EcfProgress.ERROR;
    }
}
