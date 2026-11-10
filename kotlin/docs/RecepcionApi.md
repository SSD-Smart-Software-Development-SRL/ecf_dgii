# RecepcionApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**getEcfReceptionRequest**](RecepcionApi.md#getEcfReceptionRequest) | **GET** /recepcion/{messageId} |  |
| [**getEcfReceptorByMessageId**](RecepcionApi.md#getEcfReceptorByMessageId) | **GET** /recepcion/{rnc}/{messageId} |  |
| [**searchEcfReceptionRequests**](RecepcionApi.md#searchEcfReceptionRequests) | **GET** /recepcion |  |
| [**searchEcfReceptionRequestsByRnc**](RecepcionApi.md#searchEcfReceptionRequestsByRnc) | **GET** /recepcion/{rnc} |  |
| [**sendAprobacionComercial**](RecepcionApi.md#sendAprobacionComercial) | **POST** /recepcion/{messageId}/acecf |  |


<a id="getEcfReceptionRequest"></a>
# **getEcfReceptionRequest**
> getEcfReceptionRequest(messageId)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val messageId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
try {
    apiInstance.getEcfReceptionRequest(messageId)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#getEcfReceptionRequest")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#getEcfReceptionRequest")
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

<a id="getEcfReceptorByMessageId"></a>
# **getEcfReceptorByMessageId**
> EcfReceptorDto getEcfReceptorByMessageId(rnc, messageId)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val messageId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
try {
    val result : EcfReceptorDto = apiInstance.getEcfReceptorByMessageId(rnc, messageId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#getEcfReceptorByMessageId")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#getEcfReceptorByMessageId")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **messageId** | **java.util.UUID**|  | |

### Return type

[**EcfReceptorDto**](EcfReceptorDto.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="searchEcfReceptionRequests"></a>
# **searchEcfReceptionRequests**
> PaginatedApiResultOfEcfReceptionRequestDto searchEcfReceptionRequests(messageIds, encfs, rncs, rncEmisors, tiposEcfs, progresses, fromDate, toDate, amountFrom, amountTo, ocultarNoRecibidas, page, limit)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val messageIds : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val rncs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val rncEmisors : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val tiposEcfs : kotlin.collections.List<Int> =  // kotlin.collections.List<Int> | 
val progresses : kotlin.collections.List<Int> =  // kotlin.collections.List<Int> | 
val fromDate : kotlin.String = fromDate_example // kotlin.String | 
val toDate : kotlin.String = toDate_example // kotlin.String | 
val amountFrom : kotlin.Double = 1.2 // kotlin.Double | 
val amountTo : kotlin.Double = 1.2 // kotlin.Double | 
val ocultarNoRecibidas : kotlin.Boolean = true // kotlin.Boolean | 
val page : Int = 56 // Int | 
val limit : Int = 56 // Int | 
try {
    val result : PaginatedApiResultOfEcfReceptionRequestDto = apiInstance.searchEcfReceptionRequests(messageIds, encfs, rncs, rncEmisors, tiposEcfs, progresses, fromDate, toDate, amountFrom, amountTo, ocultarNoRecibidas, page, limit)
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
| **rncEmisors** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **tiposEcfs** | [**kotlin.collections.List&lt;Int&gt;**](Int.md)|  | [optional] |
| **progresses** | [**kotlin.collections.List&lt;Int&gt;**](Int.md)|  | [optional] |
| **fromDate** | **kotlin.String**|  | [optional] |
| **toDate** | **kotlin.String**|  | [optional] |
| **amountFrom** | **kotlin.Double**|  | [optional] |
| **amountTo** | **kotlin.Double**|  | [optional] |
| **ocultarNoRecibidas** | **kotlin.Boolean**|  | [optional] |
| **page** | **Int**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **Int**|  | [optional] [default to 25] |

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
> PaginatedApiResultOfEcfReceptionRequestDto searchEcfReceptionRequestsByRnc(rnc, messageIds, encfs, rncEmisors, tiposEcfs, progresses, fromDate, toDate, amountFrom, amountTo, ocultarNoRecibidas, page, limit)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val messageIds : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val rncEmisors : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val tiposEcfs : kotlin.collections.List<Int> =  // kotlin.collections.List<Int> | 
val progresses : kotlin.collections.List<Int> =  // kotlin.collections.List<Int> | 
val fromDate : kotlin.String = fromDate_example // kotlin.String | 
val toDate : kotlin.String = toDate_example // kotlin.String | 
val amountFrom : kotlin.Double = 1.2 // kotlin.Double | 
val amountTo : kotlin.Double = 1.2 // kotlin.Double | 
val ocultarNoRecibidas : kotlin.Boolean = true // kotlin.Boolean | 
val page : Int = 56 // Int | 
val limit : Int = 56 // Int | 
try {
    val result : PaginatedApiResultOfEcfReceptionRequestDto = apiInstance.searchEcfReceptionRequestsByRnc(rnc, messageIds, encfs, rncEmisors, tiposEcfs, progresses, fromDate, toDate, amountFrom, amountTo, ocultarNoRecibidas, page, limit)
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
| **rncEmisors** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **tiposEcfs** | [**kotlin.collections.List&lt;Int&gt;**](Int.md)|  | [optional] |
| **progresses** | [**kotlin.collections.List&lt;Int&gt;**](Int.md)|  | [optional] |
| **fromDate** | **kotlin.String**|  | [optional] |
| **toDate** | **kotlin.String**|  | [optional] |
| **amountFrom** | **kotlin.Double**|  | [optional] |
| **amountTo** | **kotlin.Double**|  | [optional] |
| **ocultarNoRecibidas** | **kotlin.Boolean**|  | [optional] |
| **page** | **Int**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **Int**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfReceptionRequestDto**](PaginatedApiResultOfEcfReceptionRequestDto.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="sendAprobacionComercial"></a>
# **sendAprobacionComercial**
> sendAprobacionComercial(messageId, sendAcecfRequest)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = RecepcionApi()
val messageId : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val sendAcecfRequest : SendAcecfRequest =  // SendAcecfRequest | 
try {
    apiInstance.sendAprobacionComercial(messageId, sendAcecfRequest)
} catch (e: ClientException) {
    println("4xx response calling RecepcionApi#sendAprobacionComercial")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling RecepcionApi#sendAprobacionComercial")
    e.printStackTrace()
}
```

### Parameters
| **messageId** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sendAcecfRequest** | [**SendAcecfRequest**](SendAcecfRequest.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

