# EcfApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
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
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    AnulacionRequest anulacionRequest = new AnulacionRequest(); // AnulacionRequest | 
    try {
      RespuestaAnulacionRango result = apiInstance.anulacionRangos(rnc, anulacionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#anulacionRangos");
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
| **anulacionRequest** | [**AnulacionRequest**](AnulacionRequest.md)|  | |

### Return type

[**RespuestaAnulacionRango**](RespuestaAnulacionRango.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/xml, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="aprobacionComercial"></a>
# **aprobacionComercial**
> aprobacionComercial(rnc, encf, sendAcecfRequest)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String encf = "encf_example"; // String | 
    SendAcecfRequest sendAcecfRequest = new SendAcecfRequest(); // SendAcecfRequest | 
    try {
      apiInstance.aprobacionComercial(rnc, encf, sendAcecfRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#aprobacionComercial");
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
| **encf** | **String**|  | |
| **sendAcecfRequest** | [**SendAcecfRequest**](SendAcecfRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="firmarSemilla"></a>
# **firmarSemilla**
> firmarSemilla(rnc, xml)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    File xml = new File("/path/to/file"); // File | 
    try {
      apiInstance.firmarSemilla(rnc, xml);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#firmarSemilla");
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
| **xml** | **File**|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getEcfById"></a>
# **getEcfById**
> List&lt;EcfResponse&gt; getEcfById(rnc, id, includeEcfContent)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    UUID id = UUID.randomUUID(); // UUID | 
    Boolean includeEcfContent = false; // Boolean | 
    try {
      List<EcfResponse> result = apiInstance.getEcfById(rnc, id, includeEcfContent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#getEcfById");
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
| **id** | **UUID**|  | |
| **includeEcfContent** | **Boolean**|  | [optional] [default to false] |

### Return type

[**List&lt;EcfResponse&gt;**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="listAnulaciones"></a>
# **listAnulaciones**
> PaginatedApiResultOfAnulacionListResponse listAnulaciones(tipoEcf, rncs, fechaDesde, fechaHasta, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    List<ECFType> tipoEcf = Arrays.asList(); // List<ECFType> | 
    List<String> rncs = Arrays.asList(); // List<String> | 
    Date fechaDesde = new Date(); // Date | 
    Date fechaHasta = new Date(); // Date | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfAnulacionListResponse result = apiInstance.listAnulaciones(tipoEcf, rncs, fechaDesde, fechaHasta, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#listAnulaciones");
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
| **tipoEcf** | [**List&lt;ECFType&gt;**](ECFType.md)|  | [optional] |
| **rncs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **fechaDesde** | **Date**|  | [optional] |
| **fechaHasta** | **Date**|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfAnulacionListResponse**](PaginatedApiResultOfAnulacionListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="queryEcf"></a>
# **queryEcf**
> List&lt;EcfResponse&gt; queryEcf(rnc, encf, includeEcfContent)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    String encf = "encf_example"; // String | 
    Boolean includeEcfContent = false; // Boolean | 
    try {
      List<EcfResponse> result = apiInstance.queryEcf(rnc, encf, includeEcfContent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#queryEcf");
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
| **encf** | **String**|  | |
| **includeEcfContent** | **Boolean**|  | [optional] [default to false] |

### Return type

[**List&lt;EcfResponse&gt;**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf31"></a>
# **recepcionEcf31**
> EcfResponse recepcionEcf31(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf31(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf31");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf32"></a>
# **recepcionEcf32**
> EcfResponse recepcionEcf32(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf32(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf32");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf33"></a>
# **recepcionEcf33**
> EcfResponse recepcionEcf33(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf33(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf33");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf34"></a>
# **recepcionEcf34**
> EcfResponse recepcionEcf34(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf34(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf34");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf41"></a>
# **recepcionEcf41**
> EcfResponse recepcionEcf41(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf41(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf41");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf43"></a>
# **recepcionEcf43**
> EcfResponse recepcionEcf43(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf43(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf43");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf44"></a>
# **recepcionEcf44**
> EcfResponse recepcionEcf44(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf44(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf44");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf45"></a>
# **recepcionEcf45**
> EcfResponse recepcionEcf45(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf45(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf45");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf46"></a>
# **recepcionEcf46**
> EcfResponse recepcionEcf46(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf46(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf46");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="recepcionEcf47"></a>
# **recepcionEcf47**
> EcfResponse recepcionEcf47(ECF)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    ECF ECF = new ECF(); // ECF | 
    try {
      EcfResponse result = apiInstance.recepcionEcf47(ECF);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#recepcionEcf47");
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
| **ECF** | [**ECF**](ECF.md)|  | |

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="searchAllEcfs"></a>
# **searchAllEcfs**
> PaginatedApiResultOfEcfResponse searchAllEcfs(encfs, ids, tiposEcfs, includeEcfContent, fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    List<String> encfs = Arrays.asList(); // List<String> | 
    List<UUID> ids = Arrays.asList(); // List<UUID> | 
    List<AllTipoECFTypes> tiposEcfs = Arrays.asList(); // List<AllTipoECFTypes> | 
    Boolean includeEcfContent = false; // Boolean | 
    Date fromFechaEmision = new Date(); // Date | 
    Date toFechaEmision = new Date(); // Date | 
    SearchEcfsAmountFromParameter amountFrom = new SearchEcfsAmountFromParameter(); // SearchEcfsAmountFromParameter | 
    SearchEcfsAmountFromParameter amountTo = new SearchEcfsAmountFromParameter(); // SearchEcfsAmountFromParameter | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfEcfResponse result = apiInstance.searchAllEcfs(encfs, ids, tiposEcfs, includeEcfContent, fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#searchAllEcfs");
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
| **encfs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **ids** | [**List&lt;UUID&gt;**](UUID.md)|  | [optional] |
| **tiposEcfs** | [**List&lt;AllTipoECFTypes&gt;**](AllTipoECFTypes.md)|  | [optional] |
| **includeEcfContent** | **Boolean**|  | [optional] [default to false] |
| **fromFechaEmision** | **Date**|  | [optional] |
| **toFechaEmision** | **Date**|  | [optional] |
| **amountFrom** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **amountTo** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfResponse**](PaginatedApiResultOfEcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="searchEcfs"></a>
# **searchEcfs**
> PaginatedApiResultOfEcfResponse searchEcfs(rnc, encfs, ids, tiposEcfs, includeEcfContent, fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.EcfApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    EcfApi apiInstance = new EcfApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    List<String> encfs = Arrays.asList(); // List<String> | 
    List<UUID> ids = Arrays.asList(); // List<UUID> | 
    List<AllTipoECFTypes> tiposEcfs = Arrays.asList(); // List<AllTipoECFTypes> | 
    Boolean includeEcfContent = false; // Boolean | 
    Date fromFechaEmision = new Date(); // Date | 
    Date toFechaEmision = new Date(); // Date | 
    SearchEcfsAmountFromParameter amountFrom = new SearchEcfsAmountFromParameter(); // SearchEcfsAmountFromParameter | 
    SearchEcfsAmountFromParameter amountTo = new SearchEcfsAmountFromParameter(); // SearchEcfsAmountFromParameter | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfEcfResponse result = apiInstance.searchEcfs(rnc, encfs, ids, tiposEcfs, includeEcfContent, fromFechaEmision, toFechaEmision, amountFrom, amountTo, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcfApi#searchEcfs");
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
| **encfs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **ids** | [**List&lt;UUID&gt;**](UUID.md)|  | [optional] |
| **tiposEcfs** | [**List&lt;AllTipoECFTypes&gt;**](AllTipoECFTypes.md)|  | [optional] |
| **includeEcfContent** | **Boolean**|  | [optional] [default to false] |
| **fromFechaEmision** | **Date**|  | [optional] |
| **toFechaEmision** | **Date**|  | [optional] |
| **amountFrom** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **amountTo** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfResponse**](PaginatedApiResultOfEcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

