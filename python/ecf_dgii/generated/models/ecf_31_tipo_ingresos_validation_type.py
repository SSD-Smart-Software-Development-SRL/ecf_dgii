from enum import Enum

class Ecf31TipoIngresosValidationType(str, Enum):
    VALUE_0 = "01"
    VALUE_1 = "02"
    VALUE_2 = "03"
    VALUE_3 = "04"
    VALUE_4 = "05"
    VALUE_5 = "06"

    def __str__(self) -> str:
        return str(self.value)
