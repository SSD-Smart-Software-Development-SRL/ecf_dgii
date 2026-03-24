# ApiKeyApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**newCompanyApiKey**](ApiKeyApi.md#newCompanyApiKey) | **POST** /apiKey |  |


<a id="newCompanyApiKey"></a>
# **newCompanyApiKey**
> Token newCompanyApiKey(newCompanyApiKey)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = ApiKeyApi()
val newCompanyApiKey : NewCompanyApiKey =  // NewCompanyApiKey | 
try {
    val result : Token = apiInstance.newCompanyApiKey(newCompanyApiKey)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling ApiKeyApi#newCompanyApiKey")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling ApiKeyApi#newCompanyApiKey")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **newCompanyApiKey** | [**NewCompanyApiKey**](NewCompanyApiKey.md)|  | |

### Return type

[**Token**](Token.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

