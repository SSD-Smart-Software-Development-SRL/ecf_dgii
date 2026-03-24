from enum import Enum

class Ecf32FormaPagoType(str, Enum):
    BONOSOCERTIFICADOSDEREGALO = "BonosOCertificadosDeRegalo"
    CHEQUESLASHTRANSFERENCIASLASHDEPOSITO = "ChequeSlashTransferenciaSlashDeposito"
    EFECTIVO = "Efectivo"
    NOTADECREDITO = "NotaDeCredito"
    OTRASFORMASDEPAGO = "OtrasFormasDePago"
    PERMUTA = "Permuta"
    TARJETADEDEBITOSLASHCREDITO = "TarjetaDeDebitoSlashCredito"
    VENTAACREDITO = "VentaACredito"

    def __str__(self) -> str:
        return str(self.value)
