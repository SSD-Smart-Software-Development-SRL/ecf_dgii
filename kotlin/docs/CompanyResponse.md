
# CompanyResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **rnc** | **kotlin.String** |  |  [optional] |
| **legalName** | **kotlin.String** |  |  [optional] |
| **name** | **kotlin.String** |  |  [optional] |
| **createdOn** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **updatedOn** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **createdBy** | **kotlin.String** |  |  [optional] |
| **updatedBy** | **kotlin.String** |  |  [optional] |
| **tenantId** | [**java.util.UUID**](java.util.UUID.md) |  |  [optional] |
| **receptorId** | **kotlin.String** |  |  [optional] |
| **urls** | [**CompanyUrlsResponse**](CompanyUrlsResponse.md) |  |  [optional] |
| **certification** | [**CertificationStateResponse**](CertificationStateResponse.md) | CERT-01: the company&#39;s certification state. |  [optional] |
| **archivedAt** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) | When the company was archived; null while it is active. |  [optional] |
| **archivedBy** | **kotlin.String** | Who archived it and why, the last time it was archived; kept after a restore as history. |  [optional] |
| **archiveReason** | **kotlin.String** |  |  [optional] |



