# AprobacionComercialApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAcecfReceptionRequest**](AprobacionComercialApi.md#getAcecfReceptionRequest) | **GET** /recepcion/acecf/{messageId} |  |
| [**searchAcecfReceptionRequests**](AprobacionComercialApi.md#searchAcecfReceptionRequests) | **GET** /recepcion/acecf |  |


<a id="getAcecfReceptionRequest"></a>
# **getAcecfReceptionRequest**
> getAcecfReceptionRequest(messageId)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = AprobacionComercialApi()
val messageId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
try {
    apiInstance.getAcecfReceptionRequest(messageId)
} catch (e: ClientException) {
    println("4xx response calling AprobacionComercialApi#getAcecfReceptionRequest")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AprobacionComercialApi#getAcecfReceptionRequest")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **messageId** | **java.util.UUID**|  | |

### Return type

null (empty response body)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

<a id="searchAcecfReceptionRequests"></a>
# **searchAcecfReceptionRequests**
> PaginatedApiResultOfAcecfReceptionRequestDto searchAcecfReceptionRequests(messageIds, encfs, rncs, progresses, page, limit)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = AprobacionComercialApi()
val messageIds : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val rncs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val progresses : kotlin.collections.List<SearchEcfReceptionRequestsTiposEcfsParameterInner> =  // kotlin.collections.List<SearchEcfReceptionRequestsTiposEcfsParameterInner> | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfAcecfReceptionRequestDto = apiInstance.searchAcecfReceptionRequests(messageIds, encfs, rncs, progresses, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AprobacionComercialApi#searchAcecfReceptionRequests")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AprobacionComercialApi#searchAcecfReceptionRequests")
    e.printStackTrace()
}
```

### Parameters
| **messageIds** | [**kotlin.collections.List&lt;java.util.UUID&gt;**](java.util.UUID.md)|  | [optional] |
| **encfs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **rncs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **progresses** | [**kotlin.collections.List&lt;SearchEcfReceptionRequestsTiposEcfsParameterInner&gt;**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfAcecfReceptionRequestDto**](PaginatedApiResultOfAcecfReceptionRequestDto.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

