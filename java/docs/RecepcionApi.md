# RecepcionApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
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
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.RecepcionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RecepcionApi apiInstance = new RecepcionApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    UUID messageId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.getAcecfReceptionRequest(rnc, messageId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecepcionApi#getAcecfReceptionRequest");
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
| **messageId** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getEcfReceptionRequest"></a>
# **getEcfReceptionRequest**
> getEcfReceptionRequest(rnc, messageId)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.RecepcionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RecepcionApi apiInstance = new RecepcionApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    UUID messageId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.getEcfReceptionRequest(rnc, messageId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecepcionApi#getEcfReceptionRequest");
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
| **messageId** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="searchAcecfReceptionRequests"></a>
# **searchAcecfReceptionRequests**
> PaginatedApiResultOfAcecfReceptionRequestDto searchAcecfReceptionRequests(messageIds, encfs, rncs, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.RecepcionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RecepcionApi apiInstance = new RecepcionApi(defaultClient);
    List<UUID> messageIds = Arrays.asList(); // List<UUID> | 
    List<String> encfs = Arrays.asList(); // List<String> | 
    List<String> rncs = Arrays.asList(); // List<String> | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfAcecfReceptionRequestDto result = apiInstance.searchAcecfReceptionRequests(messageIds, encfs, rncs, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecepcionApi#searchAcecfReceptionRequests");
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
| **messageIds** | [**List&lt;UUID&gt;**](UUID.md)|  | [optional] |
| **encfs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **rncs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfAcecfReceptionRequestDto**](PaginatedApiResultOfAcecfReceptionRequestDto.md)

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

<a id="searchAcecfReceptionRequestsByRnc"></a>
# **searchAcecfReceptionRequestsByRnc**
> PaginatedApiResultOfAcecfReceptionRequestDto searchAcecfReceptionRequestsByRnc(rnc, messageIds, encfs, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.RecepcionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RecepcionApi apiInstance = new RecepcionApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    List<UUID> messageIds = Arrays.asList(); // List<UUID> | 
    List<String> encfs = Arrays.asList(); // List<String> | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfAcecfReceptionRequestDto result = apiInstance.searchAcecfReceptionRequestsByRnc(rnc, messageIds, encfs, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecepcionApi#searchAcecfReceptionRequestsByRnc");
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
| **messageIds** | [**List&lt;UUID&gt;**](UUID.md)|  | [optional] |
| **encfs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfAcecfReceptionRequestDto**](PaginatedApiResultOfAcecfReceptionRequestDto.md)

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

<a id="searchEcfReceptionRequests"></a>
# **searchEcfReceptionRequests**
> PaginatedApiResultOfEcfReceptionRequestDto searchEcfReceptionRequests(messageIds, encfs, rncs, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.RecepcionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RecepcionApi apiInstance = new RecepcionApi(defaultClient);
    List<UUID> messageIds = Arrays.asList(); // List<UUID> | 
    List<String> encfs = Arrays.asList(); // List<String> | 
    List<String> rncs = Arrays.asList(); // List<String> | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfEcfReceptionRequestDto result = apiInstance.searchEcfReceptionRequests(messageIds, encfs, rncs, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecepcionApi#searchEcfReceptionRequests");
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
| **messageIds** | [**List&lt;UUID&gt;**](UUID.md)|  | [optional] |
| **encfs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **rncs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfReceptionRequestDto**](PaginatedApiResultOfEcfReceptionRequestDto.md)

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

<a id="searchEcfReceptionRequestsByRnc"></a>
# **searchEcfReceptionRequestsByRnc**
> PaginatedApiResultOfEcfReceptionRequestDto searchEcfReceptionRequestsByRnc(rnc, messageIds, encfs, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.RecepcionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RecepcionApi apiInstance = new RecepcionApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    List<UUID> messageIds = Arrays.asList(); // List<UUID> | 
    List<String> encfs = Arrays.asList(); // List<String> | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfEcfReceptionRequestDto result = apiInstance.searchEcfReceptionRequestsByRnc(rnc, messageIds, encfs, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecepcionApi#searchEcfReceptionRequestsByRnc");
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
| **messageIds** | [**List&lt;UUID&gt;**](UUID.md)|  | [optional] |
| **encfs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfEcfReceptionRequestDto**](PaginatedApiResultOfEcfReceptionRequestDto.md)

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

