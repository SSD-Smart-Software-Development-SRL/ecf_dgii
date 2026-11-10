

# EcfReceptionRequestDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messageId** | **UUID** |  |  [optional] |
|**tenantId** | **UUID** |  |  [optional] |
|**companyRnc** | **String** |  |  [optional] |
|**fileName** | **String** |  |  [optional] |
|**progress** | [**SearchEcfReceptionRequestsTiposEcfsParameterInner**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md) |  |  [optional] |
|**createdOn** | **Date** |  |  [optional] |
|**updatedOn** | **Date** |  |  [optional] |
|**errorMessage** | **String** |  |  [optional] |
|**encf** | **String** |  |  [optional] |
|**rncEmisor** | **String** |  |  [optional] |
|**tipoEcf** | **AllTipoECFTypes** |  |  [optional] |
|**resultInternalFileName** | **String** |  |  [optional] |
|**montoTotal** | [**EcfReceptionRequestDtoMontoTotal**](EcfReceptionRequestDtoMontoTotal.md) |  |  [optional] |
|**reprocessedOn** | **Date** | When the reception was run again after it ended without registering the e-CF. |  [optional] |
|**recuperada** | **Boolean** | True when the first reception failed and the e-CF was registered by running it again, so the UI can flag it as recovered. |  [optional] |



