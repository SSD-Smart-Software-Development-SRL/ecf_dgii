from enum import StrEnum


class DGIIEnvironment(StrEnum):
    CERTIFICATION = "Certification"
    PRODUCTION = "Production"
    TEST = "Test"

    def __str__(self) -> str:
        return str(self.value)
