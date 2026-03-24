"""Polling utilities with exponential backoff for ECF processing."""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field
from typing import Any

from .exceptions import PollingMaxRetriesError, PollingTimeoutError


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


TERMINAL_PROGRESS = {"Completed", "Failed", "Rejected"}


async def poll_until_complete(
    poll_fn: Any,
    *,
    options: PollingOptions | None = None,
) -> Any:
    """Call *poll_fn* repeatedly until the result indicates completion.

    ``poll_fn`` must be an async callable that returns an object with a
    ``progress`` attribute (or dict key). Polling stops when ``progress``
    is in a terminal state.
    """
    opts = options or PollingOptions()
    delay = opts.initial_delay
    retries = 0
    start = time.monotonic()

    while True:
        result = await poll_fn()

        progress = getattr(result, "progress", None)
        if progress is None and isinstance(result, dict):
            progress = result.get("progress")

        progress_value = progress.value if hasattr(progress, "value") else str(progress)

        if progress_value in TERMINAL_PROGRESS:
            return result

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
