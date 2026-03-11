# RespuestaConsultaEstado

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codigo** | **Int** | Código asociado al estado de validación del e-CF recibido.             Posibles valores:             * 0No encontrado - No se encontró el comprobante en los registros * 1Aceptado - El e-CF generado por el emisor fue aceptado y tiene validez fiscal * 2Rechazado - Corresponde a la nulidad del comprobante generado por el emisor | [optional] 
**estado** | **String** | Estado de validación otorgado por Impuestos Internos al e-CF recibido. Descripción textual del estado del comprobante fiscal electrónico. | [optional] 
**rncEmisor** | **String** | Número de registro nacional del contribuyente que envió el e-CF. RNC del emisor del comprobante fiscal electrónico. | [optional] 
**ncfElectronico** | **String** | Número de secuencia utilizada por el contribuyente en el e-CF. Número de comprobante fiscal electrónico (e-NCF) utilizado en la transacción. | [optional] 
**montoTotal** | **Double** | Monto total extraído del e-CF recibido. Valor total de la transacción en pesos dominicanos. | [optional] 
**totalITBIS** | **Double** | Total de ITBIS extraído del e-CF recibido. Monto total del Impuesto sobre Transferencias de Bienes Industrializados y Servicios. | [optional] 
**fechaEmision** | **String** | Fecha de emisión extraída del e-CF recibido. Fecha en que fue emitido el comprobante fiscal electrónico. | [optional] 
**fechaFirma** | **String** | Fecha de firma extraída del e-CF recibido. Fecha en que fue firmado digitalmente el comprobante fiscal electrónico. | [optional] 
**rncComprador** | **String** | RNC del comprador extraído del e-CF recibido (si aplica). Número de registro nacional del contribuyente comprador, cuando corresponde. | [optional] 
**codigoSeguridad** | **String** | Código de seguridad extraído de los primeros seis (6) dígitos del hash generado  en el SignatureValue de la firma digital del e-CF recibido. Código de seguridad de 6 caracteres para validación del comprobante. | [optional] 
**idExtranjero** | **String** | Identificación de extranjero extraída del e-CF recibido (si aplica). Número de identificación del comprador extranjero cuando corresponde. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


