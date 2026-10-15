from enum import StrEnum


class EstadoType(StrEnum):
    ECFACEPTADO = "ECFAceptado"
    ECFRECHAZADO = "ECFRechazado"

    def __str__(self) -> str:
        return str(self.value)
