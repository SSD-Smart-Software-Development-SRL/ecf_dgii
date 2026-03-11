# EcfApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**anulacionRangos**](EcfApi.md#anulacionRangos) | **POST** /ecf/anularrango/{rnc} |  |
| [**aprobacionComercial**](EcfApi.md#aprobacionComercial) | **POST** /ecf/aprobacioncomercial/{rnc}/{encf} |  |
| [**firmarSemilla**](EcfApi.md#firmarSemilla) | **POST** /ecf/FirmarSemilla/{rnc} |  |
| [**getEcfById**](EcfApi.md#getEcfById) | **GET** /ecf/{rnc}/message/{id} |  |
| [**listAnulaciones**](EcfApi.md#listAnulaciones) | **GET** /ecf/anulaciones |  |
| [**queryEcf**](EcfApi.md#queryEcf) | **GET** /ecf/{rnc}/{encf} |  |
| [**recepcionEcf31**](EcfApi.md#recepcionEcf31) | **POST** /ecf/31 |  |
| [**recepcionEcf32**](EcfApi.md#recepcionEcf32) | **POST** /ecf/32 |  |
| [**recepcionEcf33**](EcfApi.md#recepcionEcf33) | **POST** /ecf/33 |  |
| [**recepcionEcf34**](EcfApi.md#recepcionEcf34) | **POST** /ecf/34 |  |
| [**recepcionEcf41**](EcfApi.md#recepcionEcf41) | **POST** /ecf/41 |  |
| [**recepcionEcf43**](EcfApi.md#recepcionEcf43) | **POST** /ecf/43 |  |
| [**recepcionEcf44**](EcfApi.md#recepcionEcf44) | **POST** /ecf/44 |  |
| [**recepcionEcf45**](EcfApi.md#recepcionEcf45) | **POST** /ecf/45 |  |
| [**recepcionEcf46**](EcfApi.md#recepcionEcf46) | **POST** /ecf/46 |  |
| [**recepcionEcf47**](EcfApi.md#recepcionEcf47) | **POST** /ecf/47 |  |
| [**searchAllEcfs**](EcfApi.md#searchAllEcfs) | **GET** /ecf |  |
| [**searchEcfs**](EcfApi.md#searchEcfs) | **GET** /ecf/{rnc} |  |


<a id="anulacionRangos"></a>
# **anulacionRangos**
> RespuestaAnulacionRango anulacionRangos(rnc, anulacionRequest)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val anulacionRequest : AnulacionRequest =  // AnulacionRequest | 
try {
    val result : RespuestaAnulacionRango = apiInstance.anulacionRangos(rnc, anulacionRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#anulacionRangos")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#anulacionRangos")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **anulacionRequest** | [**AnulacionRequest**](AnulacionRequest.md)|  | |

### Return type

[**RespuestaAnulacionRango**](RespuestaAnulacionRango.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="aprobacionComercial"></a>
# **aprobacionComercial**
> aprobacionComercial(rnc, encf, sendAcecfRequest)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val encf : kotlin.String = encf_example // kotlin.String | 
val sendAcecfRequest : SendAcecfRequest =  // SendAcecfRequest | 
try {
    apiInstance.aprobacionComercial(rnc, encf, sendAcecfRequest)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#aprobacionComercial")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#aprobacionComercial")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **encf** | **kotlin.String**|  | |
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

<a id="firmarSemilla"></a>
# **firmarSemilla**
> firmarSemilla(rnc, xml)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val xml : java.io.File = BINARY_DATA_HERE // java.io.File | 
try {
    apiInstance.firmarSemilla(rnc, xml)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#firmarSemilla")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#firmarSemilla")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **xml** | **java.io.File**|  | |

### Return type

null (empty response body)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

<a id="getEcfById"></a>
# **getEcfById**
> kotlin.collections.List&lt;EcfResponse&gt; getEcfById(rnc, id, includeEcfContent)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val id : java.util.UUID = 38400000-8cf0-11bd-b23e-10b96e4ef00d // java.util.UUID | 
val includeEcfContent : kotlin.Boolean = true // kotlin.Boolean | 
try {
    val result : kotlin.collections.List<EcfResponse> = apiInstance.getEcfById(rnc, id, includeEcfContent)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#getEcfById")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#getEcfById")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **id** | **java.util.UUID**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **includeEcfContent** | **kotlin.Boolean**|  | [optional] [default to false] |

### Return type

[**kotlin.collections.List&lt;EcfResponse&gt;**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="listAnulaciones"></a>
# **listAnulaciones**
> PaginatedApiResultOfAnulacionListResponse listAnulaciones(tipoEcf, rncs, fechaDesde, fechaHasta, page, limit)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val tipoEcf : kotlin.collections.List<ECFType> =  // kotlin.collections.List<ECFType> | 
val rncs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val fechaDesde : java.time.OffsetDateTime = 2013-10-20T19:20:30+01:00 // java.time.OffsetDateTime | 
val fechaHasta : java.time.OffsetDateTime = 2013-10-20T19:20:30+01:00 // java.time.OffsetDateTime | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfAnulacionListResponse = apiInstance.listAnulaciones(tipoEcf, rncs, fechaDesde, fechaHasta, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#listAnulaciones")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#listAnulaciones")
    e.printStackTrace()
}
```

### Parameters
| **tipoEcf** | [**kotlin.collections.List&lt;ECFType&gt;**](ECFType.md)|  | [optional] |
| **rncs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **fechaDesde** | **java.time.OffsetDateTime**|  | [optional] |
| **fechaHasta** | **java.time.OffsetDateTime**|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfAnulacionListResponse**](PaginatedApiResultOfAnulacionListResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="queryEcf"></a>
# **queryEcf**
> kotlin.collections.List&lt;EcfResponse&gt; queryEcf(rnc, encf, includeEcfContent)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val encf : kotlin.String = encf_example // kotlin.String | 
val includeEcfContent : kotlin.Boolean = true // kotlin.Boolean | 
try {
    val result : kotlin.collections.List<EcfResponse> = apiInstance.queryEcf(rnc, encf, includeEcfContent)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#queryEcf")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#queryEcf")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **encf** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **includeEcfContent** | **kotlin.Boolean**|  | [optional] [default to false] |

### Return type

[**kotlin.collections.List&lt;EcfResponse&gt;**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf31"></a>
# **recepcionEcf31**
> EcfResponse recepcionEcf31(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf31(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf31")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf31")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf32"></a>
# **recepcionEcf32**
> EcfResponse recepcionEcf32(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf32(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf32")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf32")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf33"></a>
# **recepcionEcf33**
> EcfResponse recepcionEcf33(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf33(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf33")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf33")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf34"></a>
# **recepcionEcf34**
> EcfResponse recepcionEcf34(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf34(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf34")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf34")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf41"></a>
# **recepcionEcf41**
> EcfResponse recepcionEcf41(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf41(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf41")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf41")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf43"></a>
# **recepcionEcf43**
> EcfResponse recepcionEcf43(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf43(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf43")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf43")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf44"></a>
# **recepcionEcf44**
> EcfResponse recepcionEcf44(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf44(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf44")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf44")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf45"></a>
# **recepcionEcf45**
> EcfResponse recepcionEcf45(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf45(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf45")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf45")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf46"></a>
# **recepcionEcf46**
> EcfResponse recepcionEcf46(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf46(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf46")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf46")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="recepcionEcf47"></a>
# **recepcionEcf47**
> EcfResponse recepcionEcf47(ECF)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val ECF : ECF =  // ECF | 
try {
    val result : EcfResponse = apiInstance.recepcionEcf47(ECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#recepcionEcf47")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#recepcionEcf47")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

<a id="searchAllEcfs"></a>
# **searchAllEcfs**
> PaginatedApiResultOfEcfResponse searchAllEcfs(encfs, ids, tiposEcfs, includeEcfContent, fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val ids : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val tiposEcfs : kotlin.collections.List<AllTipoECFTypes> =  // kotlin.collections.List<AllTipoECFTypes> | 
val includeEcfContent : kotlin.Boolean = true // kotlin.Boolean | 
val fromFechaEmision : java.time.OffsetDateTime = 2013-10-20T19:20:30+01:00 // java.time.OffsetDateTime | 
val toFechaEmision : java.time.OffsetDateTime = 2013-10-20T19:20:30+01:00 // java.time.OffsetDateTime | 
val amountFrom : SearchEcfsAmountFromParameter = 1.2 // SearchEcfsAmountFromParameter | 
val amountTo : SearchEcfsAmountFromParameter = 1.2 // SearchEcfsAmountFromParameter | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfEcfResponse = apiInstance.searchAllEcfs(encfs, ids, tiposEcfs, includeEcfContent, fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#searchAllEcfs")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#searchAllEcfs")
    e.printStackTrace()
}
```

### Parameters
| **encfs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **ids** | [**kotlin.collections.List&lt;java.util.UUID&gt;**](java.util.UUID.md)|  | [optional] |
| **tiposEcfs** | [**kotlin.collections.List&lt;AllTipoECFTypes&gt;**](AllTipoECFTypes.md)|  | [optional] |
| **includeEcfContent** | **kotlin.Boolean**|  | [optional] [default to false] |
| **fromFechaEmision** | **java.time.OffsetDateTime**|  | [optional] |
| **toFechaEmision** | **java.time.OffsetDateTime**|  | [optional] |
| **amountFrom** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **amountTo** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfResponse**](PaginatedApiResultOfEcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="searchEcfs"></a>
# **searchEcfs**
> PaginatedApiResultOfEcfResponse searchEcfs(rnc, encfs, ids, tiposEcfs, includeEcfContent, fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = EcfApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val encfs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val ids : kotlin.collections.List<java.util.UUID> =  // kotlin.collections.List<java.util.UUID> | 
val tiposEcfs : kotlin.collections.List<AllTipoECFTypes> =  // kotlin.collections.List<AllTipoECFTypes> | 
val includeEcfContent : kotlin.Boolean = true // kotlin.Boolean | 
val fromFechaEmision : java.time.OffsetDateTime = 2013-10-20T19:20:30+01:00 // java.time.OffsetDateTime | 
val toFechaEmision : java.time.OffsetDateTime = 2013-10-20T19:20:30+01:00 // java.time.OffsetDateTime | 
val amountFrom : SearchEcfsAmountFromParameter = 1.2 // SearchEcfsAmountFromParameter | 
val amountTo : SearchEcfsAmountFromParameter = 1.2 // SearchEcfsAmountFromParameter | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfEcfResponse = apiInstance.searchEcfs(rnc, encfs, ids, tiposEcfs, includeEcfContent, fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling EcfApi#searchEcfs")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling EcfApi#searchEcfs")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **encfs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **ids** | [**kotlin.collections.List&lt;java.util.UUID&gt;**](java.util.UUID.md)|  | [optional] |
| **tiposEcfs** | [**kotlin.collections.List&lt;AllTipoECFTypes&gt;**](AllTipoECFTypes.md)|  | [optional] |
| **includeEcfContent** | **kotlin.Boolean**|  | [optional] [default to false] |
| **fromFechaEmision** | **java.time.OffsetDateTime**|  | [optional] |
| **toFechaEmision** | **java.time.OffsetDateTime**|  | [optional] |
| **amountFrom** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **amountTo** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfResponse**](PaginatedApiResultOfEcfResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

