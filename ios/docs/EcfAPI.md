# EcfAPI

All URIs are relative to *https://api.test.ecfx.ssd.com.do*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anulacionRangos**](EcfAPI.md#anulacionrangos) | **POST** /ecf/anularrango/{rnc} | 
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
let anulacionRequest = AnulacionRequest(cantidaDeNcfAnulados: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), detalleAnulacion: [DetalleAnulacionRequest(tipoEcf: ECFType(), cantidadeNcfAnulados: nil, noLinea: [nil], secuencias: [SecuenciaRequest(desdeEncf: "desdeEncf_example", hastaEncf: "hastaEncf_example")])]) // AnulacionRequest | 

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

# **firmarSemilla**
```swift
    open class func firmarSemilla(rnc: String, xml: URL, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let rnc = "rnc_example" // String | 
let xml = URL(string: "https://example.com")! // URL | 

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
 **xml** | **URL** |  | 

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
    open class func listAnulaciones(tipoEcf: [ECFType]? = nil, rncs: [String]? = nil, fechaDesde: Date? = nil, fechaHasta: Date? = nil, page: GetCompaniesPageParameter? = nil, limit: GetCompaniesLimitParameter? = nil, completion: @escaping (_ data: PaginatedApiResultOfAnulacionListResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let tipoEcf = [ECFType()] // [ECFType] |  (optional)
let rncs = ["inner_example"] // [String] |  (optional)
let fechaDesde = Date() // Date |  (optional)
let fechaHasta = Date() // Date |  (optional)
let page = GetCompanies_Page_parameter() // GetCompaniesPageParameter |  (optional) (default to 1)
let limit = GetCompanies_Limit_parameter() // GetCompaniesLimitParameter |  (optional) (default to 25)

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
 **page** | **GetCompaniesPageParameter** |  | [optional] [default to 1]
 **limit** | **GetCompaniesLimitParameter** |  | [optional] [default to 25]

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
    open class func recepcionEcf31(ecf31ECF: Ecf31ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf31ECF = Ecf31ECF(encabezado: Ecf31Encabezado(version: Ecf31VersionType(), idDoc: Ecf31IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), indicadorEnvioDiferido: IndicadorEnvioDiferidoType(), indicadorMontoGravado: IndicadorMontoGravadoType(), indicadorServicioTodoIncluido: IndicadorServicioTodoIncluidoType(), tipoIngresos: Ecf31TipoIngresosValidationType(), tipoPago: Ecf31TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [Ecf31FormaDePago(formaPago: Ecf31FormaPagoType(), montoPago: Ecf31FormaDePago_montoPago())], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf31Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", codigoVendedor: "codigoVendedor_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", zonaVenta: "zonaVenta_example", rutaVenta: "rutaVenta_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf31Comprador(rncComprador: "rncComprador_example", razonSocialComprador: "razonSocialComprador_example", contactoComprador: "contactoComprador_example", correoComprador: "correoComprador_example", direccionComprador: "direccionComprador_example", municipioComprador: nil, provinciaComprador: nil, fechaEntrega: Date(), contactoEntrega: "contactoEntrega_example", direccionEntrega: "direccionEntrega_example", telefonoAdicional: "telefonoAdicional_example", fechaOrdenCompra: Date(), numeroOrdenCompra: "numeroOrdenCompra_example", codigoInternoComprador: "codigoInternoComprador_example", responsablePago: "responsablePago_example", informacionAdicionalComprador: "informacionAdicionalComprador_example"), informacionesAdicionales: Ecf31InformacionesAdicionales(fechaEmbarque: Date(), numeroEmbarque: "numeroEmbarque_example", numeroContenedor: "numeroContenedor_example", numeroReferencia: "numeroReferencia_example", pesoBruto: Ecf31DescuentoORecargo_montoDescuentooRecargo(), pesoNeto: nil, unidadPesoBruto: UnidadMedidaType(), unidadPesoNeto: nil, cantidadBulto: nil, unidadBulto: nil, volumenBulto: Ecf31ImpuestoAdicional2_montoImpuestoSelectivoConsumoEspecifico(), unidadVolumen: nil), transporte: Ecf31Transporte(conductor: "conductor_example", documentoTransporte: "documentoTransporte_example", ficha: "ficha_example", placa: "placa_example", rutaTransporte: "rutaTransporte_example", zonaTransporte: "zonaTransporte_example", numeroAlbaran: "numeroAlbaran_example"), totales: Ecf31Totales(montoGravadoTotal: nil, montoGravadoI1: nil, montoGravadoI2: nil, montoGravadoI3: nil, montoExento: nil, itbiS1: nil, itbiS2: nil, itbiS3: nil, totalITBIS: nil, totalITBIS1: nil, totalITBIS2: nil, totalITBIS3: nil, montoImpuestoAdicional: nil, impuestosAdicionales: [Ecf31ImpuestoAdicional2(tipoImpuesto: Ecf31CodificacionTipoImpuestosType(), tasaImpuestoAdicional: Ecf31ImpuestoAdicional2_tasaImpuestoAdicional(), montoImpuestoSelectivoConsumoEspecifico: nil, montoImpuestoSelectivoConsumoAdvalorem: nil, otrosImpuestosAdicionales: nil)], montoTotal: nil, montoNoFacturable: Ecf31Totales_montoNoFacturable(), montoPeriodo: nil, saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil, totalITBISRetenido: nil, totalISRRetencion: nil, totalITBISPercepcion: nil, totalISRPercepcion: nil), otraMoneda: Ecf31OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoGravadoTotalOtraMoneda: nil, montoGravado1OtraMoneda: nil, montoGravado2OtraMoneda: nil, montoGravado3OtraMoneda: nil, montoExentoOtraMoneda: nil, totalITBISOtraMoneda: nil, totalITBIS1OtraMoneda: nil, totalITBIS2OtraMoneda: nil, totalITBIS3OtraMoneda: nil, montoImpuestoAdicionalOtraMoneda: nil, impuestosAdicionalesOtraMoneda: [Ecf31ImpuestoAdicionalOtraMoneda(tipoImpuestoOtraMoneda: nil, tasaImpuestoAdicionalOtraMoneda: nil, montoImpuestoSelectivoConsumoEspecificoOtraMoneda: nil, montoImpuestoSelectivoConsumoAdvaloremOtraMoneda: nil, otrosImpuestosAdicionalesOtraMoneda: nil)], montoTotalOtraMoneda: nil)), detallesItems: [Ecf31Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf31CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf31IndicadorFacturacionType(), retencion: Ecf31Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoITBISRetenido: nil, montoISRRetenido: nil), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf31IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: nil, cantidadReferencia: nil, unidadReferencia: nil, tablaSubcantidad: [Ecf31SubcantidadItem(subcantidad: Ecf31OtraMonedaDetalle_precioOtraMoneda(), codigoSubcantidad: nil)], gradosAlcohol: Ecf31DescuentoORecargo_valorDescuentooRecargo(), precioUnitarioReferencia: nil, fechaElaboracion: Date(), fechaVencimientoItem: Date(), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), descuentoMonto: nil, tablaSubDescuento: [Ecf31SubDescuento(tipoSubDescuento: Ecf31TipoDescuentoRecargoType(), subDescuentoPorcentaje: nil, montoSubDescuento: nil)], recargoMonto: nil, tablaSubRecargo: [Ecf31SubRecargo(tipoSubRecargo: nil, subRecargoPorcentaje: nil, montoSubRecargo: nil)], tablaImpuestoAdicional: [Ecf31ImpuestoAdicional(tipoImpuesto: nil)], otraMonedaDetalle: Ecf31OtraMonedaDetalle(precioOtraMoneda: nil, descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf31Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalMontoGravadoTotal: nil, subTotalMontoGravadoI1: nil, subTotalMontoGravadoI2: nil, subTotalMontoGravadoI3: nil, subTotaITBIS: nil, subTotaITBIS1: nil, subTotaITBIS2: nil, subTotaITBIS3: nil, subTotalImpuestoAdicional: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], descuentosORecargos: [Ecf31DescuentoORecargo(numeroLinea: nil, tipoAjuste: Ecf31TipoAjusteType(), indicadorNorma1007: IndicadorNorma1007Type(), descripcionDescuentooRecargo: "descripcionDescuentooRecargo_example", tipoValor: TipoDescuentoRecargoType(), valorDescuentooRecargo: nil, montoDescuentooRecargo: nil, montoDescuentooRecargoOtraMoneda: nil, indicadorFacturacionDescuentooRecargo: IndicadorFacturacionDRType())], paginacion: [Ecf31Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalMontoGravadoPagina: nil, subtotalMontoGravado1Pagina: nil, subtotalMontoGravado2Pagina: nil, subtotalMontoGravado3Pagina: nil, subtotalExentoPagina: nil, subtotalItbisPagina: nil, subtotalItbis1Pagina: nil, subtotalItbis2Pagina: nil, subtotalItbis3Pagina: nil, subtotalImpuestoAdicionalPagina: nil, subtotalImpuestoAdicional: Ecf31SubtotalImpuestoAdicional(subtotalImpuestoSelectivoConsumoEspecificoPagina: nil, subtotalOtrosImpuesto: nil), montoSubtotalPagina: nil, subtotalMontoNoFacturablePagina: nil)], informacionReferencia: Ecf31InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // Ecf31ECF | 

EcfAPI.recepcionEcf31(ecf31ECF: ecf31ECF) { (response, error) in
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
 **ecf31ECF** | [**Ecf31ECF**](Ecf31ECF.md) |  | 

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
    open class func recepcionEcf32(ecf32ECF: Ecf32ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf32ECF = Ecf32ECF(encabezado: Ecf32Encabezado(version: Ecf32VersionType(), idDoc: Ecf32IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", indicadorEnvioDiferido: IndicadorEnvioDiferidoType(), indicadorMontoGravado: IndicadorMontoGravadoType(), indicadorServicioTodoIncluido: IndicadorServicioTodoIncluidoType(), tipoIngresos: Ecf32TipoIngresosValidationType(), tipoPago: Ecf32TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [Ecf32FormaDePago(formaPago: Ecf32FormaPagoType(), montoPago: Ecf31FormaDePago_montoPago())], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf32Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", codigoVendedor: "codigoVendedor_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", zonaVenta: "zonaVenta_example", rutaVenta: "rutaVenta_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf32Comprador(rncComprador: "rncComprador_example", identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example", contactoComprador: "contactoComprador_example", correoComprador: "correoComprador_example", direccionComprador: "direccionComprador_example", municipioComprador: nil, provinciaComprador: nil, fechaEntrega: Date(), contactoEntrega: "contactoEntrega_example", direccionEntrega: "direccionEntrega_example", telefonoAdicional: "telefonoAdicional_example", fechaOrdenCompra: Date(), numeroOrdenCompra: "numeroOrdenCompra_example", codigoInternoComprador: "codigoInternoComprador_example", responsablePago: "responsablePago_example", informacionAdicionalComprador: "informacionAdicionalComprador_example"), informacionesAdicionales: Ecf32InformacionesAdicionales(fechaEmbarque: Date(), numeroEmbarque: "numeroEmbarque_example", numeroContenedor: "numeroContenedor_example", numeroReferencia: "numeroReferencia_example", pesoBruto: Ecf31DescuentoORecargo_montoDescuentooRecargo(), pesoNeto: nil, unidadPesoBruto: UnidadMedidaType(), unidadPesoNeto: nil, cantidadBulto: nil, unidadBulto: nil, volumenBulto: Ecf31ImpuestoAdicional2_montoImpuestoSelectivoConsumoEspecifico(), unidadVolumen: nil), transporte: Ecf32Transporte(conductor: "conductor_example", documentoTransporte: "documentoTransporte_example", ficha: "ficha_example", placa: "placa_example", rutaTransporte: "rutaTransporte_example", zonaTransporte: "zonaTransporte_example", numeroAlbaran: "numeroAlbaran_example"), totales: Ecf32Totales(montoGravadoTotal: nil, montoGravadoI1: nil, montoGravadoI2: nil, montoGravadoI3: nil, montoExento: nil, itbiS1: nil, itbiS2: nil, itbiS3: nil, totalITBIS: nil, totalITBIS1: nil, totalITBIS2: nil, totalITBIS3: nil, montoImpuestoAdicional: nil, impuestosAdicionales: [Ecf32ImpuestoAdicional2(tipoImpuesto: Ecf32CodificacionTipoImpuestosType(), tasaImpuestoAdicional: Ecf31ImpuestoAdicional2_tasaImpuestoAdicional(), montoImpuestoSelectivoConsumoEspecifico: nil, montoImpuestoSelectivoConsumoAdvalorem: nil, otrosImpuestosAdicionales: nil)], montoTotal: nil, montoNoFacturable: Ecf31Totales_montoNoFacturable(), montoPeriodo: nil, saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil), otraMoneda: Ecf32OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoGravadoTotalOtraMoneda: nil, montoGravado1OtraMoneda: nil, montoGravado2OtraMoneda: nil, montoGravado3OtraMoneda: nil, montoExentoOtraMoneda: nil, totalITBISOtraMoneda: nil, totalITBIS1OtraMoneda: nil, totalITBIS2OtraMoneda: nil, totalITBIS3OtraMoneda: nil, montoImpuestoAdicionalOtraMoneda: nil, impuestosAdicionalesOtraMoneda: [Ecf32ImpuestoAdicionalOtraMoneda(tipoImpuestoOtraMoneda: nil, tasaImpuestoAdicionalOtraMoneda: nil, montoImpuestoSelectivoConsumoEspecificoOtraMoneda: nil, montoImpuestoSelectivoConsumoAdvaloremOtraMoneda: nil, otrosImpuestosAdicionalesOtraMoneda: nil)], montoTotalOtraMoneda: nil)), detallesItems: [Ecf32Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf32CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf32IndicadorFacturacionType(), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf32IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: nil, cantidadReferencia: nil, unidadReferencia: nil, tablaSubcantidad: [Ecf32SubcantidadItem(subcantidad: Ecf31OtraMonedaDetalle_precioOtraMoneda(), codigoSubcantidad: nil)], gradosAlcohol: Ecf31DescuentoORecargo_valorDescuentooRecargo(), precioUnitarioReferencia: nil, fechaElaboracion: Date(), fechaVencimientoItem: Date(), mineria: Ecf32Mineria(pesoNetoKilogramo: nil, pesoNetoMineria: nil, tipoAfiliacion: TipoAfiliacionType(), liquidacion: LiquidacionType()), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), descuentoMonto: nil, tablaSubDescuento: [Ecf32SubDescuento(tipoSubDescuento: Ecf32TipoDescuentoRecargoType(), subDescuentoPorcentaje: nil, montoSubDescuento: nil)], recargoMonto: nil, tablaSubRecargo: [Ecf32SubRecargo(tipoSubRecargo: nil, subRecargoPorcentaje: nil, montoSubRecargo: nil)], tablaImpuestoAdicional: [Ecf32ImpuestoAdicional(tipoImpuesto: nil)], otraMonedaDetalle: Ecf32OtraMonedaDetalle(precioOtraMoneda: nil, descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf32Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalMontoGravadoTotal: nil, subTotalMontoGravadoI1: nil, subTotalMontoGravadoI2: nil, subTotalMontoGravadoI3: nil, subTotaITBIS: nil, subTotaITBIS1: nil, subTotaITBIS2: nil, subTotaITBIS3: nil, subTotalImpuestoAdicional: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], descuentosORecargos: [Ecf32DescuentoORecargo(numeroLinea: nil, tipoAjuste: Ecf32TipoAjusteType(), indicadorNorma1007: IndicadorNorma1007Type(), descripcionDescuentooRecargo: "descripcionDescuentooRecargo_example", tipoValor: TipoDescuentoRecargoType(), valorDescuentooRecargo: nil, montoDescuentooRecargo: nil, montoDescuentooRecargoOtraMoneda: nil, indicadorFacturacionDescuentooRecargo: IndicadorFacturacionDRType())], paginacion: [Ecf32Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalMontoGravadoPagina: nil, subtotalMontoGravado1Pagina: nil, subtotalMontoGravado2Pagina: nil, subtotalMontoGravado3Pagina: nil, subtotalExentoPagina: nil, subtotalItbisPagina: nil, subtotalItbis1Pagina: nil, subtotalItbis2Pagina: nil, subtotalItbis3Pagina: nil, subtotalImpuestoAdicionalPagina: nil, subtotalImpuestoAdicional: Ecf32SubtotalImpuestoAdicional(subtotalImpuestoSelectivoConsumoEspecificoPagina: nil, subtotalOtrosImpuesto: nil), montoSubtotalPagina: nil, subtotalMontoNoFacturablePagina: nil)], informacionReferencia: Ecf32InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // Ecf32ECF | 

EcfAPI.recepcionEcf32(ecf32ECF: ecf32ECF) { (response, error) in
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
 **ecf32ECF** | [**Ecf32ECF**](Ecf32ECF.md) |  | 

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
    open class func recepcionEcf33(ecf33ECF: Ecf33ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf33ECF = Ecf33ECF(encabezado: Ecf33Encabezado(version: Ecf33VersionType(), idDoc: Ecf33IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), indicadorEnvioDiferido: IndicadorEnvioDiferidoType(), indicadorMontoGravado: IndicadorMontoGravadoType(), indicadorServicioTodoIncluido: IndicadorServicioTodoIncluidoType(), tipoIngresos: TipoIngresosValidationType(), tipoPago: Ecf33TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [Ecf33FormaDePago(formaPago: Ecf33FormaPagoType(), montoPago: Ecf31FormaDePago_montoPago())], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf33Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", codigoVendedor: "codigoVendedor_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", zonaVenta: "zonaVenta_example", rutaVenta: "rutaVenta_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf33Comprador(rncComprador: "rncComprador_example", identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example", contactoComprador: "contactoComprador_example", correoComprador: "correoComprador_example", direccionComprador: "direccionComprador_example", municipioComprador: nil, provinciaComprador: nil, fechaEntrega: Date(), contactoEntrega: "contactoEntrega_example", direccionEntrega: "direccionEntrega_example", telefonoAdicional: "telefonoAdicional_example", fechaOrdenCompra: Date(), numeroOrdenCompra: "numeroOrdenCompra_example", codigoInternoComprador: "codigoInternoComprador_example", responsablePago: "responsablePago_example", informacionAdicionalComprador: "informacionAdicionalComprador_example"), informacionesAdicionales: Ecf33InformacionesAdicionales(fechaEmbarque: Date(), numeroEmbarque: "numeroEmbarque_example", numeroContenedor: "numeroContenedor_example", numeroReferencia: "numeroReferencia_example", pesoBruto: Ecf31DescuentoORecargo_montoDescuentooRecargo(), pesoNeto: nil, unidadPesoBruto: UnidadMedidaType(), unidadPesoNeto: nil, cantidadBulto: nil, unidadBulto: nil, volumenBulto: Ecf31ImpuestoAdicional2_montoImpuestoSelectivoConsumoEspecifico(), unidadVolumen: nil), transporte: Ecf33Transporte(conductor: "conductor_example", documentoTransporte: "documentoTransporte_example", ficha: "ficha_example", placa: "placa_example", rutaTransporte: "rutaTransporte_example", zonaTransporte: "zonaTransporte_example", numeroAlbaran: "numeroAlbaran_example"), totales: Ecf33Totales(montoGravadoTotal: nil, montoGravadoI1: nil, montoGravadoI2: nil, montoGravadoI3: nil, montoExento: nil, itbiS1: nil, itbiS2: nil, itbiS3: nil, totalITBIS: nil, totalITBIS1: nil, totalITBIS2: nil, totalITBIS3: nil, montoImpuestoAdicional: nil, impuestosAdicionales: [Ecf33ImpuestoAdicional2(tipoImpuesto: Ecf33CodificacionTipoImpuestosType(), tasaImpuestoAdicional: Ecf31ImpuestoAdicional2_tasaImpuestoAdicional(), montoImpuestoSelectivoConsumoEspecifico: nil, montoImpuestoSelectivoConsumoAdvalorem: nil, otrosImpuestosAdicionales: nil)], montoTotal: nil, montoNoFacturable: Ecf31Totales_montoNoFacturable(), montoPeriodo: nil, saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil, totalITBISRetenido: nil, totalISRRetencion: nil, totalITBISPercepcion: nil, totalISRPercepcion: nil), otraMoneda: Ecf33OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoGravadoTotalOtraMoneda: nil, montoGravado1OtraMoneda: nil, montoGravado2OtraMoneda: nil, montoGravado3OtraMoneda: nil, montoExentoOtraMoneda: nil, totalITBISOtraMoneda: nil, totalITBIS1OtraMoneda: nil, totalITBIS2OtraMoneda: nil, totalITBIS3OtraMoneda: nil, montoImpuestoAdicionalOtraMoneda: nil, impuestosAdicionalesOtraMoneda: [Ecf33ImpuestoAdicionalOtraMoneda(tipoImpuestoOtraMoneda: nil, tasaImpuestoAdicionalOtraMoneda: nil, montoImpuestoSelectivoConsumoEspecificoOtraMoneda: nil, montoImpuestoSelectivoConsumoAdvaloremOtraMoneda: nil, otrosImpuestosAdicionalesOtraMoneda: nil)], montoTotalOtraMoneda: nil)), detallesItems: [Ecf33Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf33CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf33IndicadorFacturacionType(), retencion: Ecf33Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoITBISRetenido: nil, montoISRRetenido: nil), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf33IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: nil, cantidadReferencia: nil, unidadReferencia: nil, tablaSubcantidad: [Ecf33SubcantidadItem(subcantidad: Ecf31OtraMonedaDetalle_precioOtraMoneda(), codigoSubcantidad: nil)], gradosAlcohol: Ecf31DescuentoORecargo_valorDescuentooRecargo(), precioUnitarioReferencia: nil, fechaElaboracion: Date(), fechaVencimientoItem: Date(), mineria: Ecf33Mineria(pesoNetoKilogramo: nil, pesoNetoMineria: nil, tipoAfiliacion: TipoAfiliacionType(), liquidacion: LiquidacionType()), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), descuentoMonto: nil, tablaSubDescuento: [Ecf33SubDescuento(tipoSubDescuento: Ecf33TipoDescuentoRecargoType(), subDescuentoPorcentaje: nil, montoSubDescuento: nil)], recargoMonto: nil, tablaSubRecargo: [Ecf33SubRecargo(tipoSubRecargo: nil, subRecargoPorcentaje: nil, montoSubRecargo: nil)], tablaImpuestoAdicional: [Ecf33ImpuestoAdicional(tipoImpuesto: nil)], otraMonedaDetalle: Ecf33OtraMonedaDetalle(precioOtraMoneda: nil, descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf33Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalMontoGravadoTotal: nil, subTotalMontoGravadoI1: nil, subTotalMontoGravadoI2: nil, subTotalMontoGravadoI3: nil, subTotaITBIS: nil, subTotaITBIS1: nil, subTotaITBIS2: nil, subTotaITBIS3: nil, subTotalImpuestoAdicional: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], descuentosORecargos: [Ecf33DescuentoORecargo(numeroLinea: nil, tipoAjuste: Ecf33TipoAjusteType(), indicadorNorma1007: IndicadorNorma1007Type(), descripcionDescuentooRecargo: "descripcionDescuentooRecargo_example", tipoValor: TipoDescuentoRecargoType(), valorDescuentooRecargo: nil, montoDescuentooRecargo: nil, montoDescuentooRecargoOtraMoneda: nil, indicadorFacturacionDescuentooRecargo: IndicadorFacturacionDRType())], paginacion: [Ecf33Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalMontoGravadoPagina: nil, subtotalMontoGravado1Pagina: nil, subtotalMontoGravado2Pagina: nil, subtotalMontoGravado3Pagina: nil, subtotalExentoPagina: nil, subtotalItbisPagina: nil, subtotalItbis1Pagina: nil, subtotalItbis2Pagina: nil, subtotalItbis3Pagina: nil, subtotalImpuestoAdicionalPagina: nil, subtotalImpuestoAdicional: Ecf33SubtotalImpuestoAdicional(subtotalImpuestoSelectivoConsumoEspecificoPagina: nil, subtotalOtrosImpuesto: nil), montoSubtotalPagina: nil, subtotalMontoNoFacturablePagina: nil)], informacionReferencia: Ecf33InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: Ecf33CodigoModificacionType(), razonModificacion: "razonModificacion_example")) // Ecf33ECF | 

EcfAPI.recepcionEcf33(ecf33ECF: ecf33ECF) { (response, error) in
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
 **ecf33ECF** | [**Ecf33ECF**](Ecf33ECF.md) |  | 

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
    open class func recepcionEcf34(ecf34ECF: Ecf34ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf34ECF = Ecf34ECF(encabezado: Ecf34Encabezado(version: Ecf34VersionType(), idDoc: Ecf34IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", indicadorNotaCredito: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), indicadorEnvioDiferido: IndicadorEnvioDiferidoType(), indicadorMontoGravado: IndicadorMontoGravadoType(), indicadorServicioTodoIncluido: IndicadorServicioTodoIncluidoType(), tipoIngresos: TipoIngresosValidationType(), tipoPago: Ecf34TipoPagoType(), fechaLimitePago: Date(), fechaDesde: Date(), fechaHasta: Date(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf34Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", codigoVendedor: "codigoVendedor_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", zonaVenta: "zonaVenta_example", rutaVenta: "rutaVenta_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf34Comprador(rncComprador: "rncComprador_example", identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example", contactoComprador: "contactoComprador_example", correoComprador: "correoComprador_example", direccionComprador: "direccionComprador_example", municipioComprador: nil, provinciaComprador: nil, fechaEntrega: Date(), contactoEntrega: "contactoEntrega_example", direccionEntrega: "direccionEntrega_example", telefonoAdicional: "telefonoAdicional_example", fechaOrdenCompra: Date(), numeroOrdenCompra: "numeroOrdenCompra_example", codigoInternoComprador: "codigoInternoComprador_example", responsablePago: "responsablePago_example", informacionAdicionalComprador: "informacionAdicionalComprador_example"), informacionesAdicionales: Ecf34InformacionesAdicionales(fechaEmbarque: Date(), numeroEmbarque: "numeroEmbarque_example", numeroContenedor: "numeroContenedor_example", numeroReferencia: "numeroReferencia_example", pesoBruto: Ecf31DescuentoORecargo_montoDescuentooRecargo(), pesoNeto: nil, unidadPesoBruto: UnidadMedidaType(), unidadPesoNeto: nil, cantidadBulto: nil, unidadBulto: nil, volumenBulto: Ecf31ImpuestoAdicional2_montoImpuestoSelectivoConsumoEspecifico(), unidadVolumen: nil), transporte: Ecf34Transporte(conductor: "conductor_example", documentoTransporte: "documentoTransporte_example", ficha: "ficha_example", placa: "placa_example", rutaTransporte: "rutaTransporte_example", zonaTransporte: "zonaTransporte_example", numeroAlbaran: "numeroAlbaran_example"), totales: Ecf34Totales(montoGravadoTotal: nil, montoGravadoI1: nil, montoGravadoI2: nil, montoGravadoI3: nil, montoExento: nil, itbiS1: nil, itbiS2: nil, itbiS3: nil, totalITBIS: nil, totalITBIS1: nil, totalITBIS2: nil, totalITBIS3: nil, montoImpuestoAdicional: nil, impuestosAdicionales: [Ecf34ImpuestoAdicional2(tipoImpuesto: CodificacionTipoImpuestosType(), tasaImpuestoAdicional: Ecf31DescuentoORecargo_valorDescuentooRecargo(), montoImpuestoSelectivoConsumoEspecifico: nil, montoImpuestoSelectivoConsumoAdvalorem: nil, otrosImpuestosAdicionales: nil)], montoTotal: Ecf31FormaDePago_montoPago(), montoNoFacturable: Ecf31Totales_montoNoFacturable(), montoPeriodo: nil, saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil, totalITBISRetenido: nil, totalISRRetencion: nil, totalITBISPercepcion: nil, totalISRPercepcion: nil), otraMoneda: Ecf34OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoGravadoTotalOtraMoneda: nil, montoGravado1OtraMoneda: nil, montoGravado2OtraMoneda: nil, montoGravado3OtraMoneda: nil, montoExentoOtraMoneda: nil, totalITBISOtraMoneda: nil, totalITBIS1OtraMoneda: nil, totalITBIS2OtraMoneda: nil, totalITBIS3OtraMoneda: nil, montoImpuestoAdicionalOtraMoneda: nil, impuestosAdicionalesOtraMoneda: [Ecf34ImpuestoAdicionalOtraMoneda(tipoImpuestoOtraMoneda: Ecf34CodificacionTipoImpuestosType(), tasaImpuestoAdicionalOtraMoneda: Ecf31ImpuestoAdicional2_tasaImpuestoAdicional(), montoImpuestoSelectivoConsumoEspecificoOtraMoneda: nil, montoImpuestoSelectivoConsumoAdvaloremOtraMoneda: nil, otrosImpuestosAdicionalesOtraMoneda: nil)], montoTotalOtraMoneda: nil)), detallesItems: [Ecf34Item(numeroLinea: nil, tablaCodigosItem: [Ecf34CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf34IndicadorFacturacionType(), retencion: Ecf34Retencion(indicadorAgenteRetencionoPercepcion: IndicadorAgenteRetencionoPercepcionType(), montoITBISRetenido: nil, montoISRRetenido: nil), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf34IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: nil, cantidadReferencia: nil, unidadReferencia: nil, tablaSubcantidad: [Ecf34SubcantidadItem(subcantidad: Ecf31OtraMonedaDetalle_precioOtraMoneda(), codigoSubcantidad: nil)], gradosAlcohol: nil, precioUnitarioReferencia: nil, fechaElaboracion: Date(), fechaVencimientoItem: Date(), mineria: Ecf34Mineria(pesoNetoKilogramo: nil, pesoNetoMineria: nil, tipoAfiliacion: TipoAfiliacionType(), liquidacion: LiquidacionType()), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), descuentoMonto: nil, tablaSubDescuento: [Ecf34SubDescuento(tipoSubDescuento: Ecf34TipoDescuentoRecargoType(), subDescuentoPorcentaje: nil, montoSubDescuento: nil)], recargoMonto: nil, tablaSubRecargo: [Ecf34SubRecargo(tipoSubRecargo: nil, subRecargoPorcentaje: nil, montoSubRecargo: nil)], tablaImpuestoAdicional: [Ecf34ImpuestoAdicional(tipoImpuesto: nil)], otraMonedaDetalle: Ecf34OtraMonedaDetalle(precioOtraMoneda: nil, descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf34Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalMontoGravadoTotal: nil, subTotalMontoGravadoI1: nil, subTotalMontoGravadoI2: nil, subTotalMontoGravadoI3: nil, subTotaITBIS: nil, subTotaITBIS1: nil, subTotaITBIS2: nil, subTotaITBIS3: nil, subTotalImpuestoAdicional: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], descuentosORecargos: [Ecf34DescuentoORecargo(numeroLinea: nil, tipoAjuste: Ecf34TipoAjusteType(), indicadorNorma1007: IndicadorNorma1007Type(), descripcionDescuentooRecargo: "descripcionDescuentooRecargo_example", tipoValor: TipoDescuentoRecargoType(), valorDescuentooRecargo: nil, montoDescuentooRecargo: nil, montoDescuentooRecargoOtraMoneda: nil, indicadorFacturacionDescuentooRecargo: IndicadorFacturacionDRType())], paginacion: [Ecf34Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalMontoGravadoPagina: nil, subtotalMontoGravado1Pagina: nil, subtotalMontoGravado2Pagina: nil, subtotalMontoGravado3Pagina: nil, subtotalExentoPagina: nil, subtotalItbisPagina: nil, subtotalItbis1Pagina: nil, subtotalItbis2Pagina: nil, subtotalItbis3Pagina: nil, subtotalImpuestoAdicionalPagina: nil, subtotalImpuestoAdicional: Ecf34SubtotalImpuestoAdicional(subtotalImpuestoSelectivoConsumoEspecificoPagina: nil, subtotalOtrosImpuesto: nil), montoSubtotalPagina: nil, subtotalMontoNoFacturablePagina: nil)], informacionReferencia: Ecf34InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: Ecf34CodigoModificacionType(), razonModificacion: "razonModificacion_example")) // Ecf34ECF | 

EcfAPI.recepcionEcf34(ecf34ECF: ecf34ECF) { (response, error) in
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
 **ecf34ECF** | [**Ecf34ECF**](Ecf34ECF.md) |  | 

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
    open class func recepcionEcf41(ecf41ECF: Ecf41ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf41ECF = Ecf41ECF(encabezado: Ecf41Encabezado(version: Ecf41VersionType(), idDoc: Ecf41IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), indicadorMontoGravado: IndicadorMontoGravadoType(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [Ecf41FormaDePago(formaPago: Ecf41FormaPagoType(), montoPago: Ecf31FormaDePago_montoPago())], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf41Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf41Comprador(rncComprador: "rncComprador_example", razonSocialComprador: "razonSocialComprador_example", contactoComprador: "contactoComprador_example", correoComprador: "correoComprador_example", direccionComprador: "direccionComprador_example", municipioComprador: nil, provinciaComprador: nil, codigoInternoComprador: "codigoInternoComprador_example", responsablePago: "responsablePago_example", informacionAdicionalComprador: "informacionAdicionalComprador_example"), totales: Ecf41Totales(montoGravadoTotal: Ecf31DescuentoORecargo_montoDescuentooRecargo(), montoGravadoI1: nil, montoGravadoI2: nil, montoGravadoI3: nil, montoExento: nil, itbiS1: nil, itbiS2: nil, itbiS3: nil, totalITBIS: nil, totalITBIS1: nil, totalITBIS2: nil, totalITBIS3: nil, montoTotal: nil, montoPeriodo: Ecf31Totales_montoNoFacturable(), saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil, totalITBISRetenido: nil, totalISRRetencion: nil, totalITBISPercepcion: nil, totalISRPercepcion: nil), otraMoneda: Ecf41OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoGravadoTotalOtraMoneda: nil, montoGravado1OtraMoneda: nil, montoGravado2OtraMoneda: nil, montoGravado3OtraMoneda: nil, montoExentoOtraMoneda: nil, totalITBISOtraMoneda: nil, totalITBIS1OtraMoneda: nil, totalITBIS2OtraMoneda: nil, totalITBIS3OtraMoneda: nil, montoTotalOtraMoneda: nil)), detallesItems: [Ecf41Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf41CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf41IndicadorFacturacionType(), retencion: Ecf41Retencion(indicadorAgenteRetencionoPercepcion: Ecf41IndicadorAgenteRetencionoPercepcionType(), montoITBISRetenido: nil, montoISRRetenido: nil), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf41IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: UnidadMedidaType(), fechaElaboracion: Date(), fechaVencimientoItem: Date(), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), descuentoMonto: nil, tablaSubDescuento: [Ecf41SubDescuento(tipoSubDescuento: Ecf41TipoDescuentoRecargoType(), subDescuentoPorcentaje: Ecf31DescuentoORecargo_valorDescuentooRecargo(), montoSubDescuento: nil)], recargoMonto: nil, tablaSubRecargo: [Ecf41SubRecargo(tipoSubRecargo: nil, subRecargoPorcentaje: nil, montoSubRecargo: nil)], otraMonedaDetalle: Ecf41OtraMonedaDetalle(precioOtraMoneda: Ecf31OtraMonedaDetalle_precioOtraMoneda(), descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf41Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalMontoGravadoTotal: nil, subTotalMontoGravadoI1: nil, subTotalMontoGravadoI2: nil, subTotalMontoGravadoI3: nil, subTotaITBIS: nil, subTotaITBIS1: nil, subTotaITBIS2: nil, subTotaITBIS3: nil, subTotalImpuestoAdicional: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], descuentosORecargos: [Ecf41DescuentoORecargo(numeroLinea: nil, tipoAjuste: Ecf41TipoAjusteType(), descripcionDescuentooRecargo: "descripcionDescuentooRecargo_example", tipoValor: TipoDescuentoRecargoType(), valorDescuentooRecargo: nil, montoDescuentooRecargo: nil, montoDescuentooRecargoOtraMoneda: nil, indicadorFacturacionDescuentooRecargo: IndicadorFacturacionDRType())], paginacion: [Ecf41Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalMontoGravadoPagina: nil, subtotalMontoGravado1Pagina: nil, subtotalMontoGravado2Pagina: nil, subtotalMontoGravado3Pagina: nil, subtotalExentoPagina: nil, subtotalItbisPagina: nil, subtotalItbis1Pagina: nil, subtotalItbis2Pagina: nil, subtotalItbis3Pagina: nil, montoSubtotalPagina: nil)], informacionReferencia: Ecf41InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // Ecf41ECF | 

EcfAPI.recepcionEcf41(ecf41ECF: ecf41ECF) { (response, error) in
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
 **ecf41ECF** | [**Ecf41ECF**](Ecf41ECF.md) |  | 

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
    open class func recepcionEcf43(ecf43ECF: Ecf43ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf43ECF = Ecf43ECF(encabezado: Ecf43Encabezado(version: Ecf43VersionType(), idDoc: Ecf43IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf43Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), totales: Ecf43Totales(montoExento: Ecf31DescuentoORecargo_montoDescuentooRecargo(), montoTotal: Ecf31FormaDePago_montoPago(), montoPeriodo: Ecf31Totales_montoNoFacturable(), saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil), otraMoneda: Ecf43OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoExentoOtraMoneda: nil, montoTotalOtraMoneda: nil)), detallesItems: [Ecf43Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf43CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf43IndicadorFacturacionType(), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf43IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: UnidadMedidaType(), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), otraMonedaDetalle: Ecf43OtraMonedaDetalle(precioOtraMoneda: Ecf31OtraMonedaDetalle_precioOtraMoneda(), descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf43Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], paginacion: [Ecf43Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalExentoPagina: nil, montoSubtotalPagina: nil)], informacionReferencia: Ecf43InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // Ecf43ECF | 

EcfAPI.recepcionEcf43(ecf43ECF: ecf43ECF) { (response, error) in
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
 **ecf43ECF** | [**Ecf43ECF**](Ecf43ECF.md) |  | 

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
    open class func recepcionEcf44(ecf44ECF: Ecf44ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf44ECF = Ecf44ECF(encabezado: Ecf44Encabezado(version: Ecf44VersionType(), idDoc: Ecf44IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), indicadorEnvioDiferido: IndicadorEnvioDiferidoType(), indicadorServicioTodoIncluido: IndicadorServicioTodoIncluidoType(), tipoIngresos: Ecf44TipoIngresosValidationType(), tipoPago: Ecf44TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [Ecf44FormaDePago(formaPago: Ecf44FormaPagoType(), montoPago: Ecf31FormaDePago_montoPago())], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf44Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", codigoVendedor: "codigoVendedor_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", zonaVenta: "zonaVenta_example", rutaVenta: "rutaVenta_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf44Comprador(rncComprador: "rncComprador_example", identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example", contactoComprador: "contactoComprador_example", correoComprador: "correoComprador_example", direccionComprador: "direccionComprador_example", municipioComprador: nil, provinciaComprador: nil, fechaEntrega: Date(), contactoEntrega: "contactoEntrega_example", direccionEntrega: "direccionEntrega_example", telefonoAdicional: "telefonoAdicional_example", fechaOrdenCompra: Date(), numeroOrdenCompra: "numeroOrdenCompra_example", codigoInternoComprador: "codigoInternoComprador_example", responsablePago: "responsablePago_example", informacionAdicionalComprador: "informacionAdicionalComprador_example"), informacionesAdicionales: Ecf44InformacionesAdicionales(fechaEmbarque: Date(), numeroEmbarque: "numeroEmbarque_example", numeroContenedor: "numeroContenedor_example", numeroReferencia: "numeroReferencia_example", pesoBruto: Ecf31DescuentoORecargo_montoDescuentooRecargo(), pesoNeto: nil, unidadPesoBruto: UnidadMedidaType(), unidadPesoNeto: nil, cantidadBulto: nil, unidadBulto: nil, volumenBulto: Ecf31ImpuestoAdicional2_montoImpuestoSelectivoConsumoEspecifico(), unidadVolumen: nil), transporte: Ecf44Transporte(conductor: "conductor_example", documentoTransporte: "documentoTransporte_example", ficha: "ficha_example", placa: "placa_example", rutaTransporte: "rutaTransporte_example", zonaTransporte: "zonaTransporte_example", numeroAlbaran: "numeroAlbaran_example"), totales: Ecf44Totales(montoExento: nil, montoImpuestoAdicional: nil, impuestosAdicionales: [Ecf44ImpuestoAdicional2(tipoImpuesto: Ecf44CodificacionTipoImpuestosType(), tasaImpuestoAdicional: Ecf31ImpuestoAdicional2_tasaImpuestoAdicional(), otrosImpuestosAdicionales: Ecf31Item_cantidadItem())], montoTotal: nil, montoNoFacturable: Ecf31Totales_montoNoFacturable(), montoPeriodo: nil, saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil), otraMoneda: Ecf44OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoExentoOtraMoneda: nil, montoImpuestoAdicionalOtraMoneda: nil, impuestosAdicionalesOtraMoneda: [Ecf44ImpuestoAdicionalOtraMoneda(tipoImpuestoOtraMoneda: CodificacionTipoImpuestosType(), tasaImpuestoAdicionalOtraMoneda: Ecf31DescuentoORecargo_valorDescuentooRecargo(), otrosImpuestosAdicionalesOtraMoneda: nil)], montoTotalOtraMoneda: nil)), detallesItems: [Ecf44Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf44CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf44IndicadorFacturacionType(), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf44IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: nil, unidadMedida: nil, fechaElaboracion: Date(), fechaVencimientoItem: Date(), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), descuentoMonto: nil, tablaSubDescuento: [Ecf44SubDescuento(tipoSubDescuento: Ecf44TipoDescuentoRecargoType(), subDescuentoPorcentaje: nil, montoSubDescuento: nil)], recargoMonto: nil, tablaSubRecargo: [Ecf44SubRecargo(tipoSubRecargo: nil, subRecargoPorcentaje: nil, montoSubRecargo: nil)], tablaImpuestoAdicional: [Ecf44ImpuestoAdicional(tipoImpuesto: nil)], otraMonedaDetalle: Ecf44OtraMonedaDetalle(precioOtraMoneda: Ecf31OtraMonedaDetalle_precioOtraMoneda(), descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf44Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalImpuestoAdicional: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], descuentosORecargos: [Ecf44DescuentoORecargo(numeroLinea: nil, tipoAjuste: Ecf44TipoAjusteType(), descripcionDescuentooRecargo: "descripcionDescuentooRecargo_example", tipoValor: TipoDescuentoRecargoType(), valorDescuentooRecargo: nil, montoDescuentooRecargo: nil, montoDescuentooRecargoOtraMoneda: nil, indicadorFacturacionDescuentooRecargo: IndicadorFacturacionDRType())], paginacion: [Ecf44Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalExentoPagina: nil, subtotalImpuestoAdicionalPagina: nil, subtotalImpuestoAdicional: Ecf44SubtotalImpuestoAdicional(subtotalOtrosImpuesto: nil), montoSubtotalPagina: nil, subtotalMontoNoFacturablePagina: nil)], informacionReferencia: Ecf44InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // Ecf44ECF | 

EcfAPI.recepcionEcf44(ecf44ECF: ecf44ECF) { (response, error) in
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
 **ecf44ECF** | [**Ecf44ECF**](Ecf44ECF.md) |  | 

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
    open class func recepcionEcf45(ecf45ECF: Ecf45ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf45ECF = Ecf45ECF(encabezado: Ecf45Encabezado(version: Ecf45VersionType(), idDoc: Ecf45IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), indicadorEnvioDiferido: IndicadorEnvioDiferidoType(), indicadorMontoGravado: IndicadorMontoGravadoType(), indicadorServicioTodoIncluido: IndicadorServicioTodoIncluidoType(), tipoIngresos: Ecf45TipoIngresosValidationType(), tipoPago: Ecf45TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [Ecf45FormaDePago(formaPago: Ecf45FormaPagoType(), montoPago: Ecf31FormaDePago_montoPago())], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf45Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", codigoVendedor: "codigoVendedor_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", zonaVenta: "zonaVenta_example", rutaVenta: "rutaVenta_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf45Comprador(rncComprador: "rncComprador_example", razonSocialComprador: "razonSocialComprador_example", contactoComprador: "contactoComprador_example", correoComprador: "correoComprador_example", direccionComprador: "direccionComprador_example", municipioComprador: nil, provinciaComprador: nil, fechaEntrega: Date(), contactoEntrega: "contactoEntrega_example", direccionEntrega: "direccionEntrega_example", telefonoAdicional: "telefonoAdicional_example", fechaOrdenCompra: Date(), numeroOrdenCompra: "numeroOrdenCompra_example", codigoInternoComprador: "codigoInternoComprador_example", responsablePago: "responsablePago_example", informacionAdicionalComprador: "informacionAdicionalComprador_example"), informacionesAdicionales: Ecf45InformacionesAdicionales(fechaEmbarque: Date(), numeroEmbarque: "numeroEmbarque_example", numeroContenedor: "numeroContenedor_example", numeroReferencia: "numeroReferencia_example", pesoBruto: Ecf31DescuentoORecargo_montoDescuentooRecargo(), pesoNeto: nil, unidadPesoBruto: UnidadMedidaType(), unidadPesoNeto: nil, cantidadBulto: nil, unidadBulto: nil, volumenBulto: Ecf31ImpuestoAdicional2_montoImpuestoSelectivoConsumoEspecifico(), unidadVolumen: nil), transporte: Ecf45Transporte(conductor: "conductor_example", documentoTransporte: "documentoTransporte_example", ficha: "ficha_example", placa: "placa_example", rutaTransporte: "rutaTransporte_example", zonaTransporte: "zonaTransporte_example", numeroAlbaran: "numeroAlbaran_example"), totales: Ecf45Totales(montoGravadoTotal: nil, montoGravadoI1: nil, montoGravadoI2: nil, montoGravadoI3: nil, montoExento: nil, itbiS1: nil, itbiS2: nil, itbiS3: nil, totalITBIS: nil, totalITBIS1: nil, totalITBIS2: nil, totalITBIS3: nil, montoImpuestoAdicional: nil, impuestosAdicionales: [Ecf45ImpuestoAdicional2(tipoImpuesto: Ecf45CodificacionTipoImpuestosType(), tasaImpuestoAdicional: Ecf31ImpuestoAdicional2_tasaImpuestoAdicional(), montoImpuestoSelectivoConsumoEspecifico: nil, montoImpuestoSelectivoConsumoAdvalorem: nil, otrosImpuestosAdicionales: nil)], montoTotal: nil, montoNoFacturable: Ecf31Totales_montoNoFacturable(), montoPeriodo: nil, saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil), otraMoneda: Ecf45OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoGravadoTotalOtraMoneda: nil, montoGravado1OtraMoneda: nil, montoGravado2OtraMoneda: nil, montoGravado3OtraMoneda: nil, montoExentoOtraMoneda: nil, totalITBISOtraMoneda: nil, totalITBIS1OtraMoneda: nil, totalITBIS2OtraMoneda: nil, totalITBIS3OtraMoneda: nil, montoImpuestoAdicionalOtraMoneda: nil, impuestosAdicionalesOtraMoneda: [Ecf45ImpuestoAdicionalOtraMoneda(tipoImpuestoOtraMoneda: CodificacionTipoImpuestosType(), tasaImpuestoAdicionalOtraMoneda: Ecf31DescuentoORecargo_valorDescuentooRecargo(), montoImpuestoSelectivoConsumoEspecificoOtraMoneda: nil, montoImpuestoSelectivoConsumoAdvaloremOtraMoneda: nil, otrosImpuestosAdicionalesOtraMoneda: nil)], montoTotalOtraMoneda: nil)), detallesItems: [Ecf45Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf45CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf45IndicadorFacturacionType(), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf45IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: nil, cantidadReferencia: nil, unidadReferencia: nil, tablaSubcantidad: [Ecf45SubcantidadItem(subcantidad: Ecf31OtraMonedaDetalle_precioOtraMoneda(), codigoSubcantidad: nil)], gradosAlcohol: nil, precioUnitarioReferencia: nil, fechaElaboracion: Date(), fechaVencimientoItem: Date(), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), descuentoMonto: nil, tablaSubDescuento: [Ecf45SubDescuento(tipoSubDescuento: Ecf45TipoDescuentoRecargoType(), subDescuentoPorcentaje: nil, montoSubDescuento: nil)], recargoMonto: nil, tablaSubRecargo: [Ecf45SubRecargo(tipoSubRecargo: nil, subRecargoPorcentaje: nil, montoSubRecargo: nil)], tablaImpuestoAdicional: [Ecf45ImpuestoAdicional(tipoImpuesto: nil)], otraMonedaDetalle: Ecf45OtraMonedaDetalle(precioOtraMoneda: nil, descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf45Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalMontoGravadoTotal: nil, subTotalMontoGravadoI1: nil, subTotalMontoGravadoI2: nil, subTotalMontoGravadoI3: nil, subTotaITBIS: nil, subTotaITBIS1: nil, subTotaITBIS2: nil, subTotaITBIS3: nil, subTotalImpuestoAdicional: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], descuentosORecargos: [Ecf45DescuentoORecargo(numeroLinea: nil, tipoAjuste: Ecf45TipoAjusteType(), indicadorNorma1007: IndicadorNorma1007Type(), descripcionDescuentooRecargo: "descripcionDescuentooRecargo_example", tipoValor: TipoDescuentoRecargoType(), valorDescuentooRecargo: nil, montoDescuentooRecargo: nil, montoDescuentooRecargoOtraMoneda: nil, indicadorFacturacionDescuentooRecargo: IndicadorFacturacionDRType())], paginacion: [Ecf45Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalMontoGravadoPagina: nil, subtotalMontoGravado1Pagina: nil, subtotalMontoGravado2Pagina: nil, subtotalMontoGravado3Pagina: nil, subtotalExentoPagina: nil, subtotalItbisPagina: nil, subtotalItbis1Pagina: nil, subtotalItbis2Pagina: nil, subtotalItbis3Pagina: nil, subtotalImpuestoAdicionalPagina: nil, subtotalImpuestoAdicional: Ecf45SubtotalImpuestoAdicional(subtotalImpuestoSelectivoConsumoEspecificoPagina: nil, subtotalOtrosImpuesto: nil), montoSubtotalPagina: nil, subtotalMontoNoFacturablePagina: nil)], informacionReferencia: Ecf45InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // Ecf45ECF | 

EcfAPI.recepcionEcf45(ecf45ECF: ecf45ECF) { (response, error) in
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
 **ecf45ECF** | [**Ecf45ECF**](Ecf45ECF.md) |  | 

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
    open class func recepcionEcf46(ecf46ECF: Ecf46ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf46ECF = Ecf46ECF(encabezado: Ecf46Encabezado(version: Ecf46VersionType(), idDoc: Ecf46IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), indicadorEnvioDiferido: IndicadorEnvioDiferidoType(), tipoIngresos: Ecf46TipoIngresosValidationType(), tipoPago: Ecf46TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [Ecf46FormaDePago(formaPago: Ecf46FormaPagoType(), montoPago: Ecf31FormaDePago_montoPago())], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf46Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", codigoVendedor: "codigoVendedor_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", zonaVenta: "zonaVenta_example", rutaVenta: "rutaVenta_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf46Comprador(rncComprador: "rncComprador_example", identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example", contactoComprador: "contactoComprador_example", correoComprador: "correoComprador_example", direccionComprador: "direccionComprador_example", municipioComprador: nil, provinciaComprador: nil, paisComprador: "paisComprador_example", fechaEntrega: Date(), contactoEntrega: "contactoEntrega_example", direccionEntrega: "direccionEntrega_example", telefonoAdicional: "telefonoAdicional_example", fechaOrdenCompra: Date(), numeroOrdenCompra: "numeroOrdenCompra_example", codigoInternoComprador: "codigoInternoComprador_example", responsablePago: "responsablePago_example", informacionAdicionalComprador: "informacionAdicionalComprador_example"), informacionesAdicionales: Ecf46InformacionesAdicionales(fechaEmbarque: Date(), numeroEmbarque: "numeroEmbarque_example", numeroContenedor: "numeroContenedor_example", numeroReferencia: "numeroReferencia_example", nombrePuertoEmbarque: "nombrePuertoEmbarque_example", condicionesEntrega: "condicionesEntrega_example", totalFob: Ecf31ImpuestoAdicional2_montoImpuestoSelectivoConsumoEspecifico(), seguro: nil, flete: nil, otrosGastos: nil, totalCif: Ecf31DescuentoORecargo_montoDescuentooRecargo(), regimenAduanero: "regimenAduanero_example", nombrePuertoSalida: "nombrePuertoSalida_example", nombrePuertoDesembarque: "nombrePuertoDesembarque_example", pesoBruto: nil, pesoNeto: nil, unidadPesoBruto: UnidadMedidaType(), unidadPesoNeto: nil, cantidadBulto: nil, unidadBulto: nil, volumenBulto: nil, unidadVolumen: nil), transporte: Ecf46Transporte(viaTransporte: ViaTransporteType(), paisOrigen: "paisOrigen_example", direccionDestino: "direccionDestino_example", paisDestino: "paisDestino_example", rncIdentificacionCompaniaTransportista: "rncIdentificacionCompaniaTransportista_example", nombreCompaniaTransportista: "nombreCompaniaTransportista_example", numeroViaje: "numeroViaje_example", conductor: "conductor_example", documentoTransporte: "documentoTransporte_example", ficha: "ficha_example", placa: "placa_example", rutaTransporte: "rutaTransporte_example", zonaTransporte: "zonaTransporte_example", numeroAlbaran: "numeroAlbaran_example"), totales: Ecf46Totales(montoGravadoTotal: nil, montoGravadoI3: nil, itbiS3: nil, totalITBIS: nil, totalITBIS3: nil, montoTotal: nil, montoNoFacturable: Ecf31Totales_montoNoFacturable(), montoPeriodo: nil, saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil), otraMoneda: Ecf46OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoGravadoTotalOtraMoneda: nil, montoGravado3OtraMoneda: nil, totalITBISOtraMoneda: nil, totalITBIS3OtraMoneda: nil, montoTotalOtraMoneda: nil)), detallesItems: [Ecf46Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf46CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf46IndicadorFacturacionType(), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf46IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: nil, fechaElaboracion: Date(), fechaVencimientoItem: Date(), mineria: Ecf46Mineria(pesoNetoKilogramo: Ecf31OtraMonedaDetalle_precioOtraMoneda(), pesoNetoMineria: nil, tipoAfiliacion: TipoAfiliacionType(), liquidacion: LiquidacionType()), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), descuentoMonto: nil, tablaSubDescuento: [Ecf46SubDescuento(tipoSubDescuento: Ecf46TipoDescuentoRecargoType(), subDescuentoPorcentaje: Ecf31DescuentoORecargo_valorDescuentooRecargo(), montoSubDescuento: nil)], recargoMonto: nil, tablaSubRecargo: [Ecf46SubRecargo(tipoSubRecargo: nil, subRecargoPorcentaje: nil, montoSubRecargo: nil)], otraMonedaDetalle: Ecf46OtraMonedaDetalle(precioOtraMoneda: nil, descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf46Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalMontoGravadoTotal: nil, subTotalMontoGravadoI3: nil, subTotaITBIS: nil, subTotaITBIS3: nil, montoSubTotal: nil, lineas: nil)], descuentosORecargos: [Ecf46DescuentoORecargo(numeroLinea: nil, tipoAjuste: Ecf46TipoAjusteType(), descripcionDescuentooRecargo: "descripcionDescuentooRecargo_example", tipoValor: TipoDescuentoRecargoType(), valorDescuentooRecargo: nil, montoDescuentooRecargo: nil, montoDescuentooRecargoOtraMoneda: nil, indicadorFacturacionDescuentooRecargo: IndicadorFacturacionDRType())], paginacion: [Ecf46Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalMontoGravadoPagina: nil, subtotalMontoGravado3Pagina: nil, subtotalItbisPagina: nil, subtotalItbis3Pagina: nil, montoSubtotalPagina: nil, subtotalMontoNoFacturablePagina: nil)], informacionReferencia: Ecf46InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // Ecf46ECF | 

EcfAPI.recepcionEcf46(ecf46ECF: ecf46ECF) { (response, error) in
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
 **ecf46ECF** | [**Ecf46ECF**](Ecf46ECF.md) |  | 

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
    open class func recepcionEcf47(ecf47ECF: Ecf47ECF, completion: @escaping (_ data: EcfResponse?, _ error: Error?) -> Void)
```



### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import EcfDgiiClient

let ecf47ECF = Ecf47ECF(encabezado: Ecf47Encabezado(version: Ecf47VersionType(), idDoc: Ecf47IdDoc(tipoeCF: TipoeCFType(), encf: "encf_example", fechaVencimientoSecuencia: Date(), tipoPago: TipoPagoType(), fechaLimitePago: Date(), terminoPago: "terminoPago_example", tablaFormasPago: [Ecf47FormaDePago(formaPago: Ecf47FormaPagoType(), montoPago: Ecf31FormaDePago_montoPago())], tipoCuentaPago: TipoCuentaPagoType(), numeroCuentaPago: "numeroCuentaPago_example", bancoPago: "bancoPago_example", fechaDesde: Date(), fechaHasta: Date(), totalPaginas: Ecf31IdDoc_totalPaginas()), emisor: Ecf47Emisor(rncEmisor: "rncEmisor_example", razonSocialEmisor: "razonSocialEmisor_example", nombreComercial: "nombreComercial_example", sucursal: "sucursal_example", direccionEmisor: "direccionEmisor_example", municipio: ProvinciaMunicipioType(), provincia: nil, tablaTelefonoEmisor: ["tablaTelefonoEmisor_example"], correoEmisor: "correoEmisor_example", webSite: "webSite_example", actividadEconomica: "actividadEconomica_example", numeroFacturaInterna: "numeroFacturaInterna_example", numeroPedidoInterno: "numeroPedidoInterno_example", informacionAdicionalEmisor: "informacionAdicionalEmisor_example", fechaEmision: Date()), comprador: Ecf47Comprador(identificadorExtranjero: "identificadorExtranjero_example", razonSocialComprador: "razonSocialComprador_example"), transporte: Ecf47Transporte(paisDestino: "paisDestino_example"), totales: Ecf47Totales(montoExento: Ecf31DescuentoORecargo_montoDescuentooRecargo(), montoTotal: nil, montoPeriodo: Ecf31Totales_montoNoFacturable(), saldoAnterior: nil, montoAvancePago: nil, valorPagar: nil, totalISRRetencion: nil), otraMoneda: Ecf47OtraMoneda(tipoMoneda: TipoMonedaType(), tipoCambio: Ecf31OtraMoneda_tipoCambio(), montoExentoOtraMoneda: nil, montoTotalOtraMoneda: nil)), detallesItems: [Ecf47Item(numeroLinea: SearchEcfReceptionRequests_TiposEcfs_parameter_inner(), tablaCodigosItem: [Ecf47CodigosItem(tipoCodigo: "tipoCodigo_example", codigoItem: "codigoItem_example")], indicadorFacturacion: Ecf47IndicadorFacturacionType(), retencion: Ecf47Retencion(indicadorAgenteRetencionoPercepcion: Ecf47IndicadorAgenteRetencionoPercepcionType(), montoISRRetenido: nil), nombreItem: "nombreItem_example", indicadorBienoServicio: Ecf47IndicadorBienoServicioType(), descripcionItem: "descripcionItem_example", cantidadItem: Ecf31Item_cantidadItem(), unidadMedida: UnidadMedidaType(), precioUnitarioItem: Ecf31Item_precioUnitarioItem(), otraMonedaDetalle: Ecf47OtraMonedaDetalle(precioOtraMoneda: Ecf31OtraMonedaDetalle_precioOtraMoneda(), descuentoOtraMoneda: nil, recargoOtraMoneda: nil, montoItemOtraMoneda: nil), montoItem: nil)], subtotales: [Ecf47Subtotal(numeroSubTotal: nil, descripcionSubtotal: "descripcionSubtotal_example", orden: nil, subTotalExento: nil, montoSubTotal: nil, lineas: nil)], paginacion: [Ecf47Pagina(paginaNo: nil, noLineaDesde: nil, noLineaHasta: nil, subtotalExentoPagina: nil, montoSubtotalPagina: nil)], informacionReferencia: Ecf47InformacionReferencia(ncfModificado: "ncfModificado_example", rncOtroContribuyente: "rncOtroContribuyente_example", fechaNCFModificado: Date(), codigoModificacion: CodigoModificacionType())) // Ecf47ECF | 

