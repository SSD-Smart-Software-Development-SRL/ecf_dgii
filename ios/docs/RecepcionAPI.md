# RecepcionAPI

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAcecfReceptionRequest**](RecepcionAPI.md#getacecfreceptionrequest) | **GET** /recepcion/{rnc}/acecf/{messageId} | 
[**getEcfReceptionRequest**](RecepcionAPI.md#getecfreceptionrequest) | **GET** /recepcion/{rnc}/ecf/{messageId} | 
[**searchAcecfReceptionRequests**](RecepcionAPI.md#searchacecfreceptionrequests) | **GET** /recepcion/acecf | 
[**searchAcecfReceptionRequestsByRnc**](RecepcionAPI.md#searchacecfreceptionrequestsbyrnc) | **GET** /recepcion/{rnc}/acecf | 
[**searchEcfReceptionRequests**](RecepcionAPI.md#searchecfreceptionrequests) | **GET** /recepcion/ecf | 
[**searchEcfReceptionRequestsByRnc**](RecepcionAPI.md#searchecfreceptionrequestsbyrnc) | **GET** /recepcion/{rnc}/ecf | 


# **getAcecfReceptionRequest**
```swift
    open class func getAcecfReceptionRequest(rnc: String, messageId: UUID, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let messageId = 987 // UUID | 

RecepcionAPI.getAcecfReceptionRequest(rnc: rnc, messageId: messageId) { (response, error) in
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
 **messageId** | **UUID** |  | 

### Return type

Void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getEcfReceptionRequest**
```swift
    open class func getEcfReceptionRequest(rnc: String, messageId: UUID, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let messageId = 987 // UUID | 

RecepcionAPI.getEcfReceptionRequest(rnc: rnc, messageId: messageId) { (response, error) in
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
    open class func searchAcecfReceptionRequests(messageIds: [UUID]? = nil, encfs: [String]? = nil, rncs: [String]? = nil, page: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: PaginatedApiResultOfAcecfReceptionRequestDto?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let messageIds = [123] // [UUID] |  (optional)
let encfs = ["inner_example"] // [String] |  (optional)
let rncs = ["inner_example"] // [String] |  (optional)
let page = 987 // Int |  (optional) (default to 1)
let limit = 987 // Int |  (optional) (default to 25)

RecepcionAPI.searchAcecfReceptionRequests(messageIds: messageIds, encfs: encfs, rncs: rncs, page: page, limit: limit) { (response, error) in
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
 **page** | **Int** |  | [optional] [default to 1]
 **limit** | **Int** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfAcecfReceptionRequestDto**](PaginatedApiResultOfAcecfReceptionRequestDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchAcecfReceptionRequestsByRnc**
```swift
    open class func searchAcecfReceptionRequestsByRnc(rnc: String, messageIds: [UUID]? = nil, encfs: [String]? = nil, page: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: PaginatedApiResultOfAcecfReceptionRequestDto?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let messageIds = [123] // [UUID] |  (optional)
let encfs = ["inner_example"] // [String] |  (optional)
let page = 987 // Int |  (optional) (default to 1)
let limit = 987 // Int |  (optional) (default to 25)

RecepcionAPI.searchAcecfReceptionRequestsByRnc(rnc: rnc, messageIds: messageIds, encfs: encfs, page: page, limit: limit) { (response, error) in
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
 **messageIds** | [**[UUID]**](UUID.md) |  | [optional] 
 **encfs** | [**[String]**](String.md) |  | [optional] 
 **page** | **Int** |  | [optional] [default to 1]
 **limit** | **Int** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfAcecfReceptionRequestDto**](PaginatedApiResultOfAcecfReceptionRequestDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchEcfReceptionRequests**
```swift
    open class func searchEcfReceptionRequests(messageIds: [UUID]? = nil, encfs: [String]? = nil, rncs: [String]? = nil, page: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: PaginatedApiResultOfEcfReceptionRequestDto?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let messageIds = [123] // [UUID] |  (optional)
let encfs = ["inner_example"] // [String] |  (optional)
let rncs = ["inner_example"] // [String] |  (optional)
let page = 987 // Int |  (optional) (default to 1)
let limit = 987 // Int |  (optional) (default to 25)

RecepcionAPI.searchEcfReceptionRequests(messageIds: messageIds, encfs: encfs, rncs: rncs, page: page, limit: limit) { (response, error) in
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
 **page** | **Int** |  | [optional] [default to 1]
 **limit** | **Int** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfEcfReceptionRequestDto**](PaginatedApiResultOfEcfReceptionRequestDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchEcfReceptionRequestsByRnc**
```swift
    open class func searchEcfReceptionRequestsByRnc(rnc: String, messageIds: [UUID]? = nil, encfs: [String]? = nil, page: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: PaginatedApiResultOfEcfReceptionRequestDto?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let messageIds = [123] // [UUID] |  (optional)
let encfs = ["inner_example"] // [String] |  (optional)
let page = 987 // Int |  (optional) (default to 1)
let limit = 987 // Int |  (optional) (default to 25)

RecepcionAPI.searchEcfReceptionRequestsByRnc(rnc: rnc, messageIds: messageIds, encfs: encfs, page: page, limit: limit) { (response, error) in
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
 **messageIds** | [**[UUID]**](UUID.md) |  | [optional] 
 **encfs** | [**[String]**](String.md) |  | [optional] 
 **page** | **Int** |  | [optional] [default to 1]
 **limit** | **Int** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfEcfReceptionRequestDto**](PaginatedApiResultOfEcfReceptionRequestDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

