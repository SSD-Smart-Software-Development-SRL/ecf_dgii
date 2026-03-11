# # RespuestaAnulacionRango

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rnc** | **string** | Número de Registro Nacional del Contribuyente que envió la anulación.  Corresponde al RNC del contribuyente que solicitó la anulación de las secuencias. Este valor debe coincidir con el RNC autorizado para realizar transacciones de anulación y debe estar registrado como Facturador Electrónico en la DGII. | [optional]
**codigo** | **string** | Código asociado al resultado de la validación de la anulación.  Indica el código de estado del resultado de la operación de anulación. Los códigos proporcionan información sobre el éxito o fallo de la operación y los motivos específicos cuando hay errores. | [optional]
**nombre** | **string** | Razón social del contribuyente que realizó la anulación.  Nombre o razón social del contribuyente asociado al RNC que solicitó la anulación. Este campo proporciona información adicional para identificación del contribuyente y corresponde al nombre registrado en la DGII. | [optional]
**mensajes** | **string[]** | Mensajes asociados al resultado de la validación de la anulación.  Array de mensajes que proporcionan información detallada sobre el resultado de la operación. Puede incluir mensajes de éxito, advertencias, o errores específicos que ocurrieron durante el proceso de validación y anulación de las secuencias. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
