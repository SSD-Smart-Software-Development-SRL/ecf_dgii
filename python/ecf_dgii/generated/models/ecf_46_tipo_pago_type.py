from enum import Enum

class Ecf46TipoPagoType(str, Enum):
    CONTADO = "Contado"
    CREDITO = "Credito"
    GRATUITO = "Gratuito"

    def __str__(self) -> str:
        return str(self.value)
