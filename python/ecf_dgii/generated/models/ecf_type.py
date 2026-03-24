from enum import Enum

class ECFType(str, Enum):
    ECF31 = "ECF31"
    ECF32 = "ECF32"
    ECF33 = "ECF33"
    ECF34 = "ECF34"
    ECF41 = "ECF41"
    ECF43 = "ECF43"
    ECF44 = "ECF44"
    ECF45 = "ECF45"
    ECF46 = "ECF46"
    ECF47 = "ECF47"

    def __str__(self) -> str:
        return str(self.value)
