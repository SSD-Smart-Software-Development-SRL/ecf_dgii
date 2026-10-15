from enum import StrEnum


class IndicadorNorma1007TypeType1(StrEnum):
    INCLUIR = "Incluir"
    NOINCLUIR = "NoIncluir"

    def __str__(self) -> str:
        return str(self.value)
