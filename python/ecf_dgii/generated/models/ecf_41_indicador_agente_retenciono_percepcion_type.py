from enum import Enum

class Ecf41IndicadorAgenteRetencionoPercepcionType(str, Enum):
    PERCEPCION = "Percepcion"
    RETENCION = "Retencion"

    def __str__(self) -> str:
        return str(self.value)
