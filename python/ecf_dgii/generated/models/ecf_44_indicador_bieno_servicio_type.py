from enum import StrEnum


class Ecf44IndicadorBienoServicioType(StrEnum):
    BIEN = "Bien"
    SERVICIO = "Servicio"

    def __str__(self) -> str:
        return str(self.value)
