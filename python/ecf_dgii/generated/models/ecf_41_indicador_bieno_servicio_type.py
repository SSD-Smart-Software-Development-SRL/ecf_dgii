from enum import Enum

class Ecf41IndicadorBienoServicioType(str, Enum):
    BIEN = "Bien"
    SERVICIO = "Servicio"

    def __str__(self) -> str:
        return str(self.value)
