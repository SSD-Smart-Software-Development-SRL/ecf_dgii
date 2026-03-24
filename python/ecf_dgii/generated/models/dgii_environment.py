from enum import Enum

class DGIIEnvironment(str, Enum):
    CERTIFICATION = "Certification"
    PRODUCTION = "Production"
    TEST = "Test"

    def __str__(self) -> str:
        return str(self.value)
