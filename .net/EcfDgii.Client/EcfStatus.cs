using EcfDgii.Client.Generated.Models;

namespace EcfDgii.Client
{
    /// <summary>
    /// Helpers to interpret <see cref="EcfResponse.DgiiSubmissionState"/> together with <see cref="EcfResponse.Progress"/>.
    /// </summary>
    public static class EcfStatus
    {
        /// <summary>
        /// The DGII submission state, or null when absent, null or a value this SDK version does not know.
        /// </summary>
        public static DgiiSubmissionState? GetDgiiSubmissionState(this EcfResponse response)
            => response?.DgiiSubmissionState?.DgiiSubmissionState;

        /// <summary>
        /// DGII's result is not confirmed yet (<c>PendingReconciliation</c>): keep polling and do not
        /// resend the document or reuse its eNCF.
        /// </summary>
        public static bool IsPendingReconciliation(this EcfResponse response)
            => response.GetDgiiSubmissionState() == Generated.Models.DgiiSubmissionState.PendingReconciliation;

        /// <summary>
        /// DGII confirmed it has no record of the document (<c>NotReceived</c>): it was not accepted, the
        /// eNCF was not used and the same eNCF may be submitted again as a new request.
        /// </summary>
        public static bool CanResubmit(this EcfResponse response)
            => response.GetDgiiSubmissionState() == Generated.Models.DgiiSubmissionState.NotReceived;

        /// <summary>
        /// True when polling should stop: never while pending reconciliation, always when not received,
        /// otherwise when <see cref="EcfResponse.Progress"/> is Finished or Error.
        /// </summary>
        public static bool IsTerminal(this EcfResponse response)
        {
            if (response == null || response.IsPendingReconciliation())
                return false;
            if (response.CanResubmit())
                return true;
            return response.Progress == EcfProgress.Finished || response.Progress == EcfProgress.Error;
        }
    }
}
