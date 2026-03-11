# Ecfx\EcfDgii\CompanyApi



All URIs are relative to https://api.test.ecfx.ssd.com.do, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**deleteCompany()**](CompanyApi.md#deleteCompany) | **DELETE** /company/{rnc} |  |
| [**getCompanies()**](CompanyApi.md#getCompanies) | **GET** /company |  |
| [**getCompanyByRnc()**](CompanyApi.md#getCompanyByRnc) | **GET** /company/{rnc} |  |
| [**getCurrentCertificate()**](CompanyApi.md#getCurrentCertificate) | **GET** /company/{rnc}/certificate |  |
| [**updateCertificateCompany()**](CompanyApi.md#updateCertificateCompany) | **PUT** /company/{rnc}/certificate |  |
| [**upsertCompany()**](CompanyApi.md#upsertCompany) | **PUT** /company |  |


## `deleteCompany()`

```php
deleteCompany($rnc)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\CompanyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string

try {
    $apiInstance->deleteCompany($rnc);
} catch (Exception $e) {
    echo 'Exception when calling CompanyApi->deleteCompany: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |

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

## `getCompanies()`

```php
getCompanies($rncs, $names, $page, $limit): \Ecfx\EcfDgii\Model\PaginatedApiResultOfCompanyResponse
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\CompanyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rncs = array('rncs_example'); // string[]
$names = array('names_example'); // string[]
$page = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesPageParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesPageParameter
$limit = new \Ecfx\EcfDgii\Model\\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter(); // \Ecfx\EcfDgii\Model\GetCompaniesLimitParameter

try {
    $result = $apiInstance->getCompanies($rncs, $names, $page, $limit);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CompanyApi->getCompanies: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rncs** | [**string[]**](../Model/string.md)|  | [optional] |
| **names** | [**string[]**](../Model/string.md)|  | [optional] |
| **page** | **\Ecfx\EcfDgii\Model\GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **\Ecfx\EcfDgii\Model\GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**\Ecfx\EcfDgii\Model\PaginatedApiResultOfCompanyResponse**](../Model/PaginatedApiResultOfCompanyResponse.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCompanyByRnc()`

```php
getCompanyByRnc($rnc): \Ecfx\EcfDgii\Model\CompanyResponse
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\CompanyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string

try {
    $result = $apiInstance->getCompanyByRnc($rnc);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CompanyApi->getCompanyByRnc: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\CompanyResponse**](../Model/CompanyResponse.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `getCurrentCertificate()`

```php
getCurrentCertificate($rnc): \Ecfx\EcfDgii\Model\CertificateResponse[]
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\CompanyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string

try {
    $result = $apiInstance->getCurrentCertificate($rnc);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CompanyApi->getCurrentCertificate: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |

### Return type

[**\Ecfx\EcfDgii\Model\CertificateResponse[]**](../Model/CertificateResponse.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `updateCertificateCompany()`

```php
updateCertificateCompany($rnc, $certificate, $password)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\CompanyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$rnc = 'rnc_example'; // string
$certificate = '/path/to/file.txt'; // \SplFileObject
$password = 'password_example'; // string

try {
    $apiInstance->updateCertificateCompany($rnc, $certificate, $password);
} catch (Exception $e) {
    echo 'Exception when calling CompanyApi->updateCertificateCompany: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **string**|  | |
| **certificate** | **\SplFileObject****\SplFileObject**|  | |
| **password** | **string**|  | |

### Return type

void (empty response body)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: `multipart/form-data`
- **Accept**: `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)

## `upsertCompany()`

```php
upsertCompany($upsert_company_request)
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\CompanyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$upsert_company_request = new \Ecfx\EcfDgii\Model\UpsertCompanyRequest(); // \Ecfx\EcfDgii\Model\UpsertCompanyRequest

try {
    $apiInstance->upsertCompany($upsert_company_request);
} catch (Exception $e) {
    echo 'Exception when calling CompanyApi->upsertCompany: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **upsert_company_request** | [**\Ecfx\EcfDgii\Model\UpsertCompanyRequest**](../Model/UpsertCompanyRequest.md)|  | |

### Return type

void (empty response body)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
