
# VentanaDeMantenimiento

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **ambiente** | **kotlin.String** | Nombre del ambiente donde aplica la ventana de mantenimiento. Valores posibles: - \&quot;PreCertificacion\&quot;: Ambiente de pre-certificación - \&quot;Certificacion\&quot;: Ambiente de certificación - \&quot;Produccion\&quot;: Ambiente de producción |  [optional] |
| **horaInicio** | **kotlin.String** | Hora de inicio de la ventana de mantenimiento. Formato: \&quot;H:MM AM/PM\&quot; (ejemplo: \&quot;9:00 AM\&quot;, \&quot;1:00 PM\&quot;) |  [optional] |
| **horaFin** | **kotlin.String** | Hora de fin de la ventana de mantenimiento. Formato: \&quot;H:MM AM/PM\&quot; (ejemplo: \&quot;12:00 PM\&quot;, \&quot;4:00 PM\&quot;) |  [optional] |
| **dias** | **kotlin.collections.List&lt;kotlin.String&gt;** | Arreglo de fechas específicas cuando están programadas las ventanas de mantenimiento. Formato: \&quot;DD-MM-YYYY\&quot; (ejemplo: \&quot;06-08-2020\&quot;, \&quot;20-08-2020\&quot;) |  [optional] |



