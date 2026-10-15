"""Behavioural tests for the high-level EcfClient (HTTP mocked with pytest-httpx)."""

from __future__ import annotations

import datetime
import re
import uuid

import httpx
import pytest

from ecf_dgii import (
    EcfClient,
    EcfConnectionError,
    EcfProcessingError,
    EcfRateLimitError,
    EcfServerError,
    EcfValidationError,
    PollingOptions,
)
from ecf_dgii.generated.models import (
    Ecf32Comprador,
    Ecf32ECF,
    Ecf32Emisor,
    Ecf32Encabezado,
    Ecf32IdDoc,
    Ecf32IndicadorBienoServicioType,
    Ecf32IndicadorFacturacionType,
    Ecf32Item,
    Ecf32TipoIngresosValidationType,
    Ecf32TipoPagoType,
    Ecf32Totales,
    Ecf32VersionType,
    EcfProgress,
    TipoeCFType,
)

BASE = "https://api.test.ecfx.ssd.com.do"
RNC = "131000001"
MESSAGE_ID = str(uuid.UUID(int=1))
FAST = PollingOptions(initial_delay=0, max_delay=0, timeout=5)


def ecf_response(progress: str = "New", estatus: str | None = None, **overrides):
    body = {
        "messageId": MESSAGE_ID,
        "timestamp": "2026-10-15T10:00:00Z",
        "fechaEmision": "2026-10-15",
        "queueName": "ecf-32",
        "includeEcfContent": False,
        "ecfContent": "",
        "tipoEcf": "FacturaDeConsumoElectronica",
        "encf": "E320000000001",
        "rncEmisor": RNC,
        "rncReceptor": None,
        "montoTotal": 118.0,
        "fileName": None,
        "tenantId": str(uuid.UUID(int=2)),
        "estatus": estatus,
        "codSec": "Ab12Cd" if estatus else None,
        "fechaFirma": "2026-10-15T10:00:05Z" if estatus else None,
        "mensaje": None,
        "errors": None,
        "progress": progress,
        "emisorReceptorErrors": None,
        "secuenciaUtilizada": None,
        "dgiiEnvironment": "Test",
    }
    body.update(overrides)
    return body


def minimal_ecf32() -> Ecf32ECF:
    return Ecf32ECF(
        encabezado=Ecf32Encabezado(
            version=Ecf32VersionType.VERSION1_0,
            id_doc=Ecf32IdDoc(
                tipoe_cf=TipoeCFType.FACTURADECONSUMOELECTRONICA,
                encf="E320000000001",
                tipo_ingresos=Ecf32TipoIngresosValidationType.VALUE_0,
                tipo_pago=Ecf32TipoPagoType.CONTADO,
            ),
            emisor=Ecf32Emisor(
                rnc_emisor=RNC,
                razon_social_emisor="Empresa SRL",
                direccion_emisor="Calle 1",
                fecha_emision=datetime.date(2026, 10, 15),
            ),
            comprador=Ecf32Comprador(),
            totales=Ecf32Totales(
                monto_total=118.0,
                monto_gravado_total=100.0,
                monto_gravado_i1=100.0,
                itbi_s1=18,
                total_itbis=18.0,
                total_itbis1=18.0,
            ),
        ),
        detalles_items=[
            Ecf32Item(
                numero_linea=1,
                indicador_facturacion=Ecf32IndicadorFacturacionType.ITBIS1_18PERCENT,
                nombre_item="Producto",
                indicador_bieno_servicio=Ecf32IndicadorBienoServicioType.BIEN,
                cantidad_item=1,
                precio_unitario_item=100.0,
                monto_item=100.0,
            )
        ],
    )


def test_ecf32_serializes_with_api_field_names():
    body = minimal_ecf32().to_dict()
    id_doc = body["encabezado"]["idDoc"]
    assert id_doc["tipoeCF"] == "FacturaDeConsumoElectronica"
    assert id_doc["tipoIngresos"] == "01"
    assert body["detallesItems"][0]["indicadorFacturacion"] == "ITBIS1_18Percent"


