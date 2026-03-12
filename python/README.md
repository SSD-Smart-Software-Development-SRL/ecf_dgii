# ecf-dgii

Python SDK for the **ECF DGII API** — Dominican Republic Electronic Fiscal Receipts (Comprobantes Fiscales Electrónicos).

## Installation

```bash
pip install ecf-dgii
```

## Quick start

```python
import asyncio
from ecf_dgii import EcfClient, ECF, Encabezado, IdDoc, Emisor, Totales, Item

async def main():
    async with EcfClient(api_key="your-jwt-token", environment="test") as client:
        # Send an ECF with automatic routing and polling
        ecf = ECF(
            encabezado=Encabezado(
                version="1.0",
                idDoc=IdDoc(tipoeCF="FacturaDeCreditoFiscalElectronica", encf="E310000000001"),
                emisor=Emisor(
                    rncEmisor="123456789",
                    razonSocialEmisor="Mi Empresa SRL",
                    direccionEmisor="Calle Principal #1",
                    fechaEmision="2024-01-15",
                ),
                totales=Totales(montoTotal=1180.00),
            ),
            detallesItems=[
                Item(
                    numeroLinea=1,
                    indicadorFacturacion="ITBIS1",
                    retencion={},
                    nombreItem="Servicio de consultoría",
                    indicadorBienoServicio="Servicio",
                    cantidadItem=1,
                    precioUnitarioItem=1000.00,
                    montoItem=1000.00,
                ),
            ],
        )

        result = await client.send_ecf(ecf)
        print(f"ECF accepted: {result.encf} - Status: {result.estatus}")

asyncio.run(main())
```

## Configuration

### Authentication

The API key (JWT Bearer token) can be provided in two ways:

```python
# Direct parameter
client = EcfClient(api_key="your-jwt-token")

# Environment variable
# export ECF_API_KEY=your-jwt-token
client = EcfClient()
```

### Environments

```python
client = EcfClient(api_key="...", environment="test")   # Testing
client = EcfClient(api_key="...", environment="cert")   # Certification
client = EcfClient(api_key="...", environment="prod")   # Production

# Custom base URL
client = EcfClient(api_key="...", base_url="https://custom.api.url")
```

## Features

### Send ECF with automatic polling

The `send_ecf` method handles:
- **Routing** — automatically selects the correct endpoint based on the ECF type
- **Polling** — waits for DGII processing with exponential backoff
- **Error handling** — raises `EcfProcessingError` if DGII rejects the ECF

```python
from ecf_dgii import PollingOptions

result = await client.send_ecf(
    ecf,
    polling_options=PollingOptions(
        initial_delay=1.0,     # seconds
        max_delay=30.0,        # seconds
        max_retries=60,
        backoff_multiplier=2.0,
        timeout=300.0,         # total timeout in seconds
    ),
)
```

### Backend / Frontend Architecture

In most apps, the backend handles business logic and sends the ECF. The frontend gets a read-only token to query status directly:

```python
ecf_client = EcfClient(api_key=os.environ["ECF_BACKEND_TOKEN"], environment="prod")

# Your invoice endpoint — business logic + send to ECF SSD
@app.post("/api/v1/invoices")
async def create_invoice(request: CreateInvoiceRequest):
    # 1. Validate and save your internal invoice
    invoice = await validate_and_save(request)
    # 2. Convert to ECF format
    ecf = convert_to_ecf(invoice)
    # 3. Send to ECF SSD (no polling)
    response = await ecf_client.raw_post("/ecf/31", ecf)
    await update_invoice(invoice.id, message_id=response["messageId"])
    return {"id": invoice.id, "messageId": response["messageId"]}

# Separate endpoint: generate read-only token for frontend
@app.get("/api/v1/ecf-token")
async def get_ecf_token():
    api_key = await ecf_client.create_api_key({...})  # scoped to tenant/RNC
    return {"token": api_key["token"]}
```

The frontend stores the token securely, renews it on `401` or expiry, and queries ECF SSD directly. See the [main README](../README.md#arquitectura-backend--frontend) for the full diagram.

> **`send_ecf`** wraps send + polling into a single call. For apps with a frontend, use the individual endpoints.

### Company management

```python
# List companies
companies = await client.get_companies(page=1, limit=10)

# Get by RNC
company = await client.get_company_by_rnc("123456789")

# Create or update
from ecf_dgii import UpsertCompanyRequest
await client.upsert_company(UpsertCompanyRequest(
    rnc="123456789",
    legalName="Mi Empresa SRL",
    name="Mi Empresa",
))

# Delete
await client.delete_company("123456789")
```

### Certificate management

```python
# Get certificates
certs = await client.get_certificate("123456789")

# Upload certificate
with open("cert.p12", "rb") as f:
    await client.update_certificate("123456789", f, password="cert-password")
```

### Query ECFs

```python
# Query by RNC and eNCF
results = await client.query_ecf("123456789", "E310000000001")

# Search with filters
from ecf_dgii import AllTipoECFTypes
page = await client.search_ecfs(
    "123456789",
    tipos_ecfs=[AllTipoECFTypes.FACTURA_DE_CREDITO_FISCAL_ELECTRONICA],
    from_fecha_emision="2024-01-01T00:00:00",
    page=1,
    limit=50,
)
```

### Aprobación comercial

```python
from ecf_dgii import SendAcecfRequest, EstadoType
await client.aprobacion_comercial(
    "123456789",
    "E310000000001",
    SendAcecfRequest(
        estado=EstadoType.ECF_ACEPTADO,
        rncComprador="987654321",
    ),
)
```

### Anulación de rangos

```python
from ecf_dgii import AnulacionRequest, DetalleAnulacionRequest, SecuenciaRequest, ECFType
result = await client.anulacion_rangos(
    "123456789",
    AnulacionRequest(
        cantidaDeNcfAnulados=5,
        detalleAnulacion=[
            DetalleAnulacionRequest(
                tipoEcf=ECFType.ECF31,
                cantidadeNcfAnulados=5,
                noLinea=[1],
                secuencias=[SecuenciaRequest(secuenciaDesde="E310000000001", secuenciaHasta="E310000000005")],
            ),
        ],
    ),
)
```

### DGII consultations

```python
# Directorio
entries = await client.consulta_directorio_listado("123456789")

# Estado
estado = await client.consulta_estado(
    "123456789",
    rnc_emisor="123456789",
    ncf_electronico="E310000000001",
    rnc_comprador="987654321",
    codigo_seguridad="ABC123",
)

# Estatus servicios
servicios = await client.estatus_servicios("123456789")
```

## Error handling

```python
from ecf_dgii import (
    EcfApiError,
    EcfValidationError,
    EcfAuthenticationError,
    EcfProcessingError,
    PollingTimeoutError,
)

try:
    result = await client.send_ecf(ecf)
except EcfValidationError as e:
    print(f"Bad request: {e.detail}")
except EcfAuthenticationError:
    print("Invalid API key")
except EcfProcessingError as e:
    print(f"DGII rejected: {e.response.errors}")
except PollingTimeoutError:
    print("Processing took too long")
except EcfApiError as e:
    print(f"API error {e.status_code}: {e}")
```

## License

MIT
