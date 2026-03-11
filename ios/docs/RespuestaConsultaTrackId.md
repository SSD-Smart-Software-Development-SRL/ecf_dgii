# RespuestaConsultaTrackId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trackId** | **String** | Obtiene el número único generado por Impuestos Internos para identificar un e-CF recibido. Este identificador se obtiene como respuesta del servicio de recepción de e-CF. El identificador único del track. Puede ser null si no está disponible. | [optional] 
**codigo** | **String** | Obtiene el código asociado al estado de validación del e-CF recibido. Un código que indica el resultado de la validación. Los valores típicos son: - \&quot;0\&quot;: No encontrado - \&quot;1\&quot;: Aceptado - \&quot;2\&quot;: Rechazado - \&quot;3\&quot;: En Proceso - \&quot;4\&quot;: Aceptado Condicional | [optional] 
**estado** | **String** | Obtiene el estado de validación otorgado por Impuestos Internos al e-CF recibido. Descripción textual del estado. Puede incluir valores como: - \&quot;No encontrado\&quot;: No se encontró el trackid en los registros - \&quot;Aceptado\&quot;: Implica la validez del e-CF - \&quot;Rechazado\&quot;: Implica la nulidad del comprobante para fines tributarios - \&quot;En Proceso\&quot;: El comprobante aún no ha sido validado - \&quot;Aceptado Condicional\&quot;: El comprobante no cumplió en algún punto pero no ameritó el rechazo | [optional] 
**rnc** | **String** | Obtiene el número de registro nacional del contribuyente que envió el e-CF. El RNC del emisor del comprobante. Puede ser null si no está disponible. | [optional] 
**encf** | **String** | Obtiene el número de secuencia utilizada por el contribuyente en el e-CF. El número de comprobante fiscal electrónico (e-NCF). Puede ser null si no está disponible. | [optional] 
**secuenciaUtilizada** | **Bool** | Indica si el número de secuencia puede ser reutilizada en otro e-CF. True si la secuencia puede reutilizarse, False si no puede reutilizarse.  Este parámetro permite dar a conocer si el número de secuencia que fue recibido por Impuestos Internos puede reutilizarse en otro Comprobante Fiscal Electrónico (e-CF) en el escenario de que el resultado de la validación haya sido \&quot;Rechazado\&quot; por los siguientes motivos: - Certificado y/o firma inválida - Estructura del comprobante (XML) no es válida - Firmante del comprobante fiscal electrónico no corresponde a un delegado autorizado - El e-NCF no está autorizado para el RNC Emisor - El e-NCF autorizado se encuentra vencido - El RNC Emisor no corresponde a un emisor electrónico - El RNC Emisor no existe o no se encuentra activo | [optional] 
**fechaRecepcion** | **String** | Obtiene la fecha en la cual Impuestos Internos recibió el e-CF. La fecha de recepción del comprobante. Puede ser null si no está disponible. El formato típico es ISO 8601 o un formato de fecha legible. | [optional] 
**mensajes** | [Mensaje] | Obtiene los mensajes asociados al estado de validación del e-CF recibido. Un array de mensajes que proporcionan información detallada sobre el estado de validación. Puede ser null si no hay mensajes disponibles. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


