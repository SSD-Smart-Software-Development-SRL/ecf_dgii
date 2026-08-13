from unittest.mock import AsyncMock, patch

import pytest

from ecf_dgii import EcfProcessingError, EcfProgress, EcfResponse
from ecf_dgii.client import EcfClient


@pytest.mark.asyncio
async def test_send_ecf_success() -> None:
    client = EcfClient(api_key="mock-key")

    mock_post_res = AsyncMock()
    mock_post_res.status_code.value = 200
    mock_post_res.parsed = EcfResponse.from_dict(
        {
            "messageId": "11111111-1111-1111-1111-111111111111",
            "timestamp": "2026-06-14T09:00:00",
            "fechaEmision": "2026-06-14",
            "queueName": "test-queue",
            "includeEcfContent": False,
            "ecfContent": "",
            "tipoEcf": "FacturaDeCreditoFiscalElectronica",
            "encf": "E310000000001",
            "rncEmisor": "131460941",
            "rncReceptor": None,
            "montoTotal": 1000.0,
            "fileName": None,
            "tenantId": "11111111-1111-1111-1111-111111111111",
            "estatus": None,
            "codSec": None,
            "fechaFirma": None,
            "mensaje": None,
            "errors": None,
            "progress": "New",
            "emisorReceptorErrors": None,
            "secuenciaUtilizada": None,
            "dgiiEnvironment": "Test",
        }
    )

    mock_get_res = AsyncMock()
    mock_get_res.status_code.value = 200
    mock_get_res.parsed = [
        EcfResponse.from_dict(
            {
                "messageId": "11111111-1111-1111-1111-111111111111",
                "timestamp": "2026-06-14T09:00:00",
                "fechaEmision": "2026-06-14",
                "queueName": "test-queue",
                "includeEcfContent": False,
                "ecfContent": "",
                "tipoEcf": "FacturaDeCreditoFiscalElectronica",
                "encf": "E310000000001",
                "rncEmisor": "131460941",
                "rncReceptor": None,
                "montoTotal": 1000.0,
                "fileName": None,
                "tenantId": "11111111-1111-1111-1111-111111111111",
                "estatus": None,
                "codSec": None,
                "fechaFirma": None,
                "mensaje": None,
                "errors": None,
                "progress": "Finished",
                "emisorReceptorErrors": None,
                "secuenciaUtilizada": None,
                "dgiiEnvironment": "Test",
            }
        )
    ]

    ecf_payload = {
        "encabezado": {
            "idDoc": {"tipoeCF": "FacturaDeCreditoFiscalElectronica", "encf": "E310000000001"},
            "emisor": {"rncEmisor": "131460941"},
        }
    }

    with (
        patch("ecf_dgii.generated.api.ecf.recepcion_ecf_31.asyncio_detailed", return_value=mock_post_res),
        patch("ecf_dgii.client.EcfClient.query_ecf", return_value=mock_get_res.parsed),
    ):
        result = await client.send_ecf(ecf_payload)
        assert result.progress == EcfProgress.FINISHED
        assert str(result.message_id) == "11111111-1111-1111-1111-111111111111"


@pytest.mark.asyncio
async def test_send_ecf_error() -> None:
    client = EcfClient(api_key="mock-key")

    mock_post_res = AsyncMock()
    mock_post_res.status_code.value = 200
    mock_post_res.parsed = EcfResponse.from_dict(
        {
            "messageId": "11111111-1111-1111-1111-111111111111",
            "timestamp": "2026-06-14T09:00:00",
            "fechaEmision": "2026-06-14",
            "queueName": "test-queue",
            "includeEcfContent": False,
            "ecfContent": "",
            "tipoEcf": "FacturaDeCreditoFiscalElectronica",
            "encf": "E310000000001",
            "rncEmisor": "131460941",
            "rncReceptor": None,
            "montoTotal": 1000.0,
            "fileName": None,
            "tenantId": "11111111-1111-1111-1111-111111111111",
            "estatus": None,
            "codSec": None,
            "fechaFirma": None,
            "mensaje": None,
            "errors": None,
            "progress": "New",
            "emisorReceptorErrors": None,
            "secuenciaUtilizada": None,
            "dgiiEnvironment": "Test",
        }
    )

    mock_get_res = AsyncMock()
    mock_get_res.status_code.value = 200
    mock_get_res.parsed = [
        EcfResponse.from_dict(
            {
                "messageId": "11111111-1111-1111-1111-111111111111",
                "timestamp": "2026-06-14T09:00:00",
                "fechaEmision": "2026-06-14",
                "queueName": "test-queue",
                "includeEcfContent": False,
                "ecfContent": "",
                "tipoEcf": "FacturaDeCreditoFiscalElectronica",
                "encf": "E310000000001",
                "rncEmisor": "131460941",
                "rncReceptor": None,
                "montoTotal": 1000.0,
                "fileName": None,
                "tenantId": "11111111-1111-1111-1111-111111111111",
                "estatus": None,
                "codSec": None,
                "fechaFirma": None,
                "mensaje": None,
                "errors": "RNC Comprador invalido",
                "progress": "Error",
                "emisorReceptorErrors": None,
                "secuenciaUtilizada": None,
                "dgiiEnvironment": "Test",
            }
        )
    ]

    ecf_payload = {
        "encabezado": {
            "idDoc": {"tipoeCF": "FacturaDeCreditoFiscalElectronica", "encf": "E310000000001"},
            "emisor": {"rncEmisor": "131460941"},
        }
    }

    with (
        patch("ecf_dgii.generated.api.ecf.recepcion_ecf_31.asyncio_detailed", return_value=mock_post_res),
        patch("ecf_dgii.client.EcfClient.query_ecf", return_value=mock_get_res.parsed),
    ):
        with pytest.raises(EcfProcessingError) as exc_info:
            await client.send_ecf(ecf_payload)

        assert exc_info.value.message == "RNC Comprador invalido"
        assert exc_info.value.status_code == 0
