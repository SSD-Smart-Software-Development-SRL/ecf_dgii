"""High-level async client for the ECF DGII API."""

from __future__ import annotations

import os
from typing import Any, Literal, Sequence
from uuid import UUID

import httpx

from .exceptions import raise_for_status
from .generated.client import AuthenticatedClient
from .generated.types import UNSET, Unset
from .generated.models import (
    AllTipoECFTypesType1,
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
    EcfResponse,
    ECFType,
    FirmarSemillaRequest,
    NewCompanyApiKey,
    PaginatedApiResultOfAnulacionListResponse,
    PaginatedApiResultOfCompanyResponse,
    PaginatedApiResultOfEcfResponse,
    PaginatedApiResultOfAcecfReceptionRequestDto,
    PaginatedApiResultOfEcfReceptionRequestDto,
    ProblemDetails,
    RespuestaAnulacionRango,
    RespuestaConsultaEstado,
    RespuestaConsultaRFCE,
    RespuestaConsultaTimbre,
    RespuestaConsultaTrackId,
    RespuestaEstatusServicio,
    RespuestaVentanaDeMantenimiento,
    SecuenciaRequest,
    SendAcecfRequest,
    UpsertCompanyRequest,
)
from .generated.api.ecf import (
    anulacion_rangos,
    aprobacion_comercial,
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
    get_acecf_reception_request,
    get_ecf_reception_request,
    search_acecf_reception_requests,
    search_acecf_reception_requests_by_rnc,
    search_ecf_reception_requests,
    search_ecf_reception_requests_by_rnc,
)
from .generated.api.api_key import new_company_api_key
from .polling import PollingOptions, poll_until_complete

Environment = Literal["test", "cert", "prod"]

ENVIRONMENT_URLS: dict[str, str] = {
    "test": "https://api.test.ecfx.ssd.com.do",
    "cert": "https://api.cert.ecfx.ssd.com.do",
    "prod": "https://api.prod.ecfx.ssd.com.do",
}

ECF_TYPE_MAP: dict[str, str] = {
    "31": "31",
    "32": "32",
    "33": "33",
    "34": "34",
    "41": "41",
    "43": "43",
    "44": "44",
    "45": "45",
    "46": "46",
    "47": "47",
}

