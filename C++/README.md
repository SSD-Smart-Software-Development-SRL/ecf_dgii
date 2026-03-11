# ECF DGII C++ SDK Client

C++ SDK client for the ECF DGII API (Electronic Fiscal Receipt - Dominican Republic).

## Overview

This library provides a high-level C++ client for submitting electronic fiscal receipts (e-CF) to the DGII through the ECF API. It includes:

- **Auto-generated models and API classes** from the OpenAPI specification using [OpenAPI Generator](https://openapi-generator.tech) (`cpp-restsdk`)
- **High-level `EcfClient`** with a `sendEcf()` method that handles routing, polling, and error handling automatically
- **Direct API access** to all raw endpoints via the underlying generated API objects

## Installation

### Option 1: vcpkg (Recommended)

Add to your `vcpkg.json`:

```json
{
  "dependencies": ["ecf-dgii-client"]
}
```

Or install directly:

```sh
vcpkg install ecf-dgii-client
```

Then in your CMakeLists.txt:

```cmake
find_package(ecf-dgii-client REQUIRED)
target_link_libraries(your_target PRIVATE ecf-dgii-client::ecf-dgii-client)
```

### Option 2: Conan

Add to your `conanfile.txt`:

```ini
[requires]
ecf-dgii-client/0.1.0

[generators]
CMakeDeps
CMakeToolchain
```

Or in `conanfile.py`:

```python
def requirements(self):
    self.requires("ecf-dgii-client/0.1.0")
```

Then in your CMakeLists.txt:

```cmake
find_package(ecf-dgii-client REQUIRED)
target_link_libraries(your_target PRIVATE ecf-dgii-client::ecf-dgii-client)
```

### Option 3: NuGet (Visual Studio / Windows)

```sh
nuget install ecf-dgii-client.cpp
```

Or via the Visual Studio NuGet Package Manager, search for `ecf-dgii-client.cpp`.

### Option 4: Build from Source

#### Prerequisites

Install [cpprestsdk](https://github.com/Microsoft/cpprestsdk) and [Boost](https://www.boost.org/):

- **macOS**: `brew install cpprestsdk boost`
- **Linux (Debian/Ubuntu)**: `sudo apt-get install libcpprest-dev libboost-all-dev`
- **Windows**: `vcpkg install cpprestsdk cpprestsdk:x64-windows boost-uuid boost-uuid:x64-windows`

#### Build & Install

```sh
mkdir build && cd build
cmake ..
cmake --build .
sudo cmake --install .
```

Then in your CMakeLists.txt:

```cmake
find_package(ecf-dgii-client REQUIRED)
target_link_libraries(your_target PRIVATE ecf-dgii-client::ecf-dgii-client)
```

## Quick Start

### High-Level Client (Recommended)

The `EcfClient` provides a simple interface that handles routing to the correct endpoint, polling for completion, and error handling:

```cpp
#include <ecf-dgii-client/EcfClient.h>

using namespace ecf_dgii;
using namespace org::openapitools::client::model;

int main() {
    // Configure the client
    EcfClientConfig config;
    config.apiKey = "your-jwt-token";   // or set ECF_API_KEY env var
    config.environment = "test";         // "test", "cert", or "prod"

    EcfClient client(config);

    // Build an ECF
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

    // ... set items, totals, etc.

    // Send and wait for result (handles routing + polling automatically)
    try {
        auto result = client.sendEcf(ecf).get();
        std::cout << "ECF processed! Message ID: "
                  << utility::conversions::to_utf8string(result->getMessageId())
                  << std::endl;
    } catch (const EcfError& e) {
        std::cerr << "ECF Error: " << e.what() << std::endl;
        // Access the full response: e.getResponse()
    } catch (const PollingTimeoutError& e) {
        std::cerr << "Polling timed out" << std::endl;
    } catch (const PollingMaxRetriesError& e) {
        std::cerr << "Max retries exceeded" << std::endl;
    }

    return 0;
}
```

### Polling Options

Customize polling behavior:

```cpp
PollingOptions options;
options.initialDelay = std::chrono::milliseconds(2000);
options.maxDelay = std::chrono::milliseconds(60000);
options.maxRetries = 30;
options.backoffMultiplier = 1.5;
options.timeout = std::chrono::milliseconds(300000);  // 5 minutes

auto result = client.sendEcf(ecf, options).get();
```

### Direct API Access

Access all raw API endpoints through the generated API objects:

```cpp
EcfClient client(config);

// Company operations
auto companies = client.companyApi()->getCompanies(
    boost::none, boost::none, boost::optional<int32_t>(1), boost::optional<int32_t>(25)
).get();

// ECF query
auto ecfResults = client.ecfApi()->queryEcf(
    _XPLATSTR("123456789"), _XPLATSTR("E310000000001"), boost::optional<bool>(false)
).get();

// DGII operations
auto status = client.dgiiApi()->estatusServicios(_XPLATSTR("123456789")).get();

// Reception operations
auto requests = client.recepcionApi()->searchEcfReceptionRequests(
    boost::none, boost::none, boost::none, boost::none, boost::none
).get();
```

## Authentication

The API uses JWT Bearer token authentication. Provide your API key in one of two ways:

1. **Direct configuration**: `config.apiKey = "your-jwt-token";`
2. **Environment variable**: `export ECF_API_KEY="your-jwt-token"`

## Environments

| Environment | URL |
|-------------|-----|
| `test` | `https://api.test.ecfx.ssd.com.do` |
| `cert` | `https://api.cert.ecfx.ssd.com.do` |
| `prod` | `https://api.prod.ecfx.ssd.com.do` |

You can also set a custom base URL via `config.baseUrl` or the `ECF_API_URL` environment variable.

## ECF Type Routing

The `sendEcf()` method automatically routes to the correct endpoint based on `tipoeCF`:

| ECF Type | Route | Description |
|----------|-------|-------------|
| FacturaDeCreditoFiscalElectronica | `/ecf/31` | Electronic fiscal credit invoice |
| FacturaDeConsumoElectronica | `/ecf/32` | Electronic consumer invoice |
| NotaDeDebitoElectronica | `/ecf/33` | Electronic debit note |
| NotaDeCreditoElectronica | `/ecf/34` | Electronic credit note |
| ComprasElectronico | `/ecf/41` | Electronic purchases |
| GastosMenoresElectronico | `/ecf/43` | Electronic minor expenses |
| RegimenesEspecialesElectronico | `/ecf/44` | Electronic special regimes |
| GubernamentalElectronico | `/ecf/45` | Electronic governmental |
| ComprobanteDeExportacionesElectronico | `/ecf/46` | Electronic export receipt |
| ComprobanteParaPagosAlExteriorElectronico | `/ecf/47` | Electronic foreign payment receipt |

## Publishing

### ConanCenter

1. Fork [conan-center-index](https://github.com/conan-io/conan-center-index)
2. Create `recipes/ecf-dgii-client/all/conanfile.py` using the `conanfile.py` in this repo as a starting point (adapted for conan-center-index conventions)
3. Add `recipes/ecf-dgii-client/config.yml` with version mappings
4. Submit a pull request

Test locally first:

```sh
conan create . --build=missing
conan test test_package ecf-dgii-client/0.1.0
```

### vcpkg

1. Fork [vcpkg](https://github.com/microsoft/vcpkg)
2. Copy `vcpkg/portfile.cmake` to `ports/ecf-dgii-client/portfile.cmake`
3. Copy `vcpkg.json` to `ports/ecf-dgii-client/vcpkg.json`
4. Update the `SHA512` in `portfile.cmake` with the actual hash after creating the release tag
5. Run `vcpkg x-add-version ecf-dgii-client` to update version database
6. Submit a pull request

Test locally:

```sh
vcpkg install ecf-dgii-client --overlay-ports=./vcpkg
```

### NuGet

```sh
nuget pack ecf-dgii-client.nuspec
nuget push ecf-dgii-client.cpp.0.1.0.nupkg -Source https://api.nuget.org/v3/index.json -ApiKey YOUR_API_KEY
```

## Generator Info

- API version: v1
- Generator version: 7.20.0
- Build package: `org.openapitools.codegen.languages.CppRestSdkClientCodegen`
