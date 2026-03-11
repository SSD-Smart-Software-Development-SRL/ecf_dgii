# ApiKeyApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**newCompanyApiKey**](ApiKeyApi.md#newCompanyApiKey) | **POST** /apiKey |  |


<a id="newCompanyApiKey"></a>
# **newCompanyApiKey**
> Token newCompanyApiKey(newCompanyApiKey)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.ApiKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ApiKeyApi apiInstance = new ApiKeyApi(defaultClient);
    NewCompanyApiKey newCompanyApiKey = new NewCompanyApiKey(); // NewCompanyApiKey | 
    try {
      Token result = apiInstance.newCompanyApiKey(newCompanyApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeyApi#newCompanyApiKey");
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
| **newCompanyApiKey** | [**NewCompanyApiKey**](NewCompanyApiKey.md)|  | |

### Return type

[**Token**](Token.md)

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

