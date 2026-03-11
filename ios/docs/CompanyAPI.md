# CompanyAPI

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCompany**](CompanyAPI.md#deletecompany) | **DELETE** /company/{rnc} | 
[**getCompanies**](CompanyAPI.md#getcompanies) | **GET** /company | 
[**getCompanyByRnc**](CompanyAPI.md#getcompanybyrnc) | **GET** /company/{rnc} | 
[**getCurrentCertificate**](CompanyAPI.md#getcurrentcertificate) | **GET** /company/{rnc}/certificate | 
[**updateCertificateCompany**](CompanyAPI.md#updatecertificatecompany) | **PUT** /company/{rnc}/certificate | 
[**upsertCompany**](CompanyAPI.md#upsertcompany) | **PUT** /company | 


# **deleteCompany**
```swift
    open class func deleteCompany(rnc: String, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 

CompanyAPI.deleteCompany(rnc: rnc) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rnc** | **String** |  | 

### Return type

Void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getCompanies**
```swift
    open class func getCompanies(rncs: [String]? = nil, names: [String]? = nil, page: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: PaginatedApiResultOfCompanyResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rncs = ["inner_example"] // [String] |  (optional)
let names = ["inner_example"] // [String] |  (optional)
let page = 987 // Int |  (optional) (default to 1)
let limit = 987 // Int |  (optional) (default to 25)

CompanyAPI.getCompanies(rncs: rncs, names: names, page: page, limit: limit) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rncs** | [**[String]**](String.md) |  | [optional] 
 **names** | [**[String]**](String.md) |  | [optional] 
 **page** | **Int** |  | [optional] [default to 1]
 **limit** | **Int** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfCompanyResponse**](PaginatedApiResultOfCompanyResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getCompanyByRnc**
```swift
    open class func getCompanyByRnc(rnc: String, completion: @escaping (_ data: CompanyResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 

CompanyAPI.getCompanyByRnc(rnc: rnc) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rnc** | **String** |  | 

### Return type

[**CompanyResponse**](CompanyResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getCurrentCertificate**
```swift
    open class func getCurrentCertificate(rnc: String, completion: @escaping (_ data: [CertificateResponse]?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 

CompanyAPI.getCurrentCertificate(rnc: rnc) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rnc** | **String** |  | 

### Return type

[**[CertificateResponse]**](CertificateResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateCertificateCompany**
```swift
    open class func updateCertificateCompany(rnc: String, certificate: Data, password: String, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let certificate = Data([9, 8, 7]) // Data | 
let password = "password_example" // String | 

CompanyAPI.updateCertificateCompany(rnc: rnc, certificate: certificate, password: password) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rnc** | **String** |  | 
 **certificate** | **Data** |  | 
 **password** | **String** |  | 

### Return type

Void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsertCompany**
```swift
    open class func upsertCompany(upsertCompanyRequest: UpsertCompanyRequest, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let upsertCompanyRequest = UpsertCompanyRequest(rnc: "rnc_example", legalName: "legalName_example", name: "name_example") // UpsertCompanyRequest | 

CompanyAPI.upsertCompany(upsertCompanyRequest: upsertCompanyRequest) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsertCompanyRequest** | [**UpsertCompanyRequest**](UpsertCompanyRequest.md) |  | 

### Return type

Void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

