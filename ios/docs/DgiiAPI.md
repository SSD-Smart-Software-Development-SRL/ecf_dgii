# DgiiAPI

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consultaDirectorioListado**](DgiiAPI.md#consultadirectoriolistado) | **GET** /dgii/{rnc}/consultadirectorio/listado | 
[**consultaDirectorioObtenerDirectorioPorRnc**](DgiiAPI.md#consultadirectorioobtenerdirectorioporrnc) | **GET** /dgii/{rnc}/consultadirectorio/obtener-directorio-por-rnc | 
[**consultaEstado**](DgiiAPI.md#consultaestado) | **GET** /dgii/{rnc}/consultaestado/estado | 
[**consultaRFCE**](DgiiAPI.md#consultarfce) | **GET** /dgii/{rnc}/consultarfce/consulta | 
[**consultaResultado**](DgiiAPI.md#consultaresultado) | **GET** /dgii/{rnc}/consultaresultado/estado | 
[**consultaTimbre**](DgiiAPI.md#consultatimbre) | **GET** /dgii/{rnc}/consultatimbre | 
[**consultaTimbreFC**](DgiiAPI.md#consultatimbrefc) | **GET** /dgii/{rnc}/consultatimbrefc | 
[**consultaTrackId**](DgiiAPI.md#consultatrackid) | **GET** /dgii/{rnc}/consultatrackids/consulta | 
[**estatusServiciosObtenerEstatus**](DgiiAPI.md#estatusserviciosobtenerestatus) | **GET** /dgii/{rnc}/estatusservicios/obtener-estatus | 
[**estatusServiciosObtenerVentanasMantenimiento**](DgiiAPI.md#estatusserviciosobtenerventanasmantenimiento) | **GET** /dgii/{rnc}/estatusservicios/obtener-ventanas-mantenimiento | 


# **consultaDirectorioListado**
```swift
    open class func consultaDirectorioListado(rnc: String, completion: @escaping (_ data: [Directorio]?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 

DgiiAPI.consultaDirectorioListado(rnc: rnc) { (response, error) in
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

[**[Directorio]**](Directorio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultaDirectorioObtenerDirectorioPorRnc**
```swift
    open class func consultaDirectorioObtenerDirectorioPorRnc(rnc: String, RNC: String, completion: @escaping (_ data: Directorio?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let RNC = "RNC_example" // String | 

DgiiAPI.consultaDirectorioObtenerDirectorioPorRnc(rnc: rnc, RNC: RNC) { (response, error) in
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
 **RNC** | **String** |  | 

### Return type

[**Directorio**](Directorio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultaEstado**
```swift
    open class func consultaEstado(rnc: String, rncEmisor: String, ncfElectronico: String, rncComprador: String, codigoSeguridad: String, completion: @escaping (_ data: RespuestaConsultaEstado?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let rncEmisor = "rncEmisor_example" // String | 
let ncfElectronico = "ncfElectronico_example" // String | 
let rncComprador = "rncComprador_example" // String | 
let codigoSeguridad = "codigoSeguridad_example" // String | 

DgiiAPI.consultaEstado(rnc: rnc, rncEmisor: rncEmisor, ncfElectronico: ncfElectronico, rncComprador: rncComprador, codigoSeguridad: codigoSeguridad) { (response, error) in
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
 **rncEmisor** | **String** |  | 
 **ncfElectronico** | **String** |  | 
 **rncComprador** | **String** |  | 
 **codigoSeguridad** | **String** |  | 

### Return type

[**RespuestaConsultaEstado**](RespuestaConsultaEstado.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultaRFCE**
```swift
    open class func consultaRFCE(rnc: String, rNCEmisor: String, ENCF: String, codSeguridadECF: String, completion: @escaping (_ data: RespuestaConsultaRFCE?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let rNCEmisor = "rNCEmisor_example" // String | 
let ENCF = "ENCF_example" // String | 
let codSeguridadECF = "codSeguridadECF_example" // String | 

DgiiAPI.consultaRFCE(rnc: rnc, rNCEmisor: rNCEmisor, ENCF: ENCF, codSeguridadECF: codSeguridadECF) { (response, error) in
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
 **rNCEmisor** | **String** |  | 
 **ENCF** | **String** |  | 
 **codSeguridadECF** | **String** |  | 

### Return type

[**RespuestaConsultaRFCE**](RespuestaConsultaRFCE.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultaResultado**
```swift
    open class func consultaResultado(rnc: String, trackId: String, completion: @escaping (_ data: RespuestaConsultaTrackId?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let trackId = "trackId_example" // String | 

DgiiAPI.consultaResultado(rnc: rnc, trackId: trackId) { (response, error) in
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
 **trackId** | **String** |  | 

### Return type

[**RespuestaConsultaTrackId**](RespuestaConsultaTrackId.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultaTimbre**
```swift
    open class func consultaTimbre(rnc: String, rncemisor: String, encf: String, montototal: String, codigoseguridad: String, completion: @escaping (_ data: RespuestaConsultaTimbre?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let rncemisor = "rncemisor_example" // String | 
let encf = "encf_example" // String | 
let montototal = "montototal_example" // String | 
let codigoseguridad = "codigoseguridad_example" // String | 

DgiiAPI.consultaTimbre(rnc: rnc, rncemisor: rncemisor, encf: encf, montototal: montototal, codigoseguridad: codigoseguridad) { (response, error) in
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
 **rncemisor** | **String** |  | 
 **encf** | **String** |  | 
 **montototal** | **String** |  | 
 **codigoseguridad** | **String** |  | 

### Return type

[**RespuestaConsultaTimbre**](RespuestaConsultaTimbre.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultaTimbreFC**
```swift
    open class func consultaTimbreFC(rnc: String, rncemisor: String, encf: String, montototal: String, codigoseguridad: String, completion: @escaping (_ data: RespuestaConsultaTimbre?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let rncemisor = "rncemisor_example" // String | 
let encf = "encf_example" // String | 
let montototal = "montototal_example" // String | 
let codigoseguridad = "codigoseguridad_example" // String | 

DgiiAPI.consultaTimbreFC(rnc: rnc, rncemisor: rncemisor, encf: encf, montototal: montototal, codigoseguridad: codigoseguridad) { (response, error) in
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
 **rncemisor** | **String** |  | 
 **encf** | **String** |  | 
 **montototal** | **String** |  | 
 **codigoseguridad** | **String** |  | 

### Return type

[**RespuestaConsultaTimbre**](RespuestaConsultaTimbre.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consultaTrackId**
```swift
    open class func consultaTrackId(rnc: String, rncEmisor: String, encf: String, completion: @escaping (_ data: RespuestaConsultaTrackId?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let rncEmisor = "rncEmisor_example" // String | 
let encf = "encf_example" // String | 

DgiiAPI.consultaTrackId(rnc: rnc, rncEmisor: rncEmisor, encf: encf) { (response, error) in
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
 **rncEmisor** | **String** |  | 
 **encf** | **String** |  | 

### Return type

[**RespuestaConsultaTrackId**](RespuestaConsultaTrackId.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estatusServiciosObtenerEstatus**
```swift
    open class func estatusServiciosObtenerEstatus(rnc: String, completion: @escaping (_ data: [RespuestaEstatusServicio]?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 

DgiiAPI.estatusServiciosObtenerEstatus(rnc: rnc) { (response, error) in
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

[**[RespuestaEstatusServicio]**](RespuestaEstatusServicio.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estatusServiciosObtenerVentanasMantenimiento**
```swift
    open class func estatusServiciosObtenerVentanasMantenimiento(rnc: String, completion: @escaping (_ data: RespuestaVentanaDeMantenimiento?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 

DgiiAPI.estatusServiciosObtenerVentanasMantenimiento(rnc: rnc) { (response, error) in
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

[**RespuestaVentanaDeMantenimiento**](RespuestaVentanaDeMantenimiento.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

