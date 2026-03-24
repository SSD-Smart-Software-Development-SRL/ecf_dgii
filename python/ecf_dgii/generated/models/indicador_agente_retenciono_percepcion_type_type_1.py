from enum import Enum

class IndicadorAgenteRetencionoPercepcionTypeType1(str, Enum):
    PERCEPCION = "Percepcion"
    RETENCION = "Retencion"

    def __str__(self) -> str:
        return str(self.value)
