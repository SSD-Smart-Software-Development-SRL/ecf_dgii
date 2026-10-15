from enum import StrEnum


class Ecf41TipoAjusteType(StrEnum):
    D = "D"
    R = "R"

    def __str__(self) -> str:
        return str(self.value)
