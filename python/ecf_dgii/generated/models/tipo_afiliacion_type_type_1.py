from enum import StrEnum


class TipoAfiliacionTypeType1(StrEnum):
    AFILIADA = "Afiliada"
    NOAFILIADA = "NoAfiliada"

    def __str__(self) -> str:
        return str(self.value)
