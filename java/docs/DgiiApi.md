# DgiiApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
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
> List&lt;Directorio&gt; consultaDirectorioListado(rnc)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    try {
      List<Directorio> result = apiInstance.consultaDirectorioListado(rnc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#consultaDirectorioListado");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |

### Return type

[**List&lt;Directorio&gt;**](Directorio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="consultaDirectorioObtenerDirectorioPorRnc"></a>
# **consultaDirectorioObtenerDirectorioPorRnc**
> Directorio consultaDirectorioObtenerDirectorioPorRnc(rnc, RNC)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String RNC = "RNC_example"; // String | 
    try {
      Directorio result = apiInstance.consultaDirectorioObtenerDirectorioPorRnc(rnc, RNC);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#consultaDirectorioObtenerDirectorioPorRnc");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |
| **RNC** | **String**|  | |

### Return type

[**Directorio**](Directorio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="consultaEstado"></a>
# **consultaEstado**
> RespuestaConsultaEstado consultaEstado(rnc, rncEmisor, ncfElectronico, rncComprador, codigoSeguridad)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String rncEmisor = "rncEmisor_example"; // String | 
    String ncfElectronico = "ncfElectronico_example"; // String | 
    String rncComprador = "rncComprador_example"; // String | 
    String codigoSeguridad = "codigoSeguridad_example"; // String | 
    try {
      RespuestaConsultaEstado result = apiInstance.consultaEstado(rnc, rncEmisor, ncfElectronico, rncComprador, codigoSeguridad);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#consultaEstado");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |
| **rncEmisor** | **String**|  | |
| **ncfElectronico** | **String**|  | |
| **rncComprador** | **String**|  | |
| **codigoSeguridad** | **String**|  | |

### Return type

[**RespuestaConsultaEstado**](RespuestaConsultaEstado.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="consultaRFCE"></a>
# **consultaRFCE**
> RespuestaConsultaRFCE consultaRFCE(rnc, rnCEmisor, ENCF, codSeguridadECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String rnCEmisor = "rnCEmisor_example"; // String | 
    String ENCF = "ENCF_example"; // String | 
    String codSeguridadECF = "codSeguridadECF_example"; // String | 
    try {
      RespuestaConsultaRFCE result = apiInstance.consultaRFCE(rnc, rnCEmisor, ENCF, codSeguridadECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#consultaRFCE");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |
| **rnCEmisor** | **String**|  | |
| **ENCF** | **String**|  | |
| **codSeguridadECF** | **String**|  | |

### Return type

[**RespuestaConsultaRFCE**](RespuestaConsultaRFCE.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="consultaResultado"></a>
# **consultaResultado**
> RespuestaConsultaTrackId consultaResultado(rnc, trackId)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String trackId = "trackId_example"; // String | 
    try {
      RespuestaConsultaTrackId result = apiInstance.consultaResultado(rnc, trackId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#consultaResultado");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |
| **trackId** | **String**|  | |

### Return type

[**RespuestaConsultaTrackId**](RespuestaConsultaTrackId.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="consultaTimbre"></a>
# **consultaTimbre**
> RespuestaConsultaTimbre consultaTimbre(rnc, rncemisor, encf, montototal, codigoseguridad)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String rncemisor = "rncemisor_example"; // String | 
    String encf = "encf_example"; // String | 
    String montototal = "montototal_example"; // String | 
    String codigoseguridad = "codigoseguridad_example"; // String | 
    try {
      RespuestaConsultaTimbre result = apiInstance.consultaTimbre(rnc, rncemisor, encf, montototal, codigoseguridad);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#consultaTimbre");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |
| **rncemisor** | **String**|  | |
| **encf** | **String**|  | |
| **montototal** | **String**|  | |
| **codigoseguridad** | **String**|  | |

### Return type

[**RespuestaConsultaTimbre**](RespuestaConsultaTimbre.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="consultaTimbreFC"></a>
# **consultaTimbreFC**
> RespuestaConsultaTimbre consultaTimbreFC(rnc, rncemisor, encf, montototal, codigoseguridad)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String rncemisor = "rncemisor_example"; // String | 
    String encf = "encf_example"; // String | 
    String montototal = "montototal_example"; // String | 
    String codigoseguridad = "codigoseguridad_example"; // String | 
    try {
      RespuestaConsultaTimbre result = apiInstance.consultaTimbreFC(rnc, rncemisor, encf, montototal, codigoseguridad);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#consultaTimbreFC");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |
| **rncemisor** | **String**|  | |
| **encf** | **String**|  | |
| **montototal** | **String**|  | |
| **codigoseguridad** | **String**|  | |

### Return type

[**RespuestaConsultaTimbre**](RespuestaConsultaTimbre.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="consultaTrackId"></a>
# **consultaTrackId**
> RespuestaConsultaTrackId consultaTrackId(rnc, rncEmisor, encf)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String rncEmisor = "rncEmisor_example"; // String | 
    String encf = "encf_example"; // String | 
    try {
      RespuestaConsultaTrackId result = apiInstance.consultaTrackId(rnc, rncEmisor, encf);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#consultaTrackId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |
| **rncEmisor** | **String**|  | |
| **encf** | **String**|  | |

### Return type

[**RespuestaConsultaTrackId**](RespuestaConsultaTrackId.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="estatusServiciosObtenerEstatus"></a>
# **estatusServiciosObtenerEstatus**
> List&lt;RespuestaEstatusServicio&gt; estatusServiciosObtenerEstatus(rnc)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    try {
      List<RespuestaEstatusServicio> result = apiInstance.estatusServiciosObtenerEstatus(rnc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#estatusServiciosObtenerEstatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |

### Return type

[**List&lt;RespuestaEstatusServicio&gt;**](RespuestaEstatusServicio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="estatusServiciosObtenerVentanasMantenimiento"></a>
# **estatusServiciosObtenerVentanasMantenimiento**
> RespuestaVentanaDeMantenimiento estatusServiciosObtenerVentanasMantenimiento(rnc)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.DgiiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    DgiiApi apiInstance = new DgiiApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    try {
      RespuestaVentanaDeMantenimiento result = apiInstance.estatusServiciosObtenerVentanasMantenimiento(rnc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DgiiApi#estatusServiciosObtenerVentanasMantenimiento");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **rnc** | **String**|  | |

### Return type

[**RespuestaVentanaDeMantenimiento**](RespuestaVentanaDeMantenimiento.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

