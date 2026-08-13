# Align Python SDK with TypeScript Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Align the Python ECF DGII SDK with the TypeScript SDK (the source of truth), removing legacy backward compatibility, unifiying ECF sending operations under a single `send_ecf` method with automatic polling, correcting a critical polling completion status bug, renaming methods, and establishing a robust unit test suite.

**Architecture:** We will create a generic `poll_until_complete` utility in Python matching TS's behavior, implement a unified `send_ecf` routing and polling system with extraction logic for both dicts and generated models, rename all methods in `EcfClient` and `EcfFrontendClient` to match TS naming, and verify everything with pytest.

**Tech Stack:** Python 3.12, httpx, pytest, pytest-asyncio, pytest-httpx, attrs

---

## Task 1: Setup Testing Environment and Test Polling

Create a test configuration and a unit test for the corrected polling utility, then implement the new polling functionality.

**Files:**
- Create: `python/tests/__init__.py`
- Create: `python/tests/conftest.py`
- Create: `python/tests/test_polling.py`
- Modify: `python/ecf_dgii/polling.py`

- [ ] **Step 1: Create `tests/__init__.py` and `tests/conftest.py`**

Create `python/tests/__init__.py`:
```python
# Blank file to make tests a package
```

Create `python/tests/conftest.py` to enable pytest-asyncio:
```python
import pytest

@pytest.fixture
def anyio_backend():
    return "asyncio"
```

- [ ] **Step 2: Write failing tests for `poll_until_complete`**

Create `python/tests/test_polling.py`:
```python
import pytest
from unittest.mock import AsyncMock
from ecf_dgii.polling import poll_until_complete, PollingOptions
from ecf_dgii.exceptions import PollingTimeoutError, PollingMaxRetriesError

@pytest.mark.asyncio
async def test_poll_until_complete_success():
    # Setup mock function returning values
    mock_fn = AsyncMock()
    mock_fn.side_effect = ["Processing", "Processing", "Finished"]

    # Call poll_until_complete: stop when value is "Finished"
    result = await poll_until_complete(
        mock_fn,
        is_complete=lambda r: r == "Finished",
        options=PollingOptions(initial_delay=0.01, max_delay=0.05, max_retries=5)
    )

    assert result == "Finished"
    assert mock_fn.call_count == 3

@pytest.mark.asyncio
async def test_poll_until_complete_max_retries():
    mock_fn = AsyncMock()
    mock_fn.return_value = "Processing"

    with pytest.raises(PollingMaxRetriesError):
        await poll_until_complete(
            mock_fn,
            is_complete=lambda r: r == "Finished",
            options=PollingOptions(initial_delay=0.01, max_delay=0.05, max_retries=2)
        )
```

- [ ] **Step 3: Run the test to verify it fails**

Run in `python` directory:
```bash
pytest tests/test_polling.py -v
```
Expected output: Fail due to `poll_until_complete()` missing argument `is_complete` or incompatible signature.

- [ ] **Step 4: Update `polling.py` implementation**

Replace the contents of `python/ecf_dgii/polling.py`:
```python
"""Polling utilities with exponential backoff for ECF processing."""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass
from typing import Any, Callable, Coroutine, TypeVar

from .exceptions import PollingMaxRetriesError, PollingTimeoutError

T = TypeVar("T")


@dataclass
class PollingOptions:
    """Configuration for polling ECF processing status.

    Attributes:
        initial_delay: Seconds to wait before the first poll. Default: 1.0 (matching TS 1000ms).
        max_delay: Maximum seconds between polls. Default: 30.0 (matching TS 30000ms).
        max_retries: Maximum number of poll attempts. Default: 60 (matching TS 60).
        backoff_multiplier: Multiplier applied to delay each iteration. Default: 2.0 (matching TS 2).
        timeout: Total timeout in seconds. Optional.
    """

    initial_delay: float = 1.0
    max_delay: float = 30.0
    max_retries: int = 60
    backoff_multiplier: float = 2.0
    timeout: float | None = None


async def poll_until_complete(
    poll_fn: Callable[[], Coroutine[Any, Any, T]],
    is_complete: Callable[[T], bool],
    options: PollingOptions | None = None,
) -> T:
    """Call *poll_fn* repeatedly until `is_complete` returns True, using exponential backoff."""
    opts = options or PollingOptions()
    delay = opts.initial_delay
    retries = 0
    start = time.monotonic()

    while True:
        result = await poll_fn()

        if is_complete(result):
            return result

        retries += 1
        if opts.max_retries and retries >= opts.max_retries:
            raise PollingMaxRetriesError(f"Polling exceeded {opts.max_retries} retries")

        if opts.timeout is not None and (time.monotonic() - start) >= opts.timeout:
            raise PollingTimeoutError(f"Polling timed out after {opts.timeout}s")

        await asyncio.sleep(delay)
        delay = min(delay * opts.backoff_multiplier, opts.max_delay)
```

