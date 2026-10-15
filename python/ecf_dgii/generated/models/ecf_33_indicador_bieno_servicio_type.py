from enum import StrEnum


class Ecf33IndicadorBienoServicioType(StrEnum):
    BIEN = "Bien"
    SERVICIO = "Servicio"

    def __str__(self) -> str:
        return str(self.value)