EcfAPI.recepcionEcf47(ecf47ECF: ecf47ECF) { (response, error) in
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
 **ecf47ECF** | [**Ecf47ECF**](Ecf47ECF.md) |  | 

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
    open class func searchAllEcfs(encfs: [String]? = nil, ids: [UUID]? = nil, tiposEcfs: [AllTipoECFTypes]? = nil, includeEcfContent: Bool? = nil, fromFechaEmision: Date? = nil, toFechaEmision: Date? = nil, amountFrom: SearchEcfsAmountFromParameter? = nil, amountTo: SearchEcfsAmountFromParameter? = nil, progresses: [EcfProgress]? = nil, dgiiEstados: [EcfEstado]? = nil, page: GetCompaniesPageParameter? = nil, limit: GetCompaniesLimitParameter? = nil, completion: @escaping (_ data: PaginatedApiResultOfEcfResponse?, _ error: Error?) -> Void)
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
let amountFrom = SearchEcfs_AmountFrom_parameter() // SearchEcfsAmountFromParameter |  (optional)
let amountTo = SearchEcfs_AmountFrom_parameter() // SearchEcfsAmountFromParameter |  (optional)
let progresses = [EcfProgress()] // [EcfProgress] |  (optional)
let dgiiEstados = [EcfEstado()] // [EcfEstado] |  (optional)
let page = GetCompanies_Page_parameter() // GetCompaniesPageParameter |  (optional) (default to 1)
let limit = GetCompanies_Limit_parameter() // GetCompaniesLimitParameter |  (optional) (default to 25)

EcfAPI.searchAllEcfs(encfs: encfs, ids: ids, tiposEcfs: tiposEcfs, includeEcfContent: includeEcfContent, fromFechaEmision: fromFechaEmision, toFechaEmision: toFechaEmision, amountFrom: amountFrom, amountTo: amountTo, progresses: progresses, dgiiEstados: dgiiEstados, page: page, limit: limit) { (response, error) in
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
 **amountFrom** | **SearchEcfsAmountFromParameter** |  | [optional] 
 **amountTo** | **SearchEcfsAmountFromParameter** |  | [optional] 
 **progresses** | [**[EcfProgress]**](EcfProgress.md) |  | [optional] 
 **dgiiEstados** | [**[EcfEstado]**](EcfEstado.md) |  | [optional] 
 **page** | **GetCompaniesPageParameter** |  | [optional] [default to 1]
 **limit** | **GetCompaniesLimitParameter** |  | [optional] [default to 25]

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
    open class func searchEcfs(rnc: String, encfs: [String]? = nil, ids: [UUID]? = nil, tiposEcfs: [AllTipoECFTypes]? = nil, includeEcfContent: Bool? = nil, fromFechaEmision: Date? = nil, toFechaEmision: Date? = nil, amountFrom: SearchEcfsAmountFromParameter? = nil, amountTo: SearchEcfsAmountFromParameter? = nil, progresses: [EcfProgress]? = nil, dgiiEstados: [EcfEstado]? = nil, page: GetCompaniesPageParameter? = nil, limit: GetCompaniesLimitParameter? = nil, completion: @escaping (_ data: PaginatedApiResultOfEcfResponse?, _ error: Error?) -> Void)
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
let amountFrom = SearchEcfs_AmountFrom_parameter() // SearchEcfsAmountFromParameter |  (optional)
let amountTo = SearchEcfs_AmountFrom_parameter() // SearchEcfsAmountFromParameter |  (optional)
let progresses = [EcfProgress()] // [EcfProgress] |  (optional)
let dgiiEstados = [EcfEstado()] // [EcfEstado] |  (optional)
let page = GetCompanies_Page_parameter() // GetCompaniesPageParameter |  (optional) (default to 1)
let limit = GetCompanies_Limit_parameter() // GetCompaniesLimitParameter |  (optional) (default to 25)

EcfAPI.searchEcfs(rnc: rnc, encfs: encfs, ids: ids, tiposEcfs: tiposEcfs, includeEcfContent: includeEcfContent, fromFechaEmision: fromFechaEmision, toFechaEmision: toFechaEmision, amountFrom: amountFrom, amountTo: amountTo, progresses: progresses, dgiiEstados: dgiiEstados, page: page, limit: limit) { (response, error) in
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
 **amountFrom** | **SearchEcfsAmountFromParameter** |  | [optional] 
 **amountTo** | **SearchEcfsAmountFromParameter** |  | [optional] 
 **progresses** | [**[EcfProgress]**](EcfProgress.md) |  | [optional] 
 **dgiiEstados** | [**[EcfEstado]**](EcfEstado.md) |  | [optional] 
 **page** | **GetCompaniesPageParameter** |  | [optional] [default to 1]
 **limit** | **GetCompaniesLimitParameter** |  | [optional] [default to 25]

### Return type

[**PaginatedApiResultOfEcfResponse**](PaginatedApiResultOfEcfResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

