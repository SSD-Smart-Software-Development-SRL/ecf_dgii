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
**impresionUrl** | **String** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


