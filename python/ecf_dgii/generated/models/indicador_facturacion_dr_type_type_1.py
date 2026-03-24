from enum import Enum

class IndicadorFacturacionDRTypeType1(str, Enum):
    EXENTO_E = "Exento_E"
    ITBIS1_18PERCENT = "ITBIS1_18Percent"
    ITBIS2_16PERCENT = "ITBIS2_16Percent"
    ITBIS3_0PERCENT = "ITBIS3_0Percent"

    def __str__(self) -> str:
        return str(self.value)
