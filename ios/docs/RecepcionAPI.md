# RecepcionAPI

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEcfReceptionRequest**](RecepcionAPI.md#getecfreceptionrequest) | **GET** /recepcion/{messageId} | 
[**getEcfReceptorByMessageId**](RecepcionAPI.md#getecfreceptorbymessageid) | **GET** /recepcion/{rnc}/{messageId} | 
[**searchEcfReceptionRequests**](RecepcionAPI.md#searchecfreceptionrequests) | **GET** /recepcion | 
[**searchEcfReceptionRequestsByRnc**](RecepcionAPI.md#searchecfreceptionrequestsbyrnc) | **GET** /recepcion/{rnc} | 
[**sendAprobacionComercial**](RecepcionAPI.md#sendaprobacioncomercial) | **POST** /recepcion/{messageId}/acecf | 


# **getEcfReceptionRequest**
```swift
    open class func getEcfReceptionRequest(messageId: UUID, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let messageId = 987 // UUID | 

RecepcionAPI.getEcfReceptionRequest(messageId: messageId) { (response, error) in
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

# **getEcfReceptorByMessageId**
```swift
    open class func getEcfReceptorByMessageId(rnc: String, messageId: UUID, completion: @escaping (_ data: EcfReceptorDto?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let messageId = 987 // UUID | 

RecepcionAPI.getEcfReceptorByMessageId(rnc: rnc, messageId: messageId) { (response, error) in
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

[**EcfReceptorDto**](EcfReceptorDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchEcfReceptionRequests**
```swift
    open class func searchEcfReceptionRequests(messageIds: [UUID]? = nil, encfs: [String]? = nil, rncs: [String]? = nil, rncEmisors: [String]? = nil, tiposEcfs: [SearchEcfReceptionRequestsTiposEcfsParameterInner]? = nil, progresses: [SearchEcfReceptionRequestsTiposEcfsParameterInner]? = nil, fromDate: String? = nil, toDate: String? = nil, amountFrom: SearchEcfsAmountFromParameter? = nil, amountTo: SearchEcfsAmountFromParameter? = nil, page: GetCompaniesPageParameter? = nil, limit: GetCompaniesLimitParameter? = nil, completion: @escaping (_ data: PaginatedApiResultOfEcfReceptionRequestDto?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let messageIds = [123] // [UUID] |  (optional)
let encfs = ["inner_example"] // [String] |  (optional)
let rncs = ["inner_example"] // [String] |  (optional)
let rncEmisors = ["inner_example"] // [String] |  (optional)
let tiposEcfs = [SearchEcfReceptionRequests_TiposEcfs_parameter_inner()] // [SearchEcfReceptionRequestsTiposEcfsParameterInner] |  (optional)
let progresses = [SearchEcfReceptionRequests_TiposEcfs_parameter_inner()] // [SearchEcfReceptionRequestsTiposEcfsParameterInner] |  (optional)
let fromDate = "fromDate_example" // String |  (optional)
let toDate = "toDate_example" // String |  (optional)
let amountFrom = SearchEcfs_AmountFrom_parameter() // SearchEcfsAmountFromParameter |  (optional)
let amountTo = SearchEcfs_AmountFrom_parameter() // SearchEcfsAmountFromParameter |  (optional)
let page = GetCompanies_Page_parameter() // GetCompaniesPageParameter |  (optional) (default to 1)
let limit = GetCompanies_Limit_parameter() // GetCompaniesLimitParameter |  (optional) (default to 25)

RecepcionAPI.searchEcfReceptionRequests(messageIds: messageIds, encfs: encfs, rncs: rncs, rncEmisors: rncEmisors, tiposEcfs: tiposEcfs, progresses: progresses, fromDate: fromDate, toDate: toDate, amountFrom: amountFrom, amountTo: amountTo, page: page, limit: limit) { (response, error) in
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
 **rncEmisors** | [**[String]**](String.md) |  | [optional] 
 **tiposEcfs** | [**[SearchEcfReceptionRequestsTiposEcfsParameterInner]**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md) |  | [optional] 
 **progresses** | [**[SearchEcfReceptionRequestsTiposEcfsParameterInner]**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md) |  | [optional] 
 **fromDate** | **String** |  | [optional] 
 **toDate** | **String** |  | [optional] 
 **amountFrom** | **SearchEcfsAmountFromParameter** |  | [optional] 
 **amountTo** | **SearchEcfsAmountFromParameter** |  | [optional] 
 **page** | **GetCompaniesPageParameter** |  | [optional] [default to 1]
 **limit** | **GetCompaniesLimitParameter** |  | [optional] [default to 25]

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
    open class func searchEcfReceptionRequestsByRnc(rnc: String, messageIds: [UUID]? = nil, encfs: [String]? = nil, rncEmisors: [String]? = nil, tiposEcfs: [SearchEcfReceptionRequestsTiposEcfsParameterInner]? = nil, progresses: [SearchEcfReceptionRequestsTiposEcfsParameterInner]? = nil, fromDate: String? = nil, toDate: String? = nil, amountFrom: SearchEcfsAmountFromParameter? = nil, amountTo: SearchEcfsAmountFromParameter? = nil, page: GetCompaniesPageParameter? = nil, limit: GetCompaniesLimitParameter? = nil, completion: @escaping (_ data: PaginatedApiResultOfEcfReceptionRequestDto?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let messageIds = [123] // [UUID] |  (optional)
let encfs = ["inner_example"] // [String] |  (optional)
let rncEmisors = ["inner_example"] // [String] |  (optional)
let tiposEcfs = [SearchEcfReceptionRequests_TiposEcfs_parameter_inner()] // [SearchEcfReceptionRequestsTiposEcfsParameterInner] |  (optional)
let progresses = [SearchEcfReceptionRequests_TiposEcfs_parameter_inner()] // [SearchEcfReceptionRequestsTiposEcfsParameterInner] |  (optional)
let fromDate = "fromDate_example" // String |  (optional)
let toDate = "toDate_example" // String |  (optional)
let amountFrom = SearchEcfs_AmountFrom_parameter() // SearchEcfsAmountFromParameter |  (optional)
let amountTo = SearchEcfs_AmountFrom_parameter() // SearchEcfsAmountFromParameter |  (optional)
let page = GetCompanies_Page_parameter() // GetCompaniesPageParameter |  (optional) (default to 1)
let limit = GetCompanies_Limit_parameter() // GetCompaniesLimitParameter |  (optional) (default to 25)

RecepcionAPI.searchEcfReceptionRequestsByRnc(rnc: rnc, messageIds: messageIds, encfs: encfs, rncEmisors: rncEmisors, tiposEcfs: tiposEcfs, progresses: progresses, fromDate: fromDate, toDate: toDate, amountFrom: amountFrom, amountTo: amountTo, page: page, limit: limit) { (response, error) in
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
 **rncEmisors** | [**[String]**](String.md) |  | [optional] 
 **tiposEcfs** | [**[SearchEcfReceptionRequestsTiposEcfsParameterInner]**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md) |  | [optional] 
 **progresses** | [**[SearchEcfReceptionRequestsTiposEcfsParameterInner]**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md) |  | [optional] 
 **fromDate** | **String** |  | [optional] 
 **toDate** | **String** |  | [optional] 
 **amountFrom** | **SearchEcfsAmountFromParameter** |  | [optional] 
 **amountTo** | **SearchEcfsAmountFromParameter** |  | [optional] 
 **page** | **GetCompaniesPageParameter** |  | [optional] [default to 1]
 **limit** | **GetCompaniesLimitParameter** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfEcfReceptionRequestDto**](PaginatedApiResultOfEcfReceptionRequestDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sendAprobacionComercial**
```swift
    open class func sendAprobacionComercial(messageId: UUID, sendAcecfRequest: SendAcecfRequest, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let messageId = 987 // UUID | 
let sendAcecfRequest = SendAcecfRequest(detalleMotivoRechazo: "detalleMotivoRechazo_example", estadoType: EstadoType()) // SendAcecfRequest | 

RecepcionAPI.sendAprobacionComercial(messageId: messageId, sendAcecfRequest: sendAcecfRequest) { (response, error) in
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
 **sendAcecfRequest** | [**SendAcecfRequest**](SendAcecfRequest.md) |  | 

### Return type

Void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

