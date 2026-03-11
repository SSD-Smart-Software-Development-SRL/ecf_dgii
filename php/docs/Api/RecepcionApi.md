# Ecfx\EcfDgii\RecepcionApi



All URIs are relative to https://api.test.ecfx.ssd.com.do, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAcecfReceptionRequest()**](RecepcionApi.md#getAcecfReceptionRequest) | **GET** /recepcion/{rnc}/acecf/{messageId} |  |
| [**getEcfReceptionRequest()**](RecepcionApi.md#getEcfReceptionRequest) | **GET** /recepcion/{rnc}/ecf/{messageId} |  |
| [**searchAcecfReceptionRequests()**](RecepcionApi.md#searchAcecfReceptionRequests) | **GET** /recepcion/acecf |  |
| [**searchAcecfReceptionRequestsByRnc()**](RecepcionApi.md#searchAcecfReceptionRequestsByRnc) | **GET** /recepcion/{rnc}/acecf |  |
| [**searchEcfReceptionRequests()**](RecepcionApi.md#searchEcfReceptionRequests) | **GET** /recepcion/ecf |  |
| [**searchEcfReceptionRequestsByRnc()**](RecepcionApi.md#searchEcfReceptionRequestsByRnc) | **GET** /recepcion/{rnc}/ecf |  |


## `getAcecfReceptionRequest()`

```php
getAcecfReceptionRequest($rnc, $message_id)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\RecepcionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$message_id = 'message_id_example'; // string

try {
    $apiInstance->getAcecfReceptionRequest($rnc, $message_id);
} catch (Exception $e) {
    echo 'Exception when calling RecepcionApi->getAcecfReceptionRequest: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **message_id** | **string**|  | |

### Return type

void (empty response body)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getEcfReceptionRequest()`

```php
getEcfReceptionRequest($rnc, $message_id)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\RecepcionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$message_id = 'message_id_example'; // string

try {
    $apiInstance->getEcfReceptionRequest($rnc, $message_id);
} catch (Exception $e) {
    echo 'Exception when calling RecepcionApi->getEcfReceptionRequest: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **message_id** | **string**|  | |

### Return type

void (empty response body)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAcecfReceptionRequests()`

```php
searchAcecfReceptionRequests($message_ids, $encfs, $rncs, $page, $limit): \Ecfx\EcfDgii\Model\PaginatedApiResultOfAcecfReceptionRequestDto
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\RecepcionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$message_ids = array('message_ids_example'); // string[]
$encfs = array('encfs_example'); // string[]
$rncs = array('rncs_example'); // string[]
$page = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesPageParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesPageParameter
$limit = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesLimitParameter

try {
    $result = $apiInstance->searchAcecfReceptionRequests($message_ids, $encfs, $rncs, $page, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecepcionApi->searchAcecfReceptionRequests: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **message_ids** | [**string[]**](../Model/string.md)|  | [optional] |
| **encfs** | [**string[]**](../Model/string.md)|  | [optional] |
| **rncs** | [**string[]**](../Model/string.md)|  | [optional] |
| **page** | **\Ecfx\EcfDgii\Model\GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**\Ecfx\EcfDgii\Model\PaginatedApiResultOfAcecfReceptionRequestDto**](../Model/PaginatedApiResultOfAcecfReceptionRequestDto.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchAcecfReceptionRequestsByRnc()`

```php
searchAcecfReceptionRequestsByRnc($rnc, $message_ids, $encfs, $page, $limit): \Ecfx\EcfDgii\Model\PaginatedApiResultOfAcecfReceptionRequestDto
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\RecepcionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$message_ids = array('message_ids_example'); // string[]
$encfs = array('encfs_example'); // string[]
$page = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesPageParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesPageParameter
$limit = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesLimitParameter

try {
    $result = $apiInstance->searchAcecfReceptionRequestsByRnc($rnc, $message_ids, $encfs, $page, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecepcionApi->searchAcecfReceptionRequestsByRnc: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **message_ids** | [**string[]**](../Model/string.md)|  | [optional] |
| **encfs** | [**string[]**](../Model/string.md)|  | [optional] |
| **page** | **\Ecfx\EcfDgii\Model\GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**\Ecfx\EcfDgii\Model\PaginatedApiResultOfAcecfReceptionRequestDto**](../Model/PaginatedApiResultOfAcecfReceptionRequestDto.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchEcfReceptionRequests()`

```php
searchEcfReceptionRequests($message_ids, $encfs, $rncs, $page, $limit): \Ecfx\EcfDgii\Model\PaginatedApiResultOfEcfReceptionRequestDto
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\RecepcionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$message_ids = array('message_ids_example'); // string[]
$encfs = array('encfs_example'); // string[]
$rncs = array('rncs_example'); // string[]
$page = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesPageParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesPageParameter
$limit = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesLimitParameter

try {
    $result = $apiInstance->searchEcfReceptionRequests($message_ids, $encfs, $rncs, $page, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecepcionApi->searchEcfReceptionRequests: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **message_ids** | [**string[]**](../Model/string.md)|  | [optional] |
| **encfs** | [**string[]**](../Model/string.md)|  | [optional] |
| **rncs** | [**string[]**](../Model/string.md)|  | [optional] |
| **page** | **\Ecfx\EcfDgii\Model\GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**\Ecfx\EcfDgii\Model\PaginatedApiResultOfEcfReceptionRequestDto**](../Model/PaginatedApiResultOfEcfReceptionRequestDto.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `searchEcfReceptionRequestsByRnc()`

```php
searchEcfReceptionRequestsByRnc($rnc, $message_ids, $encfs, $page, $limit): \Ecfx\EcfDgii\Model\PaginatedApiResultOfEcfReceptionRequestDto
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\RecepcionApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$message_ids = array('message_ids_example'); // string[]
$encfs = array('encfs_example'); // string[]
$page = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesPageParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesPageParameter
$limit = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesLimitParameter

try {
    $result = $apiInstance->searchEcfReceptionRequestsByRnc($rnc, $message_ids, $encfs, $page, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling RecepcionApi->searchEcfReceptionRequestsByRnc: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **message_ids** | [**string[]**](../Model/string.md)|  | [optional] |
| **encfs** | [**string[]**](../Model/string.md)|  | [optional] |
| **page** | **\Ecfx\EcfDgii\Model\GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**\Ecfx\EcfDgii\Model\PaginatedApiResultOfEcfReceptionRequestDto**](../Model/PaginatedApiResultOfEcfReceptionRequestDto.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
