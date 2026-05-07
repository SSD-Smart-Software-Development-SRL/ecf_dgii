# RecepcionApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEcfReceptionRequest**](RecepcionApi.md#getEcfReceptionRequest) | **GET** /recepcion/{messageId} |  |
| [**getEcfReceptorByMessageId**](RecepcionApi.md#getEcfReceptorByMessageId) | **GET** /recepcion/{rnc}/{messageId} |  |
| [**searchEcfReceptionRequests**](RecepcionApi.md#searchEcfReceptionRequests) | **GET** /recepcion |  |
| [**searchEcfReceptionRequestsByRnc**](RecepcionApi.md#searchEcfReceptionRequestsByRnc) | **GET** /recepcion/{rnc} |  |
| [**sendAprobacionComercial**](RecepcionApi.md#sendAprobacionComercial) | **POST** /recepcion/{messageId}/acecf |  |


<a id="getEcfReceptionRequest"></a>
# **getEcfReceptionRequest**
> getEcfReceptionRequest(messageId)



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
    UUID messageId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.getEcfReceptionRequest(messageId);
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

<a id="getEcfReceptorByMessageId"></a>
# **getEcfReceptorByMessageId**
> EcfReceptorDto getEcfReceptorByMessageId(rnc, messageId)



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
      EcfReceptorDto result = apiInstance.getEcfReceptorByMessageId(rnc, messageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecepcionApi#getEcfReceptorByMessageId");
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

[**EcfReceptorDto**](EcfReceptorDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="searchEcfReceptionRequests"></a>
# **searchEcfReceptionRequests**
> PaginatedApiResultOfEcfReceptionRequestDto searchEcfReceptionRequests(messageIds, encfs, rncs, rncEmisors, tiposEcfs, progresses, fromDate, toDate, amountFrom, amountTo, page, limit)



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
    List<String> rncEmisors = Arrays.asList(); // List<String> | 
    List<SearchEcfReceptionRequestsTiposEcfsParameterInner> tiposEcfs = Arrays.asList(); // List<SearchEcfReceptionRequestsTiposEcfsParameterInner> | 
    List<SearchEcfReceptionRequestsTiposEcfsParameterInner> progresses = Arrays.asList(); // List<SearchEcfReceptionRequestsTiposEcfsParameterInner> | 
    String fromDate = "fromDate_example"; // String | 
    String toDate = "toDate_example"; // String | 
    SearchEcfsAmountFromParameter amountFrom = new SearchEcfsAmountFromParameter(); // SearchEcfsAmountFromParameter | 
    SearchEcfsAmountFromParameter amountTo = new SearchEcfsAmountFromParameter(); // SearchEcfsAmountFromParameter | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfEcfReceptionRequestDto result = apiInstance.searchEcfReceptionRequests(messageIds, encfs, rncs, rncEmisors, tiposEcfs, progresses, fromDate, toDate, amountFrom, amountTo, page, limit);
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
| **rncEmisors** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **tiposEcfs** | [**List&lt;SearchEcfReceptionRequestsTiposEcfsParameterInner&gt;**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md)|  | [optional] |
| **progresses** | [**List&lt;SearchEcfReceptionRequestsTiposEcfsParameterInner&gt;**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md)|  | [optional] |
| **fromDate** | **String**|  | [optional] |
| **toDate** | **String**|  | [optional] |
| **amountFrom** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **amountTo** | **SearchEcfsAmountFromParameter**|  | [optional] |
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
> PaginatedApiResultOfEcfReceptionRequestDto searchEcfReceptionRequestsByRnc(rnc, messageIds, encfs, rncEmisors, tiposEcfs, progresses, fromDate, toDate, amountFrom, amountTo, page, limit)



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
    List<String> rncEmisors = Arrays.asList(); // List<String> | 
    List<SearchEcfReceptionRequestsTiposEcfsParameterInner> tiposEcfs = Arrays.asList(); // List<SearchEcfReceptionRequestsTiposEcfsParameterInner> | 
    List<SearchEcfReceptionRequestsTiposEcfsParameterInner> progresses = Arrays.asList(); // List<SearchEcfReceptionRequestsTiposEcfsParameterInner> | 
    String fromDate = "fromDate_example"; // String | 
    String toDate = "toDate_example"; // String | 
    SearchEcfsAmountFromParameter amountFrom = new SearchEcfsAmountFromParameter(); // SearchEcfsAmountFromParameter | 
    SearchEcfsAmountFromParameter amountTo = new SearchEcfsAmountFromParameter(); // SearchEcfsAmountFromParameter | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfEcfReceptionRequestDto result = apiInstance.searchEcfReceptionRequestsByRnc(rnc, messageIds, encfs, rncEmisors, tiposEcfs, progresses, fromDate, toDate, amountFrom, amountTo, page, limit);
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
| **rncEmisors** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **tiposEcfs** | [**List&lt;SearchEcfReceptionRequestsTiposEcfsParameterInner&gt;**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md)|  | [optional] |
| **progresses** | [**List&lt;SearchEcfReceptionRequestsTiposEcfsParameterInner&gt;**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md)|  | [optional] |
| **fromDate** | **String**|  | [optional] |
| **toDate** | **String**|  | [optional] |
| **amountFrom** | **SearchEcfsAmountFromParameter**|  | [optional] |
| **amountTo** | **SearchEcfsAmountFromParameter**|  | [optional] |
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

<a id="sendAprobacionComercial"></a>
# **sendAprobacionComercial**
> sendAprobacionComercial(messageId, sendAcecfRequest)



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
    UUID messageId = UUID.randomUUID(); // UUID | 
    SendAcecfRequest sendAcecfRequest = new SendAcecfRequest(); // SendAcecfRequest | 
    try {
      apiInstance.sendAprobacionComercial(messageId, sendAcecfRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecepcionApi#sendAprobacionComercial");
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
| **messageId** | **UUID**|  | |
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

