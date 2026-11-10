
# EcfReceptionRequestDto

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **messageId** | [**java.util.UUID**](java.util.UUID.md) |  |  [optional] |
| **tenantId** | [**java.util.UUID**](java.util.UUID.md) |  |  [optional] |
| **companyRnc** | **kotlin.String** |  |  [optional] |
| **fileName** | **kotlin.String** |  |  [optional] |
| **progress** | **kotlin.Int** |  |  [optional] |
| **createdOn** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **updatedOn** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **errorMessage** | **kotlin.String** |  |  [optional] |
| **encf** | **kotlin.String** |  |  [optional] |
| **rncEmisor** | **kotlin.String** |  |  [optional] |
| **tipoEcf** | [**AllTipoECFTypes**](AllTipoECFTypes.md) |  |  [optional] |
| **resultInternalFileName** | **kotlin.String** |  |  [optional] |
| **montoTotal** | [**EcfReceptionRequestDtoMontoTotal**](EcfReceptionRequestDtoMontoTotal.md) |  |  [optional] |
| **reprocessedOn** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) | When the reception was run again after it ended without registering the e-CF. |  [optional] |
| **recuperada** | **kotlin.Boolean** | True when the first reception failed and the e-CF was registered by running it again, so the UI can flag it as recovered. |  [optional] |



