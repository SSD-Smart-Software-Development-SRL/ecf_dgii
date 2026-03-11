"""High-level client for the ECF DGII API."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, BinaryIO, Literal, Sequence
from uuid import UUID

import httpx

from .enums import AllTipoECFTypes, ECFType, EcfProgress, TipoeCFType
from .exceptions import (
    EcfApiError,
    EcfAuthenticationError,
    EcfForbiddenError,
    EcfNotFoundError,
    EcfProcessingError,
    EcfServerError,
    EcfValidationError,
)
from .models import (
    AcecfReceptionRequestDto,
    AnulacionListResponse,
    AnulacionRequest,
    CertificateResponse,
    CompanyResponse,
    Directorio,
    ECF,
    EcfReceptionRequestDto,
    EcfResponse,
    NewCompanyApiKey,
    PaginatedAcecfReceptionRequestDto,
    PaginatedAnulacionListResponse,
    PaginatedCompanyResponse,
    PaginatedEcfReceptionRequestDto,
    PaginatedEcfResponse,
    RespuestaAnulacionRango,
    RespuestaConsultaEstado,
    RespuestaConsultaRFCE,
    RespuestaConsultaTimbre,
    RespuestaConsultaTrackId,
    RespuestaEstatusServicio,
    RespuestaVentanaDeMantenimiento,
    SendAcecfRequest,
    Token,
    UpsertCompanyRequest,
)
from .polling import PollingOptions, poll_until_complete

Environment = Literal["test", "cert", "prod"]

ENVIRONMENT_URLS: dict[Environment, str] = {
    "test": "https://api.test.ecfx.ssd.com.do",
    "cert": "https://api.cert.ecfx.ssd.com.do",
    "prod": "https://api.prod.ecfx.ssd.com.do",
}

ECF_TYPE_ROUTE_MAP: dict[str, str] = {
    "FacturaDeCreditoFiscalElectronica": "31",
    "FacturaDeConsumoElectronica": "32",
    "NotaDeDebitoElectronica": "33",
    "NotaDeCreditoElectronica": "34",
    "ComprasElectronico": "41",
    "GastosMenoresElectronico": "43",
    "RegimenesEspecialesElectronico": "44",
    "GubernamentalElectronico": "45",
    "ComprobanteDeExportacionesElectronico": "46",
    "ComprobanteParaPagosAlExteriorElectronico": "47",
}


def _raise_for_status(response: httpx.Response) -> None:
    """Raise a typed exception for non-2xx responses."""
    if response.is_success:
        return
    detail = None
    try:
        detail = response.json()
    except Exception:
        detail = response.text
    status = response.status_code
    msg = f"HTTP {status}: {detail}"
    if status == 400:
        raise EcfValidationError(msg, status, detail)
    if status == 401:
        raise EcfAuthenticationError(msg, status, detail)
    if status == 403:
        raise EcfForbiddenError(msg, status, detail)
    if status == 404:
        raise EcfNotFoundError(msg, status, detail)
    if status >= 500:
        raise EcfServerError(msg, status, detail)
    raise EcfApiError(msg, status, detail)


class EcfClient:
    """High-level async client for the ECF DGII API.

    Parameters
    ----------
    api_key:
        JWT Bearer token. Falls back to ``ECF_API_KEY`` env var.
    base_url:
        Full base URL override. Takes precedence over *environment*.
        Falls back to ``ECF_API_URL`` env var.
    environment:
        Target environment (``test``, ``cert``, ``prod``). Defaults to ``test``.
    timeout:
        Request timeout in seconds. Defaults to 30.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        environment: Environment = "test",
        timeout: float = 30.0,
    ) -> None:
        resolved_key = api_key or os.environ.get("ECF_API_KEY", "")
        if not resolved_key:
            raise ValueError(
                "api_key must be provided or set via the ECF_API_KEY environment variable"
            )

        resolved_url = base_url or os.environ.get("ECF_API_URL") or ENVIRONMENT_URLS[environment]

        self._client = httpx.AsyncClient(
            base_url=resolved_url,
            headers={
                "Authorization": f"Bearer {resolved_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            timeout=timeout,
        )

    async def __aenter__(self) -> EcfClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self._client.aclose()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    async def _request(
        self,
        method: str,
        path: str,
        *,
        json: Any = None,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        files: Any = None,
        content_type: str | None = None,
    ) -> httpx.Response:
        headers = {}
        if content_type:
            headers["Content-Type"] = content_type
        if files or data:
            headers.pop("Content-Type", None)

        response = await self._client.request(
            method,
            path,
            json=json,
            params=params,
            data=data,
            files=files,
            headers=headers if headers else None,
        )
        _raise_for_status(response)
        return response

    @staticmethod
    def _clean_params(params: dict[str, Any]) -> dict[str, Any]:
        """Remove None values from query params."""
        return {k: v for k, v in params.items() if v is not None}

    # ======================================================================
    # HIGH-LEVEL: Send ECF + poll
    # ======================================================================

    async def send_ecf(self, ecf: ECF, polling_options: PollingOptions | None = None) -> EcfResponse:
        """Send an ECF and poll until processing completes.

        Automatically routes to the correct endpoint based on
        ``ecf.encabezado.id_doc.tipo_ecf`` and polls until the status
        reaches ``Finished`` or ``Error``.

        Parameters
        ----------
        ecf:
            The ECF document to send.
        polling_options:
            Optional polling configuration for backoff, retries, timeout.

        Returns
        -------
        EcfResponse
            The final ECF response once processing is complete.

        Raises
        ------
        EcfProcessingError
            If processing finishes with ``Error`` status.
        """
        tipo_ecf = ecf.encabezado.id_doc.tipo_ecf.value
        route = ECF_TYPE_ROUTE_MAP.get(tipo_ecf)
        if not route:
            raise ValueError(f"Unknown tipoeCF: {tipo_ecf}")

        rnc = ecf.encabezado.emisor.rnc_emisor
        encf = ecf.encabezado.id_doc.encf

        # POST to the typed endpoint
        initial_response = await self._post_ecf(route, ecf)

        # Poll until complete
        async def _poll_fn() -> EcfResponse:
            results = await self.query_ecf(rnc, encf)
            match = next((r for r in results if r.message_id == initial_response.message_id), None)
            if match is None and results:
                match = results[0]
            if match is None:
                raise EcfApiError("No ECF response found for the given rnc/encf")
            return match

        result = await poll_until_complete(
            _poll_fn,
            lambda r: r.progress in (EcfProgress.FINISHED, EcfProgress.ERROR),
            polling_options,
        )

        if result.progress == EcfProgress.ERROR:
            raise EcfProcessingError(
                result.errors or result.mensaje or "ECF processing failed",
                result,
            )

        return result

    async def _post_ecf(self, route: str, ecf: ECF) -> EcfResponse:
        body = ecf.model_dump(by_alias=True, exclude_none=True)
        resp = await self._request("POST", f"/ecf/{route}", json=body)
        return EcfResponse.model_validate(resp.json())

    # ======================================================================
    # Company operations
    # ======================================================================

    async def get_companies(
        self,
        *,
        rncs: Sequence[str] | None = None,
        names: Sequence[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedCompanyResponse:
        """List companies with optional filters."""
        params = self._clean_params({"Rncs": rncs, "Names": names, "Page": page, "Limit": limit})
        resp = await self._request("GET", "/company", params=params)
        return PaginatedCompanyResponse.model_validate(resp.json())

    async def get_company_by_rnc(self, rnc: str) -> CompanyResponse:
        """Get a company by RNC."""
        resp = await self._request("GET", f"/company/{rnc}")
        return CompanyResponse.model_validate(resp.json())

    async def upsert_company(self, company: UpsertCompanyRequest) -> None:
        """Create or update a company."""
        body = company.model_dump(by_alias=True, exclude_none=True)
        await self._request("PUT", "/company", json=body)

    async def delete_company(self, rnc: str) -> None:
        """Delete a company by RNC."""
        await self._request("DELETE", f"/company/{rnc}")

    # ======================================================================
    # Certificate operations
    # ======================================================================

    async def get_certificate(self, rnc: str) -> list[CertificateResponse]:
        """Get the current certificate(s) for a company."""
        resp = await self._request("GET", f"/company/{rnc}/certificate")
        return [CertificateResponse.model_validate(c) for c in resp.json()]

    async def update_certificate(self, rnc: str, certificate: BinaryIO, password: str) -> None:
        """Upload a new certificate for a company.

        Parameters
        ----------
        rnc:
            The company RNC.
        certificate:
            A file-like object for the certificate file (.p12 / .pfx).
        password:
            The certificate password.
        """
        await self._request(
            "PUT",
            f"/company/{rnc}/certificate",
            files={"certificate": certificate},
            data={"password": password},
        )

    # ======================================================================
    # ECF query operations
    # ======================================================================

    async def query_ecf(self, rnc: str, encf: str, *, include_ecf_content: bool = False) -> list[EcfResponse]:
        """Query ECFs by RNC and eNCF."""
        params = self._clean_params({"includeEcfContent": include_ecf_content})
        resp = await self._request("GET", f"/ecf/{rnc}/{encf}", params=params)
        return [EcfResponse.model_validate(r) for r in resp.json()]

    async def get_ecf_by_id(
        self, rnc: str, message_id: str | UUID, *, include_ecf_content: bool = False
    ) -> list[EcfResponse]:
        """Get a specific ECF by message ID."""
        params = self._clean_params({"includeEcfContent": include_ecf_content})
        resp = await self._request("GET", f"/ecf/{rnc}/message/{message_id}", params=params)
        return [EcfResponse.model_validate(r) for r in resp.json()]

    async def search_ecfs(
        self,
        rnc: str,
        *,
        encfs: Sequence[str] | None = None,
        ids: Sequence[str] | None = None,
        tipos_ecfs: Sequence[AllTipoECFTypes] | None = None,
        include_ecf_content: bool = False,
        from_fecha_emision: str | None = None,
        to_fecha_emision: str | None = None,
        amount_from: float | None = None,
        amount_to: float | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedEcfResponse:
        """Search ECFs for a specific RNC."""
        params = self._clean_params({
            "Encfs": encfs,
            "Ids": ids,
            "TiposEcfs": [t.value for t in tipos_ecfs] if tipos_ecfs else None,
            "IncludeEcfContent": include_ecf_content,
            "FromFechaEmision": from_fecha_emision,
            "ToFechaEmision": to_fecha_emision,
            "AmountFrom": amount_from,
            "AmountTo": amount_to,
            "Page": page,
            "Limit": limit,
        })
        resp = await self._request("GET", f"/ecf/{rnc}", params=params)
        return PaginatedEcfResponse.model_validate(resp.json())

    async def search_all_ecfs(
        self,
        *,
        encfs: Sequence[str] | None = None,
        ids: Sequence[str] | None = None,
        tipos_ecfs: Sequence[AllTipoECFTypes] | None = None,
        include_ecf_content: bool = False,
        from_fecha_emision: str | None = None,
        to_fecha_emision: str | None = None,
        amount_from: float | None = None,
        amount_to: float | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedEcfResponse:
        """Search all ECFs across all companies."""
        params = self._clean_params({
            "Encfs": encfs,
            "Ids": ids,
            "TiposEcfs": [t.value for t in tipos_ecfs] if tipos_ecfs else None,
            "IncludeEcfContent": include_ecf_content,
            "FromFechaEmision": from_fecha_emision,
            "ToFechaEmision": to_fecha_emision,
            "AmountFrom": amount_from,
            "AmountTo": amount_to,
            "Page": page,
            "Limit": limit,
        })
        resp = await self._request("GET", "/ecf", params=params)
        return PaginatedEcfResponse.model_validate(resp.json())

    # ======================================================================
    # Aprobacion comercial
    # ======================================================================

    async def aprobacion_comercial(self, rnc: str, encf: str, request: SendAcecfRequest) -> None:
        """Send aprobacion comercial for an ECF."""
        body = request.model_dump(by_alias=True, exclude_none=True)
        await self._request("POST", f"/ecf/aprobacioncomercial/{rnc}/{encf}", json=body)

    # ======================================================================
    # Anulacion rangos
    # ======================================================================

    async def anulacion_rangos(self, rnc: str, request: AnulacionRequest) -> RespuestaAnulacionRango:
        """Request range annulment."""
        body = request.model_dump(by_alias=True, exclude_none=True)
        resp = await self._request("POST", f"/ecf/anularrango/{rnc}", json=body)
        return RespuestaAnulacionRango.model_validate(resp.json())

    async def list_anulaciones(
        self,
        *,
        tipo_ecf: Sequence[ECFType] | None = None,
        rncs: Sequence[str] | None = None,
        fecha_desde: str | None = None,
        fecha_hasta: str | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedAnulacionListResponse:
        """List annulments."""
        params = self._clean_params({
            "TipoEcf": [t.value for t in tipo_ecf] if tipo_ecf else None,
            "Rncs": rncs,
            "FechaDesde": fecha_desde,
            "FechaHasta": fecha_hasta,
            "Page": page,
            "Limit": limit,
        })
        resp = await self._request("GET", "/ecf/anulaciones", params=params)
        return PaginatedAnulacionListResponse.model_validate(resp.json())

    # ======================================================================
    # Firmar semilla
    # ======================================================================

    async def firmar_semilla(self, rnc: str, xml: BinaryIO) -> httpx.Response:
        """Sign a seed XML for a company.

        Parameters
        ----------
        rnc:
            The company RNC.
        xml:
            A file-like object with the seed XML content.

        Returns
        -------
        httpx.Response
            The raw response (the API returns 200 with no schema).
        """
        return await self._request(
            "POST",
            f"/ecf/FirmarSemilla/{rnc}",
            files={"xml": xml},
        )

    # ======================================================================
    # Recepcion operations
    # ======================================================================

    async def search_ecf_reception_requests(
        self,
        *,
        message_ids: Sequence[str] | None = None,
        encfs: Sequence[str] | None = None,
        rncs: Sequence[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedEcfReceptionRequestDto:
        """Search ECF reception requests."""
        params = self._clean_params({
            "MessageIds": message_ids,
            "Encfs": encfs,
            "Rncs": rncs,
            "Page": page,
            "Limit": limit,
        })
        resp = await self._request("GET", "/recepcion/ecf", params=params)
        return PaginatedEcfReceptionRequestDto.model_validate(resp.json())

    async def search_acecf_reception_requests(
        self,
        *,
        message_ids: Sequence[str] | None = None,
        encfs: Sequence[str] | None = None,
        rncs: Sequence[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedAcecfReceptionRequestDto:
        """Search ACECF reception requests."""
        params = self._clean_params({
            "MessageIds": message_ids,
            "Encfs": encfs,
            "Rncs": rncs,
            "Page": page,
            "Limit": limit,
        })
        resp = await self._request("GET", "/recepcion/acecf", params=params)
        return PaginatedAcecfReceptionRequestDto.model_validate(resp.json())

    async def search_ecf_reception_requests_by_rnc(
        self,
        rnc: str,
        *,
        message_ids: Sequence[str] | None = None,
        encfs: Sequence[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedEcfReceptionRequestDto:
        """Search ECF reception requests by RNC."""
        params = self._clean_params({
            "MessageIds": message_ids,
            "Encfs": encfs,
            "Page": page,
            "Limit": limit,
        })
        resp = await self._request("GET", f"/recepcion/{rnc}/ecf", params=params)
        return PaginatedEcfReceptionRequestDto.model_validate(resp.json())

    async def get_ecf_reception_request(self, rnc: str, message_id: str | UUID) -> EcfReceptionRequestDto:
        """Get a specific ECF reception request."""
        resp = await self._request("GET", f"/recepcion/{rnc}/ecf/{message_id}")
        return EcfReceptionRequestDto.model_validate(resp.json())

    async def search_acecf_reception_requests_by_rnc(
        self,
        rnc: str,
        *,
        message_ids: Sequence[str] | None = None,
        encfs: Sequence[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedAcecfReceptionRequestDto:
        """Search ACECF reception requests by RNC."""
        params = self._clean_params({
            "MessageIds": message_ids,
            "Encfs": encfs,
            "Page": page,
            "Limit": limit,
        })
        resp = await self._request("GET", f"/recepcion/{rnc}/acecf", params=params)
        return PaginatedAcecfReceptionRequestDto.model_validate(resp.json())

    async def get_acecf_reception_request(self, rnc: str, message_id: str | UUID) -> AcecfReceptionRequestDto:
        """Get a specific ACECF reception request."""
        resp = await self._request("GET", f"/recepcion/{rnc}/acecf/{message_id}")
        return AcecfReceptionRequestDto.model_validate(resp.json())

    # ======================================================================
    # DGII operations
    # ======================================================================

    async def consulta_directorio_listado(self, rnc: str) -> list[Directorio]:
        """Consulta directorio - listado."""
        resp = await self._request("GET", f"/dgii/{rnc}/consultadirectorio/listado")
        return [Directorio.model_validate(d) for d in resp.json()]

    async def consulta_directorio_por_rnc(self, rnc: str, *, rnc_consulta: str) -> Directorio:
        """Consulta directorio - obtener directorio por RNC."""
        params = {"RNC": rnc_consulta}
        resp = await self._request("GET", f"/dgii/{rnc}/consultadirectorio/obtener-directorio-por-rnc", params=params)
        return Directorio.model_validate(resp.json())

    async def consulta_estado(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        ncf_electronico: str,
        rnc_comprador: str,
        codigo_seguridad: str,
    ) -> RespuestaConsultaEstado:
        """Consulta estado."""
        params = {
            "rncEmisor": rnc_emisor,
            "ncfElectronico": ncf_electronico,
            "rncComprador": rnc_comprador,
            "codigoSeguridad": codigo_seguridad,
        }
        resp = await self._request("GET", f"/dgii/{rnc}/consultaestado/estado", params=params)
        return RespuestaConsultaEstado.model_validate(resp.json())

    async def consulta_resultado(self, rnc: str, *, track_id: str) -> RespuestaConsultaTrackId:
        """Consulta resultado."""
        resp = await self._request("GET", f"/dgii/{rnc}/consultaresultado/estado", params={"trackId": track_id})
        return RespuestaConsultaTrackId.model_validate(resp.json())

    async def consulta_rfce(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
        cod_seguridad_ecf: str,
    ) -> RespuestaConsultaRFCE:
        """Consulta RFCE."""
        params = {
            "RNC_Emisor": rnc_emisor,
            "ENCF": encf,
            "Cod_Seguridad_eCF": cod_seguridad_ecf,
        }
        resp = await self._request("GET", f"/dgii/{rnc}/consultarfce/consulta", params=params)
        return RespuestaConsultaRFCE.model_validate(resp.json())

    async def consulta_timbre(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
        monto_total: str,
        codigo_seguridad: str,
    ) -> RespuestaConsultaTimbre:
        """Consulta timbre."""
        params = {
            "rncemisor": rnc_emisor,
            "encf": encf,
            "montototal": monto_total,
            "codigoseguridad": codigo_seguridad,
        }
        resp = await self._request("GET", f"/dgii/{rnc}/consultatimbre", params=params)
        return RespuestaConsultaTimbre.model_validate(resp.json())

    async def consulta_timbre_fc(
        self,
        rnc: str,
        *,
        rnc_emisor: str,
        encf: str,
        monto_total: str,
        codigo_seguridad: str,
    ) -> RespuestaConsultaTimbre:
        """Consulta timbre FC."""
        params = {
            "rncemisor": rnc_emisor,
            "encf": encf,
            "montototal": monto_total,
            "codigoseguridad": codigo_seguridad,
        }
        resp = await self._request("GET", f"/dgii/{rnc}/consultatimbrefc", params=params)
        return RespuestaConsultaTimbre.model_validate(resp.json())

    async def consulta_track_id(self, rnc: str, *, rnc_emisor: str, encf: str) -> RespuestaConsultaTrackId:
        """Consulta track IDs."""
        params = {"rncEmisor": rnc_emisor, "encf": encf}
        resp = await self._request("GET", f"/dgii/{rnc}/consultatrackids/consulta", params=params)
        return RespuestaConsultaTrackId.model_validate(resp.json())

    async def estatus_servicios(self, rnc: str) -> list[RespuestaEstatusServicio]:
        """Estatus servicios - obtener estatus."""
        resp = await self._request("GET", f"/dgii/{rnc}/estatusservicios/obtener-estatus")
        return [RespuestaEstatusServicio.model_validate(s) for s in resp.json()]

    async def ventanas_mantenimiento(self, rnc: str) -> RespuestaVentanaDeMantenimiento:
        """Estatus servicios - obtener ventanas de mantenimiento."""
        resp = await self._request("GET", f"/dgii/{rnc}/estatusservicios/obtener-ventanas-mantenimiento")
        return RespuestaVentanaDeMantenimiento.model_validate(resp.json())

    # ======================================================================
    # ApiKey operations
    # ======================================================================

    async def create_api_key(self, request: NewCompanyApiKey) -> Token:
        """Create a new API key."""
        body = request.model_dump(by_alias=True, exclude_none=True)
        resp = await self._request("POST", "/apiKey", json=body)
        return Token.model_validate(resp.json())
