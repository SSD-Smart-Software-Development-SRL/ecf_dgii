# ECF DGII PHP SDK

PHP SDK for the ECF DGII electronic fiscal receipt API (Dominican Republic).

Generated from the [OpenAPI specification](https://api.prod.ecfx.ssd.com.do) using [OpenAPI Generator](https://openapi-generator.tech), with a high-level `EcfService` for simplified ECF submission with automatic routing and polling.

## Installation

```bash
composer require ecfx/ecf-dgii-php
```

### Requirements

- PHP 8.1+
- ext-curl
- ext-json
- ext-mbstring

## Quick Start

### Configuration

```php
use Ecfx\EcfDgii\Configuration;

$config = Configuration::getDefaultConfiguration()
    ->setHost('https://api.prod.ecfx.ssd.com.do')  // or api.test / api.cert
    ->setAccessToken('your-jwt-token');
```

Available environments:
- **Test:** `https://api.test.ecfx.ssd.com.do`
- **Certification:** `https://api.cert.ecfx.ssd.com.do`
- **Production:** `https://api.prod.ecfx.ssd.com.do`

### High-Level: Send an ECF (recommended)

The `EcfService` handles routing, submission, and polling automatically:

```php
use GuzzleHttp\Client;
use Ecfx\EcfDgii\Configuration;
use Ecfx\EcfDgii\EcfService;
use Ecfx\EcfDgii\EcfProcessingException;
use Ecfx\EcfDgii\EcfPollingTimeoutException;
use Ecfx\EcfDgii\Api\EcfApi;
use Ecfx\EcfDgii\Model\ECF;
use Ecfx\EcfDgii\Model\Encabezado;
use Ecfx\EcfDgii\Model\IdDoc;
use Ecfx\EcfDgii\Model\Emisor;
use Ecfx\EcfDgii\Model\Comprador;
use Ecfx\EcfDgii\Model\Totales;
use Ecfx\EcfDgii\Model\Item;
use Ecfx\EcfDgii\Model\TipoeCFType;
use Ecfx\EcfDgii\Model\VersionType;

// 1. Configure
$config = Configuration::getDefaultConfiguration()
    ->setHost('https://api.test.ecfx.ssd.com.do')
    ->setAccessToken(getenv('ECF_DGII_TOKEN'));

// 2. Create the API client and service
$ecfApi = new EcfApi(new Client(), $config);
$service = new EcfService($ecfApi, pollingMaxAttempts: 30, pollingIntervalSeconds: 2);

// 3. Build the ECF
$ecf = new ECF([
    'encabezado' => new Encabezado([
        'version' => VersionType::VERSION1_0,
        'id_doc' => new IdDoc([
            'tipoe_cf' => TipoeCFType::FACTURA_DE_CREDITO_FISCAL_ELECTRONICA,
            'encf' => 'E310000000001',
        ]),
        'emisor' => new Emisor([
            'rnc_emisor' => '123456789',
            'razon_social_emisor' => 'Mi Empresa SRL',
            'direccion_emisor' => 'Calle Principal #1, Santo Domingo',
            'fecha_emision' => '2026-03-11',
        ]),
        'totales' => new Totales([
            'monto_total' => 1180.00,
        ]),
    ]),
    'detalles_items' => [
        new Item([
            'numero_linea' => 1,
            'nombre_item' => 'Servicio de consultoría',
            'indicador_facturacion' => 1,
            'cantidad_item' => 1,
            'precio_unitario_item' => 1000.00,
            'monto_item' => 1000.00,
        ]),
    ],
]);

// 4. Send — routes automatically, polls until finished
try {
    $result = $service->sendEcf($ecf);

    echo "ECF accepted!\n";
    echo "Message ID: " . $result->getMessageId() . "\n";
    echo "Status: " . $result->getEstatus() . "\n";
    echo "ENCF: " . $result->getEncf() . "\n";
} catch (EcfProcessingException $e) {
    echo "ECF rejected: " . $e->getMessage() . "\n";
    $response = $e->getEcfResponse();
    if ($response) {
        echo "Errors: " . $response->getErrors() . "\n";
    }
} catch (EcfPollingTimeoutException $e) {
    echo "Polling timed out: " . $e->getMessage() . "\n";
}
```

### Backend / Frontend Architecture

In most apps, the backend sends the ECF and the frontend queries the status directly:

```php
// Backend: send ECF with main token — no polling
$ecfApi = new EcfApi(new Client(), $config);
$response = $ecfApi->recepcionEcf31($rnc, $ecf);
$messageId = $response->getMessageId();

// Generate a read-only token for the frontend
$apiKeyApi = new ApiKeyApi(new Client(), $config);
$apiKey = $apiKeyApi->newCompanyApiKey($request); // scoped to tenant/RNC
$frontendToken = $apiKey->getToken();
// Return $frontendToken + $messageId to the frontend
```

The frontend then uses `$frontendToken` to query ECF SSD directly without going through your backend. See the [main README](../README.md#arquitectura-backend--frontend) for the full diagram.

> **`EcfService::sendEcf`** is a convenience that wraps send + polling. For apps with a frontend, use the individual endpoints.

### Low-Level: Use API Clients Directly

For full control, use the generated API classes directly:

```php
use GuzzleHttp\Client;
use Ecfx\EcfDgii\Configuration;
use Ecfx\EcfDgii\Api\CompanyApi;
use Ecfx\EcfDgii\Api\EcfApi;
use Ecfx\EcfDgii\Api\DgiiApi;
use Ecfx\EcfDgii\Api\RecepcionApi;
use Ecfx\EcfDgii\Api\ApiKeyApi;

$config = Configuration::getDefaultConfiguration()
    ->setHost('https://api.prod.ecfx.ssd.com.do')
    ->setAccessToken('your-jwt-token');

$client = new Client();

// Company operations
$companyApi = new CompanyApi($client, $config);
$companies = $companyApi->getCompanies();
$company = $companyApi->getCompanyByRnc('123456789');

// ECF operations
$ecfApi = new EcfApi($client, $config);
$response = $ecfApi->recepcionEcf31($ecf);           // Submit factura de crédito fiscal
$results = $ecfApi->searchEcfs('123456789');           // Search ECFs by RNC
$ecfById = $ecfApi->getEcfById('123456789', $msgId);  // Get ECF by message ID
$ecfApi->aprobacionComercial('123456789', $encf, $acecfRequest); // Commercial approval

// DGII consultations
$dgiiApi = new DgiiApi($client, $config);
$directorio = $dgiiApi->consultaDirectorioListado('123456789');
$estado = $dgiiApi->consultaEstado('123456789', $rncEmisor, $ncf, $rncComprador, $codSeg);
$timbre = $dgiiApi->consultaTimbre('123456789', $rncEmisor, $encf, $monto, $codSeg);
$servicios = $dgiiApi->estatusServiciosObtenerEstatus('123456789');

// Reception tracking
$recepcionApi = new RecepcionApi($client, $config);
$requests = $recepcionApi->searchEcfReceptionRequests();
```

## API Reference

### API Classes

| Class | Description |
|-------|-------------|
| `EcfService` | High-level ECF submission with auto-routing and polling |
| `CompanyApi` | Company CRUD and certificate management |
| `EcfApi` | ECF submission (types 31-47), queries, searches, anulaciones |
| `DgiiApi` | DGII consultations (directorio, estado, timbre, track IDs, etc.) |
| `RecepcionApi` | Reception request tracking |
| `ApiKeyApi` | API key management |

### ECF Types

| Type | Route | Description |
|------|-------|-------------|
| FacturaDeCreditoFiscalElectronica | /ecf/31 | Factura de Crédito Fiscal |
| FacturaDeConsumoElectronica | /ecf/32 | Factura de Consumo |
| NotaDeDebitoElectronica | /ecf/33 | Nota de Débito |
| NotaDeCreditoElectronica | /ecf/34 | Nota de Crédito |
| ComprasElectronico | /ecf/41 | Compras |
| GastosMenoresElectronico | /ecf/43 | Gastos Menores |
| RegimenesEspecialesElectronico | /ecf/44 | Regímenes Especiales |
| GubernamentalElectronico | /ecf/45 | Gubernamental |
| ComprobanteDeExportacionesElectronico | /ecf/46 | Exportaciones |
| ComprobanteParaPagosAlExteriorElectronico | /ecf/47 | Pagos al Exterior |

## Error Handling

| Exception | When |
|-----------|------|
| `EcfProcessingException` | DGII rejects the ECF during processing |
| `EcfPollingTimeoutException` | Polling exceeds max attempts without a final result |
| `ApiException` | HTTP/network errors communicating with the API |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `ECF_DGII_TOKEN` | JWT Bearer token for API authentication |

## Regenerating from OpenAPI Spec

```bash
openapi-generator generate \
  -i path/to/openapi/v1.json \
  -g php \
  -c openapi-generator-config.json \
  -o . \
  --skip-validate-spec
```

## License

MIT
