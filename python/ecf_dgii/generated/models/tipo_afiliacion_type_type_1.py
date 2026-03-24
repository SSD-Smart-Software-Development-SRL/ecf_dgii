from enum import Enum

class TipoAfiliacionTypeType1(str, Enum):
    AFILIADA = "Afiliada"
    NOAFILIADA = "NoAfiliada"

    def __str__(self) -> str:
        return str(self.value)
