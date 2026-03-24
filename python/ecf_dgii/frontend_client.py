"""Read-only frontend client for the ECF DGII API."""

from __future__ import annotations

import base64
import logging
import os
import warnings
from pathlib import Path
from typing import Any, Callable, Optional, Sequence
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

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Default encrypted file-based token cache
# ---------------------------------------------------------------------------

_CACHE_DIR = Path.home() / ".ecf-dgii"
_TOKEN_FILE = _CACHE_DIR / "token.enc"
_KEY_FILE = _CACHE_DIR / "token.key"


def _ensure_cache_dir() -> None:
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)


try:
    from cryptography.fernet import Fernet

    def _get_or_create_key() -> bytes:
        _ensure_cache_dir()
        if _KEY_FILE.exists():
            return _KEY_FILE.read_bytes()
        key = Fernet.generate_key()
        _KEY_FILE.write_bytes(key)
        _KEY_FILE.chmod(0o600)
        return key

    def _default_cache_token(token: str) -> None:
        """Encrypt and store token to disk using Fernet."""
        key = _get_or_create_key()
        f = Fernet(key)
        encrypted = f.encrypt(token.encode("utf-8"))
        _ensure_cache_dir()
        _TOKEN_FILE.write_bytes(encrypted)
        _TOKEN_FILE.chmod(0o600)

    def _default_get_cached_token() -> Optional[str]:
        """Read and decrypt token from disk using Fernet."""
        if not _TOKEN_FILE.exists() or not _KEY_FILE.exists():
            return None
        try:
            key = _KEY_FILE.read_bytes()
            f = Fernet(key)
            return f.decrypt(_TOKEN_FILE.read_bytes()).decode("utf-8")
        except Exception:
            logger.debug("Failed to decrypt cached token, returning None")
            return None

    _USING_FERNET = True

except ImportError:
    warnings.warn(
        "cryptography package not installed. "
        "Token cache will use base64 encoding (NOT encrypted). "
        "Install cryptography for secure token storage: pip install cryptography",
        stacklevel=2,
    )

    def _default_cache_token(token: str) -> None:  # type: ignore[misc]
        """Store token to disk using base64 encoding (no encryption)."""
        _ensure_cache_dir()
        encoded = base64.b64encode(token.encode("utf-8"))
        _TOKEN_FILE.write_bytes(encoded)
        _TOKEN_FILE.chmod(0o600)

    def _default_get_cached_token() -> Optional[str]:  # type: ignore[misc]
        """Read token from disk using base64 decoding (no encryption)."""
        if not _TOKEN_FILE.exists():
            return None
        try:
            return base64.b64decode(_TOKEN_FILE.read_bytes()).decode("utf-8")
        except Exception:
            logger.debug("Failed to read cached token, returning None")
            return None

    _USING_FERNET = False


class EcfFrontendClient:
    """Read-only async client exposing only GET endpoints of the ECF DGII API.

    This client is intended for frontend / dashboard usage where write
    operations are not needed.

    Token lifecycle is handled automatically:
    - On each request, checks ``get_cached_token()``. If None, calls
      ``get_token()`` then ``cache_token(token)``.
    - On 401 responses, calls ``get_token()`` again, updates the cache,
      and retries the request.

    Parameters
    ----------
    get_token:
        **Required.** Callback that fetches a fresh read-only token.
        Typically calls your backend's ``GET /ecf-token`` endpoint.
    cache_token:
        Optional callback to store a token. Default: encrypted file on
        disk at ``~/.ecf-dgii/token.enc`` using Fernet (falls back to
        base64 if ``cryptography`` is not installed).
    get_cached_token:
        Optional callback to retrieve a previously cached token. Default:
        read from ``~/.ecf-dgii/token.enc``.
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
        get_token: Callable[[], str],
        cache_token: Optional[Callable[[str], None]] = None,
        get_cached_token: Optional[Callable[[], Optional[str]]] = None,
        base_url: str | None = None,
        environment: Environment = "test",
        timeout: float = 30.0,
    ) -> None:
        self._get_token = get_token
        self._cache_token = cache_token or _default_cache_token
        self._get_cached_token = get_cached_token or _default_get_cached_token

        resolved_url = base_url or os.environ.get("ECF_API_URL") or ENVIRONMENT_URLS[environment]

        self._client = httpx.AsyncClient(
            base_url=resolved_url,
            headers={
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
    # Token management
    # ------------------------------------------------------------------

    def _resolve_token(self) -> str:
        """Return a valid token, fetching and caching if necessary."""
        token = self._get_cached_token()
        if token:
            return token
        token = self._get_token()
        self._cache_token(token)
        return token

    def _refresh_token(self) -> str:
        """Force-fetch a new token and update the cache."""
        token = self._get_token()
        self._cache_token(token)
        return token

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    async def _get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> httpx.Response:
        token = self._resolve_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = await self._client.request("GET", path, params=params, headers=headers)

        # On 401, refresh token and retry once
        if response.status_code == 401:
            token = self._refresh_token()
            headers = {"Authorization": f"Bearer {token}"}
            response = await self._client.request("GET", path, params=params, headers=headers)

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


def create_frontend_client(
    *,
    get_token: Callable[[], str],
    cache_token: Optional[Callable[[str], None]] = None,
    get_cached_token: Optional[Callable[[], Optional[str]]] = None,
    base_url: str | None = None,
    environment: Environment = "test",
    timeout: float = 30.0,
) -> EcfFrontendClient:
    """Factory that creates a restricted read-only client suitable for frontend use.

    Only GET endpoints are exposed. See :class:`EcfFrontendClient` for full
    parameter documentation.
    """
    return EcfFrontendClient(
        get_token=get_token,
        cache_token=cache_token,
        get_cached_token=get_cached_token,
        base_url=base_url,
        environment=environment,
        timeout=timeout,
    )
