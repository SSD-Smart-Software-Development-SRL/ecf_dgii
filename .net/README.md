# EcfDgii.Client - .NET SDK

Official .NET SDK for the ECF DGII API (Electronic Fiscal Receipts - Dominican Republic).

## Installation

```bash
dotnet add package EcfDgii.Client
```

## Quick Start

```csharp
using EcfDgii.Client;
using EcfDgii.Client.Generated.Models;

// Create the client (reads ECF_API_KEY from environment by default)
var client = new EcfClient(new EcfClientOptions
{
    ApiKey = "your-jwt-token",
    Environment = EcfEnvironment.Cert // Test, Cert, or Prod
});

// --- High-level: Send an ECF and wait for the result ---
var ecf = new ECF
{
    Encabezado = new Encabezado
    {
        IdDoc = new IdDoc
        {
            TipoeCF = TipoeCFType.FacturaDeCreditoFiscalElectronica,
            Encf = "E310000000001"
        },
        Emisor = new Emisor
        {
            RncEmisor = "123456789"
        }
    },
    DetallesItems = new List<Item>
    {
        // ... your line items
    }
};

try
{
    // SendEcfAsync routes to the correct endpoint, polls until done, and returns the result
    EcfResponse result = await client.SendEcfAsync(ecf);
    Console.WriteLine($"Status: {result.Progress}");
    Console.WriteLine($"Message: {result.Mensaje}");
}
catch (EcfException ex)
{
    Console.WriteLine($"ECF Error: {ex.Message}");
    Console.WriteLine($"Errors: {ex.Response.Errors}");
}
```

## Configuration

### Environment Variables

| Variable       | Description                                      |
|---------------|--------------------------------------------------|
| `ECF_API_KEY` | JWT Bearer token for API authentication           |
| `ECF_API_URL` | Base URL override (takes precedence over environment) |

### Options

```csharp
var client = new EcfClient(new EcfClientOptions
{
    ApiKey = "your-jwt-token",       // or set ECF_API_KEY env var
    BaseUrl = "https://custom.url",  // or set ECF_API_URL env var
    Environment = EcfEnvironment.Prod // Test (default), Cert, or Prod
});
```

### Environments

| Environment | URL |
|------------|-----|
| Test       | `https://api.test.ecfx.ssd.com.do` |
| Cert       | `https://api.cert.ecfx.ssd.com.do` |
| Prod       | `https://api.prod.ecfx.ssd.com.do` |

## Usage

### High-Level: Send ECF with Automatic Routing and Polling

The `SendEcfAsync` method handles everything:
1. Routes to the correct endpoint based on `TipoeCF` (31, 32, 33, 34, 41, 43, 44, 45, 46, 47)
2. Submits the ECF
3. Polls the status endpoint with exponential backoff until processing completes
4. Returns the final result or throws `EcfException` on error

```csharp
var result = await client.SendEcfAsync(ecf, new PollingOptions
{
    InitialDelayMs = 1000,
    MaxDelayMs = 30000,
    MaxRetries = 60,
    BackoffMultiplier = 2,
    TimeoutMs = 120000  // 2 minutes total timeout
});
```

### Low-Level: Direct API Access

Access all raw endpoints through the Kiota-generated `Api` property:

```csharp
// Company operations
var companies = await client.Api.Company.GetAsync();
var company = await client.Api.Company["123456789"].GetAsync();
await client.Api.Company.PutAsync(new UpsertCompanyRequest { /* ... */ });
await client.Api.Company["123456789"].DeleteAsync();

// Certificate operations
var certs = await client.Api.Company["123456789"].Certificate.GetAsync();

// ECF query operations
var ecfList = await client.Api.Ecf["123456789"].GetAsync(config =>
{
    config.QueryParameters.Page = "1";
    config.QueryParameters.Limit = "25";
});
var ecfByEncf = await client.Api.Ecf["123456789"]["E310000000001"].GetAsync();
var ecfById = await client.Api.Ecf["123456789"].Message["message-guid"].GetAsync();

// Search all ECFs
var allEcfs = await client.Api.Ecf.GetAsync(config =>
{
    config.QueryParameters.Page = "1";
    config.QueryParameters.Limit = "25";
});

// Aprobacion comercial
await client.Api.Ecf.Aprobacioncomercial["123456789"]["E310000000001"]
    .PostAsync(new SendAcecfRequest { /* ... */ });

// Anulacion de rangos
var anulacion = await client.Api.Ecf.Anularrango["123456789"]
    .PostAsync(new AnulacionRequest { /* ... */ });
var anulaciones = await client.Api.Ecf.Anulaciones.GetAsync();

// Recepcion operations
var ecfRequests = await client.Api.Recepcion.Ecf.GetAsync();
var acecfRequests = await client.Api.Recepcion.Acecf.GetAsync();

// DGII consultations
var directorio = await client.Api.Dgii["123456789"].Consultadirectorio.Listado.GetAsync();
var estado = await client.Api.Dgii["123456789"].Consultaestado.Estado.GetAsync(config =>
{
    config.QueryParameters.RncEmisor = "123456789";
    config.QueryParameters.NcfElectronico = "E310000000001";
    config.QueryParameters.RncComprador = "987654321";
    config.QueryParameters.CodigoSeguridad = "ABC123";
});
var estatus = await client.Api.Dgii["123456789"].Estatusservicios.ObtenerEstatus.GetAsync();

// API Key management
await client.Api.ApiKey.PostAsync(new NewCompanyApiKey { /* ... */ });
```

### Cancellation Support

All async methods support `CancellationToken`:

```csharp
using var cts = new CancellationTokenSource(TimeSpan.FromMinutes(5));
var result = await client.SendEcfAsync(ecf, cancellationToken: cts.Token);
```

## ECF Type Mapping

| TipoeCFType | Route | Description |
|------------|-------|-------------|
| `FacturaDeCreditoFiscalElectronica` | `/ecf/31` | Factura de Credito Fiscal |
| `FacturaDeConsumoElectronica` | `/ecf/32` | Factura de Consumo |
| `NotaDeDebitoElectronica` | `/ecf/33` | Nota de Debito |
| `NotaDeCreditoElectronica` | `/ecf/34` | Nota de Credito |
| `ComprasElectronico` | `/ecf/41` | Compras |
| `GastosMenoresElectronico` | `/ecf/43` | Gastos Menores |
| `RegimenesEspecialesElectronico` | `/ecf/44` | Regimenes Especiales |
| `GubernamentalElectronico` | `/ecf/45` | Gubernamental |
| `ComprobanteDeExportacionesElectronico` | `/ecf/46` | Exportaciones |
| `ComprobanteParaPagosAlExteriorElectronico` | `/ecf/47` | Pagos al Exterior |

## Error Handling

| Exception | When |
|----------|------|
| `EcfException` | ECF processing completed with `Error` status |
| `PollingMaxRetriesException` | Polling exceeded max retries (default 60) |
| `PollingTimeoutException` | Polling exceeded timeout |
| `ProblemDetails` (Kiota) | HTTP 4xx/5xx responses from raw API calls |

## License

MIT