- [ ] **Step 5: Run tests to verify they pass**

Run:
```bash
pytest tests/test_polling.py -v
```
Expected output: `2 passed`

- [ ] **Step 6: Commit**

```bash
git add python/tests/__init__.py python/tests/conftest.py python/tests/test_polling.py python/ecf_dgii/polling.py
git commit -m "refactor: update polling utility to match TS generic behavior and default options"
```

---

## Task 2: Implement Property Extractor Helper

Implement the nested attribute extractor helper `_get_nested` to robustly read `tipoe_cf`, `rnc_emisor`, and `encf` from ECF objects or dicts.

**Files:**
- Modify: `python/ecf_dgii/client.py`
- Create: `python/tests/test_extractor.py`

- [ ] **Step 1: Write tests for property extractor**

Create `python/tests/test_extractor.py`:
```python
import pytest
from ecf_dgii.client import _get_nested

class MockIdDoc:
    def __init__(self, tipoe_cf):
        self.tipoe_cf = tipoe_cf
        self.encf = "E310000000001"

class MockEmisor:
    def __init__(self, rnc):
        self.rnc_emisor = rnc

class MockEncabezado:
    def __init__(self, tipoe_cf, rnc):
        self.id_doc = MockIdDoc(tipoe_cf)
        self.emisor = MockEmisor(rnc)

class MockECF:
    def __init__(self, tipoe_cf, rnc):
        self.encabezado = MockEncabezado(tipoe_cf, rnc)

def test_get_nested_from_objects():
    obj = MockECF("FacturaDeCreditoFiscalElectronica", "131460941")
    assert _get_nested(obj, "encabezado", "id_doc", "tipoe_cf") == "FacturaDeCreditoFiscalElectronica"
    assert _get_nested(obj, "encabezado", "emisor", "rnc_emisor") == "131460941"

def test_get_nested_from_dict():
    payload = {
        "encabezado": {
            "idDoc": {
                "tipoeCF": "FacturaDeConsumoElectronica",
                "encf": "E320000000002"
            },
            "emisor": {
                "rncEmisor": "987654321"
            }
        }
    }
    assert _get_nested(payload, "encabezado", "id_doc", "tipoe_cf") == "FacturaDeConsumoElectronica"
    assert _get_nested(payload, "encabezado", "emisor", "rnc_emisor") == "987654321"
```

- [ ] **Step 2: Run test to verify it fails**

Run:
```bash
pytest tests/test_extractor.py -v
```
Expected output: Fail because `_get_nested` is not defined in `client.py` or cannot be imported.

- [ ] **Step 3: Define `_get_nested` in `client.py`**

Add `_get_nested` helper function near the top of `python/ecf_dgii/client.py`:
```python
def _get_nested(obj: Any, *keys: str) -> Any:
    """Helper to get nested attribute or dict key case-insensitively/snake-camel-agnostically."""
    curr = obj
    for key in keys:
        if curr is None:
            return None
        if isinstance(curr, dict):
            found = False
            if key in curr:
                curr = curr[key]
                found = True
            else:
                alternatives = {
                    key,
                    key.lower(),
                    key.replace("_", ""),
                    "".join(["_" + c.lower() if c.isupper() else c for c in key]).lstrip("_"),
                    "".join([word.capitalize() if i > 0 else word for i, word in enumerate(key.split("_"))])
                }
                for alt in alternatives:
                    if alt in curr:
                        curr = curr[alt]
                        found = True
                        break
            if not found:
                return None
        else:
            found = False
            alternatives = {
                key,
                key.lower(),
                "".join(["_" + c.lower() if c.isupper() else c for c in key]).lstrip("_"),
                "".join([word.capitalize() if i > 0 else word for i, word in enumerate(key.split("_"))])
            }
            for alt in alternatives:
                if hasattr(curr, alt):
                    curr = getattr(curr, alt)
                    if hasattr(curr, "value"):
                        curr = curr.value
                    found = True
                    break
            if not found:
                return None
    return curr
```

