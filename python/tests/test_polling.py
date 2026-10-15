"""Tests for poll_until_complete terminal-state handling."""

from __future__ import annotations

import pytest

from ecf_dgii import PollingMaxRetriesError, PollingOptions
from ecf_dgii.generated.models import EcfProgress
from ecf_dgii.polling import poll_until_complete

FAST = PollingOptions(initial_delay=0, max_delay=0, timeout=5)


class _Result:
    def __init__(self, progress):
        self.progress = progress


def _sequence(*progresses):
    items = iter(progresses)

    async def poll():
        return _Result(next(items))

    return poll


@pytest.mark.parametrize("terminal", [EcfProgress.FINISHED, EcfProgress.ERROR])
async def test_stops_on_terminal_progress(terminal):
    result = await poll_until_complete(_sequence(EcfProgress.NEW, EcfProgress.PROCESSING, terminal), options=FAST)
    assert result.progress == terminal


async def test_accepts_plain_dicts():
    async def poll():
        return {"progress": "Finished"}

    assert (await poll_until_complete(poll, options=FAST))["progress"] == "Finished"


async def test_max_retries():
    async def poll():
        return _Result(EcfProgress.PROCESSING)

    with pytest.raises(PollingMaxRetriesError):
        await poll_until_complete(poll, options=PollingOptions(initial_delay=0, max_delay=0, max_retries=3))
