from enum import Enum

class AllTipoECFTypesType1(str, Enum):
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
