from enum import Enum

class IndicadorNorma1007TypeType1(str, Enum):
    INCLUIR = "Incluir"
    NOINCLUIR = "NoIncluir"

    def __str__(self) -> str:
        return str(self.value)
