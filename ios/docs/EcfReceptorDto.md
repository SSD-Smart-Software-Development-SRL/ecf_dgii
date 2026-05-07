# EcfReceptorDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecfReceptorId** | **UUID** |  | [optional] 
**tenantId** | **UUID** |  | [optional] 
**companyRnc** | **String** |  | [optional] 
**encf** | **String** |  | [optional] 
**rncEmisor** | **String** |  | [optional] 
**rncReceptor** | **String** |  | [optional] 
**tipoEcf** | [**AllTipoECFTypes**](AllTipoECFTypes.md) |  | [optional] 
**montoTotal** | [**SearchEcfsAmountFromParameter**](SearchEcfsAmountFromParameter.md) |  | [optional] 
**fechaEmision** | **Date** |  | [optional] 
**fileName** | **String** |  | [optional] 
**rawJsonData** | **String** |  | [optional] 
**createdOn** | **Date** |  | [optional] 
**fechaFirma** | **Date** |  | [optional] 
**codSec** | **String** |  | [optional] 
**estado** | [**EcfReceptorDtoEstado**](EcfReceptorDtoEstado.md) |  | [optional] 
**progress** | [**EcfReceptorDtoProgress**](EcfReceptorDtoProgress.md) |  | [optional] 
**ambiente** | **String** | DGII environment serving this tenant (\&quot;Test\&quot;/\&quot;Certification\&quot;/\&quot;Production\&quot;). | [optional] 
**urlImpresion** | **String** | DGII consulta-timbre URL with QR query string. | [optional] 
**acecfs** | [AcecfSummaryDto] |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


