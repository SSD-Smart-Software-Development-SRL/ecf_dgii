from enum import Enum

class IndicadorEnvioDiferidoTypeType1(str, Enum):
    ENVIODIFERIDOAUTORIZADO = "EnvioDiferidoAutorizado"

    def __str__(self) -> str:
        return str(self.value)
