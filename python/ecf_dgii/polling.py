"""Polling utilities with exponential backoff for ECF processing."""

from __future__ import annotations

import asyncio
import time
from collections.abc import Callable, Coroutine
from dataclasses import dataclass
from typing import Any, TypeVar

from .exceptions import PollingMaxRetriesError, PollingTimeoutError

T = TypeVar("T")


@dataclass
class PollingOptions:
    """Configuration for polling ECF processing status.

    Attributes:
        initial_delay: Seconds to wait before the first poll. Default: 1.0 (matching TS 1000ms).
        max_delay: Maximum seconds between polls. Default: 30.0 (matching TS 30000ms).
        max_retries: Maximum number of poll attempts. Default: 60 (matching TS 60).
        backoff_multiplier: Multiplier applied to delay each iteration. Default: 2.0 (matching TS 2).
        timeout: Total timeout in seconds. Optional.
    """

    initial_delay: float = 1.0
    max_delay: float = 30.0
    max_retries: int = 60
    backoff_multiplier: float = 2.0
    timeout: float | None = None


async def poll_until_complete(
    poll_fn: Callable[[], Coroutine[Any, Any, T]],
    is_complete: Callable[[T], bool],
    options: PollingOptions | None = None,
) -> T:
    """Call *poll_fn* repeatedly until `is_complete` returns True, using exponential backoff."""
    opts = options or PollingOptions()
    delay = opts.initial_delay
    retries = 0
    start = time.monotonic()

    while True:
        result = await poll_fn()

        if is_complete(result):
            return result

        retries += 1
        if opts.max_retries and retries >= opts.max_retries:
            raise PollingMaxRetriesError(f"Polling exceeded {opts.max_retries} retries")

        if opts.timeout is not None and (time.monotonic() - start) >= opts.timeout:
            raise PollingTimeoutError(f"Polling timed out after {opts.timeout}s")

        await asyncio.sleep(delay)
        delay = min(delay * opts.backoff_multiplier, opts.max_delay)
