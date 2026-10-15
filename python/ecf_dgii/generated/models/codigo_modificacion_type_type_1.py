from enum import StrEnum


class CodigoModificacionTypeType1(StrEnum):
    ANULAELNCFMODIFICADO = "AnulaElNCFModificado"
    CORRIGEMONTOSDELNCFMODIFICADO = "CorrigeMontosDelNCFModificado"
    CORRIGETEXTODELCOMPROBANTEFISCALMODIFICADO = "CorrigeTextoDelComprobanteFiscalModificado"
    REEMPLAZONCFEMITIDOENCONTINGENCIA = "ReemplazoNCFEmitidoEnContingencia"
    REFERENCIAFACTURACONSUMOELECTRONICA = "ReferenciaFacturaConsumoElectronica"

    def __str__(self) -> str:
        return str(self.value)
