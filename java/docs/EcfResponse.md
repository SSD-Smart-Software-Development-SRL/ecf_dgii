

# EcfResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageId** | **UUID** |  |  |
|**timestamp** | **Date** |  |  |
|**fechaEmision** | **Date** |  |  |
|**queueName** | **String** |  |  |
|**includeEcfContent** | **Boolean** |  |  |
|**ecfContent** | **String** |  |  |
|**tipoEcf** | **AllTipoECFTypes** |  |  |
|**encf** | **String** |  |  |
|**rncEmisor** | **String** |  |  |
|**rncReceptor** | **String** |  |  [optional] |
|**montoTotal** | [**SearchEcfsAmountFromParameter**](SearchEcfsAmountFromParameter.md) |  |  |
|**fileName** | **String** |  |  [optional] |
|**tenantId** | **UUID** |  |  |
|**estatus** | **EcfEstado** |  |  [optional] |
|**codSec** | **String** |  |  [optional] |
|**fechaFirma** | **Date** |  |  [optional] |
|**mensaje** | **String** |  |  [optional] |
|**errors** | **String** |  |  [optional] |
|**progress** | **EcfProgress** |  |  |
|**emisorReceptorErrors** | **String** |  |  [optional] |
|**secuenciaUtilizada** | **Boolean** |  |  [optional] |
|**dgiiEnvironment** | **DGIIEnvironment** |  |  |
|**acecfs** | [**List&lt;AcecfSummaryDto&gt;**](AcecfSummaryDto.md) | ACECFs received from the receptor for this outbound ECF. |  [optional] |
|**receptorDirectoryStatus** | **ReceptorDirectoryStatus** |  |  [optional] |
|**dgiiSubmissionState** | **DgiiSubmissionState** | Where the DGII transmission of this ECF stands. Null for documents created before durable submission. &#x60;PendingReconciliation&#x60;: DGII&#39;s answer is not confirmed yet; do not resend or reuse the eNCF. &#x60;NotReceived&#x60;: DGII confirmed it has no record of the document (Progress is Error, Estatus is null and SecuenciaUtilizada is false); the same eNCF may be submitted again as a new request. |  [optional] |
|**impresionUrl** | **String** |  |  [optional] |



