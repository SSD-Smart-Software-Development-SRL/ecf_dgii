from enum import Enum

class Ecf31TipoAjusteType(str, Enum):
    D = "D"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
