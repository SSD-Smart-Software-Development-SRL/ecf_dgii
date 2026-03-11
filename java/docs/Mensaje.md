

# Mensaje

Representa un mensaje asociado al estado de validación de un comprobante fiscal electrónico (e-CF). Este modelo se utiliza en las respuestas de consulta de resultado para proporcionar información detallada sobre el estado de procesamiento y cualquier mensaje relacionado.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**valor** | **String** | Obtiene el valor textual del mensaje que describe el estado o resultado de la validación. El texto descriptivo del mensaje. Puede ser null si no hay mensaje disponible. |  [optional] |
|**codigo** | [**MensajeCodigo**](MensajeCodigo.md) |  |  [optional] |



