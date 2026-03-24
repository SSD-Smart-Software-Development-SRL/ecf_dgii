# DgiiApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**consultaDirectorioListado**](DgiiApi.md#consultaDirectorioListado) | **GET** /dgii/{rnc}/consultadirectorio/listado |  |
| [**consultaDirectorioObtenerDirectorioPorRnc**](DgiiApi.md#consultaDirectorioObtenerDirectorioPorRnc) | **GET** /dgii/{rnc}/consultadirectorio/obtener-directorio-por-rnc |  |
| [**consultaEstado**](DgiiApi.md#consultaEstado) | **GET** /dgii/{rnc}/consultaestado/estado |  |
| [**consultaRFCE**](DgiiApi.md#consultaRFCE) | **GET** /dgii/{rnc}/consultarfce/consulta |  |
| [**consultaResultado**](DgiiApi.md#consultaResultado) | **GET** /dgii/{rnc}/consultaresultado/estado |  |
| [**consultaTimbre**](DgiiApi.md#consultaTimbre) | **GET** /dgii/{rnc}/consultatimbre |  |
| [**consultaTimbreFC**](DgiiApi.md#consultaTimbreFC) | **GET** /dgii/{rnc}/consultatimbrefc |  |
| [**consultaTrackId**](DgiiApi.md#consultaTrackId) | **GET** /dgii/{rnc}/consultatrackids/consulta |  |
| [**estatusServiciosObtenerEstatus**](DgiiApi.md#estatusServiciosObtenerEstatus) | **GET** /dgii/{rnc}/estatusservicios/obtener-estatus |  |
| [**estatusServiciosObtenerVentanasMantenimiento**](DgiiApi.md#estatusServiciosObtenerVentanasMantenimiento) | **GET** /dgii/{rnc}/estatusservicios/obtener-ventanas-mantenimiento |  |


<a id="consultaDirectorioListado"></a>
# **consultaDirectorioListado**
> kotlin.collections.List&lt;Directorio&gt; consultaDirectorioListado(rnc)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
try {
    val result : kotlin.collections.List<Directorio> = apiInstance.consultaDirectorioListado(rnc)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#consultaDirectorioListado")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#consultaDirectorioListado")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **kotlin.String**|  | |

### Return type

[**kotlin.collections.List&lt;Directorio&gt;**](Directorio.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="consultaDirectorioObtenerDirectorioPorRnc"></a>
# **consultaDirectorioObtenerDirectorioPorRnc**
> Directorio consultaDirectorioObtenerDirectorioPorRnc(rnc, RNC)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val RNC : kotlin.String = RNC_example // kotlin.String | 
try {
    val result : Directorio = apiInstance.consultaDirectorioObtenerDirectorioPorRnc(rnc, RNC)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#consultaDirectorioObtenerDirectorioPorRnc")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#consultaDirectorioObtenerDirectorioPorRnc")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **RNC** | **kotlin.String**|  | |

### Return type

[**Directorio**](Directorio.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="consultaEstado"></a>
# **consultaEstado**
> RespuestaConsultaEstado consultaEstado(rnc, rncEmisor, ncfElectronico, rncComprador, codigoSeguridad)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val rncEmisor : kotlin.String = rncEmisor_example // kotlin.String | 
val ncfElectronico : kotlin.String = ncfElectronico_example // kotlin.String | 
val rncComprador : kotlin.String = rncComprador_example // kotlin.String | 
val codigoSeguridad : kotlin.String = codigoSeguridad_example // kotlin.String | 
try {
    val result : RespuestaConsultaEstado = apiInstance.consultaEstado(rnc, rncEmisor, ncfElectronico, rncComprador, codigoSeguridad)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#consultaEstado")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#consultaEstado")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **rncEmisor** | **kotlin.String**|  | |
| **ncfElectronico** | **kotlin.String**|  | |
| **rncComprador** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **codigoSeguridad** | **kotlin.String**|  | |

### Return type

[**RespuestaConsultaEstado**](RespuestaConsultaEstado.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="consultaRFCE"></a>
# **consultaRFCE**
> RespuestaConsultaRFCE consultaRFCE(rnc, rnCEmisor, ENCF, codSeguridadECF)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val rnCEmisor : kotlin.String = rnCEmisor_example // kotlin.String | 
val ENCF : kotlin.String = ENCF_example // kotlin.String | 
val codSeguridadECF : kotlin.String = codSeguridadECF_example // kotlin.String | 
try {
    val result : RespuestaConsultaRFCE = apiInstance.consultaRFCE(rnc, rnCEmisor, ENCF, codSeguridadECF)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#consultaRFCE")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#consultaRFCE")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **rnCEmisor** | **kotlin.String**|  | |
| **ENCF** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **codSeguridadECF** | **kotlin.String**|  | |

### Return type

[**RespuestaConsultaRFCE**](RespuestaConsultaRFCE.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="consultaResultado"></a>
# **consultaResultado**
> RespuestaConsultaTrackId consultaResultado(rnc, trackId)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val trackId : kotlin.String = trackId_example // kotlin.String | 
try {
    val result : RespuestaConsultaTrackId = apiInstance.consultaResultado(rnc, trackId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#consultaResultado")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#consultaResultado")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **trackId** | **kotlin.String**|  | |

### Return type

[**RespuestaConsultaTrackId**](RespuestaConsultaTrackId.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="consultaTimbre"></a>
# **consultaTimbre**
> RespuestaConsultaTimbre consultaTimbre(rnc, rncemisor, encf, montototal, codigoseguridad)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val rncemisor : kotlin.String = rncemisor_example // kotlin.String | 
val encf : kotlin.String = encf_example // kotlin.String | 
val montototal : kotlin.String = montototal_example // kotlin.String | 
val codigoseguridad : kotlin.String = codigoseguridad_example // kotlin.String | 
try {
    val result : RespuestaConsultaTimbre = apiInstance.consultaTimbre(rnc, rncemisor, encf, montototal, codigoseguridad)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#consultaTimbre")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#consultaTimbre")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **rncemisor** | **kotlin.String**|  | |
| **encf** | **kotlin.String**|  | |
| **montototal** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **codigoseguridad** | **kotlin.String**|  | |

### Return type

[**RespuestaConsultaTimbre**](RespuestaConsultaTimbre.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="consultaTimbreFC"></a>
# **consultaTimbreFC**
> RespuestaConsultaTimbre consultaTimbreFC(rnc, rncemisor, encf, montototal, codigoseguridad)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val rncemisor : kotlin.String = rncemisor_example // kotlin.String | 
val encf : kotlin.String = encf_example // kotlin.String | 
val montototal : kotlin.String = montototal_example // kotlin.String | 
val codigoseguridad : kotlin.String = codigoseguridad_example // kotlin.String | 
try {
    val result : RespuestaConsultaTimbre = apiInstance.consultaTimbreFC(rnc, rncemisor, encf, montototal, codigoseguridad)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#consultaTimbreFC")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#consultaTimbreFC")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **rncemisor** | **kotlin.String**|  | |
| **encf** | **kotlin.String**|  | |
| **montototal** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **codigoseguridad** | **kotlin.String**|  | |

### Return type

[**RespuestaConsultaTimbre**](RespuestaConsultaTimbre.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="consultaTrackId"></a>
# **consultaTrackId**
> RespuestaConsultaTrackId consultaTrackId(rnc, rncEmisor, encf)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val rncEmisor : kotlin.String = rncEmisor_example // kotlin.String | 
val encf : kotlin.String = encf_example // kotlin.String | 
try {
    val result : RespuestaConsultaTrackId = apiInstance.consultaTrackId(rnc, rncEmisor, encf)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#consultaTrackId")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#consultaTrackId")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **rncEmisor** | **kotlin.String**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **encf** | **kotlin.String**|  | |

### Return type

[**RespuestaConsultaTrackId**](RespuestaConsultaTrackId.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="estatusServiciosObtenerEstatus"></a>
# **estatusServiciosObtenerEstatus**
> kotlin.collections.List&lt;RespuestaEstatusServicio&gt; estatusServiciosObtenerEstatus(rnc)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
try {
    val result : kotlin.collections.List<RespuestaEstatusServicio> = apiInstance.estatusServiciosObtenerEstatus(rnc)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#estatusServiciosObtenerEstatus")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#estatusServiciosObtenerEstatus")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **kotlin.String**|  | |

### Return type

[**kotlin.collections.List&lt;RespuestaEstatusServicio&gt;**](RespuestaEstatusServicio.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="estatusServiciosObtenerVentanasMantenimiento"></a>
# **estatusServiciosObtenerVentanasMantenimiento**
> RespuestaVentanaDeMantenimiento estatusServiciosObtenerVentanasMantenimiento(rnc)



### Example
```kotlin
// Import classes:
//import dom.com.ssd.ecfx.sdk.infrastructure.*
//import dom.com.ssd.ecfx.sdk.models.*

val apiInstance = DgiiApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
try {
    val result : RespuestaVentanaDeMantenimiento = apiInstance.estatusServiciosObtenerVentanasMantenimiento(rnc)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DgiiApi#estatusServiciosObtenerVentanasMantenimiento")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DgiiApi#estatusServiciosObtenerVentanasMantenimiento")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **kotlin.String**|  | |

### Return type

[**RespuestaVentanaDeMantenimiento**](RespuestaVentanaDeMantenimiento.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

