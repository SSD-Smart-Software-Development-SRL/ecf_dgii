from enum import StrEnum


class DgiiSubmissionStateType1(StrEnum):
    ACCEPTED = "Accepted"
    NOTRECEIVED = "NotReceived"
    PENDINGRECONCILIATION = "PendingReconciliation"
    PREPARED = "Prepared"
    REJECTED = "Rejected"
    RESERVATIONBLOCKED = "ReservationBlocked"
    SENDING = "Sending"
    VALIDATIONFAILED = "ValidationFailed"

    def __str__(self) -> str:
        return str(self.value)
