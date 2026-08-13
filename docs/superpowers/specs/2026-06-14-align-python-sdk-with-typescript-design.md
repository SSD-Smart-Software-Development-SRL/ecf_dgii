# Design Spec: Aligning Python SDK with TypeScript SDK

We are aligning the python SDK 1:1 with the TypeScript SDK (considered the source of truth). This includes cleaning up backward compatibility, correcting the polling terminal states bug, unifiying sending operations, renaming methods, and matching the client surfaces exactly.

## 1. Polling Refactoring (`python/ecf_dgii/polling.py`)

Align the polling implementation with TypeScript's generic approach.

### Signature & Defaults
```python
from typing import Any, Callable, Coroutine, TypeVar

T = TypeVar("T")

async def poll_until_complete(
    poll_fn: Callable[[], Coroutine[Any, Any, T]],
    is_complete: Callable[[T], bool],
    options: PollingOptions | None = None,
) -> T:
```

* `PollingOptions` default values:
  - `initial_delay`: `1.0` (matching TS 1000ms)
  - `max_delay`: `30.0` (matching TS 30000ms)
  - `max_retries`: `60` (matching TS 60)
  - `backoff_multiplier`: `2.0` (matching TS 2)
  - `timeout`: `None` (optional, default in TS is undefined)

### Implementation
- The loop will await `poll_fn()`.
- Evaluate `is_complete(result)`. If `True`, return the result.
- Handle `max_retries` and `timeout` elapsed time.
- Sleep for `delay`, apply exponential backoff multiplied by `backoff_multiplier` up to `max_delay`.

---

## 2. Generic `send_ecf` in `EcfClient` (`python/ecf_dgii/client.py`)

Provide a single method for sending any ECF and polling until finished, matching TypeScript's `sendEcf`.

### Signature
```python
async def send_ecf(
    self,
    ecf: Any,
    polling_options: PollingOptions | None = None,
) -> EcfResponse:
```

### Extraction Logic
Robustly extract properties from the ECF payload (supporting both dictionary input and generated model objects with camelCase/snake_case attributes or keys):
- `tipoe_cf` / `tipoeCF`: Found in `encabezado.id_doc.tipoe_cf` or `encabezado.idDoc.tipoeCF`.
- `rnc_emisor` / `rncEmisor`: Found in `encabezado.emisor.rnc_emisor` or `encabezado.emisor.rncEmisor`.
- `encf`: Found in `encabezado.id_doc.encf` or `encabezado.idDoc.encf`.

### Endpoint Routing
Map the ECF type to route:
- `FacturaDeCreditoFiscalElectronica` -> `31`
- `FacturaDeConsumoElectronica` -> `32`
- `NotaDeDebitoElectronica` -> `33`
- `NotaDeCreditoElectronica` -> `34`
- `ComprasElectronico` -> `41`
- `GastosMenoresElectronico` -> `43`
- `RegimenesEspecialesElectronico` -> `44`
- `GubernamentalElectronico` -> `45`
- `ComprobanteDeExportacionesElectronico` -> `46`
- `ComprobanteParaPagosAlExteriorElectronico` -> `47`

Execute the corresponding POST request:
`recepcion_ecf_{route}.asyncio_detailed(client=self._client, body=ecf)`

### Polling & Processing Error
Poll using `poll_until_complete`:
- `poll_fn`: Calls `query_ecf` for the RNC and eNCF, and finds the entry matching the `message_id` returned by the POST call (fallback to the first one).
- `is_complete`: Returns `True` if `progress` is `EcfProgress.FINISHED` ("Finished") or `EcfProgress.ERROR` ("Error").
- If `progress` is `EcfProgress.ERROR`, raise `EcfProcessingError(EcfApiError)` with the final response.

---

## 3. Client Method Alignment

Rename the client methods to use snake_case variants of their TS counterparts, discarding redundant methods.

| TypeScript Client Method | Proposed Python Client Method | Status / Action |
| --- | --- | --- |
| `sendEcf` | `send_ecf` | **New / Unified** |
| `getCompanies` | `get_companies` | Match |
| `getCompanyByRnc` | `get_company_by_rnc` | Match |
| `upsertCompany` | `upsert_company` | Match |
| `deleteCompany` | `delete_company` | Match |
| `getCertificate` | `get_certificate` | Renamed from `get_current_certificate` |
| `updateCertificate` | `update_certificate` | Renamed from `update_certificate_company`, takes `certificate: bytes` & `password: str` |
| `queryEcf` | `query_ecf` | Match |
| `searchEcfs` | `search_ecfs` | Match |
| `searchAllEcfs` | `search_all_ecfs` | Match |
| `getEcfById` | `get_ecf_by_id` | Match |
| `anulacionRangos` | `anulacion_rangos` | Match |
| `listAnulaciones` | `list_anulaciones` | Match |
| `firmarSemilla` | `firmar_semilla` | Match, takes `xml: bytes` |
| `searchEcfReceptionRequests` | `search_ecf_reception_requests` | Match |
| `searchAcecfReceptionRequests` | `search_acecf_reception_requests` | Match |
| `searchEcfReceptionRequestsByRnc` | `search_ecf_reception_requests_by_rnc` | Match |
| `getEcfReceptionRequest` | `get_ecf_reception_request` | Mapped to GET `/recepcion/{rnc}/{messageId}` (previously `get_ecf_receptor_by_message_id`) |
| `getAcecfReceptionRequest` | `get_acecf_reception_request` | Match |
| `aprobacionComercial` | `aprobacion_comercial` | Renamed from `send_aprobacion_comercial` |
| `consultaDirectorioListado` | `consulta_directorio_listado` | Renamed from `consulta_directorio` |
| `consultaDirectorioPorRnc` | `consulta_directorio_por_rnc` | Match |
| `consultaEstado` | `consulta_estado` | Match |
| `consultaResultado` | `consulta_resultado` | Match |
| `consultaRFCE` | `consulta_rfce` | Match |
| `consultaTimbre` | `consulta_timbre` | Match |
| `consultaTimbreFC` | `consulta_timbre_fc` | Match |
| `consultaTrackId` | `consulta_track_id` | Match |
| `estatusServicios` | `estatus_servicios` | Renamed from `estatus_servicio` |
| `ventanasMantenimiento` | `ventanas_mantenimiento` | Match |
| `createApiKey` | `create_api_key` | Renamed from `new_company_api_key` |

*Note: All old typed send methods (`send_ecf31`, `send_ecf31_and_poll`, etc.) and the old `get_ecf_reception_request` that queried `/recepcion/{messageId}` will be completely removed.*

---

## 4. Frontend Client Alignment (`python/ecf_dgii/frontend_client.py`)

Ensure `EcfFrontendClient` exposes only the 6 GET methods that are present in TypeScript's `EcfFrontendClient`:
- `query_ecf`
- `search_ecfs`
- `search_all_ecfs`
- `get_ecf_by_id`
- `get_companies`
- `get_company_by_rnc`

---

## 5. Exports Alignment (`python/ecf_dgii/__init__.py`)

Update `__init__.py` to export:
- Clients: `EcfClient`, `EcfFrontendClient`, `create_frontend_client`
- Configuration: `Environment`, `ENVIRONMENT_URLS`, `PollingOptions`
- Exceptions: `EcfApiError`, `EcfValidationError`, `EcfAuthenticationError`, `EcfForbiddenError`, `EcfNotFoundError`, `EcfServerError`, `EcfProcessingError`, `PollingTimeoutError`, `PollingMaxRetriesError`
- Appropriate generated models.
