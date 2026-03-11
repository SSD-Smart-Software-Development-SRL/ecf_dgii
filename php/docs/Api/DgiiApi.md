# Ecfx\EcfDgii\DgiiApi



All URIs are relative to https://api.test.ecfx.ssd.com.do, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**consultaDirectorioListado()**](DgiiApi.md#consultaDirectorioListado) | **GET** /dgii/{rnc}/consultadirectorio/listado |  |
| [**consultaDirectorioObtenerDirectorioPorRnc()**](DgiiApi.md#consultaDirectorioObtenerDirectorioPorRnc) | **GET** /dgii/{rnc}/consultadirectorio/obtener-directorio-por-rnc |  |
| [**consultaEstado()**](DgiiApi.md#consultaEstado) | **GET** /dgii/{rnc}/consultaestado/estado |  |
| [**consultaRFCE()**](DgiiApi.md#consultaRFCE) | **GET** /dgii/{rnc}/consultarfce/consulta |  |
| [**consultaResultado()**](DgiiApi.md#consultaResultado) | **GET** /dgii/{rnc}/consultaresultado/estado |  |
| [**consultaTimbre()**](DgiiApi.md#consultaTimbre) | **GET** /dgii/{rnc}/consultatimbre |  |
| [**consultaTimbreFC()**](DgiiApi.md#consultaTimbreFC) | **GET** /dgii/{rnc}/consultatimbrefc |  |
| [**consultaTrackId()**](DgiiApi.md#consultaTrackId) | **GET** /dgii/{rnc}/consultatrackids/consulta |  |
| [**estatusServiciosObtenerEstatus()**](DgiiApi.md#estatusServiciosObtenerEstatus) | **GET** /dgii/{rnc}/estatusservicios/obtener-estatus |  |
| [**estatusServiciosObtenerVentanasMantenimiento()**](DgiiApi.md#estatusServiciosObtenerVentanasMantenimiento) | **GET** /dgii/{rnc}/estatusservicios/obtener-ventanas-mantenimiento |  |


## `consultaDirectorioListado()`

```php
consultaDirectorioListado($rnc): \Ecfx\EcfDgii\Model\Directorio[]
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string

try {
    $result = $apiInstance->consultaDirectorioListado($rnc);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->consultaDirectorioListado: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\Directorio[]**](../Model/Directorio.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `consultaDirectorioObtenerDirectorioPorRnc()`

```php
consultaDirectorioObtenerDirectorioPorRnc($rnc, $rnc2): \Ecfx\EcfDgii\Model\Directorio
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$rnc2 = 'rnc_example'; // string

try {
    $result = $apiInstance->consultaDirectorioObtenerDirectorioPorRnc($rnc, $rnc2);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->consultaDirectorioObtenerDirectorioPorRnc: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **rnc2** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\Directorio**](../Model/Directorio.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `consultaEstado()`

```php
consultaEstado($rnc, $rnc_emisor, $ncf_electronico, $rnc_comprador, $codigo_seguridad): \Ecfx\EcfDgii\Model\RespuestaConsultaEstado
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$rnc_emisor = 'rnc_emisor_example'; // string
$ncf_electronico = 'ncf_electronico_example'; // string
$rnc_comprador = 'rnc_comprador_example'; // string
$codigo_seguridad = 'codigo_seguridad_example'; // string

try {
    $result = $apiInstance->consultaEstado($rnc, $rnc_emisor, $ncf_electronico, $rnc_comprador, $codigo_seguridad);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->consultaEstado: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **rnc_emisor** | **string**|  | |
| **ncf_electronico** | **string**|  | |
| **rnc_comprador** | **string**|  | |
| **codigo_seguridad** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\RespuestaConsultaEstado**](../Model/RespuestaConsultaEstado.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `consultaRFCE()`

```php
consultaRFCE($rnc, $rnc_emisor, $encf, $cod_seguridad_e_cf): \Ecfx\EcfDgii\Model\RespuestaConsultaRFCE
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$rnc_emisor = 'rnc_emisor_example'; // string
$encf = 'encf_example'; // string
$cod_seguridad_e_cf = 'cod_seguridad_e_cf_example'; // string

try {
    $result = $apiInstance->consultaRFCE($rnc, $rnc_emisor, $encf, $cod_seguridad_e_cf);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->consultaRFCE: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **rnc_emisor** | **string**|  | |
| **encf** | **string**|  | |
| **cod_seguridad_e_cf** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\RespuestaConsultaRFCE**](../Model/RespuestaConsultaRFCE.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `consultaResultado()`

```php
consultaResultado($rnc, $track_id): \Ecfx\EcfDgii\Model\RespuestaConsultaTrackId
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$track_id = 'track_id_example'; // string

try {
    $result = $apiInstance->consultaResultado($rnc, $track_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->consultaResultado: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **track_id** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\RespuestaConsultaTrackId**](../Model/RespuestaConsultaTrackId.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `consultaTimbre()`

```php
consultaTimbre($rnc, $rncemisor, $encf, $montototal, $codigoseguridad): \Ecfx\EcfDgii\Model\RespuestaConsultaTimbre
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$rncemisor = 'rncemisor_example'; // string
$encf = 'encf_example'; // string
$montototal = 'montototal_example'; // string
$codigoseguridad = 'codigoseguridad_example'; // string

try {
    $result = $apiInstance->consultaTimbre($rnc, $rncemisor, $encf, $montototal, $codigoseguridad);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->consultaTimbre: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **rncemisor** | **string**|  | |
| **encf** | **string**|  | |
| **montototal** | **string**|  | |
| **codigoseguridad** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\RespuestaConsultaTimbre**](../Model/RespuestaConsultaTimbre.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `consultaTimbreFC()`

```php
consultaTimbreFC($rnc, $rncemisor, $encf, $montototal, $codigoseguridad): \Ecfx\EcfDgii\Model\RespuestaConsultaTimbre
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$rncemisor = 'rncemisor_example'; // string
$encf = 'encf_example'; // string
$montototal = 'montototal_example'; // string
$codigoseguridad = 'codigoseguridad_example'; // string

try {
    $result = $apiInstance->consultaTimbreFC($rnc, $rncemisor, $encf, $montototal, $codigoseguridad);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->consultaTimbreFC: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **rncemisor** | **string**|  | |
| **encf** | **string**|  | |
| **montototal** | **string**|  | |
| **codigoseguridad** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\RespuestaConsultaTimbre**](../Model/RespuestaConsultaTimbre.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `consultaTrackId()`

```php
consultaTrackId($rnc, $rnc_emisor, $encf): \Ecfx\EcfDgii\Model\RespuestaConsultaTrackId
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$rnc_emisor = 'rnc_emisor_example'; // string
$encf = 'encf_example'; // string

try {
    $result = $apiInstance->consultaTrackId($rnc, $rnc_emisor, $encf);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->consultaTrackId: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **rnc_emisor** | **string**|  | |
| **encf** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\RespuestaConsultaTrackId**](../Model/RespuestaConsultaTrackId.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `estatusServiciosObtenerEstatus()`

```php
estatusServiciosObtenerEstatus($rnc): \Ecfx\EcfDgii\Model\RespuestaEstatusServicio[]
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string

try {
    $result = $apiInstance->estatusServiciosObtenerEstatus($rnc);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->estatusServiciosObtenerEstatus: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\RespuestaEstatusServicio[]**](../Model/RespuestaEstatusServicio.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `estatusServiciosObtenerVentanasMantenimiento()`

```php
estatusServiciosObtenerVentanasMantenimiento($rnc): \Ecfx\EcfDgii\Model\RespuestaVentanaDeMantenimiento
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\DgiiApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string

try {
    $result = $apiInstance->estatusServiciosObtenerVentanasMantenimiento($rnc);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DgiiApi->estatusServiciosObtenerVentanasMantenimiento: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\RespuestaVentanaDeMantenimiento**](../Model/RespuestaVentanaDeMantenimiento.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
