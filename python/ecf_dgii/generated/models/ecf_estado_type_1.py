from enum import Enum

class EcfEstadoType1(str, Enum):
    ACEPTADO = "Aceptado"
    ACEPTADOCONDICIONAL = "AceptadoCondicional"
    ENPROCESO = "EnProceso"
    NOENCONTRADO = "NoEncontrado"
    RECHAZADO = "Rechazado"

    def __str__(self) -> str:
        return str(self.value)
