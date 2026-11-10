
# EcfResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **messageId** | [**java.util.UUID**](java.util.UUID.md) |  |  |
| **timestamp** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  |
| **fechaEmision** | [**java.time.LocalDate**](java.time.LocalDate.md) |  |  |
| **queueName** | **kotlin.String** |  |  |
| **includeEcfContent** | **kotlin.Boolean** |  |  |
| **ecfContent** | **kotlin.String** |  |  |
| **tipoEcf** | [**AllTipoECFTypes**](AllTipoECFTypes.md) |  |  |
| **encf** | **kotlin.String** |  |  |
| **rncEmisor** | **kotlin.String** |  |  |
| **montoTotal** | **kotlin.Double** |  |  |
| **tenantId** | [**java.util.UUID**](java.util.UUID.md) |  |  |
| **progress** | [**EcfProgress**](EcfProgress.md) |  |  |
| **dgiiEnvironment** | [**DGIIEnvironment**](DGIIEnvironment.md) |  |  |
| **rncReceptor** | **kotlin.String** |  |  [optional] |
| **fileName** | **kotlin.String** |  |  [optional] |
| **estatus** | [**EcfEstado**](EcfEstado.md) |  |  [optional] |
| **codSec** | **kotlin.String** |  |  [optional] |
| **fechaFirma** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **mensaje** | **kotlin.String** |  |  [optional] |
| **errors** | **kotlin.String** |  |  [optional] |
| **emisorReceptorErrors** | **kotlin.String** |  |  [optional] |
| **secuenciaUtilizada** | **kotlin.Boolean** |  |  [optional] |
| **acecfs** | [**kotlin.collections.List&lt;AcecfSummaryDto&gt;**](AcecfSummaryDto.md) | ACECFs received from the receptor for this outbound ECF. |  [optional] |
| **receptorDirectoryStatus** | [**ReceptorDirectoryStatus**](ReceptorDirectoryStatus.md) |  |  [optional] |
| **dgiiSubmissionState** | [**DgiiSubmissionState**](DgiiSubmissionState.md) | Where the DGII transmission of this ECF stands. Null for documents created before durable submission. &#x60;PendingReconciliation&#x60;: DGII&#39;s answer is not confirmed yet; do not resend or reuse the eNCF. &#x60;NotReceived&#x60;: DGII confirmed it has no record of the document (Progress is Error, Estatus is null and SecuenciaUtilizada is false); the same eNCF may be submitted again as a new request. |  [optional] |
| **impresionUrl** | **kotlin.String** |  |  [optional] |



