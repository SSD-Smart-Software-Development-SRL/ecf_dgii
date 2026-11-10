"""Polling utilities with exponential backoff for ECF processing."""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field
from typing import Any

from .exceptions import PollingMaxRetriesError, PollingTimeoutError
from .generated.types import Unset


@dataclass
class PollingOptions:
    """Configuration for polling ECF processing status.

    Attributes:
        initial_delay: Seconds to wait before the first poll.
        max_delay: Maximum seconds between polls.
        max_retries: Maximum number of poll attempts (0 = unlimited).
        backoff_multiplier: Multiplier applied to delay each iteration.
        timeout: Total timeout in seconds (0 = unlimited).
    """

    initial_delay: float = 2.0
    max_delay: float = 30.0
    max_retries: int = 0
    backoff_multiplier: float = 1.5
    timeout: float = 300.0


TERMINAL_PROGRESS = {"Finished", "Error"}

# ``EcfResponse.dgii_submission_state`` values that override ``progress``.
PENDING_RECONCILIATION = "PendingReconciliation"
"""DGII's answer is not confirmed yet: keep polling; never resend or reuse the eNCF."""
NOT_RECEIVED = "NotReceived"
"""DGII has no record of the document: final, not accepted; the same eNCF may be sent again."""


def _value(result: Any, attr: str, key: str) -> str | None:
    value = getattr(result, attr, None)
    if value is None and isinstance(result, dict):
        value = result.get(key)
    if value is None or isinstance(value, Unset):
        return None
    return str(value.value if hasattr(value, "value") else value)


def submission_state(result: Any) -> str | None:
    """Return ``dgii_submission_state`` as a plain string (``None`` when absent or null).

    Unknown values from newer API versions are returned as-is instead of failing.
    """
    return _value(result, "dgii_submission_state", "dgiiSubmissionState")


def is_pending_reconciliation(result: Any) -> bool:
    """True while DGII's result is unconfirmed. Do not resend or reuse the eNCF."""
    return submission_state(result) == PENDING_RECONCILIATION


def can_resubmit(result: Any) -> bool:
    """True when DGII confirmed it never received the document (``NotReceived``).

    The e-CF was not accepted and its eNCF was not used, so the same eNCF may be
    submitted again as a new request.
    """
    return submission_state(result) == NOT_RECEIVED


def is_terminal(result: Any) -> bool:
    """True when polling should stop.

    ``PendingReconciliation`` keeps polling and ``NotReceived`` stops it, whatever
    ``progress`` says; otherwise ``progress`` must be ``Finished`` or ``Error``.
    """
    state = submission_state(result)
    if state == PENDING_RECONCILIATION:
        return False
    if state == NOT_RECEIVED:
        return True
    return _value(result, "progress", "progress") in TERMINAL_PROGRESS


async def poll_until_complete(
    poll_fn: Any,
    *,
    options: PollingOptions | None = None,
) -> Any:
    """Call *poll_fn* repeatedly until the result indicates completion.

    ``poll_fn`` must be an async callable that returns an ``EcfResponse`` (or
    a dict with the same keys). Polling stops when :func:`is_terminal` is true.
    """
    opts = options or PollingOptions()
    delay = opts.initial_delay
    retries = 0
    start = time.monotonic()

    while True:
        result = await poll_fn()

        if is_terminal(result):
            return result

        progress_value = _value(result, "progress", "progress")

        if opts.timeout and (time.monotonic() - start) >= opts.timeout:
            raise PollingTimeoutError(
                f"Polling timed out after {opts.timeout}s (last progress: {progress_value})"
            )

        retries += 1
        if opts.max_retries and retries >= opts.max_retries:
            raise PollingMaxRetriesError(
                f"Polling exceeded {opts.max_retries} retries (last progress: {progress_value})"
            )

        await asyncio.sleep(delay)
        delay = min(delay * opts.backoff_multiplier, opts.max_delay)
