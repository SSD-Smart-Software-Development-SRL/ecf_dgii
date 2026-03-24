from enum import Enum

class IndicadorMontoGravadoTypeType1(str, Enum):
    CONITBISINCLUIDO = "ConITBISIncluido"
    SINITBISINCLUIDO = "SinITBISIncluido"

    def __str__(self) -> str:
        return str(self.value)
