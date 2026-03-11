# RecepcionApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getAcecfReceptionRequest**](RecepcionApi.md#getAcecfReceptionRequest) | **GET** /recepcion/{rnc}/acecf/{messageId} |  |
| [**getEcfReceptionRequest**](RecepcionApi.md#getEcfReceptionRequest) | **GET** /recepcion/{rnc}/ecf/{messageId} |  |
| [**searchAcecfReceptionRequests**](RecepcionApi.md#searchAcecfReceptionRequests) | **GET** /recepcion/acecf |  |
| [**searchAcecfReceptionRequestsByRnc**](RecepcionApi.md#searchAcecfReceptionRequestsByRnc) | **GET** /recepcion/{rnc}/acecf |  |
| [**searchEcfReceptionRequests**](RecepcionApi.md#searchEcfReceptionRequests) | **GET** /recepcion/ecf |  |
| [**searchEcfReceptionRequestsByRnc**](RecepcionApi.md#searchEcfReceptionRequestsByRnc) | **GET** /recepcion/{rnc}/ecf |  |


<a id="getAcecfReceptionRequest"></a>
# **getAcecfReceptionRequest**
> getAcecfReceptionRequest(rnc, messageId)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val messageId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
try {
    apiInstance.getAcecfReceptionRequest(rnc, messageId)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#getAcecfReceptionRequest")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#getAcecfReceptionRequest")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
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

<a id="getEcfReceptionRequest"></a>
# **getEcfReceptionRequest**
> getEcfReceptionRequest(rnc, messageId)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val messageId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
try {
    apiInstance.getEcfReceptionRequest(rnc, messageId)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#getEcfReceptionRequest")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#getEcfReceptionRequest")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
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
> PaginatedApiResultOfAcecfReceptionRequestDto searchAcecfReceptionRequests(messageIds, encfs, rncs, page, limit)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val messageIds : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val rncs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfAcecfReceptionRequestDto = apiInstance.searchAcecfReceptionRequests(messageIds, encfs, rncs, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#searchAcecfReceptionRequests")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#searchAcecfReceptionRequests")
    e.printStackTrace()
}
```

### Parameters
| **messageIds** | [**kotlin.collections.List&lt;java.util.UUID&gt;**](java.util.UUID.md)|  | [optional] |
| **encfs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **rncs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
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

<a id="searchAcecfReceptionRequestsByRnc"></a>
# **searchAcecfReceptionRequestsByRnc**
> PaginatedApiResultOfAcecfReceptionRequestDto searchAcecfReceptionRequestsByRnc(rnc, messageIds, encfs, page, limit)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val messageIds : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfAcecfReceptionRequestDto = apiInstance.searchAcecfReceptionRequestsByRnc(rnc, messageIds, encfs, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#searchAcecfReceptionRequestsByRnc")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#searchAcecfReceptionRequestsByRnc")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **messageIds** | [**kotlin.collections.List&lt;java.util.UUID&gt;**](java.util.UUID.md)|  | [optional] |
| **encfs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
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

<a id="searchEcfReceptionRequests"></a>
# **searchEcfReceptionRequests**
> PaginatedApiResultOfEcfReceptionRequestDto searchEcfReceptionRequests(messageIds, encfs, rncs, page, limit)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val messageIds : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val rncs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfEcfReceptionRequestDto = apiInstance.searchEcfReceptionRequests(messageIds, encfs, rncs, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#searchEcfReceptionRequests")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#searchEcfReceptionRequests")
    e.printStackTrace()
}
```

### Parameters
| **messageIds** | [**kotlin.collections.List&lt;java.util.UUID&gt;**](java.util.UUID.md)|  | [optional] |
| **encfs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **rncs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfReceptionRequestDto**](PaginatedApiResultOfEcfReceptionRequestDto.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="searchEcfReceptionRequestsByRnc"></a>
# **searchEcfReceptionRequestsByRnc**
> PaginatedApiResultOfEcfReceptionRequestDto searchEcfReceptionRequestsByRnc(rnc, messageIds, encfs, page, limit)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val messageIds : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfEcfReceptionRequestDto = apiInstance.searchEcfReceptionRequestsByRnc(rnc, messageIds, encfs, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#searchEcfReceptionRequestsByRnc")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#searchEcfReceptionRequestsByRnc")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **messageIds** | [**kotlin.collections.List&lt;java.util.UUID&gt;**](java.util.UUID.md)|  | [optional] |
| **encfs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfReceptionRequestDto**](PaginatedApiResultOfEcfReceptionRequestDto.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