- [ ] **Step 4: Run tests to verify they pass**

Run:
```bash
pytest tests/test_extractor.py -v
```
Expected output: `2 passed`

- [ ] **Step 5: Commit**

```bash
git add python/ecf_dgii/client.py python/tests/test_extractor.py
git commit -m "feat: add _get_nested extractor helper supporting dicts and object models"
```

---

## Task 3: Implement Generic `send_ecf` and Clean Up Send Methods

Clean up old send methods, add mapping and routing for the generic `send_ecf`, and raise `EcfProcessingError` if status is `Error`.

**Files:**
- Modify: `python/ecf_dgii/client.py`
- Create: `python/tests/test_send_ecf.py`

- [ ] **Step 1: Write tests for `send_ecf`**

Create `python/tests/test_send_ecf.py`:
```python
import pytest
from unittest.mock import AsyncMock, patch
from ecf_dgii.client import EcfClient, EcfResponse, EcfProgress, EcfProcessingError
from ecf_dgii.generated.models import ProblemDetails

@pytest.mark.asyncio
async def test_send_ecf_success():
    client = EcfClient(api_key="mock-key")
    
    # Mock POST response
    mock_post_res = AsyncMock()
    mock_post_res.status_code.value = 200
    mock_post_res.parsed = EcfResponse.from_dict({
        "messageId": "11111111-1111-1111-1111-111111111111",
        "timestamp": "2026-06-14T09:00:00",
        "fechaEmision": "2026-06-14",
        "queueName": "test-queue",
        "includeEcfContent": False,
        "ecfContent": "",
        "tipoEcf": "FacturaDeCreditoFiscalElectronica",
        "encf": "E310000000001",
        "rncEmisor": "131460941",
        "montoTotal": 1000.0,
        "tenantId": "11111111-1111-1111-1111-111111111111",
        "progress": "New",
        "dgiiEnvironment": "Test",
    })
    
    # Mock GET /ecf/{rnc}/{encf} response
    mock_get_res = AsyncMock()
    mock_get_res.status_code.value = 200
    mock_get_res.parsed = [
        EcfResponse.from_dict({
            "messageId": "11111111-1111-1111-1111-111111111111",
            "timestamp": "2026-06-14T09:00:00",
            "fechaEmision": "2026-06-14",
            "queueName": "test-queue",
            "includeEcfContent": False,
            "ecfContent": "",
            "tipoEcf": "FacturaDeCreditoFiscalElectronica",
            "encf": "E310000000001",
            "rncEmisor": "131460941",
            "montoTotal": 1000.0,
            "tenantId": "11111111-1111-1111-1111-111111111111",
            "progress": "Finished",
            "dgiiEnvironment": "Test",
        })
    ]

    ecf_payload = {
        "encabezado": {
            "idDoc": {
                "tipoeCF": "FacturaDeCreditoFiscalElectronica",
                "encf": "E310000000001"
            },
            "emisor": {
                "rncEmisor": "131460941"
            }
        }
    }

    with patch("ecf_dgii.generated.api.ecf.recepcion_ecf_31.asyncio_detailed", return_value=mock_post_res), \
         patch("ecf_dgii.generated.api.ecf.query_ecf.asyncio_detailed", return_value=mock_get_res):
        
        result = await client.send_ecf(ecf_payload)
        assert result.progress == EcfProgress.FINISHED
        assert str(result.message_id) == "11111111-1111-1111-1111-111111111111"

@pytest.mark.asyncio
async def test_send_ecf_error():
    client = EcfClient(api_key="mock-key")
    
    mock_post_res = AsyncMock()
    mock_post_res.status_code.value = 200
    mock_post_res.parsed = EcfResponse.from_dict({
        "messageId": "11111111-1111-1111-1111-111111111111",
        "timestamp": "2026-06-14T09:00:00",
        "fechaEmision": "2026-06-14",
        "queueName": "test-queue",
        "includeEcfContent": False,
        "ecfContent": "",
        "tipoEcf": "FacturaDeCreditoFiscalElectronica",
        "encf": "E310000000001",
        "rncEmisor": "131460941",
        "montoTotal": 1000.0,
        "tenantId": "11111111-1111-1111-1111-111111111111",
        "progress": "New",
        "dgiiEnvironment": "Test",
    })
    
    mock_get_res = AsyncMock()
    mock_get_res.status_code.value = 200
    mock_get_res.parsed = [
        EcfResponse.from_dict({
            "messageId": "11111111-1111-1111-1111-111111111111",
            "timestamp": "2026-06-14T09:00:00",
            "fechaEmision": "2026-06-14",
            "queueName": "test-queue",
            "includeEcfContent": False,
            "ecfContent": "",
            "tipoEcf": "FacturaDeCreditoFiscalElectronica",
            "encf": "E310000000001",
            "rncEmisor": "131460941",
            "montoTotal": 1000.0,
            "tenantId": "11111111-1111-1111-1111-111111111111",
            "progress": "Error",
            "errors": "RNC Comprador invalido",
            "dgiiEnvironment": "Test",
        })
    ]

    ecf_payload = {
        "encabezado": {
            "idDoc": {
                "tipoeCF": "FacturaDeCreditoFiscalElectronica",
                "encf": "E310000000001"
            },
            "emisor": {
                "rncEmisor": "131460941"
            }
        }
    }

    with patch("ecf_dgii.generated.api.ecf.recepcion_ecf_31.asyncio_detailed", return_value=mock_post_res), \
         patch("ecf_dgii.generated.api.ecf.query_ecf.asyncio_detailed", return_value=mock_get_res):
        
        with pytest.raises(EcfProcessingError) as exc_info:
            await client.send_ecf(ecf_payload)
        
        assert exc_info.value.message == "RNC Comprador invalido"
        assert exc_info.value.status_code == 0
```

