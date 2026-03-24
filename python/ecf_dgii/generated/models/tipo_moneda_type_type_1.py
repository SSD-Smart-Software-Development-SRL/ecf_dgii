from enum import Enum

class TipoMonedaTypeType1(str, Enum):
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CHY = "CHY"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    HTG = "HTG"
    JPY = "JPY"
    MXN = "MXN"
    NOK = "NOK"
    SCP = "SCP"
    SEK = "SEK"
    USD = "USD"
    VEF = "VEF"
    XDR = "XDR"

    def __str__(self) -> str:
        return str(self.value)
