# Ecfx\EcfDgii\ApiKeyApi



All URIs are relative to https://api.test.ecfx.ssd.com.do, except if the operation defines another base path.

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**newCompanyApiKey()**](ApiKeyApi.md#newCompanyApiKey) | **POST** /apiKey |  |


## `newCompanyApiKey()`

```php
newCompanyApiKey($new_company_api_key): \Ecfx\EcfDgii\Model\Token
```



### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


// Configure Bearer (JWT) authorization: Bearer
$config = Ecfx\EcfDgii\Configuration::getDefaultConfiguration()->setAccessToken('YOUR_ACCESS_TOKEN');


$apiInstance = new Ecfx\EcfDgii\Api\ApiKeyApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$new_company_api_key = new \Ecfx\EcfDgii\Model\NewCompanyApiKey(); // \Ecfx\EcfDgii\Model\NewCompanyApiKey

try {
    $result = $apiInstance->newCompanyApiKey($new_company_api_key);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling ApiKeyApi->newCompanyApiKey: ', $e->getMessage(), PHP_EOL;
}
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **new_company_api_key** | [**\Ecfx\EcfDgii\Model\NewCompanyApiKey**](../Model/NewCompanyApiKey.md)|  | |

### Return type

[**\Ecfx\EcfDgii\Model\Token**](../Model/Token.md)

### Authorization

[Bearer](../../README.md#Bearer)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `application/problem+json`

[[Back to top]](#) [[Back to API list]](../../README.md#endpoints)
[[Back to Model list]](../../README.md#models)
[[Back to README]](../../README.md)