- [ ] **Step 2: Run test to verify it fails**

Run:
```bash
pytest tests/test_send_ecf.py -v
```
Expected output: Fail because `send_ecf` is not defined or `EcfProcessingError` is not correctly imported/raised.

- [ ] **Step 3: Implement `send_ecf` and remove legacy send methods**

Update `python/ecf_dgii/client.py` around lines 160 to 213 (or replace them) and update `_send_and_poll` helper.

First, define `ECF_TYPE_ROUTE_MAP`:
```python
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
```

Now, implement `send_ecf` and clean up `send_ecf31`...`send_ecf47` and `_send_and_poll` etc.:

```python
    # ------------------------------------------------------------------
    # ECF send operations
    # ------------------------------------------------------------------

    async def send_ecf(
        self,
        ecf: Any,
        polling_options: PollingOptions | None = None,
    ) -> EcfResponse:
        """Send any ECF type and poll until processing completes."""
        tipoe_cf = _get_nested(ecf, "encabezado", "id_doc", "tipoe_cf")
        if not tipoe_cf:
            raise ValueError("ECF must have encabezado.id_doc.tipoe_cf")

        route = ECF_TYPE_ROUTE_MAP.get(str(tipoe_cf))
        if not route:
            raise ValueError(f"Unknown tipoe_cf: {tipoe_cf}")

        rnc = _get_nested(ecf, "encabezado", "emisor", "rnc_emisor")
        if not rnc:
            raise ValueError("ECF must have encabezado.emisor.rnc_emisor")

        encf = _get_nested(ecf, "encabezado", "id_doc", "encf")
        if not encf:
            raise ValueError("ECF must have encabezado.id_doc.encf")

        send_funcs = {
            "31": recepcion_ecf_31.asyncio_detailed,
            "32": recepcion_ecf_32.asyncio_detailed,
            "33": recepcion_ecf_33.asyncio_detailed,
            "34": recepcion_ecf_34.asyncio_detailed,
            "41": recepcion_ecf_41.asyncio_detailed,
            "43": recepcion_ecf_43.asyncio_detailed,
            "44": recepcion_ecf_44.asyncio_detailed,
            "45": recepcion_ecf_45.asyncio_detailed,
            "46": recepcion_ecf_46.asyncio_detailed,
            "47": recepcion_ecf_47.asyncio_detailed,
        }

        response = await send_funcs[route](client=self._client, body=ecf)
        initial: EcfResponse = _parse_or_raise(response)

        async def _poll() -> EcfResponse:
            results = await self.query_ecf(rnc, encf, include_ecf_content=False)
            match = next((r for r in results if r.message_id == initial.message_id), None)
            if not match:
                match = results[0] if results else initial
            return match

        result = await poll_until_complete(
            _poll,
            is_complete=lambda r: str(getattr(r.progress, "value", r.progress)) in ("Finished", "Error"),
            options=polling_options,
        )

        progress_str = str(getattr(result.progress, "value", result.progress))
        if progress_str == "Error":
            error_msg = getattr(result, "errors", None) or getattr(result, "mensaje", None) or "ECF processing failed"
            raise EcfProcessingError(status_code=0, message=error_msg, detail=result.to_dict() if hasattr(result, "to_dict") else result)

        return result
```

