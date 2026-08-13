"""High-level async client for the ECF DGII API."""

from __future__ import annotations

import os
from io import BytesIO
from typing import Any, Literal
from uuid import UUID

import httpx

from .exceptions import EcfProcessingError, raise_for_status
from .generated.api.api_key import new_company_api_key
from .generated.api.aprobacion_comercial import (
    get_acecf_reception_request,
    search_acecf_reception_requests,
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
from .generated.api.recepcion import (
    get_ecf_receptor_by_message_id,
    search_ecf_reception_requests,
    search_ecf_reception_requests_by_rnc,
    send_aprobacion_comercial,
)
from .generated.client import AuthenticatedClient
from .generated.models import (
    AllTipoECFTypes,
    AnulacionRequest,
    CompanyResponse,
    EcfProgress,
    EcfReceptorDto,
    EcfResponse,
    ECFType,
    FirmarSemillaBody,
    NewCompanyApiKey,
    PaginatedApiResultOfAcecfReceptionRequestDto,
    PaginatedApiResultOfAnulacionListResponse,
    PaginatedApiResultOfCompanyResponse,
    PaginatedApiResultOfEcfReceptionRequestDto,
    PaginatedApiResultOfEcfResponse,
    ProblemDetails,
    RespuestaAnulacionRango,
    RespuestaConsultaEstado,
    RespuestaConsultaRFCE,
    RespuestaConsultaTimbre,
    RespuestaConsultaTrackId,
    RespuestaEstatusServicio,
    RespuestaVentanaDeMantenimiento,
    SendAcecfRequest,
    UpdateCertificateCompanyBody,
    UpsertCompanyRequest,
)
from .generated.types import UNSET, File
from .polling import PollingOptions, poll_until_complete

Environment = Literal["test", "cert", "prod"]

ENVIRONMENT_URLS: dict[str, str] = {
    "test": "https://api.test.ecfx.ssd.com.do",
    "cert": "https://api.cert.ecfx.ssd.com.do",
    "prod": "https://api.prod.ecfx.ssd.com.do",
}

ECF_TYPE_ROUTE_MAP: dict[str, Any] = {
    "FacturaDeCreditoFiscalElectronica": recepcion_ecf_31,
    "FacturaDeConsumoElectronica": recepcion_ecf_32,
    "NotaDeDebitoElectronica": recepcion_ecf_33,
    "NotaDeCreditoElectronica": recepcion_ecf_34,
    "ComprasElectronico": recepcion_ecf_41,
    "GastosMenoresElectronico": recepcion_ecf_43,
    "RegimenesEspecialesElectronico": recepcion_ecf_44,
    "GubernamentalElectronico": recepcion_ecf_45,
    "ComprobanteDeExportacionesElectronico": recepcion_ecf_46,
    "ComprobanteParaPagosAlExteriorElectronico": recepcion_ecf_47,
}


def _parse_or_raise(response: Any) -> Any:
    """Extract the parsed value from a Response, raising on error."""
    if isinstance(response.parsed, ProblemDetails):
        raise_for_status(response.status_code.value, response.parsed.to_dict())
    if response.parsed is None and response.status_code.value >= 400:
        raise_for_status(response.status_code.value, response.content.decode(errors="ignore"))
    return response.parsed


def _get_nested(obj: Any, *keys: str) -> Any:
    """Helper to get nested attribute or dict key case-insensitively/snake-camel-agnostically."""

    def normalize(s: str) -> str:
        return s.lower().replace("_", "")

    curr = obj
    for key in keys:
        if curr is None:
            return None
        norm_key = normalize(key)

        if isinstance(curr, dict):
            found = False
            if key in curr:
                curr = curr[key]
                found = True
            else:
                for k, v in curr.items():
                    if normalize(k) == norm_key:
                        curr = v
                        found = True
                        break
            if not found:
                return None
        else:
            found = False
            if hasattr(curr, key):
                curr = getattr(curr, key)
                if hasattr(curr, "value"):
                    curr = curr.value
                found = True
            else:
                for attr in dir(curr):
                    if normalize(attr) == norm_key:
                        curr = getattr(curr, attr)
                        if hasattr(curr, "value"):
                            curr = curr.value
                        found = True
                        break
            if not found:
                return None
    return curr


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
    # ECF send operations
    # ------------------------------------------------------------------

    async def send_ecf(
        self,
        ecf: Any,
        polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        """Send any ECF invoice type and poll until processing is complete.

        Raises:
            EcfProcessingError: If the invoice processing fails with an error status.
        """
        tipoe_cf = _get_nested(ecf, "encabezado", "id_doc", "tipoe_cf")
        if not tipoe_cf:
            raise ValueError("ECF must have encabezado.id_doc.tipoe_cf")

        if hasattr(tipoe_cf, "value"):
            tipoe_cf = tipoe_cf.value
        tipoe_cf_str = str(tipoe_cf)

        route_module = ECF_TYPE_ROUTE_MAP.get(tipoe_cf_str)
        if not route_module:
            raise ValueError(f"Unknown tipoeCF: {tipoe_cf_str}")

        rnc = _get_nested(ecf, "encabezado", "emisor", "rnc_emisor")
        if not rnc:
            raise ValueError("ECF must have encabezado.emisor.rnc_emisor")
        if hasattr(rnc, "value"):
            rnc = rnc.value

        encf = _get_nested(ecf, "encabezado", "id_doc", "encf")
        if not encf:
            raise ValueError("ECF must have encabezado.id_doc.encf")
        if hasattr(encf, "value"):
            encf = encf.value

        response = await route_module.asyncio_detailed(client=self._client, body=ecf)
        initial: EcfResponse = _parse_or_raise(response)

        async def _poll() -> EcfResponse:
            results = await self.query_ecf(
                str(rnc),
                str(encf),
                include_ecf_content=False,
            )
            if not results:
                return initial

            # Find matching response by message ID, fallback to the first result
            match = next((r for r in results if r.message_id == initial.message_id), None)
            return match if match is not None else results[0]

        result = await poll_until_complete(
            _poll,
            lambda r: r.progress == EcfProgress.FINISHED or r.progress == EcfProgress.ERROR,
            polling_options,
        )

        if result.progress == EcfProgress.ERROR:
            msg = result.errors or result.mensaje or "ECF processing failed"
            raise EcfProcessingError(status_code=0, message=msg, detail=result)

        return result

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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

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
            rnc=rnc,
            client=self._client,
            body=request,
        )
        return _parse_or_raise(response)  # type: ignore[no-any-return]

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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    # ------------------------------------------------------------------
    # Aprobación Comercial (ACECF)
    # ------------------------------------------------------------------

    async def aprobacion_comercial(
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
            message_id=mid,
            client=self._client,
            body=body,
        )
        return _parse_or_raise(response)

    async def firmar_semilla(
        self,
        rnc: str,
        *,
        xml: bytes,
    ) -> Any:
        """Sign a seed for DGII."""
        body = FirmarSemillaBody(
            xml=File(
                payload=BytesIO(xml),
                file_name="seed.xml",
                mime_type="application/octet-stream",
            )
        )
        response = await firmar_semilla.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            body=body,
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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    async def get_company_by_rnc(self, rnc: str) -> CompanyResponse:
        """Get a company by RNC."""
        response = await get_company_by_rnc.asyncio_detailed(
            rnc=rnc,
            client=self._client,
        )
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    async def upsert_company(self, request: UpsertCompanyRequest) -> None:
        """Create or update a company."""
        response = await upsert_company.asyncio_detailed(
            client=self._client,
            body=request,
        )
        if response.status_code.value >= 400:
            _parse_or_raise(response)

    async def delete_company(self, rnc: str) -> None:
        """Delete a company."""
        response = await delete_company.asyncio_detailed(
            rnc=rnc,
            client=self._client,
        )
        if response.status_code.value >= 400:
            _parse_or_raise(response)

    async def get_certificate(self, rnc: str) -> Any:
        """Get current certificate for a company."""
        response = await get_current_certificate.asyncio_detailed(
            rnc=rnc,
            client=self._client,
        )
        return _parse_or_raise(response)

    async def update_certificate(
        self,
        rnc: str,
        *,
        certificate: bytes,
        password: str,
    ) -> None:
        """Update company certificate."""
        body = UpdateCertificateCompanyBody(
            certificate=File(
                payload=BytesIO(certificate),
                file_name="certificate.p12",
                mime_type="application/octet-stream",
            ),
            password=password,
        )
        response = await update_certificate_company.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            body=body,
        )
        if response.status_code.value >= 400:
            _parse_or_raise(response)

    # ------------------------------------------------------------------
    # API Key operations
    # ------------------------------------------------------------------

    async def create_api_key(self, body: NewCompanyApiKey) -> Any:
        """Create a new API key for a company."""
        response = await new_company_api_key.asyncio_detailed(
            client=self._client,
            body=body,
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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    async def consulta_timbre(
        self,
        rnc: str,
        *,
        rncemisor: str,
        encf: str,
        montototal: str,
        codigoseguridad: str,
    ) -> RespuestaConsultaTimbre:
        """Query ECF stamp at DGII."""
        response = await consulta_timbre.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rncemisor=rncemisor,
            encf=encf,
            montototal=montototal,
            codigoseguridad=codigoseguridad,
        )
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    async def consulta_timbre_fc(
        self,
        rnc: str,
        *,
        rncemisor: str,
        encf: str,
        montototal: str,
        codigoseguridad: str,
    ) -> Any:
        """Query ECF stamp (fiscal credit) at DGII."""
        response = await consulta_timbre_fc.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rncemisor=rncemisor,
            encf=encf,
            montototal=montototal,
            codigoseguridad=codigoseguridad,
        )
        return _parse_or_raise(response)

    async def consulta_resultado(
        self,
        rnc: str,
        *,
        track_id: str,
    ) -> Any:
        """Query ECF result at DGII."""
        response = await consulta_resultado.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            track_id=track_id,
        )
        return _parse_or_raise(response)

    async def consulta_rfce(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
        cod_seguridad_e_cf: str,
    ) -> RespuestaConsultaRFCE:
        """Query RFCE at DGII."""
        response = await consulta_rfce.asyncio_detailed(
            rnc=rnc,
            client=self._client,
            rnc_emisor=rnc_emisor,
            encf=encf,
            cod_seguridad_e_cf=cod_seguridad_e_cf,
        )
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    async def consulta_directorio_listado(self, rnc: str) -> Any:
        """Query directory listing."""
        response = await consulta_directorio_listado.asyncio_detailed(
            rnc=rnc,
            client=self._client,
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

    async def estatus_servicios(self, rnc: str) -> list[RespuestaEstatusServicio]:
        """Get DGII service status."""
        response = await estatus_servicios_obtener_estatus.asyncio_detailed(
            rnc=rnc,
            client=self._client,
        )
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    async def ventanas_mantenimiento(self, rnc: str) -> RespuestaVentanaDeMantenimiento:
        """Get DGII maintenance windows."""
        response = await estatus_servicios_obtener_ventanas_mantenimiento.asyncio_detailed(
            rnc=rnc,
            client=self._client,
        )
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    # ------------------------------------------------------------------
    # Recepción operations
    # ------------------------------------------------------------------

    async def get_ecf_reception_request(
        self,
        rnc: str,
        message_id: str | UUID,
    ) -> EcfReceptorDto | Any:
        """Get ECF receptor by RNC and messageId (``GET /recepcion/{rnc}/{messageId}``)."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_ecf_receptor_by_message_id.asyncio_detailed(
            rnc=rnc,
            message_id=mid,
            client=self._client,
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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

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
        return _parse_or_raise(response)  # type: ignore[no-any-return]

    async def get_acecf_reception_request(self, message_id: str | UUID) -> Any:
        """Get ACECF reception request (``GET /recepcion/acecf/{messageId}``)."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_acecf_reception_request.asyncio_detailed(
            message_id=mid,
            client=self._client,
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
        return _parse_or_raise(response)  # type: ignore[no-any-return]
