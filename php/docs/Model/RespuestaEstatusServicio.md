# # RespuestaEstatusServicio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicio** | **string** | Nombre del servicio de facturación electrónica. Valores posibles incluyen: - \&quot;Autenticación\&quot; - \&quot;Recepción\&quot; - \&quot;Consulta Resultado\&quot; - \&quot;Consulta Estado\&quot; - \&quot;Consulta Directorio\&quot; - \&quot;Consulta TrackIds\&quot; - \&quot;Aprobación Comercial\&quot; - \&quot;Anulación Rangos\&quot; - \&quot;Recepción FC\&quot; | [optional]
**status** | **string** | Estado actual del servicio. Valores posibles: - \&quot;Disponible\&quot;: El servicio está disponible y operativo - \&quot;No Disponible\&quot;: El servicio no está disponible (probablemente en mantenimiento) | [optional]
**ambiente** | **string** | Ambiente donde opera el servicio. Valores posibles: - \&quot;PreCertificacion\&quot;: Ambiente de pre-certificación - \&quot;Certificacion\&quot;: Ambiente de certificación - \&quot;Produccion\&quot;: Ambiente de producción | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
