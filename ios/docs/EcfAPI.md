# EcfAPI

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anulacionRangos**](EcfAPI.md#anulacionrangos) | **POST** /ecf/anularrango/{rnc} | 
[**aprobacionComercial**](EcfAPI.md#aprobacioncomercial) | **POST** /ecf/aprobacioncomercial/{rnc}/{encf} | 
[**firmarSemilla**](EcfAPI.md#firmarsemilla) | **POST** /ecf/FirmarSemilla/{rnc} | 
[**getEcfById**](EcfAPI.md#getecfbyid) | **GET** /ecf/{rnc}/message/{id} | 
[**listAnulaciones**](EcfAPI.md#listanulaciones) | **GET** /ecf/anulaciones | 
[**queryEcf**](EcfAPI.md#queryecf) | **GET** /ecf/{rnc}/{encf} | 
[**recepcionEcf31**](EcfAPI.md#recepcionecf31) | **POST** /ecf/31 | 
[**recepcionEcf32**](EcfAPI.md#recepcionecf32) | **POST** /ecf/32 | 
[**recepcionEcf33**](EcfAPI.md#recepcionecf33) | **POST** /ecf/33 | 
[**recepcionEcf34**](EcfAPI.md#recepcionecf34) | **POST** /ecf/34 | 
[**recepcionEcf41**](EcfAPI.md#recepcionecf41) | **POST** /ecf/41 | 
[**recepcionEcf43**](EcfAPI.md#recepcionecf43) | **POST** /ecf/43 | 
[**recepcionEcf44**](EcfAPI.md#recepcionecf44) | **POST** /ecf/44 | 
[**recepcionEcf45**](EcfAPI.md#recepcionecf45) | **POST** /ecf/45 | 
[**recepcionEcf46**](EcfAPI.md#recepcionecf46) | **POST** /ecf/46 | 
[**recepcionEcf47**](EcfAPI.md#recepcionecf47) | **POST** /ecf/47 | 
[**searchAllEcfs**](EcfAPI.md#searchallecfs) | **GET** /ecf | 
[**searchEcfs**](EcfAPI.md#searchecfs) | **GET** /ecf/{rnc} | 


# **anulacionRangos**
```swift
    open class func anulacionRangos(rnc: String, anulacionRequest: AnulacionRequest, completion: @escaping (_ data: RespuestaAnulacionRango?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let anulacionRequest = AnulacionRequest(cantidaDeNcfAnulados: 123, detalleAnulacion: [DetalleAnulacionRequest(tipoEcf: ECFType(), cantidadeNcfAnulados: 123, noLinea: [123], secuencias: [SecuenciaRequest(desdeEncf: "desdeEncf_example", hastaEncf: "hastaEncf_example")])]) // AnulacionRequest | 

EcfAPI.anulacionRangos(rnc: rnc, anulacionRequest: anulacionRequest) { (response, error) in
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
 **anulacionRequest** | [**AnulacionRequest**](AnulacionRequest.md) |  | 

### Return type

[**RespuestaAnulacionRango**](RespuestaAnulacionRango.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/xml, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aprobacionComercial**
```swift
    open class func aprobacionComercial(rnc: String, encf: String, sendAcecfRequest: SendAcecfRequest, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let encf = "encf_example" // String | 
let sendAcecfRequest = SendAcecfRequest(detalleMotivoRechazo: "detalleMotivoRechazo_example", estadoType: EstadoType()) // SendAcecfRequest | 

EcfAPI.aprobacionComercial(rnc: rnc, encf: encf, sendAcecfRequest: sendAcecfRequest) { (response, error) in
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
 **encf** | **String** |  | 
 **sendAcecfRequest** | [**SendAcecfRequest**](SendAcecfRequest.md) |  | 

### Return type

Void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmarSemilla**
```swift
    open class func firmarSemilla(rnc: String, xml: Data, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let xml = Data([9, 8, 7]) // Data | 

EcfAPI.firmarSemilla(rnc: rnc, xml: xml) { (response, error) in
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
 **xml** | **Data** |  | 

### Return type

Void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getEcfById**
```swift
    open class func getEcfById(rnc: String, id: UUID, includeEcfContent: Bool? = nil, completion: @escaping (_ data: [EcfResponse]?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let id = 987 // UUID | 
let includeEcfContent = true // Bool |  (optional) (default to false)

EcfAPI.getEcfById(rnc: rnc, id: id, includeEcfContent: includeEcfContent) { (response, error) in
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
 **id** | **UUID** |  | 
 **includeEcfContent** | **Bool** |  | [optional] [default to false]

### Return type

[**[EcfResponse]**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listAnulaciones**
```swift
    open class func listAnulaciones(tipoEcf: [ECFType]? = nil, rncs: [String]? = nil, fechaDesde: Date? = nil, fechaHasta: Date? = nil, page: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: PaginatedApiResultOfAnulacionListResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let tipoEcf = [ECFType()] // [ECFType] |  (optional)
let rncs = ["inner_example"] // [String] |  (optional)
let fechaDesde = Date() // Date |  (optional)
let fechaHasta = Date() // Date |  (optional)
let page = 987 // Int |  (optional) (default to 1)
let limit = 987 // Int |  (optional) (default to 25)

EcfAPI.listAnulaciones(tipoEcf: tipoEcf, rncs: rncs, fechaDesde: fechaDesde, fechaHasta: fechaHasta, page: page, limit: limit) { (response, error) in
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
 **tipoEcf** | [**[ECFType]**](ECFType.md) |  | [optional] 
 **rncs** | [**[String]**](String.md) |  | [optional] 
 **fechaDesde** | **Date** |  | [optional] 
 **fechaHasta** | **Date** |  | [optional] 
 **page** | **Int** |  | [optional] [default to 1]
 **limit** | **Int** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfAnulacionListResponse**](PaginatedApiResultOfAnulacionListResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queryEcf**
```swift
    open class func queryEcf(rnc: String, encf: String, includeEcfContent: Bool? = nil, completion: @escaping (_ data: [EcfResponse]?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let encf = "encf_example" // String | 
let includeEcfContent = true // Bool |  (optional) (default to false)

EcfAPI.queryEcf(rnc: rnc, encf: encf, includeEcfContent: includeEcfContent) { (response, error) in
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
 **encf** | **String** |  | 
 **includeEcfContent** | **Bool** |  | [optional] [default to false]

### Return type

[**[EcfResponse]**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf31**
```swift
    open class func recepcionEcf31(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf31(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf32**
```swift
    open class func recepcionEcf32(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf32(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf33**
```swift
    open class func recepcionEcf33(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf33(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf34**
```swift
    open class func recepcionEcf34(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf34(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf41**
```swift
    open class func recepcionEcf41(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf41(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf43**
```swift
    open class func recepcionEcf43(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf43(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf44**
```swift
    open class func recepcionEcf44(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf44(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf45**
```swift
    open class func recepcionEcf45(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf45(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf46**
```swift
    open class func recepcionEcf46(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf46(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recepcionEcf47**
```swift
    open class func recepcionEcf47(ECF: ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ECF = ECF(encabezado: Encabezado(version: VersionType(), idDoc: IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [FormaDePago(formaPago: FormaPagoType(), montoPago: 123)], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: 123), emisor: Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Transporte(paisDestino: "paisDestino_example"), totales: Totales(montoExento: 123, montoTotal: 123, montoPeriodo: 123, saldoAnterior: 123, montoAvancePago: 123, valorPagar: 123, totalISRRetencion: 123), otraMoneda: OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: 123, montoExentoOtraMoneda: 123, montoTotalOtraMoneda: 123)), detallesItems: [Item(numeroLinea: 123, tablaCodigosItem: [CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: IndicadorFacturacionType(), retencion: Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: 123), nombreItem: "nombreItem_example", indicadorBienoServicio: IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: 123, unidadMedida: UnidadMedidaType(), precioUnitarioItem: 123, otraMonedaDetalle: OtraMonedaDetalle(precioOtraMoneda: 123, descuentoOtraMoneda: 123, recargoOtraMoneda: 123, montoItemOtraMoneda: 123), montoItem: 123)], subtotales: [Subtotal(numeroSubTotal: 123, descripcionSubtotal: "descripcionSubtotal_example", orden: 123, subTotalExento: 123, montoSubTotal: 123, lineas: 123)], paginacion: [Pagina(paginaNo: 123, noLineaDesde: 123, noLineaHasta: 123, subtotalExentoPagina: 123, montoSubtotalPagina: 123)], informacionReferencia: InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // ECF | 

EcfAPI.recepcionEcf47(ECF: ECF) { (response, error) in
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
 **ECF** | [**ECF**](ECF.md) |  | 

### Return type

[**EcfResponse**](EcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchAllEcfs**
```swift
    open class func searchAllEcfs(encfs: [String]? = nil, ids: [UUID]? = nil, tiposEcfs: [AllTipoECFTypes]? = nil, includeEcfContent: Bool? = nil, fromFechaEmision: Date? = nil, toFechaEmision: Date? = nil, amountFrom: Double? = nil, amountTo: Double? = nil, page: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: PaginatedApiResultOfEcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let encfs = ["inner_example"] // [String] |  (optional)
let ids = [123] // [UUID] |  (optional)
let tiposEcfs = [AllTipoECFTypes()] // [AllTipoECFTypes] |  (optional)
let includeEcfContent = true // Bool |  (optional) (default to false)
let fromFechaEmision = Date() // Date |  (optional)
let toFechaEmision = Date() // Date |  (optional)
let amountFrom = 987 // Double |  (optional)
let amountTo = 987 // Double |  (optional)
let page = 987 // Int |  (optional) (default to 1)
let limit = 987 // Int |  (optional) (default to 25)

EcfAPI.searchAllEcfs(encfs: encfs, ids: ids, tiposEcfs: tiposEcfs, includeEcfContent: includeEcfContent, fromFechaEmision: fromFechaEmision, toFechaEmision: toFechaEmision, amountFrom: amountFrom, amountTo: amountTo, page: page, limit: limit) { (response, error) in
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
 **encfs** | [**[String]**](String.md) |  | [optional] 
 **ids** | [**[UUID]**](UUID.md) |  | [optional] 
 **tiposEcfs** | [**[AllTipoECFTypes]**](AllTipoECFTypes.md) |  | [optional] 
 **includeEcfContent** | **Bool** |  | [optional] [default to false]
 **fromFechaEmision** | **Date** |  | [optional] 
 **toFechaEmision** | **Date** |  | [optional] 
 **amountFrom** | **Double** |  | [optional] 
 **amountTo** | **Double** |  | [optional] 
 **page** | **Int** |  | [optional] [default to 1]
 **limit** | **Int** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfEcfResponse**](PaginatedApiResultOfEcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **searchEcfs**
```swift
    open class func searchEcfs(rnc: String, encfs: [String]? = nil, ids: [UUID]? = nil, tiposEcfs: [AllTipoECFTypes]? = nil, includeEcfContent: Bool? = nil, fromFechaEmision: Date? = nil, toFechaEmision: Date? = nil, amountFrom: Double? = nil, amountTo: Double? = nil, page: Int? = nil, limit: Int? = nil, completion: @escaping (_ data: PaginatedApiResultOfEcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let encfs = ["inner_example"] // [String] |  (optional)
let ids = [123] // [UUID] |  (optional)
let tiposEcfs = [AllTipoECFTypes()] // [AllTipoECFTypes] |  (optional)
let includeEcfContent = true // Bool |  (optional) (default to false)
let fromFechaEmision = Date() // Date |  (optional)
let toFechaEmision = Date() // Date |  (optional)
let amountFrom = 987 // Double |  (optional)
let amountTo = 987 // Double |  (optional)
let page = 987 // Int |  (optional) (default to 1)
let limit = 987 // Int |  (optional) (default to 25)

EcfAPI.searchEcfs(rnc: rnc, encfs: encfs, ids: ids, tiposEcfs: tiposEcfs, includeEcfContent: includeEcfContent, fromFechaEmision: fromFechaEmision, toFechaEmision: toFechaEmision, amountFrom: amountFrom, amountTo: amountTo, page: page, limit: limit) { (response, error) in
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
 **encfs** | [**[String]**](String.md) |  | [optional] 
 **ids** | [**[UUID]**](UUID.md) |  | [optional] 
 **tiposEcfs** | [**[AllTipoECFTypes]**](AllTipoECFTypes.md) |  | [optional] 
 **includeEcfContent** | **Bool** |  | [optional] [default to false]
 **fromFechaEmision** | **Date** |  | [optional] 
 **toFechaEmision** | **Date** |  | [optional] 
 **amountFrom** | **Double** |  | [optional] 
 **amountTo** | **Double** |  | [optional] 
 **page** | **Int** |  | [optional] [default to 1]
 **limit** | **Int** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfEcfResponse**](PaginatedApiResultOfEcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

