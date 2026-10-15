from enum import StrEnum


class AllTipoECFTypes(StrEnum):
    ACECF = "ACECF"
    ANECF = "ANECF"
    ARECF = "ARECF"
    COMPRASELECTRONICO = "ComprasElectronico"
    COMPROBANTEDEEXPORTACIONESELECTRONICO = "ComprobanteDeExportacionesElectronico"
    COMPROBANTEPARAPAGOSALEXTERIORELECTRONICO = "ComprobanteParaPagosAlExteriorElectronico"
    FACTURADECONSUMOELECTRONICA = "FacturaDeConsumoElectronica"
    FACTURADECREDITOFISCALELECTRONICA = "FacturaDeCreditoFiscalElectronica"
    GASTOSMENORESELECTRONICO = "GastosMenoresElectronico"
    GUBERNAMENTALELECTRONICO = "GubernamentalElectronico"
    NOTADECREDITOELECTRONICA = "NotaDeCreditoElectronica"
    NOTADEDEBITOELECTRONICA = "NotaDeDebitoElectronica"
    REGIMENESESPECIALESELECTRONICO = "RegimenesEspecialesElectronico"
    RFCE = "RFCE"

    def __str__(self) -> str:
        return str(self.value)
