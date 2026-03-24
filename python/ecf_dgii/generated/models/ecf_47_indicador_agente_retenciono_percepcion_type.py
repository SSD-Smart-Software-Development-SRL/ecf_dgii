from enum import Enum

class Ecf47IndicadorAgenteRetencionoPercepcionType(str, Enum):
    PERCEPCION = "Percepcion"
    RETENCION = "Retencion"

    def __str__(self) -> str:
        return str(self.value)
