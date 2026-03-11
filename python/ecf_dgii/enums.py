"""Enumerations matching the ECF DGII API schema."""

from enum import Enum


class AllTipoECFTypes(str, Enum):
    FACTURA_DE_CREDITO_FISCAL_ELECTRONICA = "FacturaDeCreditoFiscalElectronica"
    FACTURA_DE_CONSUMO_ELECTRONICA = "FacturaDeConsumoElectronica"
    NOTA_DE_DEBITO_ELECTRONICA = "NotaDeDebitoElectronica"
    NOTA_DE_CREDITO_ELECTRONICA = "NotaDeCreditoElectronica"
    COMPRAS_ELECTRONICO = "ComprasElectronico"
    GASTOS_MENORES_ELECTRONICO = "GastosMenoresElectronico"
    REGIMENES_ESPECIALES_ELECTRONICO = "RegimenesEspecialesElectronico"
    GUBERNAMENTAL_ELECTRONICO = "GubernamentalElectronico"
    COMPROBANTE_DE_EXPORTACIONES_ELECTRONICO = "ComprobanteDeExportacionesElectronico"
    COMPROBANTE_PARA_PAGOS_AL_EXTERIOR_ELECTRONICO = "ComprobanteParaPagosAlExteriorElectronico"
    RFCE = "RFCE"
    ACECF = "ACECF"
    ARECF = "ARECF"
    ANECF = "ANECF"


class ECFType(str, Enum):
    ECF31 = "ECF31"
    ECF32 = "ECF32"
    ECF33 = "ECF33"
    ECF34 = "ECF34"
    ECF41 = "ECF41"
    ECF43 = "ECF43"
    ECF44 = "ECF44"
    ECF45 = "ECF45"
    ECF46 = "ECF46"
    ECF47 = "ECF47"


class TipoeCFType(str, Enum):
    FACTURA_DE_CREDITO_FISCAL_ELECTRONICA = "FacturaDeCreditoFiscalElectronica"
    FACTURA_DE_CONSUMO_ELECTRONICA = "FacturaDeConsumoElectronica"
    NOTA_DE_DEBITO_ELECTRONICA = "NotaDeDebitoElectronica"
    NOTA_DE_CREDITO_ELECTRONICA = "NotaDeCreditoElectronica"
    COMPRAS_ELECTRONICO = "ComprasElectronico"
    GASTOS_MENORES_ELECTRONICO = "GastosMenoresElectronico"
    REGIMENES_ESPECIALES_ELECTRONICO = "RegimenesEspecialesElectronico"
    GUBERNAMENTAL_ELECTRONICO = "GubernamentalElectronico"
    COMPROBANTE_DE_EXPORTACIONES_ELECTRONICO = "ComprobanteDeExportacionesElectronico"
    COMPROBANTE_PARA_PAGOS_AL_EXTERIOR_ELECTRONICO = "ComprobanteParaPagosAlExteriorElectronico"


class EcfEstado(str, Enum):
    NO_ENCONTRADO = "NoEncontrado"
    ACEPTADO = "Aceptado"
    RECHAZADO = "Rechazado"
    EN_PROCESO = "EnProceso"
    ACEPTADO_CONDICIONAL = "AceptadoCondicional"


class EcfProgress(str, Enum):
    NEW = "New"
    PROCESSING = "Processing"
    UPLOADED_TO_DGII = "UploadedToDgii"
    FINISHED = "Finished"
    ERROR = "Error"


class DGIIEnvironment(str, Enum):
    TEST = "Test"
    CERTIFICATION = "Certification"
    PRODUCTION = "Production"


class VersionType(str, Enum):
    VERSION_1_0 = "1.0"


class TipoPagoType(str, Enum):
    CONTADO = "Contado"
    CREDITO = "Credito"
    GRATUITO = "Gratuito"


class FormaPagoType(str, Enum):
    EFECTIVO = "Efectivo"
    CHEQUE_TRANSFERENCIA_DEPOSITO = "ChequeSlashTransferenciaSlashDeposito"
    TARJETA_DEBITO_CREDITO = "TarjetaDeDebitoSlashCredito"
    VENTA_A_CREDITO = "VentaACredito"
    BONOS_O_CERTIFICADOS_DE_REGALO = "BonosOCertificadosDeRegalo"
    PERMUTA = "Permuta"
    NOTA_DE_CREDITO = "NotaDeCredito"
    OTRAS_FORMAS_DE_PAGO = "OtrasFormasDePago"


class TipoCuentaPagoType(str, Enum):
    CORRIENTE = "CT"
    AHORRO = "AH"
    TARJETA_CREDITO = "OT"


class IndicadorFacturacionType(str, Enum):
    NO_FACTURABLE_18_PERCENT = "NoFacturable"
    ITBIS1_18_PERCENT = "ITBIS1"
    ITBIS2_16_PERCENT = "ITBIS2"
    ITBIS3_0_PERCENT = "ITBIS3"
    EXENTO = "E"


class IndicadorFacturacionDRType(str, Enum):
    ITBIS1_18_PERCENT = "ITBIS1"
    ITBIS2_16_PERCENT = "ITBIS2"
    ITBIS3_0_PERCENT = "ITBIS3"
    EXENTO = "E"


class IndicadorBienoServicioType(str, Enum):
    BIEN = "Bien"
    SERVICIO = "Servicio"


