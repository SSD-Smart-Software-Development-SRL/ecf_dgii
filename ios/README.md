# EcfDgiiClient

Swift SDK for the **ECF DGII API** — electronic fiscal receipt (e-CF) processing for the Dominican Republic.

Certified by DGII. Compatible with iOS, macOS, tvOS, and watchOS.

## Installation

### Swift Package Manager (recommended)

Add to your `Package.swift`:

```swift
dependencies: [
    .package(url: "https://github.com/puntoos/ecf-dgii-swift.git", from: "0.1.0")
]
```

Or in Xcode: **File > Add Package Dependencies** and enter the repository URL.

### CocoaPods

```ruby
pod 'EcfDgiiClient', '~> 0.1.0'
```

## Quick Start

```swift
import EcfDgiiClient

// Initialize the client
let client = EcfClient(
    apiKey: "your-jwt-bearer-token",
    environment: .prod  // .test, .cert, or .prod
)

// Send an ECF with automatic routing and polling
let ecf = ECF(
    encabezado: Encabezado(
        version: .e10,
        idDoc: IdDoc(
            tipoeCF: .facturaDeCreditoFiscalElectronica,
            encf: "E310000000001"
        ),
        emisor: Emisor(
            rncEmisor: "123456789",
            razonSocialEmisor: "Mi Empresa SRL",
            direccionEmisor: "Santo Domingo"
        ),
        totales: totales
    ),
    detallesItems: items
)

do {
    let result = try await client.sendEcf(ecf: ecf)
    print("ECF accepted: \(result.encf), status: \(result.estatus)")
} catch let error as EcfProcessingError {
    print("ECF rejected: \(error.message)")
    print("DGII response: \(error.response)")
}
```

## Features

### High-Level Client (`EcfClient`)

The `EcfClient` provides a simplified interface that handles:

- **Automatic routing** — determines the correct endpoint (31-47) from `encabezado.idDoc.tipoeCF`
- **Polling with exponential backoff** — waits for DGII processing to complete
- **Error handling** — throws `EcfProcessingError` with the full DGII response on rejection
- **Cancellation support** — via Swift structured concurrency (`Task.cancel()`)

```swift
// Custom polling options
let options = PollingOptions(
    initialDelay: 2.0,      // seconds
    maxDelay: 60.0,          // max seconds between polls
    maxRetries: 30,
    backoffMultiplier: 1.5,
    timeout: 300             // total timeout in seconds
)

let result = try await client.sendEcf(ecf: ecf, pollingOptions: options)
```

### Backend / Frontend Architecture

In most apps, the backend sends the ECF and a mobile/web frontend queries the status directly using a read-only API key. The backend generates this restricted token (scoped to tenant/RNC) via the API Keys endpoint and passes it to the client app. The app then queries ECF SSD directly without going through the backend.

See the [main README](../README.md#arquitectura-backend--frontend) for the full diagram and code examples.

> **`sendEcf`** is a convenience that wraps send + polling. For apps where the frontend handles status display, use the individual endpoints.

### Raw API Access

All generated endpoints are available via the static API classes:

```swift
// Company operations
let companies = try await CompanyAPI.getCompanies(apiConfiguration: client.apiConfiguration)
let company = try await CompanyAPI.getCompanyByRnc(rnc: "123456789", apiConfiguration: client.apiConfiguration)

// ECF queries
let ecfs = try await EcfAPI.searchEcfs(rnc: "123456789", apiConfiguration: client.apiConfiguration)
let status = try await EcfAPI.queryEcf(rnc: "123456789", encf: "E310000000001", apiConfiguration: client.apiConfiguration)

// DGII services
let directorio = try await DgiiAPI.consultaDirectorioListado(rnc: "123456789", apiConfiguration: client.apiConfiguration)
let estado = try await DgiiAPI.consultaEstado(rnc: "123456789", rncEmisor: "...", ncfElectronico: "...", rncComprador: "...", codigoSeguridad: "...", apiConfiguration: client.apiConfiguration)

// Reception
let requests = try await RecepcionAPI.searchEcfReceptionRequests(apiConfiguration: client.apiConfiguration)
```

### Environments

| Environment | Base URL |
|---|---|
| `.test` | `https://api.test.ecfx.ssd.com.do` |
| `.cert` | `https://api.cert.ecfx.ssd.com.do` |
| `.prod` | `https://api.prod.ecfx.ssd.com.do` |

```swift
// Or use a custom base URL
let client = EcfClient(apiKey: "token", baseUrl: "https://custom-url.com")
```

## ECF Types

| Type | Code | Description |
|---|---|---|
| `facturaDeCreditoFiscalElectronica` | 31 | Factura de Credito Fiscal Electronica |
| `facturaDeConsumoElectronica` | 32 | Factura de Consumo Electronica |
| `notaDeDebitoElectronica` | 33 | Nota de Debito Electronica |
| `notaDeCreditoElectronica` | 34 | Nota de Credito Electronica |
| `comprasElectronico` | 41 | Compras Electronico |
| `gastosMenoresElectronico` | 43 | Gastos Menores Electronico |
| `regimenesEspecialesElectronico` | 44 | Regimenes Especiales Electronico |
| `gubernamentalElectronico` | 45 | Gubernamental Electronico |
| `comprobanteDeExportacionesElectronico` | 46 | Comprobante de Exportaciones Electronico |
| `comprobanteParaPagosAlExteriorElectronico` | 47 | Comprobante para Pagos al Exterior Electronico |

## API Endpoints

### ECF Operations
| Method | Endpoint | Description |
|---|---|---|
| POST | `/ecf/{31-47}` | Send ECF by type |
| GET | `/ecf/{rnc}/{encf}` | Query ECF status |
| GET | `/ecf/{rnc}` | Search ECFs |
| GET | `/ecf` | Search all ECFs |
| GET | `/ecf/{rnc}/message/{id}` | Get ECF by message ID |
| POST | `/ecf/aprobacioncomercial/{rnc}/{encf}` | Commercial approval |
| POST | `/ecf/anularrango/{rnc}` | Range annulment |
| GET | `/ecf/anulaciones` | List annulments |
| POST | `/ecf/FirmarSemilla/{rnc}` | Sign seed |

### Company Operations
| Method | Endpoint | Description |
|---|---|---|
| GET | `/company` | List companies |
| GET | `/company/{rnc}` | Get company by RNC |
| PUT | `/company` | Create/update company |
| DELETE | `/company/{rnc}` | Delete company |
| GET | `/company/{rnc}/certificate` | Get certificate |
| PUT | `/company/{rnc}/certificate` | Update certificate |

### DGII Operations
| Method | Endpoint | Description |
|---|---|---|
| GET | `/dgii/{rnc}/consultadirectorio/listado` | Directory listing |
| GET | `/dgii/{rnc}/consultaestado/estado` | Status query |
| GET | `/dgii/{rnc}/consultaresultado/estado` | Result query |
| GET | `/dgii/{rnc}/consultatimbre` | Stamp query |
| GET | `/dgii/{rnc}/estatusservicios/obtener-estatus` | Service status |

## Requirements

- iOS 13.0+ / macOS 10.15+ / tvOS 13.0+ / watchOS 6.0+
- Swift 6.0+
- Xcode 16.0+

## Authentication

The API uses JWT Bearer token authentication. Pass your API key when initializing the client:

```swift
let client = EcfClient(apiKey: "your-jwt-token", environment: .prod)
```

## License

MIT
