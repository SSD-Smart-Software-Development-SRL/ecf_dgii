from enum import StrEnum


class CertificationStepType1(StrEnum):
    COMPLETED = "Completed"
    STEP1 = "Step1"
    STEP12 = "Step12"
    STEP13 = "Step13"
    STEP2 = "Step2"
    STEP3 = "Step3"
    STEP4 = "Step4"
    STEP5 = "Step5"
    STEP6 = "Step6"
    STEP7 = "Step7"
    STEP8 = "Step8"

    def __str__(self) -> str:
        return str(self.value)
