from enum import StrEnum


class ViaTransporteTypeType1(StrEnum):
    VALUE_0 = "01"
    VALUE_1 = "02"
    VALUE_2 = "03"

    def __str__(self) -> str:
        return str(self.value)
