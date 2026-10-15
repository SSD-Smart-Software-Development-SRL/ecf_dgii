from enum import StrEnum


class Ecf34CodigoModificacionType(StrEnum):
    ANULAELNCFMODIFICADO = "AnulaElNCFModificado"
    CORRIGEMONTOSDELNCFMODIFICADO = "CorrigeMontosDelNCFModificado"
    CORRIGETEXTODELCOMPROBANTEFISCALMODIFICADO = "CorrigeTextoDelComprobanteFiscalModificado"
    REEMPLAZONCFEMITIDOENCONTINGENCIA = "ReemplazoNCFEmitidoEnContingencia"
    REFERENCIAFACTURACONSUMOELECTRONICA = "ReferenciaFacturaConsumoElectronica"

    def __str__(self) -> str:
        return str(self.value)
