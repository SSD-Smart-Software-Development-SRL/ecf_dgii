"""High-level async client for the ECF DGII API."""

from __future__ import annotations

import os
from typing import Any, Literal
from uuid import UUID

import httpx

from .exceptions import raise_for_status
from .generated.client import AuthenticatedClient
from .generated.types import UNSET
from .generated.models import (
    AllTipoECFTypes,
    AnulacionRequest,
    CompanyResponse,
    Ecf31ECF,
    Ecf32ECF,
    Ecf33ECF,
    Ecf34ECF,
    Ecf41ECF,
    Ecf43ECF,
    Ecf44ECF,
    Ecf45ECF,
    Ecf46ECF,
    Ecf47ECF,
    EcfProgress,
    EcfReceptorDto,
    EcfResponse,
    ECFType,
    FirmarSemillaBody,
    NewCompanyApiKey,
    PaginatedApiResultOfAcecfReceptionRequestDto,
    PaginatedApiResultOfAnulacionListResponse,
    PaginatedApiResultOfCompanyResponse,
    PaginatedApiResultOfEcfResponse,
    PaginatedApiResultOfEcfReceptionRequestDto,
    ProblemDetails,
    RespuestaAnulacionRango,
    RespuestaConsultaEstado,
    RespuestaConsultaRFCE,
    RespuestaConsultaTimbre,
    RespuestaConsultaTrackId,
    RespuestaEstatusServicio,
    RespuestaVentanaDeMantenimiento,
    SendAcecfRequest,
    UpsertCompanyRequest,
)
from .generated.api.ecf import (
    anulacion_rangos,
    firmar_semilla,
    get_ecf_by_id,
    list_anulaciones,
    query_ecf,
    recepcion_ecf_31,
    recepcion_ecf_32,
    recepcion_ecf_33,
    recepcion_ecf_34,
    recepcion_ecf_41,
    recepcion_ecf_43,
    recepcion_ecf_44,
    recepcion_ecf_45,
    recepcion_ecf_46,
    recepcion_ecf_47,
    search_all_ecfs,
    search_ecfs,
)
from .generated.api.company import (
    delete_company,
    get_companies,
    get_company_by_rnc,
    get_current_certificate,
    update_certificate_company,
    upsert_company,
)
from .generated.api.dgii import (
    consulta_directorio_listado,
    consulta_directorio_obtener_directorio_por_rnc,
    consulta_estado,
    consulta_resultado,
    consulta_rfce,
    consulta_timbre,
    consulta_timbre_fc,
    consulta_track_id,
    estatus_servicios_obtener_estatus,
    estatus_servicios_obtener_ventanas_mantenimiento,
)
from .generated.api.recepcion import (
    get_ecf_reception_request,
    get_ecf_receptor_by_message_id,
    search_ecf_reception_requests,
    search_ecf_reception_requests_by_rnc,
    send_aprobacion_comercial,
)
from .generated.api.aprobacion_comercial import (
    get_acecf_reception_request,
    search_acecf_reception_requests,
)
from .generated.api.api_key import new_company_api_key
from .polling import PollingOptions, poll_until_complete

Environment = Literal["test", "cert", "prod"]

ENVIRONMENT_URLS: dict[str, str] = {
    "test": "https://api.test.ecfx.ssd.com.do",
    "cert": "https://api.cert.ecfx.ssd.com.do",
    "prod": "https://api.prod.ecfx.ssd.com.do",
}


def _parse_or_raise(response: Any) -> Any:
    """Extract the parsed value from a Response, raising on error."""
    if isinstance(response.parsed, ProblemDetails):
        raise_for_status(response.status_code.value, response.parsed.to_dict())
    if response.parsed is None and response.status_code.value >= 400:
        raise_for_status(response.status_code.value, response.content.decode(errors="ignore"))
    return response.parsed


