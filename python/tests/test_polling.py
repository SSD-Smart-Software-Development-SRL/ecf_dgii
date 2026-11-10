"""Tests for poll_until_complete terminal-state handling."""

from __future__ import annotations

import pytest

from ecf_dgii import PollingMaxRetriesError, PollingOptions
from ecf_dgii.generated.models import EcfProgress
from ecf_dgii.polling import can_resubmit, is_pending_reconciliation, is_terminal, poll_until_complete

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


class _Submission:
    def __init__(self, progress, state):
        self.progress = progress
        self.dgii_submission_state = state


async def test_pending_reconciliation_keeps_polling_even_if_progress_looks_final():
    items = iter([_Submission("Error", "PendingReconciliation"), _Submission("Finished", "Accepted")])

    async def poll():
        return next(items)

    result = await poll_until_complete(poll, options=FAST)
    assert result.dgii_submission_state == "Accepted"


async def test_not_received_is_terminal_and_resubmittable():
    items = iter([_Submission("UploadedToDgii", "Sending"), _Submission("Error", "NotReceived")])

    async def poll():
        return next(items)

    result = await poll_until_complete(poll, options=FAST)
    assert can_resubmit(result)
    assert not is_pending_reconciliation(result)


def test_status_helpers_accept_dicts_and_unknown_values():
    assert is_pending_reconciliation({"progress": "UploadedToDgii", "dgiiSubmissionState": "PendingReconciliation"})
    assert not is_terminal({"progress": "UploadedToDgii", "dgiiSubmissionState": "PendingReconciliation"})
    assert can_resubmit({"progress": "Error", "dgiiSubmissionState": "NotReceived"})
    assert is_terminal({"progress": "Finished", "dgiiSubmissionState": "SomeFutureState"})
    assert not can_resubmit({"progress": "Error"})
    assert not is_terminal({"progress": "Processing", "dgiiSubmissionState": None})
