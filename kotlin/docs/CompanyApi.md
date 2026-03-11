# CompanyApi

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
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
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = CompanyApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
try {
    apiInstance.deleteCompany(rnc)
} catch (e: ClientException) {
    println("4xx response calling CompanyApi#deleteCompany")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CompanyApi#deleteCompany")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **kotlin.String**|  | |

### Return type

null (empty response body)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

<a id="getCompanies"></a>
# **getCompanies**
> PaginatedApiResultOfCompanyResponse getCompanies(rncs, names, page, limit)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = CompanyApi()
val rncs : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val names : kotlin.collections.List<kotlin.String> =  // kotlin.collections.List<kotlin.String> | 
val page : GetCompaniesPageParameter = 56 // GetCompaniesPageParameter | 
val limit : GetCompaniesLimitParameter = 56 // GetCompaniesLimitParameter | 
try {
    val result : PaginatedApiResultOfCompanyResponse = apiInstance.getCompanies(rncs, names, page, limit)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CompanyApi#getCompanies")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CompanyApi#getCompanies")
    e.printStackTrace()
}
```

### Parameters
| **rncs** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **names** | [**kotlin.collections.List&lt;kotlin.String&gt;**](kotlin.String.md)|  | [optional] |
| **page** | **GetCompaniesPageParameter**|  | [optional] [default to 1] |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **limit** | **GetCompaniesLimitParameter**|  | [optional] [default to 25] |

### Return type

[**PaginatedApiResultOfCompanyResponse**](PaginatedApiResultOfCompanyResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="getCompanyByRnc"></a>
# **getCompanyByRnc**
> CompanyResponse getCompanyByRnc(rnc)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = CompanyApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
try {
    val result : CompanyResponse = apiInstance.getCompanyByRnc(rnc)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CompanyApi#getCompanyByRnc")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CompanyApi#getCompanyByRnc")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **kotlin.String**|  | |

### Return type

[**CompanyResponse**](CompanyResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="getCurrentCertificate"></a>
# **getCurrentCertificate**
> kotlin.collections.List&lt;CertificateResponse&gt; getCurrentCertificate(rnc)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = CompanyApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
try {
    val result : kotlin.collections.List<CertificateResponse> = apiInstance.getCurrentCertificate(rnc)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling CompanyApi#getCurrentCertificate")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CompanyApi#getCurrentCertificate")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **rnc** | **kotlin.String**|  | |

### Return type

[**kotlin.collections.List&lt;CertificateResponse&gt;**](CertificateResponse.md)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

<a id="updateCertificateCompany"></a>
# **updateCertificateCompany**
> updateCertificateCompany(rnc, certificate, password)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = CompanyApi()
val rnc : kotlin.String = rnc_example // kotlin.String | 
val certificate : java.io.File = BINARY_DATA_HERE // java.io.File | 
val password : kotlin.String = password_example // kotlin.String | 
try {
    apiInstance.updateCertificateCompany(rnc, certificate, password)
} catch (e: ClientException) {
    println("4xx response calling CompanyApi#updateCertificateCompany")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CompanyApi#updateCertificateCompany")
    e.printStackTrace()
}
```

### Parameters
| **rnc** | **kotlin.String**|  | |
| **certificate** | **java.io.File**|  | |
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **password** | **kotlin.String**|  | |

### Return type

null (empty response body)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json

<a id="upsertCompany"></a>
# **upsertCompany**
> upsertCompany(upsertCompanyRequest)



### Example
```kotlin
// Import classes:
//import com.ecfx.sdk.infrastructure.*
//import com.ecfx.sdk.models.*

val apiInstance = CompanyApi()
val upsertCompanyRequest : UpsertCompanyRequest =  // UpsertCompanyRequest | 
try {
    apiInstance.upsertCompany(upsertCompanyRequest)
} catch (e: ClientException) {
    println("4xx response calling CompanyApi#upsertCompany")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling CompanyApi#upsertCompany")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **upsertCompanyRequest** | [**UpsertCompanyRequest**](UpsertCompanyRequest.md)|  | |

### Return type

null (empty response body)

### Authorization


Configure Bearer:
    ApiClient.accessToken = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

