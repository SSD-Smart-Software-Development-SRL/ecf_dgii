

# CompanyResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rnc** | **String** |  |  [optional] |
|**legalName** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**createdOn** | **Date** |  |  [optional] |
|**updatedOn** | **Date** |  |  [optional] |
|**createdBy** | **String** |  |  [optional] |
|**updatedBy** | **String** |  |  [optional] |
|**tenantId** | **UUID** |  |  [optional] |
|**receptorId** | **String** |  |  [optional] |
|**urls** | [**CompanyUrlsResponse**](CompanyUrlsResponse.md) |  |  [optional] |
|**certification** | [**CertificationStateResponse**](CertificationStateResponse.md) | CERT-01: the company&#39;s certification state. |  [optional] |
|**archivedAt** | **Date** | When the company was archived; null while it is active. |  [optional] |
|**archivedBy** | **String** | Who archived it and why, the last time it was archived; kept after a restore as history. |  [optional] |
|**archiveReason** | **String** |  |  [optional] |



