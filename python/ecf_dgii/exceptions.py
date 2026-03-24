"""Typed exceptions for the ECF DGII SDK."""

from __future__ import annotations

from typing import Any


class EcfApiError(Exception):
    """Base exception for all ECF API errors."""

    def __init__(
        self,
        status_code: int,
        message: str,
        *,
        detail: Any = None,
    ) -> None:
        self.status_code = status_code
        self.message = message
        self.detail = detail
        super().__init__(f"[{status_code}] {message}")


class EcfValidationError(EcfApiError):
    """400 Bad Request - validation or client errors."""


class EcfAuthenticationError(EcfApiError):
    """401 Unauthorized - invalid or missing API key."""


class EcfForbiddenError(EcfApiError):
    """403 Forbidden - insufficient permissions."""


class EcfNotFoundError(EcfApiError):
    """404 Not Found."""


class EcfServerError(EcfApiError):
    """5xx Server Error."""


class EcfProcessingError(EcfApiError):
    """ECF was rejected by DGII during processing."""


class PollingTimeoutError(EcfApiError):
    """Polling exceeded the configured timeout."""

    def __init__(self, message: str = "Polling timed out") -> None:
        super().__init__(status_code=0, message=message)


class PollingMaxRetriesError(EcfApiError):
    """Polling exceeded the maximum number of retries."""

    def __init__(self, message: str = "Polling max retries exceeded") -> None:
        super().__init__(status_code=0, message=message)


_STATUS_MAP: dict[int, type[EcfApiError]] = {
    400: EcfValidationError,
    401: EcfAuthenticationError,
    403: EcfForbiddenError,
    404: EcfNotFoundError,
}


def raise_for_status(status_code: int, body: Any) -> None:
    """Raise a typed exception for non-2xx responses."""
    if 200 <= status_code < 300:
        return

    detail = body if isinstance(body, dict) else None
    message = ""
    if isinstance(body, dict):
        message = body.get("detail", body.get("title", str(body)))
    else:
        message = str(body) if body else f"HTTP {status_code}"

    if status_code >= 500:
        raise EcfServerError(status_code, message, detail=detail)

    exc_cls = _STATUS_MAP.get(status_code, EcfApiError)
    raise exc_cls(status_code, message, detail=detail)