class EcfClient:
    """High-level async client for the ECF DGII API.

    Usage::

        async with EcfClient(api_key="your-key") as client:
            resp = await client.query_ecf("123456789", "E310000000001")
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        environment: Environment = "test",
        timeout: float = 30.0,
    ) -> None:
        token = api_key or os.environ.get("ECF_API_KEY", "")
        resolved_url = base_url or os.environ.get("ECF_API_URL") or ENVIRONMENT_URLS[environment]

        self._client = AuthenticatedClient(
            base_url=resolved_url,
            token=token,
            raise_on_unexpected_status=False,
            timeout=httpx.Timeout(timeout),
        )
        self._environment = environment

    async def __aenter__(self) -> EcfClient:
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._client.__aexit__(*args)

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self._client.__aexit__(None, None, None)

    # ------------------------------------------------------------------
    # ECF send operations (per-type)
    # ------------------------------------------------------------------

    async def send_ecf31(self, ecf: Ecf31ECF) -> EcfResponse:
        """Send a Factura de Crédito Fiscal Electrónica (31)."""
        response = await recepcion_ecf_31.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf32(self, ecf: Ecf32ECF) -> EcfResponse:
        """Send a Factura de Consumo Electrónica (32)."""
        response = await recepcion_ecf_32.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf33(self, ecf: Ecf33ECF) -> EcfResponse:
        """Send a Nota de Débito Electrónica (33)."""
        response = await recepcion_ecf_33.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf34(self, ecf: Ecf34ECF) -> EcfResponse:
        """Send a Nota de Crédito Electrónica (34)."""
        response = await recepcion_ecf_34.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf41(self, ecf: Ecf41ECF) -> EcfResponse:
        """Send a Comprobante Electrónico de Compras (41)."""
        response = await recepcion_ecf_41.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf43(self, ecf: Ecf43ECF) -> EcfResponse:
        """Send a Comprobante Electrónico de Gastos Menores (43)."""
        response = await recepcion_ecf_43.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf44(self, ecf: Ecf44ECF) -> EcfResponse:
        """Send a Comprobante Electrónico de Regímenes Especiales (44)."""
        response = await recepcion_ecf_44.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf45(self, ecf: Ecf45ECF) -> EcfResponse:
        """Send a Comprobante Electrónico Gubernamental (45)."""
        response = await recepcion_ecf_45.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf46(self, ecf: Ecf46ECF) -> EcfResponse:
        """Send a Comprobante Electrónico de Exportaciones (46)."""
        response = await recepcion_ecf_46.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    async def send_ecf47(self, ecf: Ecf47ECF) -> EcfResponse:
        """Send a Comprobante Electrónico de Pagos al Exterior (47)."""
        response = await recepcion_ecf_47.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # ECF query operations
    # ------------------------------------------------------------------

    async def query_ecf(
        self,
        rnc: str,
        encf: str,
        *,
        include_ecf_content: bool = False,
    ) -> list[EcfResponse]:
        """Query ECFs by RNC and eNCF."""
        response = await query_ecf.asyncio_detailed(
            rnc=rnc,
            encf=encf,
            client=self._client,
            include_ecf_content=include_ecf_content,
        )
        return _parse_or_raise(response)

    async def search_ecfs(
        self,
        rnc: str,
        *,
        encfs: list[str] | None = None,
        ids: list[UUID] | None = None,
        tipos_ecfs: list[AllTipoECFTypes] | None = None,
        include_ecf_content: bool = False,
        from_fecha_emision: Any = UNSET,
        to_fecha_emision: Any = UNSET,
        amount_from: float | None = None,
        amount_to: float | None = None,
        progresses: list[EcfProgress] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfEcfResponse:
        """Search ECFs for a specific RNC."""
        response = await search_ecfs.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            encfs=encfs if encfs is not None else UNSET,
            ids=ids if ids is not None else UNSET,
            tipos_ecfs=tipos_ecfs if tipos_ecfs is not None else UNSET,
            include_ecf_content=include_ecf_content,
            from_fecha_emision=from_fecha_emision if from_fecha_emision is not UNSET else UNSET,
            to_fecha_emision=to_fecha_emision if to_fecha_emision is not UNSET else UNSET,
            amount_from=amount_from if amount_from is not None else UNSET,
            amount_to=amount_to if amount_to is not None else UNSET,
            progresses=progresses if progresses is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def search_all_ecfs(
        self,
        *,
        encfs: list[str] | None = None,
        ids: list[UUID] | None = None,
        tipos_ecfs: list[AllTipoECFTypes] | None = None,
        include_ecf_content: bool = False,
        from_fecha_emision: Any = UNSET,
        to_fecha_emision: Any = UNSET,
        amount_from: float | None = None,
        amount_to: float | None = None,
        progresses: list[EcfProgress] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfEcfResponse:
        """Search all ECFs across all companies."""
        response = await search_all_ecfs.asyncio_detailed(
            client=self._client,
            encfs=encfs if encfs is not None else UNSET,
            ids=ids if ids is not None else UNSET,
            tipos_ecfs=tipos_ecfs if tipos_ecfs is not None else UNSET,
            include_ecf_content=include_ecf_content,
            from_fecha_emision=from_fecha_emision if from_fecha_emision is not UNSET else UNSET,
            to_fecha_emision=to_fecha_emision if to_fecha_emision is not UNSET else UNSET,
            amount_from=amount_from if amount_from is not None else UNSET,
            amount_to=amount_to if amount_to is not None else UNSET,
            progresses=progresses if progresses is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def get_ecf_by_id(
        self,
        rnc: str,
        message_id: str | UUID,
        *,
        include_ecf_content: bool = False,
    ) -> list[EcfResponse]:
        """Get a specific ECF by message ID."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_ecf_by_id.asyncio_detailed(
            rnc=rnc,
            id=mid,
            client=self._client,
            include_ecf_content=include_ecf_content,
        )
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # Anulación operations
    # ------------------------------------------------------------------

    async def anulacion_rangos(
        self,
        rnc: str,
        request: AnulacionRequest,
    ) -> RespuestaAnulacionRango:
        """Request range annulment."""
        response = await anulacion_rangos.asyncio_detailed(
            rnc=rnc, client=self._client, body=request,
        )
        return _parse_or_raise(response)

    async def list_anulaciones(
        self,
        *,
        tipo_ecf: list[ECFType] | None = None,
        rncs: list[str] | None = None,
        fecha_desde: Any = UNSET,
        fecha_hasta: Any = UNSET,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfAnulacionListResponse:
        """List annulments."""
        response = await list_anulaciones.asyncio_detailed(
            client=self._client,
            tipo_ecf=tipo_ecf if tipo_ecf is not None else UNSET,
            rncs=rncs if rncs is not None else UNSET,
            fecha_desde=fecha_desde if fecha_desde is not UNSET else UNSET,
            fecha_hasta=fecha_hasta if fecha_hasta is not UNSET else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # Aprobación Comercial (ACECF)
    # ------------------------------------------------------------------

    async def send_aprobacion_comercial(
        self,
        message_id: str | UUID,
        body: SendAcecfRequest,
    ) -> Any:
        """Send commercial approval (ACECF) for an existing ECF reception by messageId.

        The ECF must have been previously received successfully (its
        ``message_id`` from the recepción response is required here).
        """
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await send_aprobacion_comercial.asyncio_detailed(
            message_id=mid, client=self._client, body=body,
        )
        return _parse_or_raise(response)

    async def firmar_semilla(
        self,
        rnc: str,
        body: FirmarSemillaBody,
    ) -> Any:
        """Sign a seed for DGII."""
        response = await firmar_semilla.asyncio_detailed(
            rnc=rnc, client=self._client, body=body,
        )
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # Company operations
    # ------------------------------------------------------------------

    async def get_companies(
        self,
        *,
        rncs: list[str] | None = None,
        names: list[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfCompanyResponse:
        """List companies with optional filters."""
        response = await get_companies.asyncio_detailed(
            client=self._client,
            rncs=rncs if rncs is not None else UNSET,
            names=names if names is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def get_company_by_rnc(self, rnc: str) -> CompanyResponse:
        """Get a company by RNC."""
        response = await get_company_by_rnc.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    async def upsert_company(self, request: UpsertCompanyRequest) -> None:
        """Create or update a company."""
        response = await upsert_company.asyncio_detailed(
            client=self._client, body=request,
        )
        if response.status_code.value >= 400:
            _parse_or_raise(response)

    async def delete_company(self, rnc: str) -> None:
        """Delete a company."""
        response = await delete_company.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        if response.status_code.value >= 400:
            _parse_or_raise(response)

    async def get_current_certificate(self, rnc: str) -> Any:
        """Get current certificate for a company."""
        response = await get_current_certificate.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    async def update_certificate_company(self, rnc: str, body: Any) -> None:
        """Update company certificate."""
        response = await update_certificate_company.asyncio_detailed(
            rnc=rnc, client=self._client, body=body,
        )
        if response.status_code.value >= 400:
            _parse_or_raise(response)

    # ------------------------------------------------------------------
    # API Key operations
    # ------------------------------------------------------------------

    async def new_company_api_key(self, body: NewCompanyApiKey) -> Any:
        """Create a new API key for a company."""
        response = await new_company_api_key.asyncio_detailed(
            client=self._client, body=body,
        )
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # DGII operations
    # ------------------------------------------------------------------

    async def consulta_estado(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        ncf_electronico: str,
        rnc_comprador: str,
        codigo_seguridad: str,
    ) -> RespuestaConsultaEstado:
        """Query ECF status at DGII."""
        response = await consulta_estado.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rnc_emisor=rnc_emisor,
            ncf_electronico=ncf_electronico,
            rnc_comprador=rnc_comprador,
            codigo_seguridad=codigo_seguridad,
        )
        return _parse_or_raise(response)

    async def consulta_track_id(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
    ) -> RespuestaConsultaTrackId:
        """Query ECF track ID at DGII."""
        response = await consulta_track_id.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rnc_emisor=rnc_emisor,
            encf=encf,
        )
        return _parse_or_raise(response)

    async def consulta_timbre(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
    ) -> RespuestaConsultaTimbre:
        """Query ECF stamp at DGII."""
        response = await consulta_timbre.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rnc_emisor=rnc_emisor,
            encf=encf,
        )
        return _parse_or_raise(response)

    async def consulta_timbre_fc(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
    ) -> Any:
        """Query ECF stamp (fiscal credit) at DGII."""
        response = await consulta_timbre_fc.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rnc_emisor=rnc_emisor,
            encf=encf,
        )
        return _parse_or_raise(response)

    async def consulta_resultado(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
    ) -> Any:
        """Query ECF result at DGII."""
        response = await consulta_resultado.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rnc_emisor=rnc_emisor,
            encf=encf,
        )
        return _parse_or_raise(response)

    async def consulta_rfce(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
    ) -> RespuestaConsultaRFCE:
        """Query RFCE at DGII."""
        response = await consulta_rfce.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rnc_emisor=rnc_emisor,
            encf=encf,
        )
        return _parse_or_raise(response)

    async def consulta_directorio(self, rnc: str) -> Any:
        """Query directory listing."""
        response = await consulta_directorio_listado.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    async def consulta_directorio_por_rnc(
        self,
        rnc: str,
        *,
        rnc_contribuyente: str,
    ) -> Any:
        """Query directory by RNC."""
        response = await consulta_directorio_obtener_directorio_por_rnc.asyncio_detailed(
            rnc_path=rnc,
            client=self._client,
            rnc_query=rnc_contribuyente,
        )
        return _parse_or_raise(response)

    async def estatus_servicio(self, rnc: str) -> list[RespuestaEstatusServicio]:
        """Get DGII service status."""
        response = await estatus_servicios_obtener_estatus.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    async def ventanas_mantenimiento(self, rnc: str) -> RespuestaVentanaDeMantenimiento:
        """Get DGII maintenance windows."""
        response = await estatus_servicios_obtener_ventanas_mantenimiento.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # Recepción operations
    # ------------------------------------------------------------------

    async def get_ecf_reception_request(self, message_id: str | UUID) -> Any:
        """Get ECF reception request by message id (``GET /recepcion/{messageId}``)."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_ecf_reception_request.asyncio_detailed(
            message_id=mid, client=self._client,
        )
        return _parse_or_raise(response)

    async def get_ecf_receptor_by_message_id(
        self,
        rnc: str,
        message_id: str | UUID,
    ) -> EcfReceptorDto | Any:
        """Get ECF receptor by RNC and messageId (``GET /recepcion/{rnc}/{messageId}``)."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_ecf_receptor_by_message_id.asyncio_detailed(
            rnc=rnc, message_id=mid, client=self._client,
        )
        return _parse_or_raise(response)

    async def search_ecf_reception_requests(
        self,
        *,
        message_ids: list[UUID] | None = None,
        encfs: list[str] | None = None,
        rncs: list[str] | None = None,
        rnc_emisors: list[str] | None = None,
        tipos_ecfs: list[Any] | None = None,
        progresses: list[Any] | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        amount_from: float | None = None,
        amount_to: float | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfEcfReceptionRequestDto:
        """Search ECF reception requests (``GET /recepcion``)."""
        response = await search_ecf_reception_requests.asyncio_detailed(
            client=self._client,
            message_ids=message_ids if message_ids is not None else UNSET,
            encfs=encfs if encfs is not None else UNSET,
            rncs=rncs if rncs is not None else UNSET,
            rnc_emisors=rnc_emisors if rnc_emisors is not None else UNSET,
            tipos_ecfs=tipos_ecfs if tipos_ecfs is not None else UNSET,
            progresses=progresses if progresses is not None else UNSET,
            from_date=from_date if from_date is not None else UNSET,
            to_date=to_date if to_date is not None else UNSET,
            amount_from=amount_from if amount_from is not None else UNSET,
            amount_to=amount_to if amount_to is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def search_ecf_reception_requests_by_rnc(
        self,
        rnc: str,
        *,
        message_ids: list[UUID] | None = None,
        encfs: list[str] | None = None,
        rnc_emisors: list[str] | None = None,
        tipos_ecfs: list[Any] | None = None,
        progresses: list[Any] | None = None,
        from_date: str | None = None,
        to_date: str | None = None,
        amount_from: float | None = None,
        amount_to: float | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfEcfReceptionRequestDto:
        """Search ECF reception requests by RNC (``GET /recepcion/{rnc}``)."""
        response = await search_ecf_reception_requests_by_rnc.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            message_ids=message_ids if message_ids is not None else UNSET,
            encfs=encfs if encfs is not None else UNSET,
            rnc_emisors=rnc_emisors if rnc_emisors is not None else UNSET,
            tipos_ecfs=tipos_ecfs if tipos_ecfs is not None else UNSET,
            progresses=progresses if progresses is not None else UNSET,
            from_date=from_date if from_date is not None else UNSET,
            to_date=to_date if to_date is not None else UNSET,
            amount_from=amount_from if amount_from is not None else UNSET,
            amount_to=amount_to if amount_to is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def get_acecf_reception_request(self, message_id: str | UUID) -> Any:
        """Get ACECF reception request (``GET /recepcion/acecf/{messageId}``)."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_acecf_reception_request.asyncio_detailed(
            message_id=mid, client=self._client,
        )
        return _parse_or_raise(response)

    async def search_acecf_reception_requests(
        self,
        *,
        message_ids: list[UUID] | None = None,
        encfs: list[str] | None = None,
        rncs: list[str] | None = None,
        progresses: list[Any] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfAcecfReceptionRequestDto:
        """Search ACECF reception requests (``GET /recepcion/acecf``)."""
        response = await search_acecf_reception_requests.asyncio_detailed(
            client=self._client,
            message_ids=message_ids if message_ids is not None else UNSET,
            encfs=encfs if encfs is not None else UNSET,
            rncs=rncs if rncs is not None else UNSET,
            progresses=progresses if progresses is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # Polling helpers
    # ------------------------------------------------------------------

    async def _send_and_poll(
        self,
        send_coro: Any,
        *,
        polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        initial: EcfResponse = await send_coro

        async def _poll() -> EcfResponse:
            results = await self.query_ecf(
                initial.rnc_emisor,
                initial.encf,
                include_ecf_content=False,
            )
            return results[0] if results else initial

        return await poll_until_complete(_poll, options=polling_options)

    async def send_ecf31_and_poll(
        self, ecf: Ecf31ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf31(ecf), polling_options=polling_options)

    async def send_ecf32_and_poll(
        self, ecf: Ecf32ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf32(ecf), polling_options=polling_options)

    async def send_ecf33_and_poll(
        self, ecf: Ecf33ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf33(ecf), polling_options=polling_options)

    async def send_ecf34_and_poll(
        self, ecf: Ecf34ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf34(ecf), polling_options=polling_options)

    async def send_ecf41_and_poll(
        self, ecf: Ecf41ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf41(ecf), polling_options=polling_options)

    async def send_ecf43_and_poll(
        self, ecf: Ecf43ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf43(ecf), polling_options=polling_options)

    async def send_ecf44_and_poll(
        self, ecf: Ecf44ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf44(ecf), polling_options=polling_options)

    async def send_ecf45_and_poll(
        self, ecf: Ecf45ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf45(ecf), polling_options=polling_options)

    async def send_ecf46_and_poll(
        self, ecf: Ecf46ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf46(ecf), polling_options=polling_options)

    async def send_ecf47_and_poll(
        self, ecf: Ecf47ECF, *, polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        return await self._send_and_poll(self.send_ecf47(ecf), polling_options=polling_options)
