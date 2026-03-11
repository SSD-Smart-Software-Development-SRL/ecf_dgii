# # RespuestaConsultaEstado

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codigo** | [**\Ecfx\EcfDgii\Model\RespuestaConsultaEstadoCodigo**](RespuestaConsultaEstadoCodigo.md) |  | [optional]
**estado** | **string** | Estado de validación otorgado por Impuestos Internos al e-CF recibido. Descripción textual del estado del comprobante fiscal electrónico. | [optional]
**rnc_emisor** | **string** | Número de registro nacional del contribuyente que envió el e-CF. RNC del emisor del comprobante fiscal electrónico. | [optional]
**ncf_electronico** | **string** | Número de secuencia utilizada por el contribuyente en el e-CF. Número de comprobante fiscal electrónico (e-NCF) utilizado en la transacción. | [optional]
**monto_total** | [**\Ecfx\EcfDgii\Model\RespuestaConsultaEstadoMontoTotal**](RespuestaConsultaEstadoMontoTotal.md) |  | [optional]
**total_itbis** | [**\Ecfx\EcfDgii\Model\RespuestaConsultaEstadoTotalITBIS**](RespuestaConsultaEstadoTotalITBIS.md) |  | [optional]
**fecha_emision** | **string** | Fecha de emisión extraída del e-CF recibido. Fecha en que fue emitido el comprobante fiscal electrónico. | [optional]
**fecha_firma** | **string** | Fecha de firma extraída del e-CF recibido. Fecha en que fue firmado digitalmente el comprobante fiscal electrónico. | [optional]
**rnc_comprador** | **string** | RNC del comprador extraído del e-CF recibido (si aplica). Número de registro nacional del contribuyente comprador, cuando corresponde. | [optional]
**codigo_seguridad** | **string** | Código de seguridad extraído de los primeros seis (6) dígitos del hash generado  en el SignatureValue de la firma digital del e-CF recibido. Código de seguridad de 6 caracteres para validación del comprobante. | [optional]
**id_extranjero** | **string** | Identificación de extranjero extraída del e-CF recibido (si aplica). Número de identificación del comprador extranjero cuando corresponde. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
