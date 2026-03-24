from enum import Enum

class TipoCuentaPagoTypeType1(str, Enum):
    AH = "AH"
    CT = "CT"
    OT = "OT"

    def __str__(self) -> str:
        return str(self.value)