class TipoAjusteType(str, Enum):
    DESCUENTO = "Descuento"
    RECARGO = "Recargo"


class TipoDescuentoRecargoType(str, Enum):
    PORCENTAJE = "Porcentaje"
    VALOR = "Valor"


class CodigoModificacionType(str, Enum):
    ANULA_EL_NCF_MODIFICADO = "AnulaElNCFModificado"
    CORRIGE_TEXTO = "CorrigeTextoDelComprobanteFiscalModificado"
    CORRIGE_MONTOS = "CorrigeMontosDelNCFModificado"
    REEMPLAZO_CONTINGENCIA = "ReemplazoNCFEmitidoEnContingencia"
    REFERENCIA_FACTURA_CONSUMO = "ReferenciaFacturaConsumoElectronica"


class IndicadorMontoGravadoType(str, Enum):
    SIN_ITBIS_INCLUIDO = "SinITBISIncluido"
    CON_ITBIS_INCLUIDO = "ConITBISIncluido"


class CodificacionTipoImpuestosType(str, Enum):
    PROPINA_LEGAL = "001"
    CONTRIBUCION_DESARROLLO_TELECOMUNICACIONES = "002"
    ISC_PRODUCTOS_TABACO = "003"
    ISC_SERVICIOS_TELECOMUNICACIONES = "004"
    ISC_PRODUCTOS_ALCOHOL = "005"
    ISC_SEGUROS = "006"
    ISC_CHEQUES = "007"
    ISC_TRANSFERENCIAS_ELECTRONICAS = "008"
    OTROS = "039"


class UnidadMedidaType(str, Enum):
    UNIDAD = "Unidad"
    PAQUETE = "Paquete"
    CAJA = "Caja"
    DOCENA = "Docena"
    KILOGRAMO = "Kilogramo"
    LIBRA = "Libra"
    ONZA = "Onza"
    LITRO = "Litro"
    GALON = "Galon"
    METRO = "Metro"
    PIE = "Pie"
    PULGADA = "Pulgada"
    METRO_CUADRADO = "MetroCuadrado"
    PIE_CUADRADO = "PieCuadrado"
    METRO_CUBICO = "MetroCubico"
    PIE_CUBICO = "PieCubico"
    HORA = "Hora"
    DIA = "Dia"
    MES = "Mes"
    ANIO = "Anio"
    SERVICIO = "Servicio"
    OTRO = "Otro"


class EstadoType(str, Enum):
    ECF_ACEPTADO = "ECFAceptado"
    ECF_RECHAZADO = "ECFRechazado"


class ProvinciaMunicipioType(str, Enum):
    DISTRITO_NACIONAL = "DistritoNacional"
    AZUA = "Azua"
    BAHORUCO = "Bahoruco"
    BARAHONA = "Barahona"
    DAJABON = "Dajabon"
    DUARTE = "Duarte"
    ELIAS_PINA = "EliasPina"
    EL_SEIBO = "ElSeibo"
    ESPAILLAT = "Espaillat"
    HATO_MAYOR = "HatoMayor"
    INDEPENDENCIA = "Independencia"
    LA_ALTAGRACIA = "LaAltagracia"
    LA_ROMANA = "LaRomana"
    LA_VEGA = "LaVega"
    MARIA_TRINIDAD_SANCHEZ = "MariaTrinidadSanchez"
    MONSENOR_NOUEL = "MonsenorNouel"
    MONTE_CRISTI = "MonteCristi"
    MONTE_PLATA = "MontePlata"
    PEDERNALES = "Pedernales"
    PERAVIA = "Peravia"
    PUERTO_PLATA = "PuertoPlata"
    HERMANAS_MIRABAL = "HermanasMirabal"
    SAMANA = "Samana"
    SAN_CRISTOBAL = "SanCristobal"
    SAN_JOSE_DE_OCOA = "SanJoseDeOcoa"
    SAN_JUAN = "SanJuan"
    SAN_PEDRO_DE_MACORIS = "SanPedroDeMacoris"
    SANCHEZ_RAMIREZ = "SanchezRamirez"
    SANTIAGO = "Santiago"
    SANTIAGO_RODRIGUEZ = "SantiagoRodriguez"
    SANTO_DOMINGO = "SantoDomingo"
    VALVERDE = "Valverde"


class IndicadorAgenteRetencionoPercepcionType(str, Enum):
    RETENCION = "Retencion"
    PERCEPCION = "Percepcion"


class IndicadorEnvioDiferidoType(str, Enum):
    ENVIO_DIFERIDO_AUTORIZADO = "EnvioDiferidoAutorizado"


class IndicadorMontoGravado(str, Enum):
    SIN_ITBIS_INCLUIDO = "SinITBISIncluido"
    CON_ITBIS_INCLUIDO = "ConITBISIncluido"


class IndicadorNorma1007Type(str, Enum):
    NO_INCLUIR = "NoIncluir"
    INCLUIR = "Incluir"


class IndicadorServicioTodoIncluidoType(str, Enum):
    INDICADOR_SERVICIO_TODO_INCLUIDO = "IndicadorServicioTodoIncluido"


class LiquidacionType(str, Enum):
    PROVISIONAL = "Provisional"
    FINAL = "Final"


class ViaTransporteType(str, Enum):
    MARITIMO = "01"
    AEREO = "02"
    TERRESTRE = "03"
