# # RespuestaConsultaRFCE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rnc** | **string** | Número de registro nacional del contribuyente que envió el e-CF. RNC del emisor del comprobante fiscal electrónico consultado. | [optional]
**encf** | **string** | Número de secuencia utilizada por el contribuyente en el ENCF. Número de comprobante fiscal electrónico (e-NCF) consultado. | [optional]
**secuencia_utilizada** | **bool** | Indica si el número de secuencia puede ser reutilizado. &#x60;true&#x60; si la secuencia NO puede reutilizarse (rechazado por motivos específicos);         &#x60;false&#x60; si la secuencia SÍ puede reutilizarse. | [optional]
**codigo** | **string** | Código asociado al estado de validación del e-CF recibido. Código numérico que indica el resultado de la validación: - 0: No encontrado - 1: Aceptado - 2: Rechazado - 4: Aceptado Condicional (solo para FC &amp;lt; RD$ 250000.00) | [optional]
**estado** | **string** | Estado de validación otorgado por Impuestos Internos al e-CF recibido. Descripción textual del estado de validación del comprobante. | [optional]
**mensajes** | [**\Ecfx\EcfDgii\Model\Mensaje[]**](Mensaje.md) | Mensajes y códigos asociados al estado de validación del e-CF recibido. Array de mensajes que proporcionan detalles adicionales sobre la validación. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
