# # VentanaDeMantenimiento

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ambiente** | **string** | Nombre del ambiente donde aplica la ventana de mantenimiento. Valores posibles: - \&quot;PreCertificacion\&quot;: Ambiente de pre-certificación - \&quot;Certificacion\&quot;: Ambiente de certificación - \&quot;Produccion\&quot;: Ambiente de producción | [optional]
**hora_inicio** | **string** | Hora de inicio de la ventana de mantenimiento. Formato: \&quot;H:MM AM/PM\&quot; (ejemplo: \&quot;9:00 AM\&quot;, \&quot;1:00 PM\&quot;) | [optional]
**hora_fin** | **string** | Hora de fin de la ventana de mantenimiento. Formato: \&quot;H:MM AM/PM\&quot; (ejemplo: \&quot;12:00 PM\&quot;, \&quot;4:00 PM\&quot;) | [optional]
**dias** | **string[]** | Arreglo de fechas específicas cuando están programadas las ventanas de mantenimiento. Formato: \&quot;DD-MM-YYYY\&quot; (ejemplo: \&quot;06-08-2020\&quot;, \&quot;20-08-2020\&quot;) | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
