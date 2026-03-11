# # RespuestaConsultaTimbre

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rnc_emisor** | **string** | Número de registro nacional del contribuyente que emitió el resumen de factura de consumo. RNC del emisor del comprobante fiscal electrónico consultado. | [optional]
**razon_social** | **string** | Razón social del contribuyente que emitió el resumen de factura de consumo. Nombre comercial o razón social del emisor del comprobante fiscal electrónico. | [optional]
**encf** | **string** | Número de secuencia utilizada por el contribuyente, extraído del resumen de factura de consumo. Número de comprobante fiscal electrónico (e-NCF) utilizado en la transacción. | [optional]
**estado** | **string** | Estado de validación otorgado por Impuestos Internos al resumen de factura de consumo recibido. Descripción textual del estado de validación del comprobante. Posibles valores: - \&quot;No fue encontrada la factura (e-CF)\&quot;: El e-CF no se encontró en la base de datos de la DGII. - \&quot;Aceptado\&quot;: Implica la validez del e-CF de la RI, incluyendo el aceptado condicional que corresponde   a que no cumplió en algún punto pero que no amerita el rechazo de este. - \&quot;Rechazado\&quot;: Corresponde a que el e-CF de la RI le fue rechazado al emisor. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
