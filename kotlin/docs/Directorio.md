
# Directorio

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **nombre** | **kotlin.String** | Obtiene el nombre legal o razón social del contribuyente electrónico. La razón social registrada tal como aparece en el registro oficial del contribuyente. Este campo es requerido y debe coincidir con el nombre de la entidad legal del contribuyente. |  [optional] |
| **rnc** | **kotlin.String** | Obtiene el Número de Registro Nacional del Contribuyente (RNC) del contribuyente electrónico. Un número de 9 dígitos que identifica de forma única al contribuyente en el sistema tributario  de la República Dominicana. Este campo es requerido y debe tener un formato de RNC válido. |  [optional] |
| **urlRecepcion** | **kotlin.String** | Obtiene la URL del servicio de recepción de facturas electrónicas. La URL completa donde otros contribuyentes pueden enviar facturas electrónicas (e-CF) a este contribuyente. Debe seguir el formato estándar: https://host/ambiente/nombreservicio/fe/recepcion/api/ecf Este campo es obligatorio para todos los contribuyentes electrónicos. |  [optional] |
| **urlAceptacion** | **kotlin.String** | Obtiene la URL del servicio de aprobación comercial. La URL completa donde otros contribuyentes pueden enviar aprobaciones comerciales para facturas recibidas. Debe seguir el formato estándar: https://host/ambiente/nombreservicio/fe/aprobacioncomercial/api/ecf Este campo es obligatorio para todos los contribuyentes electrónicos. |  [optional] |
| **urlOpcional** | **kotlin.String** | Obtiene la URL del servicio opcional de autenticación. La URL base del servicio de autenticación, si es implementado por el contribuyente. Debe seguir el formato estándar: https://host/ambiente/nombreservicio/fe/autenticacion/api/ Este campo es opcional pero recomendado para mayor seguridad. |  [optional] |



