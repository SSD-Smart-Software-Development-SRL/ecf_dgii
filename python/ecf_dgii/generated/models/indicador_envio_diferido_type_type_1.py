from enum import StrEnum


class IndicadorEnvioDiferidoTypeType1(StrEnum):
    ENVIODIFERIDOAUTORIZADO = "EnvioDiferidoAutorizado"

    def __str__(self) -> str:
        return str(self.value)
