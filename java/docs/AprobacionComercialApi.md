# AprobacionComercialApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAcecfReceptionRequest**](AprobacionComercialApi.md#getAcecfReceptionRequest) | **GET** /recepcion/acecf/{messageId} |  |
| [**searchAcecfReceptionRequests**](AprobacionComercialApi.md#searchAcecfReceptionRequests) | **GET** /recepcion/acecf |  |


<a id="getAcecfReceptionRequest"></a>
# **getAcecfReceptionRequest**
> getAcecfReceptionRequest(messageId)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.AprobacionComercialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    AprobacionComercialApi apiInstance = new AprobacionComercialApi(defaultClient);
    UUID messageId = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.getAcecfReceptionRequest(messageId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AprobacionComercialApi#getAcecfReceptionRequest");
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

<a id="searchAcecfReceptionRequests"></a>
# **searchAcecfReceptionRequests**
> PaginatedApiResultOfAcecfReceptionRequestDto searchAcecfReceptionRequests(messageIds, encfs, rncs, progresses, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.AprobacionComercialApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    AprobacionComercialApi apiInstance = new AprobacionComercialApi(defaultClient);
    List<UUID> messageIds = Arrays.asList(); // List<UUID> | 
    List<String> encfs = Arrays.asList(); // List<String> | 
    List<String> rncs = Arrays.asList(); // List<String> | 
    List<SearchEcfReceptionRequestsTiposEcfsParameterInner> progresses = Arrays.asList(); // List<SearchEcfReceptionRequestsTiposEcfsParameterInner> | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfAcecfReceptionRequestDto result = apiInstance.searchAcecfReceptionRequests(messageIds, encfs, rncs, progresses, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AprobacionComercialApi#searchAcecfReceptionRequests");
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
| **progresses** | [**List&lt;SearchEcfReceptionRequestsTiposEcfsParameterInner&gt;**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md)|  | [optional] |
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

