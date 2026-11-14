# ECF SSD — SDK Delphi

Cliente nativo de la API de ECF SSD para **Delphi / Object Pascal**. Versión inicial: **1.0.0**.
Objetivo de compatibilidad: **Delphi 10.4 Sydney o posterior, Windows Win32 y Win64**.
Depende únicamente de la RTL (`System.Net.HttpClient`, `System.Net.Mime`, `System.JSON`).
No requiere Indy, OpenSSL ni componentes visuales.

Incluye los 41 métodos de la especificación OpenAPI actual, autenticación JWT, ambientes
Test/Cert/Prod y envío de los diez tipos de e-CF con polling. Las rutas se generan;
los cuerpos usan `TJSONObject` y las respuestas generales `TJSONValue`. No hay clases
generadas para cada modelo. El resultado de alto nivel es el record `TEcfResponse`.

## Instalación

### Boss

Después de publicar la primera versión, agrega la dependencia al `boss.json` de tu
aplicación (conservando las demás dependencias) y ejecuta `boss install`:

```json
{
  "dependencies": {
    "github.com/SSD-Smart-Software-Development-SRL/ecf_dgii": "delphi-v1.0.0"
  }
}
```

Fija el tag exacto porque el monorepo contiene releases de otros lenguajes. El
`boss.json` en la raíz del repositorio apunta a `delphi/src/`.

### Instalación desde fuentes o ZIP

