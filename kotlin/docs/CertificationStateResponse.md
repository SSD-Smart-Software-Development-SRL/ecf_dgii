
# CertificationStateResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **state** | **kotlin.String** | One of CertificationStates. |  [optional] |
| **source** | **kotlin.String** | One of CertificationStateSources; null while not started. |  [optional] |
| **step** | [**CertificationStep**](CertificationStep.md) | Internal step (in progress, error). |  [optional] |
| **stepNumber** | [**CertificationStateResponseStepNumber**](CertificationStateResponseStepNumber.md) |  |  [optional] |
| **totalSteps** | **kotlin.Int** |  |  [optional] |
| **responsible** | **kotlin.String** | One of CertificationResponsibles while in progress. |  [optional] |
| **stalled** | **kotlin.Boolean** | In progress without any activity for int CertificationStateCalculator.StalledAfterDays days. |  [optional] |
| **lastActivityOn** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) |  |  [optional] |
| **certifiedOn** | [**java.time.LocalDate**](java.time.LocalDate.md) | DGII authorisation date, when known (DGII listing or declared by the customer). |  [optional] |
| **changedOn** | [**java.time.OffsetDateTime**](java.time.OffsetDateTime.md) | When the stored state last changed. |  [optional] |
| **signatureReviewPending** | **kotlin.Boolean** | A step was signed outside the platform and the signature could not be verified (CERT-04). |  [optional] |



