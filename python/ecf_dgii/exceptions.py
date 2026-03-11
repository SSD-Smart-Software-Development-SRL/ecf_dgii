"""Exceptions for the ECF DGII client."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from .models import EcfResponse


class EcfApiError(Exception):
    """Base exception for ECF API errors."""

    def __init__(self, message: str, status_code: Optional[int] = None, detail: Any = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.detail = detail


class EcfValidationError(EcfApiError):
    """Raised when the API returns a 400 Bad Request."""


class EcfAuthenticationError(EcfApiError):
    """Raised when the API returns a 401 Unauthorized."""


class EcfForbiddenError(EcfApiError):
    """Raised when the API returns a 403 Forbidden."""


class EcfNotFoundError(EcfApiError):
    """Raised when the API returns a 404 Not Found."""


class EcfServerError(EcfApiError):
    """Raised when the API returns a 500 Internal Server Error."""


class EcfProcessingError(EcfApiError):
    """Raised when ECF processing finishes with an error status."""

    def __init__(self, message: str, response: EcfResponse) -> None:
        super().__init__(message)
        self.response = response


class PollingTimeoutError(EcfApiError):
    """Raised when polling exceeds the configured timeout."""


class PollingMaxRetriesError(EcfApiError):
    """Raised when polling exceeds the maximum number of retries."""

    def __init__(self, retries: int) -> None:
        super().__init__(f"Polling exceeded maximum retries ({retries})")
        self.retries = retries
