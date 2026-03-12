"""Read-only frontend client for the ECF DGII API."""

from __future__ import annotations

import os
from typing import Any, Sequence
from uuid import UUID

import httpx

from .client import ENVIRONMENT_URLS, Environment, _raise_for_status
from .enums import AllTipoECFTypes
from .models import (
    CompanyResponse,
    EcfResponse,
    PaginatedCompanyResponse,
    PaginatedEcfResponse,
)


class EcfFrontendClient:
    """Read-only async client exposing only GET endpoints of the ECF DGII API.

    This client is intended for frontend / dashboard usage where write
    operations are not needed.

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
                "Accept": "application/json",
            },
            timeout=timeout,
        )

    async def __aenter__(self) -> EcfFrontendClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        await self._client.aclose()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    async def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> httpx.Response:
        response = await self._client.request("GET", path, params=params)
        _raise_for_status(response)
        return response

    @staticmethod
    def _clean_params(params: dict[str, Any]) -> dict[str, Any]:
        """Remove None values from query params."""
        return {k: v for k, v in params.items() if v is not None}

    # ======================================================================
    # ECF query operations
    # ======================================================================

    async def query_ecf(
        self, rnc: str, encf: str, *, include_ecf_content: bool = False
    ) -> list[EcfResponse]:
        """Query ECFs by RNC and eNCF."""
        params = self._clean_params({"includeEcfContent": include_ecf_content})
        resp = await self._get(f"/ecf/{rnc}/{encf}", params=params)
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
        resp = await self._get(f"/ecf/{rnc}", params=params)
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
        resp = await self._get("/ecf", params=params)
        return PaginatedEcfResponse.model_validate(resp.json())

    async def get_ecf_by_id(
        self, rnc: str, message_id: str | UUID, *, include_ecf_content: bool = False
    ) -> list[EcfResponse]:
        """Get a specific ECF by message ID."""
        params = self._clean_params({"includeEcfContent": include_ecf_content})
        resp = await self._get(f"/ecf/{rnc}/message/{message_id}", params=params)
        return [EcfResponse.model_validate(r) for r in resp.json()]

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
        resp = await self._get("/company", params=params)
        return PaginatedCompanyResponse.model_validate(resp.json())

    async def get_company_by_rnc(self, rnc: str) -> CompanyResponse:
        """Get a company by RNC."""
        resp = await self._get(f"/company/{rnc}")
        return CompanyResponse.model_validate(resp.json())
