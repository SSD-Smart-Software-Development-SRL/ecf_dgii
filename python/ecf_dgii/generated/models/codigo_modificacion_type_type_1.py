from enum import Enum

class CodigoModificacionTypeType1(str, Enum):
    ANULAELNCFMODIFICADO = "AnulaElNCFModificado"
    CORRIGEMONTOSDELNCFMODIFICADO = "CorrigeMontosDelNCFModificado"
    CORRIGETEXTODELCOMPROBANTEFISCALMODIFICADO = "CorrigeTextoDelComprobanteFiscalModificado"
    REEMPLAZONCFEMITIDOENCONTINGENCIA = "ReemplazoNCFEmitidoEnContingencia"
    REFERENCIAFACTURACONSUMOELECTRONICA = "ReferenciaFacturaConsumoElectronica"

    def __str__(self) -> str:
        return str(self.value)