_ECF_SEND_MODULES: dict[str, Any] = {
    "31": recepcion_ecf_31,
    "32": recepcion_ecf_32,
    "33": recepcion_ecf_33,
    "34": recepcion_ecf_34,
    "41": recepcion_ecf_41,
    "43": recepcion_ecf_43,
    "44": recepcion_ecf_44,
    "45": recepcion_ecf_45,
    "46": recepcion_ecf_46,
    "47": recepcion_ecf_47,
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
    # ECF operations
    # ------------------------------------------------------------------

    async def send_ecf(
        self,
        ecf: Ecf31ECF | Ecf32ECF | Ecf33ECF | Ecf34ECF | Ecf41ECF | Ecf43ECF | Ecf44ECF | Ecf45ECF | Ecf46ECF | Ecf47ECF,
        ecf_type: str | None = None,
    ) -> EcfResponse:
        """Send an ECF document. Auto-routes to the correct endpoint based on type."""
        if ecf_type is None:
            ecf_type = _detect_ecf_type(ecf)

        module = _ECF_SEND_MODULES.get(ecf_type)
        if module is None:
            raise ValueError(f"Unsupported ECF type: {ecf_type}")

        response = await module.asyncio_detailed(client=self._client, body=ecf)
        return _parse_or_raise(response)

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
        tipos_ecfs: list[AllTipoECFTypesType1 | None] | None = None,
        include_ecf_content: bool = False,
        from_fecha_emision: Any = UNSET,
        to_fecha_emision: Any = UNSET,
        amount_from: float | None = None,
        amount_to: float | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfEcfResponse:
        """Search ECFs for a specific RNC."""
        response = await search_ecfs.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            encfs=encfs if encfs is not None else UNSET,
            tipos_ecfs=tipos_ecfs if tipos_ecfs is not None else UNSET,
            include_ecf_content=include_ecf_content,
            from_fecha_emision=from_fecha_emision if from_fecha_emision is not UNSET else UNSET,
            to_fecha_emision=to_fecha_emision if to_fecha_emision is not UNSET else UNSET,
            amount_from=amount_from if amount_from is not None else UNSET,
            amount_to=amount_to if amount_to is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def search_all_ecfs(
        self,
        *,
        encfs: list[str] | None = None,
        tipos_ecfs: list[AllTipoECFTypesType1 | None] | None = None,
        include_ecf_content: bool = False,
        from_fecha_emision: Any = UNSET,
        to_fecha_emision: Any = UNSET,
        amount_from: float | None = None,
        amount_to: float | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfEcfResponse:
        """Search all ECFs across all companies."""
        response = await search_all_ecfs.asyncio_detailed(
            client=self._client,
            encfs=encfs if encfs is not None else UNSET,
            tipos_ecfs=tipos_ecfs if tipos_ecfs is not None else UNSET,
            include_ecf_content=include_ecf_content,
            from_fecha_emision=from_fecha_emision if from_fecha_emision is not UNSET else UNSET,
            to_fecha_emision=to_fecha_emision if to_fecha_emision is not UNSET else UNSET,
            amount_from=amount_from if amount_from is not None else UNSET,
            amount_to=amount_to if amount_to is not None else UNSET,
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
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfAnulacionListResponse:
        """List annulments."""
        response = await list_anulaciones.asyncio_detailed(
            client=self._client,
            tipo_ecf=tipo_ecf if tipo_ecf is not None else UNSET,  # type: ignore[arg-type]
            rncs=rncs if rncs is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def aprobacion_comercial(
        self,
        rnc: str,
        body: SendAcecfRequest,
    ) -> EcfResponse:
        """Send commercial approval (ACECF)."""
        response = await aprobacion_comercial.asyncio_detailed(
            rnc=rnc, client=self._client, body=body,
        )
        return _parse_or_raise(response)

    async def firmar_semilla(
        self,
        rnc: str,
        body: FirmarSemillaRequest,
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

    async def estatus_servicio(self, rnc: str) -> RespuestaEstatusServicio:
        """Get DGII service status."""
        response = await estatus_servicios_obtener_estatus.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    async def ventanas_mantenimiento(self, rnc: str) -> list[RespuestaVentanaDeMantenimiento]:
        """Get DGII maintenance windows."""
        response = await estatus_servicios_obtener_ventanas_mantenimiento.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # Recepcion operations
    # ------------------------------------------------------------------

    async def get_ecf_reception_request(self, rnc: str, message_id: str | UUID) -> Any:
        """Get ECF reception request."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_ecf_reception_request.asyncio_detailed(
            rnc=rnc, message_id=mid, client=self._client,
        )
        return _parse_or_raise(response)

    async def search_ecf_reception_requests(
        self,
        *,
        message_ids: list[UUID] | None = None,
        encfs: list[str] | None = None,
        rncs: list[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfEcfReceptionRequestDto:
        """Search ECF reception requests."""
        response = await search_ecf_reception_requests.asyncio_detailed(
            client=self._client,
            message_ids=message_ids if message_ids is not None else UNSET,
            encfs=encfs if encfs is not None else UNSET,
            rncs=rncs if rncs is not None else UNSET,
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
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfEcfReceptionRequestDto:
        """Search ECF reception requests by RNC."""
        response = await search_ecf_reception_requests_by_rnc.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            message_ids=message_ids if message_ids is not None else UNSET,
            encfs=encfs if encfs is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def get_acecf_reception_request(self, rnc: str, message_id: str | UUID) -> Any:
        """Get ACECF reception request."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_acecf_reception_request.asyncio_detailed(
            rnc=rnc, message_id=mid, client=self._client,
        )
        return _parse_or_raise(response)

    async def search_acecf_reception_requests(
        self,
        *,
        message_ids: list[UUID] | None = None,
        encfs: list[str] | None = None,
        rncs: list[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfAcecfReceptionRequestDto:
        """Search ACECF reception requests."""
        response = await search_acecf_reception_requests.asyncio_detailed(
            client=self._client,
            message_ids=message_ids if message_ids is not None else UNSET,
            encfs=encfs if encfs is not None else UNSET,
            rncs=rncs if rncs is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    async def search_acecf_reception_requests_by_rnc(
        self,
        rnc: str,
        *,
        message_ids: list[UUID] | None = None,
        encfs: list[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfAcecfReceptionRequestDto:
        """Search ACECF reception requests by RNC."""
        response = await search_acecf_reception_requests_by_rnc.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            message_ids=message_ids if message_ids is not None else UNSET,
            encfs=encfs if encfs is not None else UNSET,
            page=page,
            limit=limit,
        )
        return _parse_or_raise(response)

    # ------------------------------------------------------------------
    # Polling helper
    # ------------------------------------------------------------------

    async def send_ecf_and_poll(
        self,
        ecf: Ecf31ECF | Ecf32ECF | Ecf33ECF | Ecf34ECF | Ecf41ECF | Ecf43ECF | Ecf44ECF | Ecf45ECF | Ecf46ECF | Ecf47ECF,
        ecf_type: str | None = None,
        *,
        polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        """Send an ECF and poll until processing completes."""
        initial = await self.send_ecf(ecf, ecf_type=ecf_type)

        async def _poll() -> EcfResponse:
            results = await self.query_ecf(
                initial.rnc_emisor,
                initial.encf,
                include_ecf_content=False,
            )
            return results[0] if results else initial

        return await poll_until_complete(_poll, options=polling_options)


def _detect_ecf_type(ecf: Any) -> str:
    """Detect ECF type from the model class name."""
    name = type(ecf).__name__
    for code in ("31", "32", "33", "34", "41", "43", "44", "45", "46", "47"):
        if f"Ecf{code}" in name:
            return code
    raise ValueError(f"Cannot detect ECF type from {name}")
