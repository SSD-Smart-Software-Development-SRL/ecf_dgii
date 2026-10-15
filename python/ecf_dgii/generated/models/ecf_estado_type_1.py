from enum import StrEnum


class EcfEstadoType1(StrEnum):
    ACEPTADO = "Aceptado"
    ACEPTADOCONDICIONAL = "AceptadoCondicional"
    ENPROCESO = "EnProceso"
    NOENCONTRADO = "NoEncontrado"
    RECHAZADO = "Rechazado"

    def __str__(self) -> str:
        return str(self.value)
