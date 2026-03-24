from enum import Enum

class Ecf46TipoDescuentoRecargoType(str, Enum):
    VALUE_0 = "$"
    VALUE_1 = "%"

    def __str__(self) -> str:
        return str(self.value)
