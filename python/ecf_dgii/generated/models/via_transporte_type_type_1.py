from enum import Enum

class ViaTransporteTypeType1(str, Enum):
    VALUE_0 = "01"
    VALUE_1 = "02"
    VALUE_2 = "03"

    def __str__(self) -> str:
        return str(self.value)
