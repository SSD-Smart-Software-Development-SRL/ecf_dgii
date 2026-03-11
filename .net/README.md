# DGII ECF

| Paquetes  |              |
|-----------|--------------|
| SDK  |[![NuGet Downloads](https://img.shields.io/nuget/dt/SSDDO.ECF_DGII.SDK)](https://www.nuget.org/packages/SSDDO.ECF_DGII.SDK)|


SDK oficial para integrar la facturación electrónica (e-CF) en República Dominicana a través del servicio **[ECF SSD](https://ecf.ssd.com.do)**.

## Qué cambió en v3

Las versiones anteriores (`v1`, `v2`) requerían que cada empresa implementara la comunicación directa con la DGII: manejo de certificados, firmado de XML, semilla/token, envío de comprobantes, manejo de errores, reintentos, almacenamiento, etc. Todo eso era responsabilidad del desarrollador.

**La v3 cambia el enfoque completamente.** Ahora el SDK se conecta a la plataforma [ECF SSD](https://ecf.ssd.com.do), que se encarga de:

- ✅ Firmado de comprobantes (XML signing)
- ✅ Autenticación con la DGII (semilla/token)
- ✅ Envío y recepción de e-CF
- ✅ Validación emisor-receptor
- ✅ Almacenamiento seguro
- ✅ Reintentos automáticos
- ✅ Manejo de certificados digitales

**Tu único trabajo es:** registrarte en [ecf.ssd.com.do](https://ecf.ssd.com.do), completar la certificación DGII, obtener tu API key, y enviar tus comprobantes con este SDK.

## Comenzar

### 1. Regístrate en [ecf.ssd.com.do](https://ecf.ssd.com.do)

Crea tu cuenta, sube tu certificado digital, y completa el proceso de certificación con la DGII.

### 2. Instala el paquete

```sh
dotnet add package SSDDO.ECF_DGII.SDK
```

### 3. Envía tu primer comprobante

```csharp
using EcfDgii.Client;
using EcfDgii.Client.Generated.Models;

// Configura el cliente con tu API key (JWT obtenido en ecf.ssd.com.do)
var client = new EcfClient(new EcfClientOptions
{
    ApiKey = "tu-jwt-token",        // o usa la variable de entorno ECF_API_KEY
    Environment = EcfEnvironment.Prod
});

// Construye el comprobante
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
            RncEmisor = "123456789",
            RazonSocialEmisor = "Mi Empresa SRL",
            DireccionEmisor = "Calle Principal #1, Santo Domingo",
            FechaEmision = DateTimeOffset.Now
        },
        Comprador = new Encabezado_compradorMember1
        {
            // datos del comprador...
        },
        Totales = new Totales
        {
            // montos, ITBIS, etc.
        }
    },
    DetallesItems = new List<Item>
    {
        new Item
        {
            NombreItem = "Servicio de consultoría",
            IndicadorFacturacion = IndicadorFacturacionType.NoFacturable_18Percent,
            CantidadItem = 1,
            PrecioUnitarioItem = 10000.00,
            MontoItem = 10000.00
        }
    }
};

// Envía y espera el resultado
// SendEcfAsync hace todo: enruta al endpoint correcto, envía, y espera hasta que la DGII responda
try
{
    EcfResponse resultado = await client.SendEcfAsync(ecf);
    Console.WriteLine($"Comprobante procesado exitosamente!");
    Console.WriteLine($"Estado: {resultado.Progress}");
    Console.WriteLine($"Mensaje DGII: {resultado.Mensaje}");
    Console.WriteLine($"Código seguridad: {resultado.CodSec}");
    Console.WriteLine($"URL impresión: {resultado.ImpresionUrl}");
}
catch (EcfException ex)
{
    Console.WriteLine($"Error: {ex.Message}");
    Console.WriteLine($"Detalle: {ex.Response.Errors}");
}
```

**Eso es todo.** No necesitas manejar XML, firmar documentos, obtener semillas, ni reintentar requests. El servicio ECF SSD se encarga de todo.

## Respuesta (`EcfResponse`)

Cuando `SendEcfAsync` termina exitosamente, retorna un `EcfResponse` con toda la información que necesitas para cumplir con los requisitos de la DGII:

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `ImpresionUrl` | `string` | URL para generar el código QR requerido por la DGII en el comprobante impreso |
| `CodSec` | `string` | Código de seguridad — debe aparecer en el comprobante impreso |
| `FechaFirma` | `DateTimeOffset` | Fecha y hora en que el comprobante fue firmado digitalmente |
| `Estatus` | `EcfEstado` | Estado asignado por la DGII (`Aceptado`, `AceptadoCondicional`, `Rechazado`) |
| `Progress` | `EcfProgress` | Estado del procesamiento (`Queued`, `Sending`, `Polling`, `Finished`, `Error`) |
| `Encf` | `string` | Número de comprobante fiscal electrónico (eNCF) |
| `RncEmisor` | `string` | RNC del emisor |
| `Mensaje` | `string` | Mensaje de respuesta de la DGII |
| `Errors` | `string` | Detalle de errores (si los hay) |
| `MontoTotal` | `double` | Monto total del comprobante |
| `SecuenciaUtilizada` | `bool` | Indica si la secuencia fue utilizada |
| `DgiiEnvironment` | `DGIIEnvironment` | Ambiente DGII donde fue procesado |
| `MessageId` | `string` | Identificador único del mensaje |

### QR e Impresión del Comprobante

La DGII requiere que los comprobantes impresos incluyan un código QR. El `ImpresionUrl` contiene la URL que debe codificarse como QR:

```csharp
EcfResponse resultado = await client.SendEcfAsync(ecf);

// Datos necesarios para el comprobante impreso
string urlQr = resultado.ImpresionUrl;          // codificar como QR
string codigoSeguridad = resultado.CodSec;      // imprimir en el comprobante
DateTimeOffset fechaFirma = resultado.FechaFirma; // fecha de firma digital

// Verificar aceptación
if (resultado.Estatus == EcfEstado.Aceptado)
{
    Console.WriteLine("Comprobante aceptado por la DGII");
    Console.WriteLine($"QR URL: {urlQr}");
    Console.WriteLine($"Código seguridad: {codigoSeguridad}");
    Console.WriteLine($"Firmado: {fechaFirma}");
}
```

## Configuración

### Variables de Entorno

| Variable       | Descripción                                      |
|---------------|--------------------------------------------------|
| `ECF_API_KEY` | JWT Bearer token (obtenido en ecf.ssd.com.do)    |
| `ECF_API_URL` | URL base (solo si necesitas override)             |

### Ambientes

| Ambiente | URL | Uso |
|----------|-----|-----|
| Test     | `https://api.test.ecfx.ssd.com.do` | Desarrollo y pruebas |
| Cert     | `https://api.cert.ecfx.ssd.com.do` | Proceso de certificación DGII |
| Prod     | `https://api.prod.ecfx.ssd.com.do` | Producción |

### Opciones de Polling

`SendEcfAsync` espera automáticamente a que la DGII procese el comprobante. Puedes personalizar el comportamiento:

```csharp
var resultado = await client.SendEcfAsync(ecf, new PollingOptions
{
    InitialDelayMs = 1000,      // espera inicial entre consultas
    MaxDelayMs = 30000,         // espera máxima entre consultas
    MaxRetries = 60,            // máximo de reintentos
    BackoffMultiplier = 2,      // multiplicador exponencial
    TimeoutMs = 120000          // timeout total (2 minutos)
});
```

## Tipos de Comprobantes

| TipoeCF | Ruta | Descripción |
|---------|------|-------------|
| `FacturaDeCreditoFiscalElectronica` | `/ecf/31` | Factura de Crédito Fiscal |
| `FacturaDeConsumoElectronica` | `/ecf/32` | Factura de Consumo |
| `NotaDeDebitoElectronica` | `/ecf/33` | Nota de Débito |
| `NotaDeCreditoElectronica` | `/ecf/34` | Nota de Crédito |
| `ComprasElectronico` | `/ecf/41` | Compras |
| `GastosMenoresElectronico` | `/ecf/43` | Gastos Menores |
| `RegimenesEspecialesElectronico` | `/ecf/44` | Regímenes Especiales |
| `GubernamentalElectronico` | `/ecf/45` | Gubernamental |
| `ComprobanteDeExportacionesElectronico` | `/ecf/46` | Exportaciones |
| `ComprobanteParaPagosAlExteriorElectronico` | `/ecf/47` | Pagos al Exterior |

## Acceso Directo al API

Para operaciones que no cubre `SendEcfAsync`, usa `client.Api` directamente:

```csharp
// Consultar comprobantes
var comprobantes = await client.Api.Ecf["123456789"].GetAsync();

// Buscar un comprobante específico
var resultado = await client.Api.Ecf["123456789"]["E310000000001"].GetAsync();

// Consultar estado en la DGII
var estado = await client.Api.Dgii["123456789"].Consultaestado.Estado.GetAsync(config =>
{
    config.QueryParameters.RncEmisor = "123456789";
    config.QueryParameters.NcfElectronico = "E310000000001";
    config.QueryParameters.RncComprador = "987654321";
    config.QueryParameters.CodigoSeguridad = "ABC123";
});

// Gestión de empresas
var empresas = await client.Api.Company.GetAsync();
await client.Api.Company.PutAsync(new UpsertCompanyRequest { /* ... */ });

// Aprobación comercial
await client.Api.Ecf.Aprobacioncomercial["123456789"]["E310000000001"]
    .PostAsync(new SendAcecfRequest { /* ... */ });

// Anulación de rangos
await client.Api.Ecf.Anularrango["123456789"]
    .PostAsync(new AnulacionRequest { /* ... */ });

// Estatus de servicios DGII
var estatus = await client.Api.Dgii["123456789"].Estatusservicios.ObtenerEstatus.GetAsync();
```

## Manejo de Errores

| Excepción | Cuándo |
|----------|--------|
| `EcfException` | El comprobante fue procesado pero la DGII lo rechazó |
| `PollingMaxRetriesException` | Se agotaron los reintentos esperando respuesta |
| `PollingTimeoutException` | Se agotó el timeout esperando respuesta |

```csharp
try
{
    var resultado = await client.SendEcfAsync(ecf);
}
catch (EcfException ex)
{
    // La DGII rechazó el comprobante
    Console.WriteLine($"Rechazado: {ex.Response.Errors}");
    Console.WriteLine($"Estado DGII: {ex.Response.Estatus}");
}
catch (PollingTimeoutException)
{
    // El comprobante fue enviado pero no se recibió respuesta a tiempo
    // Puedes consultar el estado después con client.Api.Ecf[rnc][encf].GetAsync()
}
```

## Cancelación

Todas las operaciones async soportan `CancellationToken`:

```csharp
using var cts = new CancellationTokenSource(TimeSpan.FromMinutes(5));
var resultado = await client.SendEcfAsync(ecf, cancellationToken: cts.Token);
```

## Migración desde v2

| v2 (implementación propia) | v3 (ECF SSD) |
|---|---|
| Manejar certificado digital (.p12/.pfx) | Subir certificado una vez en ecf.ssd.com.do |
| Obtener semilla y firmarla | No necesario — el servicio lo maneja |
| Serializar a XML y firmar | No necesario — envías JSON, el servicio firma |
| Enviar XML a la DGII | `await client.SendEcfAsync(ecf)` |
| Parsear respuesta XML | Respuesta tipada `EcfResponse` |
| Implementar reintentos | Polling automático con backoff exponencial |
| `SSDDO.ECF_DGII.Models` + `SSDDO.ECF_DGII.SDK` | Solo `SSDDO.ECF_DGII.SDK` v3 |

## Por qué ECF SSD

> Con la v2 tenías la librería, pero aún debías implementar seguridad, almacenamiento, firmado, manejo de certificados, módulo de recepción, reintentos, y más.

**Con la v3 y [ECF SSD](https://ecf.ssd.com.do):**
- Instalas el paquete NuGet
- Te registras y certificas en [ecf.ssd.com.do](https://ecf.ssd.com.do)
- Envías comprobantes con una línea de código
- El servicio se encarga del firmado, validación, envío a DGII, almacenamiento, y más

Para más información visita [https://ecf.ssd.com.do](https://ecf.ssd.com.do)

____

🇩🇴 Hecho con plátano power

_© Smart Software Development SSD SRL 2026_