Wait, ensure `EcfProcessingError` is imported from `.exceptions`.

- [ ] **Step 4: Run tests to verify they pass**

Run:
```bash
pytest tests/test_send_ecf.py -v
```
Expected output: `2 passed`

- [ ] **Step 5: Commit**

```bash
git add python/ecf_dgii/client.py python/tests/test_send_ecf.py
git commit -m "feat: add generic send_ecf method with polling and auto-routing; clean up legacy send methods"
```

---

## Task 4: Rename and Align Client Methods

Rename remaining methods in `EcfClient` to match TypeScript names, adjusting parameters where required.

**Files:**
- Modify: `python/ecf_dgii/client.py`
- Create: `python/tests/test_client_renames.py`

- [ ] **Step 1: Write test to verify renamed methods exist and call expected endpoints**

Create `python/tests/test_client_renames.py`:
```python
import pytest
from unittest.mock import AsyncMock, patch
from ecf_dgii.client import EcfClient

@pytest.mark.asyncio
async def test_client_renamed_methods():
    client = EcfClient(api_key="mock-key")

    with patch("ecf_dgii.generated.api.company.get_current_certificate.asyncio_detailed", return_value=AsyncMock()) as m1, \
         patch("ecf_dgii.generated.api.company.update_certificate_company.asyncio_detailed", return_value=AsyncMock()) as m2, \
         patch("ecf_dgii.generated.api.recepcion.get_ecf_receptor_by_message_id.asyncio_detailed", return_value=AsyncMock()) as m3, \
         patch("ecf_dgii.generated.api.recepcion.send_aprobacion_comercial.asyncio_detailed", return_value=AsyncMock()) as m4, \
         patch("ecf_dgii.generated.api.dgii.consulta_directorio_listado.asyncio_detailed", return_value=AsyncMock()) as m5, \
         patch("ecf_dgii.generated.api.dgii.estatus_servicios_obtener_estatus.asyncio_detailed", return_value=AsyncMock()) as m6, \
         patch("ecf_dgii.generated.api.api_key.new_company_api_key.asyncio_detailed", return_value=AsyncMock()) as m7:

        await client.get_certificate("131460941")
        m1.assert_called_once()

        await client.update_certificate("131460941", certificate=b"cert", password="pwd")
        m2.assert_called_once()

        await client.get_ecf_reception_request("131460941", "11111111-1111-1111-1111-111111111111")
        m3.assert_called_once()

        from ecf_dgii.generated.models import SendAcecfRequest, EcfEstadoType1
        await client.aprobacion_comercial("11111111-1111-1111-1111-111111111111", SendAcecfRequest(estado_type=EcfEstadoType1.ECF_ACEPTADO))
        m4.assert_called_once()

        await client.consulta_directorio_listado("131460941")
        m5.assert_called_once()

        await client.estatus_servicios("131460941")
        m6.assert_called_once()

        from ecf_dgii.generated.models import NewCompanyApiKey
        await client.create_api_key(NewCompanyApiKey(legal_name="Name"))
        m7.assert_called_once()
```

