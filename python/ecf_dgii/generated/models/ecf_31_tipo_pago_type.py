from enum import StrEnum


class Ecf31TipoPagoType(StrEnum):
    CONTADO = "Contado"
    CREDITO = "Credito"
    GRATUITO = "Gratuito"

    def __str__(self) -> str:
        return str(self.value)
