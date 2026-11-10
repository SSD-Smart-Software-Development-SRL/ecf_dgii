// EcfStatus.swift
// Helpers for EcfResponse.dgiiSubmissionState (hand-written, not generated).

import Foundation

extension EcfResponse {
    /// DGII's result is not confirmed yet (`PendingReconciliation`).
    /// Keep polling; do not resend the document or reuse its eNCF.
    public var isPendingReconciliation: Bool {
        dgiiSubmissionState == .pendingReconciliation
    }

    /// DGII confirmed it has no record of the document (`NotReceived`): it was not accepted,
    /// the eNCF was not used and the same eNCF may be submitted again as a new request.
    public var canResubmit: Bool {
        dgiiSubmissionState == .notReceived
    }

    /// True when polling should stop: never while pending reconciliation, always when not
    /// received, otherwise when `progress` is `.finished` or `.error`.
    /// A nil or unknown (`.unknownDefaultOpenApi`) state falls back to `progress`.
    public var isTerminal: Bool {
        if isPendingReconciliation { return false }
        if canResubmit { return true }
        return progress == .finished || progress == .error
    }
}

extension EcfProcessingError {
    /// True when DGII never received the document; the same eNCF may be submitted again.
    public var canResubmit: Bool { response.canResubmit }
}
