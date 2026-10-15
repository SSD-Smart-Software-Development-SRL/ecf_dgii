from enum import StrEnum


class TipoCuentaPagoTypeType1(StrEnum):
    AH = "AH"
    CT = "CT"
    OT = "OT"

    def __str__(self) -> str:
        return str(self.value)
