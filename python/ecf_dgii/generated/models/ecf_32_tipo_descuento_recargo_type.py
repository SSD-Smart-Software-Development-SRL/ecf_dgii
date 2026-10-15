from enum import StrEnum


class Ecf32TipoDescuentoRecargoType(StrEnum):
    VALUE_0 = "$"
    VALUE_1 = "%"

    def __str__(self) -> str:
        return str(self.value)
