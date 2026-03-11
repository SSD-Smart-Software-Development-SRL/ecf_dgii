"""Polling utilities with exponential backoff."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Awaitable, Callable, TypeVar

from .exceptions import PollingMaxRetriesError, PollingTimeoutError

T = TypeVar("T")


@dataclass
class PollingOptions:
    """Configuration for polling behaviour."""

    initial_delay: float = 1.0
    """Initial delay between polls in seconds."""

    max_delay: float = 30.0
    """Maximum delay between polls in seconds."""

    max_retries: int = 60
    """Maximum number of retries before giving up."""

    backoff_multiplier: float = 2.0
    """Multiplier applied to the delay after each retry."""

    timeout: float | None = None
    """Total timeout in seconds. ``None`` means no timeout."""


DEFAULT_POLLING_OPTIONS = PollingOptions()


async def poll_until_complete(
    fn: Callable[[], Awaitable[T]],
    is_complete: Callable[[T], bool],
    options: PollingOptions | None = None,
) -> T:
    """Poll *fn* until *is_complete* returns ``True``, using exponential backoff.

    Parameters
    ----------
    fn:
        Async callable invoked on each poll iteration.
    is_complete:
        Predicate returning ``True`` when polling should stop.
    options:
        Optional polling configuration.

    Returns
    -------
    T
        The final result from *fn* once *is_complete* is satisfied.

    Raises
    ------
    PollingTimeoutError
        If the total *timeout* is exceeded.
    PollingMaxRetriesError
        If *max_retries* polls have been performed.
    """
    opts = options or DEFAULT_POLLING_OPTIONS
    delay = opts.initial_delay
    retries = 0
    elapsed = 0.0

    while True:
        result = await fn()

        if is_complete(result):
            return result

        retries += 1

        if retries >= opts.max_retries:
            raise PollingMaxRetriesError(opts.max_retries)

        if opts.timeout is not None and elapsed >= opts.timeout:
            raise PollingTimeoutError("Polling timed out")

        await asyncio.sleep(delay)
        elapsed += delay
        delay = min(delay * opts.backoff_multiplier, opts.max_delay)
