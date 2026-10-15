from enum import StrEnum


class LiquidacionTypeType1(StrEnum):
    FINAL = "Final"
    PROVISIONAL = "Provisional"

    def __str__(self) -> str:
        return str(self.value)
