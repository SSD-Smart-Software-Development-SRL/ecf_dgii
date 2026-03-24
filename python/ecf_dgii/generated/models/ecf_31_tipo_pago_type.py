from enum import Enum

class Ecf31TipoPagoType(str, Enum):
    CONTADO = "Contado"
    CREDITO = "Credito"
    GRATUITO = "Gratuito"

    def __str__(self) -> str:
        return str(self.value)
