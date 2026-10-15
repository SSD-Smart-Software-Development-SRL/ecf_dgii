from enum import StrEnum


class IndicadorAgenteRetencionoPercepcionTypeType1(StrEnum):
    PERCEPCION = "Percepcion"
    RETENCION = "Retencion"

    def __str__(self) -> str:
        return str(self.value)
