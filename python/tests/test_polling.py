from unittest.mock import AsyncMock

import pytest

from ecf_dgii.exceptions import PollingMaxRetriesError
from ecf_dgii.polling import PollingOptions, poll_until_complete


@pytest.mark.asyncio
async def test_poll_until_complete_success() -> None:
    mock_fn = AsyncMock()
    mock_fn.side_effect = ["Processing", "Processing", "Finished"]

    result = await poll_until_complete(
        mock_fn,
        is_complete=lambda r: r == "Finished",
        options=PollingOptions(initial_delay=0.01, max_delay=0.05, max_retries=5),
    )

    assert result == "Finished"
    assert mock_fn.call_count == 3


@pytest.mark.asyncio
async def test_poll_until_complete_max_retries() -> None:
    mock_fn = AsyncMock()
    mock_fn.return_value = "Processing"

    with pytest.raises(PollingMaxRetriesError):
        await poll_until_complete(
            mock_fn,
            is_complete=lambda r: r == "Finished",
            options=PollingOptions(initial_delay=0.01, max_delay=0.05, max_retries=2),
        )
