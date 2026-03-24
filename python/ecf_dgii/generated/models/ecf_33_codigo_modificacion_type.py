from enum import Enum

class Ecf33CodigoModificacionType(str, Enum):
    ANULAELNCFMODIFICADO = "AnulaElNCFModificado"
    CORRIGEMONTOSDELNCFMODIFICADO = "CorrigeMontosDelNCFModificado"
    CORRIGETEXTODELCOMPROBANTEFISCALMODIFICADO = "CorrigeTextoDelComprobanteFiscalModificado"
    REEMPLAZONCFEMITIDOENCONTINGENCIA = "ReemplazoNCFEmitidoEnContingencia"
    REFERENCIAFACTURACONSUMOELECTRONICA = "ReferenciaFacturaConsumoElectronica"

    def __str__(self) -> str:
        return str(self.value)
