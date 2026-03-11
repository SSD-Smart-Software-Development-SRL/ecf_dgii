# ApiKeyAPI

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newCompanyApiKey**](ApiKeyAPI.md#newcompanyapikey) | **POST** /apiKey | 


# **newCompanyApiKey**
```swift
    open class func newCompanyApiKey(newCompanyApiKey: NewCompanyApiKey, completion: @escaping (_ data: Token?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let newCompanyApiKey = NewCompanyApiKey(rnc: "rnc_example") // NewCompanyApiKey | 

ApiKeyAPI.newCompanyApiKey(newCompanyApiKey: newCompanyApiKey) { (response, error) in
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
 **newCompanyApiKey** | [**NewCompanyApiKey**](NewCompanyApiKey.md) |  | 

### Return type

[**Token**](Token.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

