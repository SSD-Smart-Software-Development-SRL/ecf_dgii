from enum import Enum

class EstadoType(str, Enum):
    ECFACEPTADO = "ECFAceptado"
    ECFRECHAZADO = "ECFRechazado"

    def __str__(self) -> str:
        return str(self.value)
