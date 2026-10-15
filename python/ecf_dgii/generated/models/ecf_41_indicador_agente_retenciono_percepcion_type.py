from enum import StrEnum


class Ecf41IndicadorAgenteRetencionoPercepcionType(StrEnum):
    PERCEPCION = "Percepcion"
    RETENCION = "Retencion"

    def __str__(self) -> str:
        return str(self.value)
