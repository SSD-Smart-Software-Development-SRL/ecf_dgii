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

## Full ECF Example

```java
import dom.com.ssd.ecfx.client.EcfClient;
import dom.com.ssd.ecfx.client.model.*;

import java.text.SimpleDateFormat;
import java.util.Arrays;

EcfClient client = new EcfClient.Builder()
    .baseUrl("https://api.prod.ecfx.ssd.com.do")
    .apiKey("your-jwt-token")
    .build();

SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");

// Build a Factura de Credito Fiscal Electronica (type 31)
Ecf31ECF ecf = new Ecf31ECF();

// Encabezado
Ecf31Encabezado encabezado = new Ecf31Encabezado();

// IdDoc
Ecf31IdDoc idDoc = new Ecf31IdDoc();
idDoc.setEncf("E310000051630");
idDoc.setTipoeCF(TipoeCFType.FACTURA_DE_CREDITO_FISCAL_ELECTRONICA);
idDoc.setTipoPago(Ecf31TipoPagoType.CONTADO);
idDoc.setTipoIngresos(Ecf31TipoIngresosValidationType._01);
idDoc.setIndicadorMontoGravado(IndicadorMontoGravadoType.CON_ITBIS_INCLUIDO);
idDoc.setFechaVencimientoSecuencia(dateFormat.parse("2028-12-31"));

Ecf31FormaDePago formaPago = new Ecf31FormaDePago();
formaPago.setFormaPago(Ecf31FormaPagoType.EFECTIVO);
formaPago.setMontoPago(new Ecf31FormaDePagoMontoPago(1015.25));
idDoc.setTablaFormasPago(Arrays.asList(formaPago));

encabezado.setIdDoc(idDoc);

// Emisor
Ecf31Emisor emisor = new Ecf31Emisor();
emisor.setRncEmisor("131460941");
emisor.setFechaEmision(dateFormat.parse("2026-01-10"));
emisor.setDireccionEmisor("AVE. ISABEL AGUIAR NO. 269, ZONA INDUSTRIAL DE HERRERA");
emisor.setRazonSocialEmisor("DOCUMENTOS ELECTRONICOS DE 02");
encabezado.setEmisor(emisor);

// Comprador
Ecf31Comprador comprador = new Ecf31Comprador();
comprador.setRncComprador("131880681");
comprador.setRazonSocialComprador("DOCUMENTOS ELECTRONICOS DE 03");
encabezado.setComprador(comprador);

// Totales
Ecf31Totales totales = new Ecf31Totales();
totales.setItbiS1(new Ecf31IdDocTotalPaginas(18));
totales.setMontoGravadoI1(new Ecf31DescuentoORecargoMontoDescuentooRecargo(762.71));
totales.setMontoGravadoTotal(new Ecf31DescuentoORecargoMontoDescuentooRecargo(762.71));
totales.setTotalITBIS1(new Ecf31DescuentoORecargoMontoDescuentooRecargo(137.29));
totales.setTotalITBIS(new Ecf31DescuentoORecargoMontoDescuentooRecargo(137.29));
totales.setMontoNoFacturable(new Ecf31TotalesMontoNoFacturable(100.0));
totales.setMontoTotal(new Ecf31FormaDePagoMontoPago(1015.25));
totales.setMontoPeriodo(new Ecf31TotalesMontoNoFacturable(1015.25));

Ecf31ImpuestoAdicional2 impAdicional = new Ecf31ImpuestoAdicional2();
impAdicional.setTipoImpuesto(Ecf31CodificacionTipoImpuestosType._002);
impAdicional.setTasaImpuestoAdicional(new Ecf31ImpuestoAdicional2TasaImpuestoAdicional(2));
impAdicional.setOtrosImpuestosAdicionales(
    new Ecf31ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico(15.25));
totales.setImpuestosAdicionales(Arrays.asList(impAdicional));
totales.setMontoImpuestoAdicional(
    new Ecf31ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico(15.25));
encabezado.setTotales(totales);

encabezado.setVersion(Ecf31VersionType.VERSION1_0);
ecf.setEncabezado(encabezado);

// DetallesItems
Ecf31Item item1 = new Ecf31Item();
item1.setMontoItem(new Ecf31FormaDePagoMontoPago(1016.95));
item1.setNombreItem("Iphone 18 Pro max");
item1.setNumeroLinea(new AcecfReceptionRequestDtoProgress(1));
item1.setCantidadItem(new Ecf31ItemCantidadItem(1));
item1.setUnidadMedida(UnidadMedidaType.UNIDAD);
item1.setPrecioUnitarioItem(new Ecf31ItemPrecioUnitarioItem(1016.95));
item1.setIndicadorFacturacion(Ecf31IndicadorFacturacionType.ITBIS1_18_PERCENT);
item1.setIndicadorBienoServicio(Ecf31IndicadorBienoServicioType.BIEN);

Ecf31ImpuestoAdicional tablaImp = new Ecf31ImpuestoAdicional();
tablaImp.setTipoImpuesto(Ecf31CodificacionTipoImpuestosType._002);
item1.setTablaImpuestoAdicional(Arrays.asList(tablaImp));

Ecf31Item item2 = new Ecf31Item();
item2.setMontoItem(new Ecf31FormaDePagoMontoPago(100.0));
item2.setNombreItem("Costo de Envío");
item2.setNumeroLinea(new AcecfReceptionRequestDtoProgress(2));
item2.setCantidadItem(new Ecf31ItemCantidadItem(1));
item2.setUnidadMedida(UnidadMedidaType.UNIDAD);
item2.setPrecioUnitarioItem(new Ecf31ItemPrecioUnitarioItem(100.0));
item2.setIndicadorFacturacion(Ecf31IndicadorFacturacionType.NO_FACTURABLE_18_PERCENT);
item2.setIndicadorBienoServicio(Ecf31IndicadorBienoServicioType.SERVICIO);

ecf.setDetallesItems(Arrays.asList(item1, item2));

// DescuentosORecargos
Ecf31DescuentoORecargo descuento = new Ecf31DescuentoORecargo();
descuento.setTipoValor(TipoDescuentoRecargoType.DOLLAR);
descuento.setTipoAjuste(Ecf31TipoAjusteType.D);
descuento.setNumeroLinea(new AcecfReceptionRequestDtoProgress(1));
descuento.setMontoDescuentooRecargo(new Ecf31DescuentoORecargoMontoDescuentooRecargo(84.75));
descuento.setDescripcionDescuentooRecargo("Descuento");
descuento.setIndicadorFacturacionDescuentooRecargo(IndicadorFacturacionDRType.ITBIS1_18_PERCENT);

ecf.setDescuentosORecargos(Arrays.asList(descuento));

// Send it
EcfResponse response = client.sendEcf("131460941", ecf);
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

## Backend / Frontend Architecture

In most apps, the backend handles business logic and sends the ECF. The frontend gets a read-only token to query status directly:

```java
// Your invoice endpoint — business logic + send to ECF SSD
@PostMapping("/api/v1/invoices")
public ResponseEntity<?> createInvoice(@RequestBody CreateInvoiceRequest request) {
    // 1. Validate and save your internal invoice
    Invoice invoice = invoiceService.validateAndSave(request);
    // 2. Convert to ECF format
    ECF ecf = mapper.toEcf(invoice);
    // 3. Send to ECF SSD (no polling)
    EcfResponse response = client.getEcfApi().recepcionEcf31(rnc, ecf);
    invoiceService.updateMessageId(invoice.getId(), response.getMessageId());
    return ResponseEntity.ok(Map.of("id", invoice.getId(), "messageId", response.getMessageId()));
}

// Separate endpoint: generate read-only token for frontend
@GetMapping("/api/v1/ecf-token")
public ResponseEntity<?> getEcfToken() {
    NewCompanyApiKeyResponse apiKey = client.getApiKeyApi().newCompanyApiKey(request); // scoped to tenant/RNC
    return ResponseEntity.ok(Map.of("token", apiKey.getToken()));
}
```

The frontend stores the token securely, renews it on `401` or expiry, and queries ECF SSD directly. See the [main README](../README.md#arquitectura-backend--frontend) for the full diagram.

> **`sendEcf`** wraps send + polling into a single call. For apps with a frontend, use the individual endpoints.

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
