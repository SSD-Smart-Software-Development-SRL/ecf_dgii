

# CertificationStateResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**state** | **String** | One of CertificationStates. |  [optional] |
|**source** | **String** | One of CertificationStateSources; null while not started. |  [optional] |
|**step** | **CertificationStep** | Internal step (in progress, error). |  [optional] |
|**stepNumber** | [**CertificationStateResponseStepNumber**](CertificationStateResponseStepNumber.md) |  |  [optional] |
|**totalSteps** | [**SearchEcfReceptionRequestsTiposEcfsParameterInner**](SearchEcfReceptionRequestsTiposEcfsParameterInner.md) |  |  [optional] |
|**responsible** | **String** | One of CertificationResponsibles while in progress. |  [optional] |
|**stalled** | **Boolean** | In progress without any activity for int CertificationStateCalculator.StalledAfterDays days. |  [optional] |
|**lastActivityOn** | **Date** |  |  [optional] |
|**certifiedOn** | **Date** | DGII authorisation date, when known (DGII listing or declared by the customer). |  [optional] |
|**changedOn** | **Date** | When the stored state last changed. |  [optional] |
|**signatureReviewPending** | **Boolean** | A step was signed outside the platform and the signature could not be verified (CERT-04). |  [optional] |



