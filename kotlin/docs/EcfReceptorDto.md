
# EcfReceptorDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **ecfReceptorId** | [**java.util.UUID**](java.util.UUID.md) |  |  [optional] |
| **tenantId** | [**java.util.UUID**](java.util.UUID.md) |  |  [optional] |
| **companyRnc** | **kotlin.String** |  |  [optional] |
| **encf** | **kotlin.String** |  |  [optional] |
| **rncEmisor** | **kotlin.String** |  |  [optional] |
| **rncReceptor** | **kotlin.String** |  |  [optional] |
| **tipoEcf** | [**AllTipoECFTypes**](AllTipoECFTypes.md) |  |  [optional] |
| **montoTotal** | [**SearchEcfsAmountFromParameter**](SearchEcfsAmountFromParameter.md) |  |  [optional] |
| **fechaEmision** | [**java.time.LocalDate**](java.time.LocalDate.md) |  |  [optional] |
| **fileName** | **kotlin.String** |  |  [optional] |
| **rawJsonData** | **kotlin.String** |  |  [optional] |
| **createdOn** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **fechaFirma** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **codSec** | **kotlin.String** |  |  [optional] |
| **estado** | [**EcfReceptorDtoEstado**](EcfReceptorDtoEstado.md) |  |  [optional] |
| **progress** | [**EcfReceptorDtoProgress**](EcfReceptorDtoProgress.md) |  |  [optional] |
| **ambiente** | **kotlin.String** | DGII environment serving this tenant (\&quot;Test\&quot;/\&quot;Certification\&quot;/\&quot;Production\&quot;). |  [optional] |
| **urlImpresion** | **kotlin.String** | DGII consulta-timbre URL with QR query string. |  [optional] |
| **acecfs** | [**kotlin.collections.List&lt;AcecfSummaryDto&gt;**](AcecfSummaryDto.md) |  |  [optional] |



