# CompanyApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteCompany**](CompanyApi.md#deleteCompany) | **DELETE** /company/{rnc} |  |
| [**getCompanies**](CompanyApi.md#getCompanies) | **GET** /company |  |
| [**getCompanyByRnc**](CompanyApi.md#getCompanyByRnc) | **GET** /company/{rnc} |  |
| [**getCurrentCertificate**](CompanyApi.md#getCurrentCertificate) | **GET** /company/{rnc}/certificate |  |
| [**updateCertificateCompany**](CompanyApi.md#updateCertificateCompany) | **PUT** /company/{rnc}/certificate |  |
| [**upsertCompany**](CompanyApi.md#upsertCompany) | **PUT** /company |  |


<a id="deleteCompany"></a>
# **deleteCompany**
> deleteCompany(rnc)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    CompanyApi apiInstance = new CompanyApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    try {
      apiInstance.deleteCompany(rnc);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApi#deleteCompany");
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

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **404** | Not Found |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getCompanies"></a>
# **getCompanies**
> PaginatedApiResultOfCompanyResponse getCompanies(rncs, names, page, limit)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    CompanyApi apiInstance = new CompanyApi(defaultClient);
    List<String> rncs = Arrays.asList(); // List<String> | 
    List<String> names = Arrays.asList(); // List<String> | 
    GetCompaniesPageParameter page = new GetCompaniesPageParameter(); // GetCompaniesPageParameter | 
    GetCompaniesLimitParameter limit = new GetCompaniesLimitParameter(); // GetCompaniesLimitParameter | 
    try {
      PaginatedApiResultOfCompanyResponse result = apiInstance.getCompanies(rncs, names, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApi#getCompanies");
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
| **rncs** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **names** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfCompanyResponse**](PaginatedApiResultOfCompanyResponse.md)

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

<a id="getCompanyByRnc"></a>
# **getCompanyByRnc**
> CompanyResponse getCompanyByRnc(rnc)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    CompanyApi apiInstance = new CompanyApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    try {
      CompanyResponse result = apiInstance.getCompanyByRnc(rnc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApi#getCompanyByRnc");
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

[**CompanyResponse**](CompanyResponse.md)

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

<a id="getCurrentCertificate"></a>
# **getCurrentCertificate**
> List&lt;CertificateResponse&gt; getCurrentCertificate(rnc)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    CompanyApi apiInstance = new CompanyApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    try {
      List<CertificateResponse> result = apiInstance.getCurrentCertificate(rnc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApi#getCurrentCertificate");
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

[**List&lt;CertificateResponse&gt;**](CertificateResponse.md)

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

<a id="updateCertificateCompany"></a>
# **updateCertificateCompany**
> updateCertificateCompany(rnc, certificate, password)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    CompanyApi apiInstance = new CompanyApi(defaultClient);
    String rnc = "rnc_example"; // String | 
    File certificate = new File("/path/to/file"); // File | 
    String password = "password_example"; // String | 
    try {
      apiInstance.updateCertificateCompany(rnc, certificate, password);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApi#updateCertificateCompany");
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
| **certificate** | **File**|  | |
| **password** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="upsertCompany"></a>
# **upsertCompany**
> upsertCompany(upsertCompanyRequest)



### Example
```java
// Import classes:
import dom.com.ssd.ecfx.client.ApiClient;
import dom.com.ssd.ecfx.client.ApiException;
import dom.com.ssd.ecfx.client.Configuration;
import dom.com.ssd.ecfx.client.auth.*;
import dom.com.ssd.ecfx.client.models.*;
import dom.com.ssd.ecfx.client.api.CompanyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.ecfx.ssd.com.do");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    CompanyApi apiInstance = new CompanyApi(defaultClient);
    UpsertCompanyRequest upsertCompanyRequest = new UpsertCompanyRequest(); // UpsertCompanyRequest | 
    try {
      apiInstance.upsertCompany(upsertCompanyRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyApi#upsertCompany");
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
| **upsertCompanyRequest** | [**UpsertCompanyRequest**](UpsertCompanyRequest.md)|  | |

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
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

