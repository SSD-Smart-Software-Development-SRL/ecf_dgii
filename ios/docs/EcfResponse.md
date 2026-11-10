# EcfResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messageId** | **UUID** |  | 
**timestamp** | **Date** |  | 
**fechaEmision** | **Date** |  | 
**queueName** | **String** |  | 
**includeEcfContent** | **Bool** |  | 
**ecfContent** | **String** |  | 
**tipoEcf** | [**AllTipoECFTypes**](AllTipoECFTypes.md) |  | 
**encf** | **String** |  | 
**rncEmisor** | **String** |  | 
**rncReceptor** | **String** |  | 
**montoTotal** | [**SearchEcfsAmountFromParameter**](SearchEcfsAmountFromParameter.md) |  | 
**fileName** | **String** |  | 
**tenantId** | **UUID** |  | 
**estatus** | [**EcfEstado**](EcfEstado.md) |  | 
**codSec** | **String** |  | 
**fechaFirma** | **Date** |  | 
**mensaje** | **String** |  | 
**errors** | **String** |  | 
**progress** | [**EcfProgress**](EcfProgress.md) |  | 
**emisorReceptorErrors** | **String** |  | 
**secuenciaUtilizada** | **Bool** |  | 
**dgiiEnvironment** | [**DGIIEnvironment**](DGIIEnvironment.md) |  | 
**acecfs** | [AcecfSummaryDto] | ACECFs received from the receptor for this outbound ECF. | [optional] 
**receptorDirectoryStatus** | [**ReceptorDirectoryStatus**](ReceptorDirectoryStatus.md) |  | [optional] 
**dgiiSubmissionState** | [**DgiiSubmissionState**](DgiiSubmissionState.md) | Where the DGII transmission of this ECF stands. Null for documents created before durable submission. &#x60;PendingReconciliation&#x60;: DGII&#39;s answer is not confirmed yet; do not resend or reuse the eNCF. &#x60;NotReceived&#x60;: DGII confirmed it has no record of the document (Progress is Error, Estatus is null and SecuenciaUtilizada is false); the same eNCF may be submitted again as a new request. | [optional] 
**impresionUrl** | **String** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


