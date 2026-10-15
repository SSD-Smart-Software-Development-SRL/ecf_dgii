from enum import StrEnum


class Ecf33TipoAjusteType(StrEnum):
    D = "D"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
