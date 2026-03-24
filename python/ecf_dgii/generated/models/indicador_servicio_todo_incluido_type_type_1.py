from enum import Enum

class IndicadorServicioTodoIncluidoTypeType1(str, Enum):
    INDICADORSERVICIOTODOINCLUIDO = "IndicadorServicioTodoIncluido"

    def __str__(self) -> str:
        return str(self.value)