- [ ] **Step 2: Run test to verify it fails**

Run:
```bash
pytest tests/test_client_renames.py -v
```
Expected output: Fail because renamed methods do not exist on `EcfClient`.

- [ ] **Step 3: Modify `EcfClient` methods in `client.py`**

Rename and update parameters of the following methods in `python/ecf_dgii/client.py`:

```python
    # ---------------------------------------------------------------------------
    # Certificate operations
    # ---------------------------------------------------------------------------

    async def get_certificate(self, rnc: str) -> Any:
        """Get current certificate for a company."""
        response = await get_current_certificate.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    async def update_certificate(self, rnc: str, *, certificate: bytes, password: str) -> None:
        """Update company certificate."""
        # Note: update_certificate_company body parameter type is body/multipart/form-data
        from .generated.models import update_certificate_company_multipart_data
        body = update_certificate_company_multipart_data.UpdateCertificateCompanyMultipartData(
            certificate=( "certificate.p12", certificate, "application/octet-stream" ),
            password=password,
        )
        response = await update_certificate_company.asyncio_detailed(
            rnc=rnc, client=self._client, body=body,
        )
        if response.status_code.value >= 400:
            _parse_or_raise(response)

    # ---------------------------------------------------------------------------
    # API Key operations
    # ---------------------------------------------------------------------------

    async def create_api_key(self, body: NewCompanyApiKey) -> Any:
        """Create a new API key for a company."""
        response = await new_company_api_key.asyncio_detailed(
            client=self._client, body=body,
        )
        return _parse_or_raise(response)

    # ---------------------------------------------------------------------------
    # DGII operations
    # ---------------------------------------------------------------------------

    async def consulta_directorio_listado(self, rnc: str) -> Any:
        """Query directory listing."""
        response = await consulta_directorio_listado.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    async def estatus_servicios(self, rnc: str) -> list[RespuestaEstatusServicio]:
        """Get DGII service status."""
        response = await estatus_servicios_obtener_estatus.asyncio_detailed(
            rnc=rnc, client=self._client,
        )
        return _parse_or_raise(response)

    # ---------------------------------------------------------------------------
    # Recepcion operations
    # ---------------------------------------------------------------------------

    async def get_ecf_reception_request(
        self,
        rnc: str,
        message_id: str | UUID,
    ) -> EcfReceptorDto | Any:
        """Get ECF receptor by RNC and messageId (GET /recepcion/{rnc}/{messageId})."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await get_ecf_receptor_by_message_id.asyncio_detailed(
            rnc=rnc, message_id=mid, client=self._client,
        )
        return _parse_or_raise(response)

    # ---------------------------------------------------------------------------
    # Aprobacion comercial
    # ---------------------------------------------------------------------------

    async def aprobacion_comercial(
        self,
        message_id: str | UUID,
        body: SendAcecfRequest,
    ) -> Any:
        """Send commercial approval (ACECF) for an ECF reception messageId."""
        mid = message_id if isinstance(message_id, UUID) else UUID(str(message_id))
        response = await send_aprobacion_comercial.asyncio_detailed(
            message_id=mid, client=self._client, body=body,
        )
        return _parse_or_raise(response)
```

Also, modify `firmar_semilla` to accept `xml: bytes`:
```python
    async def firmar_semilla(
        self,
        rnc: str,
        xml: bytes,
    ) -> Any:
        """Sign a seed for DGII."""
        from .generated.models.firmar_semilla_body import FirmarSemillaBody
        body = FirmarSemillaBody(
            xml=( "seed.xml", xml, "application/octet-stream" )
        )
        response = await firmar_semilla.asyncio_detailed(
            rnc=rnc, client=self._client, body=body,
        )
        return _parse_or_raise(response)
```

And completely remove the old definitions:
- `get_current_certificate`
- `update_certificate_company`
- `new_company_api_key`
- `consulta_directorio`
- `estatus_servicio`
- `get_ecf_receptor_by_message_id`
- `send_aprobacion_comercial`

