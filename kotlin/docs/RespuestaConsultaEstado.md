
# RespuestaConsultaEstado

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **codigo** | [**RespuestaConsultaEstadoCodigo**](RespuestaConsultaEstadoCodigo.md) |  |  [optional] |
| **estado** | **kotlin.String** | Estado de validación otorgado por Impuestos Internos al e-CF recibido. Descripción textual del estado del comprobante fiscal electrónico. |  [optional] |
| **rncEmisor** | **kotlin.String** | Número de registro nacional del contribuyente que envió el e-CF. RNC del emisor del comprobante fiscal electrónico. |  [optional] |
| **ncfElectronico** | **kotlin.String** | Número de secuencia utilizada por el contribuyente en el e-CF. Número de comprobante fiscal electrónico (e-NCF) utilizado en la transacción. |  [optional] |
| **montoTotal** | [**RespuestaConsultaEstadoMontoTotal**](RespuestaConsultaEstadoMontoTotal.md) |  |  [optional] |
| **totalITBIS** | [**RespuestaConsultaEstadoTotalITBIS**](RespuestaConsultaEstadoTotalITBIS.md) |  |  [optional] |
| **fechaEmision** | **kotlin.String** | Fecha de emisión extraída del e-CF recibido. Fecha en que fue emitido el comprobante fiscal electrónico. |  [optional] |
| **fechaFirma** | **kotlin.String** | Fecha de firma extraída del e-CF recibido. Fecha en que fue firmado digitalmente el comprobante fiscal electrónico. |  [optional] |
| **rncComprador** | **kotlin.String** | RNC del comprador extraído del e-CF recibido (si aplica). Número de registro nacional del contribuyente comprador, cuando corresponde. |  [optional] |
| **codigoSeguridad** | **kotlin.String** | Código de seguridad extraído de los primeros seis (6) dígitos del hash generado  en el SignatureValue de la firma digital del e-CF recibido. Código de seguridad de 6 caracteres para validación del comprobante. |  [optional] |
| **idExtranjero** | **kotlin.String** | Identificación de extranjero extraída del e-CF recibido (si aplica). Número de identificación del comprador extranjero cuando corresponde. |  [optional] |



