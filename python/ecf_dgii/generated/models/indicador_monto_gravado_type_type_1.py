from enum import StrEnum


class IndicadorMontoGravadoTypeType1(StrEnum):
    CONITBISINCLUIDO = "ConITBISIncluido"
    SINITBISINCLUIDO = "SinITBISIncluido"

    def __str__(self) -> str:
        return str(self.value)
