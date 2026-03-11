# ECF DGII Java SDK

Java SDK for the ECF DGII API (Dominican Republic Electronic Fiscal Receipt system).

## Installation

### Maven

```xml
<dependency>
    <groupId>dom.com.ssd.ecfx</groupId>
    <artifactId>ecf-dgii-client</artifactId>
    <version>1.0.0</version>
</dependency>
```

### Gradle

```groovy
implementation 'dom.com.ssd.ecfx:ecf-dgii-client:1.0.0'
```

## Quick Start

```java
import dom.com.ssd.ecfx.client.EcfClient;
import dom.com.ssd.ecfx.client.model.*;

// Create client
EcfClient client = new EcfClient.Builder()
    .baseUrl("https://api.prod.ecfx.ssd.com.do")
    .apiKey("your-jwt-token")
    .build();

// Send an ECF (routes automatically, polls for completion)
ECF ecf = new ECF();
// ... build your ECF document ...
EcfResponse response = client.sendEcf("your-rnc", ecf);
System.out.println("Status: " + response.getEstatus());
```

## Authentication

The API uses JWT Bearer token authentication. Set your token via:

1. **Builder**: `.apiKey("your-token")`
2. **Environment variable**: `ECF_DGII_API_KEY`

## High-Level API: sendEcf

`sendEcf(rnc, ecf)` encapsulates the full ECF submission workflow:

1. Routes the ECF to the correct endpoint based on `tipoeCF`
2. Submits the document
3. Polls for completion with exponential backoff
4. Returns the final `EcfResponse` when done

### Polling Configuration

```java
EcfClient client = new EcfClient.Builder()
    .baseUrl("https://api.prod.ecfx.ssd.com.do")
    .apiKey("your-token")
    .pollingMaxDurationMs(120_000)  // 2 minutes (default)
    .pollingIntervalMs(1_000)       // 1 second initial (default)
    .build();
```

## Raw API Access

All generated API classes are accessible for direct use:

```java
// Company management
client.getCompanyApi().getCompanies(null, null, 1, 25);
client.getCompanyApi().getCompanyByRnc("123456789");

// ECF operations
client.getEcfApi().searchEcfs("123456789", null, null, null, false, null, null, null, null, 1, 25);

// DGII queries
client.getDgiiApi().consultaEstado("rnc", "encf");

// Reception
client.getRecepcionApi().searchEcfReceptionRequests(null, null, null, 1, 25);
```

## Supported ECF Types

| Type | Code | Endpoint |
|------|------|----------|
| Factura de Credito Fiscal Electronica | 31 | `/ecf/31` |
| Factura de Consumo Electronica | 32 | `/ecf/32` |
| Nota de Debito Electronica | 33 | `/ecf/33` |
| Nota de Credito Electronica | 34 | `/ecf/34` |
| Compras Electronico | 41 | `/ecf/41` |
| Gastos Menores Electronico | 43 | `/ecf/43` |
| Regimenes Especiales Electronico | 44 | `/ecf/44` |
| Gubernamental Electronico | 45 | `/ecf/45` |
| Comprobante de Exportaciones Electronico | 46 | `/ecf/46` |
| Comprobante para Pagos al Exterior Electronico | 47 | `/ecf/47` |

## Android Compatibility

This SDK is compatible with Android API 21+ (Android 5.0). It uses:
- OkHttp (native Android HTTP support)
- ThreeTenBP (Java 8 date/time backport for Android)

## Building from Source

```bash
./mvnw clean install
```

## API Environments

| Environment | URL |
|-------------|-----|
| Test | `https://api.test.ecfx.ssd.com.do` |
| Certification | `https://api.cert.ecfx.ssd.com.do` |
| Production | `https://api.prod.ecfx.ssd.com.do` |
