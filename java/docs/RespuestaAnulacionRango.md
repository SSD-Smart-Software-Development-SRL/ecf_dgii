

# RespuestaAnulacionRango

Respuesta de anulación de rango de secuencias de e-NCF.  Representa la respuesta del servicio de anulación de rangos de secuencias de comprobantes fiscales electrónicos. Este modelo se utiliza para procesar la respuesta del servicio web de anulación de e-NCF de la DGII.  Servicio Web:• Endpoint: /api/operaciones/anularrango• Método: POST• Formato de entrada: XML (formato ANECF)• Formato de respuesta: JSON o XMLValidaciones del Servicio:• Tipo de archivo válido (XML)• Firma del documento válida• Tipo de comprobante válido• Secuencias no utilizadas previamente• RNC autorizado para realizar transaccionesReferencia Oficial:• Descripción Técnica de Facturación Electrónica v1.6, Sección \"Anulación de e-NCF\"• Formato Anulación de e-NCF v1.0 - DGII

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rnc** | **String** | Número de Registro Nacional del Contribuyente que envió la anulación.  Corresponde al RNC del contribuyente que solicitó la anulación de las secuencias. Este valor debe coincidir con el RNC autorizado para realizar transacciones de anulación y debe estar registrado como Facturador Electrónico en la DGII. |  [optional] |
|**codigo** | **String** | Código asociado al resultado de la validación de la anulación.  Indica el código de estado del resultado de la operación de anulación. Los códigos proporcionan información sobre el éxito o fallo de la operación y los motivos específicos cuando hay errores. |  [optional] |
|**nombre** | **String** | Razón social del contribuyente que realizó la anulación.  Nombre o razón social del contribuyente asociado al RNC que solicitó la anulación. Este campo proporciona información adicional para identificación del contribuyente y corresponde al nombre registrado en la DGII. |  [optional] |
|**mensajes** | **List&lt;String&gt;** | Mensajes asociados al resultado de la validación de la anulación.  Array de mensajes que proporcionan información detallada sobre el resultado de la operación. Puede incluir mensajes de éxito, advertencias, o errores específicos que ocurrieron durante el proceso de validación y anulación de las secuencias. |  [optional] |



