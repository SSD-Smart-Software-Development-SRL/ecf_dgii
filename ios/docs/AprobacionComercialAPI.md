# AprobacionComercialAPI

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAcecfReceptionRequest**](AprobacionComercialAPI.md#getacecfreceptionrequest) | **GET** /recepcion/acecf/{messageId} | 
[**searchAcecfReceptionRequests**](AprobacionComercialAPI.md#searchacecfreceptionrequests) | **GET** /recepcion/acecf | 


# **getAcecfReceptionRequest**
```swift
    open class func getAcecfReceptionRequest(messageId: UUID, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let messageId = 987 // UUID | 

AprobacionComercialAPI.getAcecfReceptionRequest(messageId: messageId) { (response, error) in
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
 **messageId** | **UUID** |  | 

### Return type

Void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchAcecfReceptionRequests**
```swift
    open class func searchAcecfReceptionRequests(messageIds: [UUID]? = nil, encfs: [String]? = nil, rncs: [String]? = nil, progresses: [SearchEcfReceptionRequestsTiposEcfsParameterInner]? = nil, page: GetCompaniesPageParameter? = nil, limit: GetCompaniesLimitParameter? = nil, completion: @escaping (_ data: PaginatedApiResultOfAcecfReceptionRequestDto?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let messageIds = [123] // [UUID] |  (optional)
let encfs = ["inner_example"] // [String] |  (optional)
let rncs = ["inner_example"] // [String] |  (optional)
let progresses = [SearchEcfReceptionRequests_TiposEcfs_parameter_inner()] // [SearchEcfReceptionRequestsTiposEcfsParameterInner] |  (optional)
let page = GetCompanies_Page_parameter() // GetCompaniesPageParameter |  (optional) (default to 1)
let limit = GetCompanies_Limit_parameter() // GetCompaniesLimitParameter |  (optional) (default to 25)

AprobacionComercialAPI.searchAcecfReceptionRequests(messageIds: messageIds, encfs: encfs, rncs: rncs, progresses: progresses, page: page, limit: limit) { (response, error) in
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
 **messageIds** | [**[UUID]**](UUID.md) |  | [optional] 
 **encfs** | [**[String]**](String.md) |  | [optional] 
 **rncs** | [**[String]**](String.md) |  | [optional] 
 **progresses** | [**[SearchEcfReceptionRequestsTiposEcfsParameterInner]**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md) |  | [optional] 
 **page** | **GetCompaniesPageParameter** |  | [optional] [default to 1]
 **limit** | **GetCompaniesLimitParameter** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfAcecfReceptionRequestDto**](PaginatedApiResultOfAcecfReceptionRequestDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

