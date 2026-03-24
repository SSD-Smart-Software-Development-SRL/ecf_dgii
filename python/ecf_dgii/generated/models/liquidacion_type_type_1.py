from enum import Enum

class LiquidacionTypeType1(str, Enum):
    FINAL = "Final"
    PROVISIONAL = "Provisional"

    def __str__(self) -> str:
        return str(self.value)
