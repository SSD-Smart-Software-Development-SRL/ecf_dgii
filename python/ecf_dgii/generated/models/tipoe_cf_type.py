from enum import Enum

class TipoeCFType(str, Enum):
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

    def __str__(self) -> str:
        return str(self.value)
