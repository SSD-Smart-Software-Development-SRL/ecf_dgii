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

from .client import ENVIRONMENT_URLS, Environment
from .exceptions import raise_for_status
from .generated.client import AuthenticatedClient
from .generated.types import UNSET
from .generated.models import (
    AllTipoECFTypesType1,
    CompanyResponse,
    EcfResponse,
    PaginatedApiResultOfCompanyResponse,
    PaginatedApiResultOfEcfResponse,
    ProblemDetails,
)
from .generated.api.ecf import query_ecf, search_ecfs, search_all_ecfs, get_ecf_by_id
from .generated.api.company import get_companies, get_company_by_rnc

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


def _parse_or_raise(response: Any) -> Any:
    """Extract parsed value, raising on error."""
    if isinstance(response.parsed, ProblemDetails):
        raise_for_status(response.status_code.value, response.parsed.to_dict())
    if response.parsed is None and response.status_code.value >= 400:
        raise_for_status(response.status_code.value, response.content.decode(errors="ignore"))
    return response.parsed


class EcfFrontendClient:
    """Read-only async client exposing only GET endpoints of the ECF DGII API.

    Token lifecycle is handled automatically:
    - On each request, checks ``get_cached_token()``. If None, calls
      ``get_token()`` then ``cache_token(token)``.
    - On 401 responses, calls ``get_token()`` again, updates the cache,
      and retries the request.

    Parameters
    ----------
    get_token:
        **Required.** Callback that fetches a fresh read-only token.
    cache_token:
        Optional callback to store a token. Default: encrypted file on
        disk at ``~/.ecf-dgii/token.enc``.
    get_cached_token:
        Optional callback to retrieve a previously cached token.
    base_url:
        Full base URL override.
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
        self._base_url = base_url or os.environ.get("ECF_API_URL") or ENVIRONMENT_URLS[environment]
        self._timeout = timeout
        self._current_client: AuthenticatedClient | None = None

    def _make_client(self, token: str) -> AuthenticatedClient:
        return AuthenticatedClient(
            base_url=self._base_url,
            token=token,
            raise_on_unexpected_status=False,
            timeout=httpx.Timeout(self._timeout),
        )

    def _resolve_client(self) -> AuthenticatedClient:
        """Return a client with a valid token, fetching and caching if necessary."""
        token = self._get_cached_token()
        if not token:
            token = self._get_token()
            self._cache_token(token)
        self._current_client = self._make_client(token)
        return self._current_client

    def _refresh_client(self) -> AuthenticatedClient:
        """Force-fetch a new token and create a new client."""
        token = self._get_token()
        self._cache_token(token)
        self._current_client = self._make_client(token)
        return self._current_client

    async def __aenter__(self) -> EcfFrontendClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        if self._current_client:
            await self._current_client.__aexit__(None, None, None)

    async def _get_with_retry(self, api_call: Any, **kwargs: Any) -> Any:
        """Execute an API call with 401 retry."""
        client = self._resolve_client()
        response = await api_call(client=client, **kwargs)
        if response.status_code.value == 401:
            client = self._refresh_client()
            response = await api_call(client=client, **kwargs)
        return _parse_or_raise(response)

    # ======================================================================
    # ECF query operations
    # ======================================================================

    async def query_ecf(
        self, rnc: str, encf: str, *, include_ecf_content: bool = False
    ) -> list[EcfResponse]:
        """Query ECFs by RNC and eNCF."""
        return await self._get_with_retry(
            query_ecf.asyncio_detailed,
            rnc=rnc,
            encf=encf,
            include_ecf_content=include_ecf_content,
        )

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
        return await self._get_with_retry(
            search_ecfs.asyncio_detailed,
            rnc=rnc,
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
        return await self._get_with_retry(
            search_all_ecfs.asyncio_detailed,
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

    async def get_ecf_by_id(
        self, rnc: str, message_id: str | UUID, *, include_ecf_content: bool = False
    ) -> list[EcfResponse]:
        """Get a specific ECF by message ID."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        return await self._get_with_retry(
            get_ecf_by_id.asyncio_detailed,
            rnc=rnc,
            id=mid,
            include_ecf_content=include_ecf_content,
        )

    # ======================================================================
    # Company operations
    # ======================================================================

    async def get_companies(
        self,
        *,
        rncs: list[str] | None = None,
        names: list[str] | None = None,
        page: int = 1,
        limit: int = 25,
    ) -> PaginatedApiResultOfCompanyResponse:
        """List companies with optional filters."""
        return await self._get_with_retry(
            get_companies.asyncio_detailed,
            rncs=rncs if rncs is not None else UNSET,
            names=names if names is not None else UNSET,
            page=page,
            limit=limit,
        )

    async def get_company_by_rnc(self, rnc: str) -> CompanyResponse:
        """Get a company by RNC."""
        return await self._get_with_retry(
            get_company_by_rnc.asyncio_detailed,
            rnc=rnc,
        )


def create_frontend_client(
    *,
    get_token: Callable[[], str],
    cache_token: Optional[Callable[[str], None]] = None,
    get_cached_token: Optional[Callable[[], Optional[str]]] = None,
    base_url: str | None = None,
    environment: Environment = "test",
    timeout: float = 30.0,
) -> EcfFrontendClient:
    """Factory that creates a restricted read-only client suitable for frontend use."""
    return EcfFrontendClient(
        get_token=get_token,
        cache_token=cache_token,
        get_cached_token=get_cached_token,
        base_url=base_url,
        environment=environment,
        timeout=timeout,
    )