- [ ] **Step 4: Run tests to verify they pass**

Run:
```bash
pytest tests/test_client_renames.py -v
```
Expected output: `1 passed`

- [ ] **Step 5: Commit**

```bash
git add python/ecf_dgii/client.py python/tests/test_client_renames.py
git commit -m "refactor: rename and align client methods with TS naming and signature conventions"
```

---

## Task 5: Align Frontend Client

Refactor `EcfFrontendClient` in `python/ecf_dgii/frontend_client.py` to expose only the 6 exact GET methods supported in TS.

**Files:**
- Modify: `python/ecf_dgii/frontend_client.py`
- Create: `python/tests/test_frontend_client.py`

- [ ] **Step 1: Write test for frontend client methods**

Create `python/tests/test_frontend_client.py`:
```python
import pytest
from unittest.mock import AsyncMock, patch
from ecf_dgii.frontend_client import EcfFrontendClient

def test_frontend_client_methods():
    client = EcfFrontendClient(get_token=lambda: "token")
    
    # Check that only the 6 allowed GET methods exist
    allowed_methods = {
        "query_ecf",
        "search_ecfs",
        "search_all_ecfs",
        "get_ecf_by_id",
        "get_companies",
        "get_company_by_rnc",
        # lifecycle methods
        "close",
    }
    
    methods = [m for m in dir(client) if not m.startswith("_")]
    for m in methods:
        assert m in allowed_methods, f"Method {m} should not be exposed on EcfFrontendClient"
```

- [ ] **Step 2: Run test to verify it fails**

Run:
```bash
pytest tests/test_frontend_client.py -v
```
Expected output: Fail because `get_companies` and `get_company_by_rnc` are missing or other non-GET methods/extra methods are exposed.

- [ ] **Step 3: Modify `frontend_client.py`**

Update `python/ecf_dgii/frontend_client.py`. Retain only the constructor, authentication logic, and the 6 allowed methods. Make sure `get_companies` and `get_company_by_rnc` call the expected endpoints:

```python
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
        tipos_ecfs: list[AllTipoECFTypes] | None = None,
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
        tipos_ecfs: list[AllTipoECFTypes] | None = None,
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run:
```bash
pytest tests/test_frontend_client.py -v
```
Expected output: `1 passed`

- [ ] **Step 5: Commit**

```bash
git add python/ecf_dgii/frontend_client.py python/tests/test_frontend_client.py
git commit -m "refactor: align EcfFrontendClient to expose only the 6 TS-matching methods"
```

---

## Task 6: Update Exports and Verify Entire Suite

Update `python/ecf_dgii/__init__.py` to export the new methods and classes, clean up exports of removed items, and run the entire test suite.

**Files:**
- Modify: `python/ecf_dgii/__init__.py`

- [ ] **Step 1: Update imports/exports in `__init__.py`**

Open `python/ecf_dgii/__init__.py` and:
- Remove: `EcfApiError` (wait, keep `EcfApiError` if it was there, but ensure only correct classes are exported).
- Replace `EcfProgress` and other models if necessary, making sure they match our new classes.
- Ensure `get_current_certificate`, `update_certificate_company`, `new_company_api_key`, `consulta_directorio`, `estatus_servicio`, `send_aprobacion_comercial` are not referenced.

Here is the clean imports block:
```python
"""ECF DGII Python SDK - Client for the Dominican Republic Electronic Fiscal Receipts API."""

from .client import EcfClient, Environment, ENVIRONMENT_URLS
from .frontend_client import EcfFrontendClient, create_frontend_client
from .exceptions import (
    EcfApiError,
    EcfAuthenticationError,
    EcfForbiddenError,
    EcfNotFoundError,
    EcfProcessingError,
    EcfServerError,
    EcfValidationError,
    PollingMaxRetriesError,
    PollingTimeoutError,
)
from .polling import PollingOptions
...
```

- [ ] **Step 2: Run all tests together**

Run:
```bash
pytest -v
```
Expected output: All test cases pass.

- [ ] **Step 3: Commit**

```bash
git add python/ecf_dgii/__init__.py
git commit -m "refactor: clean exports in __init__.py and verify the entire test suite"
```