1. Clona [ecf_dgii](https://github.com/SSD-Smart-Software-Development-SRL/ecf_dgii) o extrae el archivo de distribución Delphi cuando esté publicado.
2. En **Project → Options → Building → Delphi Compiler → Search path**, agrega la ruta absoluta a `delphi\src` (o `src` dentro del ZIP).
3. Añade `EcfDgii.Client` y `EcfDgii.Types` a tu cláusula `uses`.

También puedes compilar `EcfDgii.dpk` si tu aplicación usa paquetes en tiempo de ejecución.
Es un paquete **runtime**, sin componentes para instalar en la paleta del IDE.
El workflow [publish-delphi](../.github/workflows/publish-delphi.yml) publica el ZIP y
SHA-256 automáticamente al crear una GitHub Release `delphi-vX.Y.Z`, después de validar,
compilar y probar. Consulta [PUBLISHING.md](PUBLISHING.md) para configurar el runner
Windows una vez y publicar nuevas versiones. GetIt es un canal adicional opcional.

## Configuración

```pascal
uses EcfDgii.Client, EcfDgii.Types;

Client := TEcfClient.Create('tu-jwt-token', eeCert);
// O lee ECF_API_KEY del entorno; el ambiente predeterminado es eeTest:
Client := TEcfClient.Create;
// Para una instalación propia:
Client := TEcfClient.Create('tu-jwt-token', eeTest, 'https://tu-api.example');
Client.RequestTimeoutMs := 30000;
```

Cada línea de creación es una alternativa. Libera el cliente con `Free`.
Los ambientes son `eeTest`, `eeCert` y `eeProd`, con las URLs
`https://api.test.ecfx.ssd.com.do`, `https://api.cert.ecfx.ssd.com.do` y
`https://api.prod.ecfx.ssd.com.do`, respectivamente. `ABaseUrl` tiene prioridad sobre el ambiente.
Los redirects HTTP se rechazan; configura directamente la URL final.

Las llamadas son **síncronas**. En VCL/FMX ejecútalas en un hilo de trabajo y utiliza un
cliente por hilo. No compartas una instancia entre solicitudes concurrentes.
En aplicaciones distribuidas a usuarios finales, conserva el token con permisos de
escritura en tu backend; para consultar desde el cliente, usa un token limitado al RNC
emitido por ese backend. Esta versión no incluye cache ni renovación automática de tokens.

## Enviar un e-CF

El archivo `invoice.json` debe contener el comprobante completo según el esquema del tipo
de e-CF. Utiliza nombres JSON camelCase y los valores de enum del API
(por ejemplo, `FacturaDeCreditoFiscalElectronica`, no el número `31`). Los montos se envían
como números JSON. El SDK conserva el contenido del comprobante; la API realiza la validación fiscal.

```pascal
uses
  System.SysUtils, System.JSON, System.IOUtils,
  EcfDgii.Client, EcfDgii.Types;

procedure Enviar(const Archivo: string);
var
  Client: TEcfClient;
  Payload: TJSONValue;
  Respuesta: TEcfResponse;
begin
  Payload := TJSONObject.ParseJSONValue(TFile.ReadAllText(Archivo, TEncoding.UTF8));
  try
    if not (Payload is TJSONObject) then
      raise EArgumentException.Create('Se requiere un objeto JSON');
    Client := TEcfClient.Create('', eeTest); // ECF_API_KEY
    try
      Respuesta := Client.SendEcf(TJSONObject(Payload));
      Writeln(Respuesta.Progress);
      Writeln(Respuesta.Estatus);
      Writeln(Respuesta.CodSec);
      Writeln(Respuesta.ImpresionUrl);
    finally
      Client.Free;
    end;
  finally
    Payload.Free;
  end;
end;
```

`SendEcf` envía una sola vez a `/ecf/31`, `/32`, `/33`, `/34`, `/41`, `/43`, `/44`,
`/45`, `/46` o `/47`, y consulta `/ecf/{rnc}/{encf}`. Solo acepta la respuesta del
`messageId` enviado; nunca devuelve por error un envío anterior del mismo eNCF.
Una consulta vacía o HTTP 404 durante polling se reintenta dentro de los límites configurados.

`Finished` significa que terminó el procesamiento. Revisa también `Estatus`:
puede ser `Aceptado`, `AceptadoCondicional` o `Rechazado`. Un rechazo DGII no se
convierte automáticamente en una excepción si `Progress` es `Finished`.

### Envío sin espera y recuperación

```pascal
Enviado := Client.SubmitEcf(EcfJson);
// Persiste Enviado.MessageId en tu base de datos antes de continuar.
Final := Client.PollEcf(Rnc, Encf, Enviado.MessageId);
```

Si pierdes la conexión o vence el tiempo de espera, consulta el estado existente;
no vuelvas a enviar automáticamente la factura. `PollEcf` permite reanudar con el
`messageId` guardado sin otro POST. Si el POST pierde su respuesta, usa `QueryEcf`
para reconciliar los envíos antes de decidir un nuevo envío.

### Polling

```pascal
Opciones := TEcfPollingOptions.Default;
Opciones.InitialDelayMs := 1000;
Opciones.MaxDelayMs := 30000;
Opciones.MaxAttempts := 60;
Opciones.BackoffMultiplier := 2;
Opciones.TimeoutMs := 120000;
Respuesta := Client.SendEcf(EcfJson, Opciones);
```

La primera consulta es inmediata; `MaxAttempts` cuenta consultas, no reenvíos.
`TimeoutMs` comienza después del POST y limita el polling. Cada consulta recibe el
menor valor entre `RequestTimeoutMs` y el tiempo restante. La RTL aplica tiempos de
conexión y respuesta: una operación de red en curso puede exceder el plazo global;
no se trata de una cancelación dura. No hay reintentos automáticos de POST/PUT/DELETE,
ni de errores HTTP distintos de 404 durante polling.

## Consultas y demás operaciones

`TEcfClient` hereda todos los métodos de [EcfDgii.Api.pas](src/EcfDgii.Api.pas).
Los nombres corresponden a los `operationId` del OpenAPI.

| Área | Métodos principales |
| --- | --- |
| Empresas | `GetCompanies`, `GetCompanyByRnc`, `UpsertCompany`, `DeleteCompany` |
| Certificados | `GetCurrentCertificate`, `UpdateCertificateCompany` |
| e-CF | `QueryEcf`, `GetEcfById`, `SearchEcfs`, `SearchAllEcfs`, `RecepcionEcf31` … `RecepcionEcf47` |
| Anulación | `AnulacionRangos`, `ListAnulaciones` |
| Recepción | `SearchEcfReceptionRequests`, `GetEcfReceptionRequest`, `SearchEcfReceptionRequestsByRnc`, `GetEcfReceptorByMessageId` |
| Aprobación comercial | `SendAprobacionComercial`, `SearchAcecfReceptionRequests`, `GetAcecfReceptionRequest` |
| DGII | `ConsultaDirectorioListado`, `ConsultaDirectorioObtenerDirectorioPorRnc`, `ConsultaEstado`, `ConsultaResultado`, `ConsultaRFCE`, `ConsultaTimbre`, `ConsultaTimbreFC`, `ConsultaTrackId` |
| Servicios DGII | `EstatusServiciosObtenerEstatus`, `EstatusServiciosObtenerVentanasMantenimiento` |
| Otros | `FirmarSemilla`, `NewCompanyApiKey`, `RequestJson`, `RequestText` |

Los filtros se pasan como `TEcfQuery` con el nombre exacto del API. Repite el nombre
para filtros de tipo array. El SDK codifica las rutas y los parámetros en UTF-8.

```pascal
uses System.JSON, System.Net.URLClient, EcfDgii.Http;

Datos := Client.GetCompanies(TEcfQuery.Create(
  TNameValuePair.Create('Rncs', '131000000'),
  TNameValuePair.Create('Rncs', '132000000'),
  TNameValuePair.Create('Page', '1'),
  TNameValuePair.Create('Limit', '20')));
try
  if Datos <> nil then Writeln(Datos.ToJSON);
finally
  Datos.Free;
end;

// Certificado: multipart/form-data con certificate y password.
Client.UpdateCertificateCompany('131000000', 'certificado.p12', Password);
// Semilla: multipart/form-data con xml; devuelve el XML firmado como string.
XmlFirmado := Client.FirmarSemilla('131000000', 'semilla.xml');
```

Los parámetros de consulta se representan como texto porque forman parte de la URL;
para montos usa punto decimal. Los cuerpos JSON mantienen sus tipos numéricos.

## Memoria, respuestas y errores

- Los cuerpos `TJSONObject`/`TJSONValue` de entrada pertenecen al llamador: el SDK no los modifica ni los libera.
- Cada resultado `TJSONValue` pertenece al llamador: usa `try/finally` y `Free`. Una respuesta vacía devuelve `nil`.
- `TEcfResponse` es un record administrado: no se libera. `RawJson` conserva todos los campos originales; `FechaFirma` conserva el ISO 8601 con su zona horaria. `HasMontoTotal` y `HasSecuenciaUtilizada` distinguen ausencia/null de cero/false.
- `EEcfHttpError`: `StatusCode` y `ResponseBody` conservan el error HTTP. El mensaje no incluye el cuerpo para evitar exponer datos en logs por defecto.
- `EEcfProcessingError`: el API devolvió `Progress = Error`; consulta `Response.Errors`, `Response.Mensaje` y `Response.RawJson`.
- `EEcfPollingTimeout` / `EEcfPollingAttemptsExceeded`: límite de polling; conserva el `messageId` y consulta más tarde.
- `EEcfProtocolError`: respuesta inesperada o JSON inválido. Los errores de red/TLS de la RTL se propagan.

## Compilación y pruebas

En una **RAD Studio Command Prompt** de Windows, desde `delphi`:

```bat
scripts\test.cmd dcc32
scripts\test.cmd dcc64
```

Compila el paquete, ejecuta cinco suites offline (sin credenciales ni llamadas a la API)
y compila `examples\SendEcf.dpr`. Las pruebas comprueban los diez tipos, propiedad de
JSON, correlación del messageId, 404/vacíos, errores, backoff, límites, encoding y multipart.
Ejecuta el ejemplo solo cuando quieras enviar un comprobante al ambiente Test:

```bat
set ECF_API_KEY=tu-token-de-test
build\SendEcf.exe invoice.json
```

La implementación inicial se preparó en macOS sin compilador Delphi. La compilación
y ejecución de estas pruebas en Windows están pendientes. El workflow las exige antes
de adjuntar los archivos de distribución; necesita un runner Windows con Delphi.

## Regenerar la API

Node.js 18+ es necesario solo para mantenimiento, no para usar el SDK:

```sh
node delphi/scripts/generate.mjs
node delphi/scripts/generate.mjs --check
node --test delphi/tests/*.test.mjs
```

Por defecto lee la copia versionada `delphi/openapi-v1.json`, también incluida en
el ZIP. Actualízala desde el OpenAPI de la API antes de regenerar. `SPEC_PATH` permite
otra ubicación para desarrollo local. Solo regenera
`EcfDgii.Api.pas`; las unidades de HTTP, tipos y polling se mantienen manualmente.
Las pruebas Node verifican la cobertura de rutas y la correspondencia con el contrato;
no compilan ni ejecutan el código Delphi.

Licencia: [Apache-2.0](LICENSE).
