# ECF DGII C++ SDK Client

SDK de C++ para la API de ECF DGII (comprobantes fiscales electrónicos de República Dominicana).

## Descripción general

Esta biblioteca proporciona un cliente de alto nivel en C++ para enviar comprobantes fiscales electrónicos (e-CF) a la DGII a través de la API de ECF. Incluye:

- **Modelos y clases de API autogenerados** a partir de la especificación OpenAPI usando [OpenAPI Generator](https://openapi-generator.tech) (`cpp-restsdk`)
- **`EcfClient` de alto nivel** con un método `sendEcf()` que maneja el enrutamiento, polling y manejo de errores automáticamente
- **Acceso directo a la API** a todos los endpoints crudos mediante los objetos de API generados

## Instalación

### Opción 1: vcpkg (Recomendado)

Agregar a tu `vcpkg.json`:

```json
{
  "dependencies": ["ecf-dgii-client"]
}
```

O instalar directamente:

```sh
vcpkg install ecf-dgii-client
```

Luego en tu CMakeLists.txt:

```cmake
find_package(ecf-dgii-client REQUIRED)
target_link_libraries(your_target PRIVATE ecf-dgii-client::ecf-dgii-client)
```

### Opción 2: Conan

Agregar a tu `conanfile.txt`:

```ini
[requires]
ecf-dgii-client/0.1.0

[generators]
CMakeDeps
CMakeToolchain
```

O en `conanfile.py`:

```python
def requirements(self):
    self.requires("ecf-dgii-client/0.1.0")
```

Luego en tu CMakeLists.txt:

```cmake
find_package(ecf-dgii-client REQUIRED)
target_link_libraries(your_target PRIVATE ecf-dgii-client::ecf-dgii-client)
```

### Opción 3: NuGet (Visual Studio / Windows)

```sh
nuget install ecf-dgii-client.cpp
```

O mediante el administrador de paquetes NuGet de Visual Studio, buscar `ecf-dgii-client.cpp`.

### Opción 4: Compilar desde el código fuente

#### Requisitos previos

Instalar [cpprestsdk](https://github.com/Microsoft/cpprestsdk) y [Boost](https://www.boost.org/):

- **macOS**: `brew install cpprestsdk boost`
- **Linux (Debian/Ubuntu)**: `sudo apt-get install libcpprest-dev libboost-all-dev`
- **Windows**: `vcpkg install cpprestsdk cpprestsdk:x64-windows boost-uuid boost-uuid:x64-windows`

#### Compilar e instalar

```sh
mkdir build && cd build
cmake ..
cmake --build .
sudo cmake --install .
```

Luego en tu CMakeLists.txt:

```cmake
find_package(ecf-dgii-client REQUIRED)
target_link_libraries(your_target PRIVATE ecf-dgii-client::ecf-dgii-client)
```

## Inicio rápido

### Cliente de alto nivel (Recomendado)

`EcfClient` proporciona una interfaz simple que maneja el enrutamiento al endpoint correcto, polling hasta completar y manejo de errores:

```cpp
#include <ecf-dgii-client/EcfClient.h>

using namespace ecf_dgii;
using namespace org::openapitools::client::model;

int main() {
    // Configurar el cliente
    EcfClientConfig config;
    config.apiKey = "tu-token-jwt";      // o usar la variable de entorno ECF_API_KEY
    config.environment = "test";          // "test", "cert" o "prod"

    EcfClient client(config);

    // Construir un ECF
    auto ecf = std::make_shared<ECF>();
    auto encabezado = std::make_shared<Encabezado>();
    auto idDoc = std::make_shared<IdDoc>();
    auto emisor = std::make_shared<Emisor>();

    auto tipoEcf = std::make_shared<TipoeCFType>();
    tipoEcf->setValue(TipoeCFType::eTipoeCFType::FACTURADECREDITOFISCALELECTRONICA);
    idDoc->setTipoeCF(tipoEcf);
    idDoc->setEncf(_XPLATSTR("E310000000001"));

    emisor->setRncEmisor(_XPLATSTR("123456789"));
    emisor->setRazonSocialEmisor(_XPLATSTR("Mi Empresa SRL"));

    encabezado->setIdDoc(idDoc);
    encabezado->setEmisor(emisor);
    ecf->setEncabezado(encabezado);

    // ... establecer items, totales, etc.

    // Enviar y esperar el resultado (maneja enrutamiento + polling automáticamente)
    try {
        auto result = client.sendEcf(ecf).get();
        std::cout << "ECF procesado! Message ID: "
                  << utility::conversions::to_utf8string(result->getMessageId())
                  << std::endl;
    } catch (const EcfError& e) {
        std::cerr << "Error ECF: " << e.what() << std::endl;
        // Acceder a la respuesta completa: e.getResponse()
    } catch (const PollingTimeoutError& e) {
        std::cerr << "Tiempo de polling agotado" << std::endl;
    } catch (const PollingMaxRetriesError& e) {
        std::cerr << "Máximo de reintentos excedido" << std::endl;
    }

    return 0;
}
```

### Opciones de polling

Personalizar el comportamiento de polling:

```cpp
PollingOptions options;
options.initialDelay = std::chrono::milliseconds(2000);
options.maxDelay = std::chrono::milliseconds(60000);
options.maxRetries = 30;
options.backoffMultiplier = 1.5;
options.timeout = std::chrono::milliseconds(300000);  // 5 minutos

auto result = client.sendEcf(ecf, options).get();
```

### Arquitectura Backend / Frontend

En la mayoría de aplicaciones, el backend envía el ECF y el frontend consulta el estado directamente usando un API key de solo lectura. El backend genera este token restringido (limitado al tenant/RNC) mediante el endpoint `ApiKeyApi::newCompanyApiKey` y lo pasa al frontend. El frontend entonces consulta ECF SSD directamente sin pasar por el backend.

Para el frontend, usa `EcfFrontendClient` que expone solo los endpoints de consulta (solo lectura):

```cpp
#include <ecf-dgii-client/EcfClient.h>

using namespace ecf_dgii;

// Frontend: cliente de solo lectura
EcfClientConfig frontendConfig;
frontendConfig.apiKey = "token-solo-lectura-del-frontend";
frontendConfig.environment = "prod";

EcfFrontendClient frontendClient(frontendConfig);

// Solo operaciones de lectura disponibles
auto ecfResults = frontendClient.ecfApi()->queryEcf(
    _XPLATSTR("123456789"), _XPLATSTR("E310000000001"), boost::optional<bool>(false)
).get();
```

Consulta el [README principal](../README.md#arquitectura-backend--frontend) para el diagrama completo y ejemplos de código.

> **`sendEcf`** envuelve envío + polling en una sola llamada. Para aplicaciones con frontend, usa los endpoints individuales.

### Acceso directo a la API

Acceder a todos los endpoints crudos de la API mediante los objetos de API generados:

```cpp
EcfClient client(config);

// Operaciones de empresa
auto companies = client.companyApi()->getCompanies(
    boost::none, boost::none, boost::optional<int32_t>(1), boost::optional<int32_t>(25)
).get();

// Consulta de ECF
auto ecfResults = client.ecfApi()->queryEcf(
    _XPLATSTR("123456789"), _XPLATSTR("E310000000001"), boost::optional<bool>(false)
).get();

// Operaciones DGII
auto status = client.dgiiApi()->estatusServicios(_XPLATSTR("123456789")).get();

// Operaciones de recepción
auto requests = client.recepcionApi()->searchEcfReceptionRequests(
    boost::none, boost::none, boost::none, boost::none, boost::none
).get();
```

## Autenticación

La API usa autenticación con token Bearer JWT. Proporciona tu API key de una de estas dos formas:

1. **Configuración directa**: `config.apiKey = "tu-token-jwt";`
2. **Variable de entorno**: `export ECF_API_KEY="tu-token-jwt"`

## Entornos

| Entorno | URL |
|---------|-----|
| `test` | `https://api.test.ecfx.ssd.com.do` |
| `cert` | `https://api.cert.ecfx.ssd.com.do` |
| `prod` | `https://api.prod.ecfx.ssd.com.do` |

También puedes establecer una URL base personalizada mediante `config.baseUrl` o la variable de entorno `ECF_API_URL`.

## Enrutamiento por tipo de ECF

El método `sendEcf()` enruta automáticamente al endpoint correcto según el `tipoeCF`:

| Tipo de ECF | Ruta | Descripción |
|-------------|------|-------------|
| FacturaDeCreditoFiscalElectronica | `/ecf/31` | Factura de crédito fiscal electrónica |
| FacturaDeConsumoElectronica | `/ecf/32` | Factura de consumo electrónica |
| NotaDeDebitoElectronica | `/ecf/33` | Nota de débito electrónica |
| NotaDeCreditoElectronica | `/ecf/34` | Nota de crédito electrónica |
| ComprasElectronico | `/ecf/41` | Compras electrónico |
| GastosMenoresElectronico | `/ecf/43` | Gastos menores electrónico |
| RegimenesEspecialesElectronico | `/ecf/44` | Regímenes especiales electrónico |
| GubernamentalElectronico | `/ecf/45` | Gubernamental electrónico |
| ComprobanteDeExportacionesElectronico | `/ecf/46` | Comprobante de exportaciones electrónico |
| ComprobanteParaPagosAlExteriorElectronico | `/ecf/47` | Comprobante para pagos al exterior electrónico |

## Publicación

### ConanCenter

1. Hacer fork de [conan-center-index](https://github.com/conan-io/conan-center-index)
2. Crear `recipes/ecf-dgii-client/all/conanfile.py` usando el `conanfile.py` de este repositorio como punto de partida (adaptado a las convenciones de conan-center-index)
3. Agregar `recipes/ecf-dgii-client/config.yml` con los mapeos de versiones
4. Enviar un pull request

Probar localmente primero:

```sh
conan create . --build=missing
conan test test_package ecf-dgii-client/0.1.0
```

### vcpkg

1. Hacer fork de [vcpkg](https://github.com/microsoft/vcpkg)
2. Copiar `vcpkg/portfile.cmake` a `ports/ecf-dgii-client/portfile.cmake`
3. Copiar `vcpkg.json` a `ports/ecf-dgii-client/vcpkg.json`
4. Actualizar el `SHA512` en `portfile.cmake` con el hash real después de crear el tag de release
5. Ejecutar `vcpkg x-add-version ecf-dgii-client` para actualizar la base de datos de versiones
6. Enviar un pull request

Probar localmente:

```sh
vcpkg install ecf-dgii-client --overlay-ports=./vcpkg
```

### NuGet

```sh
nuget pack ecf-dgii-client.nuspec
nuget push ecf-dgii-client.cpp.0.1.0.nupkg -Source https://api.nuget.org/v3/index.json -ApiKey YOUR_API_KEY
```

## Ejemplo de payload ECF

Un payload ECF JSON completo con items, descuentos, impuestos adicionales y items no facturables:

```json
{
  "Encabezado": {
    "IdDoc": {
      "ENCF": "E310000051630",
      "TipoeCF": "FacturaDeCreditoFiscalElectronica",
      "TipoPago": "Contado",
      "TipoIngresos": "01",
      "TablaFormasPago": [
        {
          "FormaPago": "Efectivo",
          "MontoPago": 1015.25
        }
      ],
      "IndicadorMontoGravado": "ConITBISIncluido",
      "FechaVencimientoSecuencia": "2028-12-31T00:00:00"
    },
    "Emisor": {
      "RNCEmisor": "131460941",
      "FechaEmision": "2026-01-10",
      "DireccionEmisor": "AVE. ISABEL AGUIAR NO. 269, ZONA INDUSTRIAL DE HERRERA",
      "RazonSocialEmisor": "DOCUMENTOS ELECTRONICOS DE 02"
    },
    "Totales": {
      "ITBIS1": 18,
      "MontoGravadoI1": 762.71,
      "MontoGravadoTotal": 762.71,
      "TotalITBIS1": 137.29,
      "TotalITBIS": 137.29,
      "MontoNoFacturable": 100.0,
      "ImpuestosAdicionales": [
        {
          "TipoImpuesto": "002",
          "TasaImpuestoAdicional": 2,
          "OtrosImpuestosAdicionales": 15.25
        }
      ],
      "MontoImpuestoAdicional": 15.25,
      "MontoTotal": 1015.25,
      "MontoPeriodo": 1015.25
    },
    "Version": "Version1_0",
    "Comprador": {
      "RNCComprador": "131880681",
      "RazonSocialComprador": "DOCUMENTOS ELECTRONICOS DE 03"
    }
  },
  "DetallesItems": [
    {
      "MontoItem": 1016.95,
      "NombreItem": "Iphone 18 Pro max",
      "NumeroLinea": 1,
      "CantidadItem": 1,
      "UnidadMedida": "Unidad",
      "PrecioUnitarioItem": 1016.95,
      "IndicadorFacturacion": "ITBIS1_18Percent",
      "IndicadorBienoServicio": "Bien",
      "TablaImpuestoAdicional": [
        {
          "TipoImpuesto": "002"
        }
      ]
    },
    {
      "MontoItem": 100.0,
      "NombreItem": "Costo de Envío",
      "NumeroLinea": 2,
      "CantidadItem": 1,
      "UnidadMedida": "Unidad",
      "PrecioUnitarioItem": 100.0,
      "IndicadorFacturacion": "NoFacturable_18Percent",
      "IndicadorBienoServicio": "Servicio"
    }
  ],
  "DescuentosORecargos": [
    {
      "TipoValor": "$",
      "TipoAjuste": "D",
      "NumeroLinea": 1,
      "MontoDescuentooRecargo": 84.75,
      "DescripcionDescuentooRecargo": "Descuento",
      "IndicadorFacturacionDescuentooRecargo": "ITBIS1_18Percent"
    }
  ]
}
```

## Información del generador

- Versión de la API: v1
- Versión del generador: 7.20.0
- Paquete de compilación: `org.openapitools.codegen.languages.CppRestSdkClientCodegen`
