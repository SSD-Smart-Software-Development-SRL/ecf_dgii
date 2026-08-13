from unittest.mock import AsyncMock, patch

import pytest

from ecf_dgii.client import EcfClient


@pytest.mark.asyncio
async def test_client_renamed_methods() -> None:
    client = EcfClient(api_key="mock-key")

    mock_resp = AsyncMock()
    mock_resp.status_code.value = 200

    with (
        patch("ecf_dgii.generated.api.company.get_current_certificate.asyncio_detailed", return_value=mock_resp) as m1,
        patch(
            "ecf_dgii.generated.api.company.update_certificate_company.asyncio_detailed", return_value=mock_resp
        ) as m2,
        patch(
            "ecf_dgii.generated.api.recepcion.get_ecf_receptor_by_message_id.asyncio_detailed", return_value=mock_resp
        ) as m3,
        patch(
            "ecf_dgii.generated.api.recepcion.send_aprobacion_comercial.asyncio_detailed", return_value=mock_resp
        ) as m4,
        patch("ecf_dgii.generated.api.dgii.consulta_directorio_listado.asyncio_detailed", return_value=mock_resp) as m5,
        patch(
            "ecf_dgii.generated.api.dgii.estatus_servicios_obtener_estatus.asyncio_detailed", return_value=mock_resp
        ) as m6,
        patch("ecf_dgii.generated.api.api_key.new_company_api_key.asyncio_detailed", return_value=mock_resp) as m7,
        patch("ecf_dgii.generated.api.ecf.firmar_semilla.asyncio_detailed", return_value=mock_resp) as m8,
    ):
        await client.get_certificate("131460941")
        m1.assert_called_once()

        await client.update_certificate("131460941", certificate=b"cert", password="pwd")
        m2.assert_called_once()

        await client.get_ecf_reception_request("131460941", "11111111-1111-1111-1111-111111111111")
        m3.assert_called_once()

        from ecf_dgii.generated.models import EstadoType, SendAcecfRequest

        await client.aprobacion_comercial(
            "11111111-1111-1111-1111-111111111111", SendAcecfRequest(estado_type=EstadoType.ECFACEPTADO)
        )
        m4.assert_called_once()

        await client.consulta_directorio_listado("131460941")
        m5.assert_called_once()

        await client.estatus_servicios("131460941")
        m6.assert_called_once()

        from ecf_dgii.generated.models import NewCompanyApiKey

        await client.create_api_key(NewCompanyApiKey(rnc="131460941"))
        m7.assert_called_once()

        await client.firmar_semilla("131460941", xml=b"<xml></xml>")
        m8.assert_called_once()
