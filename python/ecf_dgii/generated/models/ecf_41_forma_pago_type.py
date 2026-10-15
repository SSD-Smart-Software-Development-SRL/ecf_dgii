from enum import StrEnum


class Ecf41FormaPagoType(StrEnum):
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
