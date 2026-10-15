from enum import StrEnum


class Ecf46IndicadorBienoServicioType(StrEnum):
    BIEN = "Bien"
    SERVICIO = "Servicio"

    def __str__(self) -> str:
        return str(self.value)
