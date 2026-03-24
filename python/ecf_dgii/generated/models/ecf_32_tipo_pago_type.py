from enum import Enum

class Ecf32TipoPagoType(str, Enum):
    CONTADO = "Contado"
    CREDITO = "Credito"
    GRATUITO = "Gratuito"

    def __str__(self) -> str:
        return str(self.value)