async def test_send_ecf32_returns_parsed_response(httpx_mock):
    httpx_mock.add_response(method="POST", url=f"{BASE}/ecf/32", json=ecf_response())
    async with EcfClient(api_key="k") as client:
        result = await client.send_ecf32(minimal_ecf32())
    assert str(result.message_id) == MESSAGE_ID
    assert result.progress == EcfProgress.NEW
    request = httpx_mock.get_request()
    assert request.headers["Authorization"] == "Bearer k"


async def test_connection_error_is_wrapped(httpx_mock):
    httpx_mock.add_exception(httpx.ConnectError("refused"))
    async with EcfClient(api_key="k") as client:
        with pytest.raises(EcfConnectionError):
            await client.send_ecf32(minimal_ecf32())


async def test_timeout_is_wrapped(httpx_mock):
    httpx_mock.add_exception(httpx.ReadTimeout("slow"))
    async with EcfClient(api_key="k") as client:
        with pytest.raises(EcfConnectionError):
            await client.get_company_by_rnc(RNC)


async def test_non_json_gateway_error_raises_server_error(httpx_mock):
    httpx_mock.add_response(status_code=502, text="<html>Bad Gateway</html>",
                            headers={"content-type": "text/html"})
    async with EcfClient(api_key="k") as client:
        with pytest.raises(EcfServerError) as exc:
            await client.send_ecf32(minimal_ecf32())
    assert exc.value.status_code == 502


async def test_rate_limit_has_its_own_error(httpx_mock):
    httpx_mock.add_response(status_code=429, json={"title": "Too many requests"})
    async with EcfClient(api_key="k") as client:
        with pytest.raises(EcfRateLimitError):
            await client.send_ecf32(minimal_ecf32())


async def test_problem_details_400_raises_validation_error(httpx_mock):
    httpx_mock.add_response(status_code=400, json={"title": "Bad", "detail": "RNC inválido"})
    async with EcfClient(api_key="k") as client:
        with pytest.raises(EcfValidationError) as exc:
            await client.send_ecf32(minimal_ecf32())
    assert "RNC inválido" in exc.value.message


async def test_send_and_poll_stops_on_finished(httpx_mock):
    httpx_mock.add_response(method="POST", url=f"{BASE}/ecf/32", json=ecf_response())
    status_url = re.compile(rf"{BASE}/ecf/{RNC}/message/{MESSAGE_ID}.*")
    httpx_mock.add_response(method="GET", url=status_url, json=[ecf_response("Processing")])
    httpx_mock.add_response(method="GET", url=status_url, json=[ecf_response("Finished", "Aceptado")])
    async with EcfClient(api_key="k") as client:
        result = await client.send_ecf32_and_poll(minimal_ecf32(), polling_options=FAST)
    assert result.progress == EcfProgress.FINISHED
    assert result.cod_sec == "Ab12Cd"


async def test_send_and_poll_raises_on_error_progress(httpx_mock):
    httpx_mock.add_response(method="POST", url=f"{BASE}/ecf/32", json=ecf_response())
    httpx_mock.add_response(
        method="GET",
        url=re.compile(rf"{BASE}/ecf/{RNC}/message/{MESSAGE_ID}.*"),
        json=[ecf_response("Error", "Rechazado", errors="Monto total no cuadra")],
    )
    async with EcfClient(api_key="k") as client:
        with pytest.raises(EcfProcessingError) as exc:
            await client.send_ecf32_and_poll(minimal_ecf32(), polling_options=FAST)
    assert "Monto total no cuadra" in exc.value.message


@pytest.mark.parametrize("tipo", ["31", "32", "33", "34", "41", "43", "44", "45", "46", "47"])
def test_every_ecf_type_has_model_and_send_methods(tipo):
    import ecf_dgii

    assert hasattr(ecf_dgii.generated.models, f"Ecf{tipo}ECF")
    assert callable(getattr(EcfClient, f"send_ecf{tipo}"))
    assert callable(getattr(EcfClient, f"send_ecf{tipo}_and_poll"))
