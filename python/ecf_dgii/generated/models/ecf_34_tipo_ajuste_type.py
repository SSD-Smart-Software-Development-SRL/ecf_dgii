from enum import StrEnum


class Ecf34TipoAjusteType(StrEnum):
    D = "D"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
