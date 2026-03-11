"""Pydantic models matching the ECF DGII API schema."""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from .enums import (
    AllTipoECFTypes,
    CodificacionTipoImpuestosType,
    CodigoModificacionType,
    DGIIEnvironment,
    ECFType,
    EcfEstado,
    EcfProgress,
    EstadoType,
    FormaPagoType,
    IndicadorAgenteRetencionoPercepcionType,
    IndicadorBienoServicioType,
    IndicadorEnvioDiferidoType,
    IndicadorFacturacionDRType,
    IndicadorFacturacionType,
    IndicadorMontoGravadoType,
    IndicadorNorma1007Type,
    IndicadorServicioTodoIncluidoType,
    LiquidacionType,
    ProvinciaMunicipioType,
    TipoAjusteType,
    TipoCuentaPagoType,
    TipoDescuentoRecargoType,
    TipoeCFType,
    TipoPagoType,
    UnidadMedidaType,
    VersionType,
    ViaTransporteType,
)


# ---------------------------------------------------------------------------
# Shared / nested models
# ---------------------------------------------------------------------------


class ProblemDetails(BaseModel):
    type: Optional[str] = None
    title: Optional[str] = None
    status: Optional[int] = None
    detail: Optional[str] = None
    instance: Optional[str] = None


# ---------------------------------------------------------------------------
# Company
# ---------------------------------------------------------------------------


class CompanyResponse(BaseModel):
    rnc: str
    legal_name: str = Field(alias="legalName")
    name: str
    created_on: datetime = Field(alias="createdOn")
    updated_on: datetime = Field(alias="updatedOn")
    created_by: str = Field(alias="createdBy")
    updated_by: str = Field(alias="updatedBy")
    tenant_id: UUID = Field(alias="tenantId")
    receptor_id: str = Field(alias="receptorId")

    model_config = {"populate_by_name": True}


class UpsertCompanyRequest(BaseModel):
    rnc: str
    legal_name: str = Field(alias="legalName")
    name: str

    model_config = {"populate_by_name": True}


class CertificateResponse(BaseModel):
    thumbprint: str
    subject: str
    issuer: str
    not_before_utc: datetime = Field(alias="notBeforeUtc")
    not_after_utc: datetime = Field(alias="notAfterUtc")
    serial_number: str = Field(alias="serialNumber")
    rnc: Optional[str] = None
    created_on: datetime = Field(alias="createdOn")
    created_by: str = Field(alias="createdBy")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# ECF models
# ---------------------------------------------------------------------------


class CodigosItem(BaseModel):
    tipo_codigo: str = Field(alias="tipoCodigo")
    codigo_item: str = Field(alias="codigoItem")

    model_config = {"populate_by_name": True}


class FormaDePago(BaseModel):
    forma_pago: FormaPagoType = Field(alias="formaPago")
    monto_pago: float = Field(alias="montoPago", ge=0)

    model_config = {"populate_by_name": True}


class IdDoc(BaseModel):
    tipo_ecf: TipoeCFType = Field(alias="tipoeCF")
    encf: str
    fecha_vencimiento_secuencia: Optional[datetime] = Field(None, alias="fechaVencimientoSecuencia")
    tipo_pago: Optional[TipoPagoType] = Field(None, alias="tipoPago")
    fecha_limite_pago: Optional[datetime] = Field(None, alias="fechaLimitePago")
    termino_pago: Optional[str] = Field(None, alias="terminoPago")
    tabla_formas_pago: Optional[list[FormaDePago]] = Field(None, alias="tablaFormasPago")
    tipo_cuenta_pago: Optional[TipoCuentaPagoType] = Field(None, alias="tipoCuentaPago")
    numero_cuenta_pago: Optional[str] = Field(None, alias="numeroCuentaPago")
    banco_pago: Optional[str] = Field(None, alias="bancoPago")
    fecha_desde: Optional[datetime] = Field(None, alias="fechaDesde")
    fecha_hasta: Optional[datetime] = Field(None, alias="fechaHasta")
    total_paginas: Optional[int] = Field(None, alias="totalPaginas")

    model_config = {"populate_by_name": True}


class Emisor(BaseModel):
    rnc_emisor: str = Field(alias="rncEmisor")
    razon_social_emisor: str = Field(alias="razonSocialEmisor")
    nombre_comercial: Optional[str] = Field(None, alias="nombreComercial")
    sucursal: Optional[str] = None
    direccion_emisor: str = Field(alias="direccionEmisor")
    municipio: Optional[ProvinciaMunicipioType] = None
    provincia: Optional[ProvinciaMunicipioType] = None
    tabla_telefono_emisor: Optional[list[str]] = Field(None, alias="tablaTelefonoEmisor")
    correo_emisor: Optional[str] = Field(None, alias="correoEmisor")
    web_site: Optional[str] = Field(None, alias="webSite")
    actividad_economica: Optional[str] = Field(None, alias="actividadEconomica")
    numero_factura_interna: Optional[str] = Field(None, alias="numeroFacturaInterna")
    numero_pedido_interno: Optional[str] = Field(None, alias="numeroPedidoInterno")
    informacion_adicional_emisor: Optional[str] = Field(None, alias="informacionAdicionalEmisor")
    fecha_emision: date = Field(alias="fechaEmision")

    model_config = {"populate_by_name": True}


class Comprador(BaseModel):
    identificador_extranjero: Optional[str] = Field(None, alias="identificadorExtranjero")
    razon_social_comprador: Optional[str] = Field(None, alias="razonSocialComprador")

    model_config = {"populate_by_name": True}


class Transporte(BaseModel):
    via_transporte: Optional[ViaTransporteType] = Field(None, alias="viaTransporte")

    model_config = {"populate_by_name": True}


class ImpuestoAdicional(BaseModel):
    tipo_impuesto: CodificacionTipoImpuestosType = Field(alias="tipoImpuesto")

    model_config = {"populate_by_name": True}


class ImpuestoAdicional2(BaseModel):
    tipo_impuesto: CodificacionTipoImpuestosType = Field(alias="tipoImpuesto")
    tasa_impuesto_adicional: float = Field(alias="tasaImpuestoAdicional", ge=0.01)
    monto_impuesto_selectivo_consumo_especifico: Optional[float] = Field(
        None, alias="montoImpuestoSelectivoConsumoEspecifico", ge=0.01
    )
    monto_impuesto_selectivo_consumo_advalorem: Optional[float] = Field(
        None, alias="montoImpuestoSelectivoConsumoAdvalorem", ge=0.01
    )
    otros_impuestos_adicionales: Optional[float] = Field(None, alias="otrosImpuestosAdicionales", ge=0.01)

    model_config = {"populate_by_name": True}


class ImpuestoAdicionalOtraMoneda(BaseModel):
    tipo_impuesto_otra_moneda: Optional[CodificacionTipoImpuestosType] = Field(
        None, alias="tipoImpuestoOtraMoneda"
    )
    tasa_impuesto_adicional_otra_moneda: Optional[float] = Field(
        None, alias="tasaImpuestoAdicionalOtraMoneda", ge=0.01
    )
    monto_impuesto_selectivo_consumo_especifico_otra_moneda: Optional[float] = Field(
        None, alias="montoImpuestoSelectivoConsumoEspecificoOtraMoneda", ge=0.01
    )
    monto_impuesto_selectivo_consumo_advalorem_otra_moneda: Optional[float] = Field(
        None, alias="montoImpuestoSelectivoConsumoAdvaloremOtraMoneda", ge=0.01
    )
    otros_impuestos_adicionales_otra_moneda: Optional[float] = Field(
        None, alias="otrosImpuestosAdicionalesOtraMoneda", ge=0.01
    )

    model_config = {"populate_by_name": True}


class Totales(BaseModel):
    monto_gravado_total: Optional[float] = Field(None, alias="montoGravadoTotal", ge=0)
    monto_gravado_i1: Optional[float] = Field(None, alias="montoGravadoI1", ge=0)
    monto_gravado_i2: Optional[float] = Field(None, alias="montoGravadoI2", ge=0)
    monto_gravado_i3: Optional[float] = Field(None, alias="montoGravadoI3", ge=0)
    monto_exento: Optional[float] = Field(None, alias="montoExento", ge=0)
    itbis1: Optional[float] = Field(None, alias="ITBIS1", ge=0)
    itbis2: Optional[float] = Field(None, alias="ITBIS2", ge=0)
    itbis3: Optional[float] = Field(None, alias="ITBIS3", ge=0)
    total_itbis: Optional[float] = Field(None, alias="totalITBIS", ge=0)
    total_itbis1: Optional[float] = Field(None, alias="totalITBIS1", ge=0)
    total_itbis2: Optional[float] = Field(None, alias="totalITBIS2", ge=0)
    total_itbis3: Optional[float] = Field(None, alias="totalITBIS3", ge=0)
    monto_total: float = Field(alias="montoTotal", ge=0)
    monto_no_facturable: Optional[float] = Field(None, alias="montoNoFacturable")
    monto_pagado: Optional[float] = Field(None, alias="montoPagado")
    total_impuestos_adicionales: Optional[float] = Field(None, alias="totalImpuestosAdicionales", ge=0)
    tabla_impuesto_adicional: Optional[list[ImpuestoAdicional2]] = Field(None, alias="tablaImpuestoAdicional")
    indicador_monto_gravado: Optional[IndicadorMontoGravadoType] = Field(None, alias="indicadorMontoGravado")
    indicador_norma_1007: Optional[IndicadorNorma1007Type] = Field(None, alias="indicadorNorma1007")
    indicador_servicio_todo_incluido: Optional[IndicadorServicioTodoIncluidoType] = Field(
        None, alias="indicadorServicioTodoIncluido"
    )
    liquidacion: Optional[LiquidacionType] = None
    indicador_envio_diferido: Optional[IndicadorEnvioDiferidoType] = Field(None, alias="indicadorEnvioDiferido")
    indicador_agente_retencion_o_percepcion: Optional[IndicadorAgenteRetencionoPercepcionType] = Field(
        None, alias="indicadorAgenteRetencionoPercepcion"
    )

    model_config = {"populate_by_name": True}


class OtraMoneda(BaseModel):
    tipo_moneda: Optional[str] = Field(None, alias="tipoMoneda")
    tipo_cambio: Optional[float] = Field(None, alias="tipoCambio", ge=0)
    monto_gravado_total_otra_moneda: Optional[float] = Field(None, alias="montoGravadoTotalOtraMoneda", ge=0)
    monto_gravado_i1_otra_moneda: Optional[float] = Field(None, alias="montoGravadoI1OtraMoneda", ge=0)
    monto_gravado_i2_otra_moneda: Optional[float] = Field(None, alias="montoGravadoI2OtraMoneda", ge=0)
    monto_gravado_i3_otra_moneda: Optional[float] = Field(None, alias="montoGravadoI3OtraMoneda", ge=0)
    monto_exento_otra_moneda: Optional[float] = Field(None, alias="montoExentoOtraMoneda", ge=0)
    total_itbis_otra_moneda: Optional[float] = Field(None, alias="totalITBISOtraMoneda", ge=0)
    total_itbis1_otra_moneda: Optional[float] = Field(None, alias="totalITBIS1OtraMoneda", ge=0)
    total_itbis2_otra_moneda: Optional[float] = Field(None, alias="totalITBIS2OtraMoneda", ge=0)
    total_itbis3_otra_moneda: Optional[float] = Field(None, alias="totalITBIS3OtraMoneda", ge=0)
    monto_total_otra_moneda: Optional[float] = Field(None, alias="montoTotalOtraMoneda", ge=0)
    total_impuestos_adicionales_otra_moneda: Optional[float] = Field(
        None, alias="totalImpuestosAdicionalesOtraMoneda", ge=0
    )
    tabla_impuesto_adicional_otra_moneda: Optional[list[ImpuestoAdicionalOtraMoneda]] = Field(
        None, alias="tablaImpuestoAdicionalOtraMoneda"
    )

    model_config = {"populate_by_name": True}


class Encabezado(BaseModel):
    version: VersionType
    id_doc: IdDoc = Field(alias="idDoc")
    emisor: Emisor
    comprador: Optional[Comprador] = None
    transporte: Optional[Transporte] = None
    totales: Totales
    otra_moneda: Optional[OtraMoneda] = Field(None, alias="otraMoneda")

    model_config = {"populate_by_name": True}


class Retencion(BaseModel):
    indicador_agente_retencion_o_percepcion: Optional[IndicadorAgenteRetencionoPercepcionType] = Field(
        None, alias="indicadorAgenteRetencionoPercepcion"
    )
    monto_retencion_renta: Optional[float] = Field(None, alias="montoRetencionRenta", ge=0)
    monto_retencion_isr: Optional[float] = Field(None, alias="montoRetencionISR", ge=0)

    model_config = {"populate_by_name": True}


class OtraMonedaDetalle(BaseModel):
    precio_otra_moneda: Optional[float] = Field(None, alias="precioOtraMoneda", ge=0)
    descuento_otra_moneda: Optional[float] = Field(None, alias="descuentoOtraMoneda", ge=0)
    monto_item_otra_moneda: Optional[float] = Field(None, alias="montoItemOtraMoneda", ge=0)

    model_config = {"populate_by_name": True}


class Item(BaseModel):
    numero_linea: int = Field(alias="numeroLinea")
    tabla_codigos_item: Optional[list[CodigosItem]] = Field(None, alias="tablaCodigosItem")
    indicador_facturacion: IndicadorFacturacionType = Field(alias="indicadorFacturacion")
    retencion: Retencion
    nombre_item: str = Field(alias="nombreItem")
    indicador_bien_o_servicio: IndicadorBienoServicioType = Field(alias="indicadorBienoServicio")
    descripcion_item: Optional[str] = Field(None, alias="descripcionItem")
    cantidad_item: float = Field(alias="cantidadItem", ge=0.01)
    unidad_medida: Optional[UnidadMedidaType] = Field(None, alias="unidadMedida")
    precio_unitario_item: float = Field(alias="precioUnitarioItem", ge=0)
    otra_moneda_detalle: Optional[OtraMonedaDetalle] = Field(None, alias="otraMonedaDetalle")
    monto_item: float = Field(alias="montoItem", ge=0)

    model_config = {"populate_by_name": True}


class DescuentoORecargo(BaseModel):
    numero_linea: int = Field(alias="numeroLinea")
    tipo_ajuste: TipoAjusteType = Field(alias="tipoAjuste")
    descripcion_descuento_o_recargo: Optional[str] = Field(None, alias="descripcionDescuentooRecargo")
    tipo_valor: Optional[TipoDescuentoRecargoType] = Field(None, alias="tipoValor")
    valor_descuento_o_recargo: Optional[float] = Field(None, alias="valorDescuentooRecargo", ge=0.01)
    monto_descuento_o_recargo: Optional[float] = Field(None, alias="montoDescuentooRecargo", ge=0)
    monto_descuento_o_recargo_otra_moneda: Optional[float] = Field(
        None, alias="montoDescuentooRecargoOtraMoneda", ge=0
    )
    indicador_facturacion_descuento_o_recargo: Optional[IndicadorFacturacionDRType] = Field(
        None, alias="indicadorFacturacionDescuentooRecargo"
    )

    model_config = {"populate_by_name": True}


class Subtotal(BaseModel):
    numero_subtotal: Optional[int] = Field(None, alias="numeroSubtotal")
    descripcion_subtotal: Optional[str] = Field(None, alias="descripcionSubtotal")
    orden_subtotal: Optional[int] = Field(None, alias="ordenSubtotal")
    sub_monto_gravado_total: Optional[float] = Field(None, alias="subMontoGravadoTotal", ge=0)
    sub_monto_gravado_i1: Optional[float] = Field(None, alias="subMontoGravadoI1", ge=0)
    sub_monto_gravado_i2: Optional[float] = Field(None, alias="subMontoGravadoI2", ge=0)
    sub_monto_gravado_i3: Optional[float] = Field(None, alias="subMontoGravadoI3", ge=0)
    sub_monto_exento: Optional[float] = Field(None, alias="subMontoExento", ge=0)
    sub_total_itbis: Optional[float] = Field(None, alias="subTotalITBIS", ge=0)
    sub_total_itbis1: Optional[float] = Field(None, alias="subTotalITBIS1", ge=0)
    sub_total_itbis2: Optional[float] = Field(None, alias="subTotalITBIS2", ge=0)
    sub_total_itbis3: Optional[float] = Field(None, alias="subTotalITBIS3", ge=0)
    sub_total: Optional[float] = Field(None, alias="subTotal", ge=0)
    tabla_descuentos_o_recargos: Optional[list[DescuentoORecargo]] = Field(
        None, alias="tablaDescuentosORecargos"
    )

    model_config = {"populate_by_name": True}


class Pagina(BaseModel):
    pagina_no: Optional[int] = Field(None, alias="paginaNo")
    no_linea_desde: Optional[int] = Field(None, alias="noLineaDesde")
    no_linea_hasta: Optional[int] = Field(None, alias="noLineaHasta")
    sub_total_monto_gravado_pagina: Optional[float] = Field(None, alias="subTotalMontoGravadoPagina", ge=0)
    sub_total_monto_gravado_i1_pagina: Optional[float] = Field(None, alias="subTotalMontoGravadoI1Pagina", ge=0)
    sub_total_monto_gravado_i2_pagina: Optional[float] = Field(None, alias="subTotalMontoGravadoI2Pagina", ge=0)
    sub_total_monto_gravado_i3_pagina: Optional[float] = Field(None, alias="subTotalMontoGravadoI3Pagina", ge=0)
    sub_total_monto_exento_pagina: Optional[float] = Field(None, alias="subTotalMontoExentoPagina", ge=0)
    sub_total_itbis_pagina: Optional[float] = Field(None, alias="subTotalITBISPagina", ge=0)
    sub_total_itbis1_pagina: Optional[float] = Field(None, alias="subTotalITBIS1Pagina", ge=0)
    sub_total_itbis2_pagina: Optional[float] = Field(None, alias="subTotalITBIS2Pagina", ge=0)
    sub_total_itbis3_pagina: Optional[float] = Field(None, alias="subTotalITBIS3Pagina", ge=0)
    monto_sub_total_pagina: Optional[float] = Field(None, alias="montoSubtotalPagina", ge=0)

    model_config = {"populate_by_name": True}


class InformacionReferencia(BaseModel):
    ncf_modificado: Optional[str] = Field(None, alias="ncfModificado")
    rnc_otro_contribuyente: Optional[str] = Field(None, alias="rncOtroContribuyente")
    fecha_ncf_modificado: Optional[datetime] = Field(None, alias="fechaNCFModificado")
    codigo_modificacion: Optional[CodigoModificacionType] = Field(None, alias="codigoModificacion")

    model_config = {"populate_by_name": True}


class ECF(BaseModel):
    encabezado: Encabezado
    detalles_items: list[Item] = Field(alias="detallesItems")
    subtotales: Optional[list[Subtotal]] = None
    paginacion: Optional[list[Pagina]] = None
    informacion_referencia: Optional[InformacionReferencia] = Field(None, alias="informacionReferencia")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# ECF response
# ---------------------------------------------------------------------------


class EcfResponse(BaseModel):
    message_id: UUID = Field(alias="messageId")
    timestamp: datetime
    fecha_emision: date = Field(alias="fechaEmision")
    queue_name: str = Field(alias="queueName")
    include_ecf_content: bool = Field(alias="includeEcfContent")
    ecf_content: str = Field(alias="ecfContent")
    tipo_ecf: AllTipoECFTypes = Field(alias="tipoEcf")
    encf: str
    rnc_emisor: str = Field(alias="rncEmisor")
    rnc_receptor: Optional[str] = Field(None, alias="rncReceptor")
    monto_total: float = Field(alias="montoTotal")
    file_name: Optional[str] = Field(None, alias="fileName")
    tenant_id: UUID = Field(alias="tenantId")
    estatus: Optional[EcfEstado] = None
    cod_sec: Optional[str] = Field(None, alias="codSec")
    fecha_firma: Optional[datetime] = Field(None, alias="fechaFirma")
    mensaje: Optional[str] = None
    errors: Optional[str] = None
    progress: EcfProgress
    emisor_receptor_errors: Optional[str] = Field(None, alias="emisorReceptorErrors")
    secuencia_utilizada: Optional[bool] = Field(None, alias="secuenciaUtilizada")
    dgii_environment: DGIIEnvironment = Field(alias="dgiiEnvironment")
    impresion_url: Optional[str] = Field(None, alias="impresionUrl")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# Anulacion
# ---------------------------------------------------------------------------


class SecuenciaRequest(BaseModel):
    secuencia_desde: str = Field(alias="secuenciaDesde")
    secuencia_hasta: str = Field(alias="secuenciaHasta")

    model_config = {"populate_by_name": True}


class DetalleAnulacionRequest(BaseModel):
    tipo_ecf: ECFType = Field(alias="tipoEcf")
    cantidad_encf_anulados: int = Field(alias="cantidadeNcfAnulados")
    no_linea: list[int] = Field(alias="noLinea")
    secuencias: list[SecuenciaRequest]

    model_config = {"populate_by_name": True}


class AnulacionRequest(BaseModel):
    cantidad_ncf_anulados: int = Field(alias="cantidaDeNcfAnulados")
    detalle_anulacion: list[DetalleAnulacionRequest] = Field(alias="detalleAnulacion")

    model_config = {"populate_by_name": True}


class Mensaje(BaseModel):
    valor: Optional[str] = None
    codigo: int


class RespuestaAnulacionRango(BaseModel):
    estado: Optional[EstadoType] = None
    mensajes: Optional[list[Mensaje]] = None


class SecuenciaRequestDto(BaseModel):
    secuencia_desde: Optional[str] = Field(None, alias="secuenciaDesde")
    secuencia_hasta: Optional[str] = Field(None, alias="secuenciaHasta")

    model_config = {"populate_by_name": True}


class DetalleAnulacionRequestDto(BaseModel):
    tipo_ecf: Optional[ECFType] = Field(None, alias="tipoEcf")
    cantidad_encf_anulados: Optional[int] = Field(None, alias="cantidadeNcfAnulados")
    no_linea: Optional[list[int]] = Field(None, alias="noLinea")
    secuencias: Optional[list[SecuenciaRequestDto]] = None

    model_config = {"populate_by_name": True}


class AnulacionListResponse(BaseModel):
    anulacion_id: UUID = Field(alias="anulacionId")
    tenant_id: UUID = Field(alias="tenantId")
    company_rnc: str = Field(alias="companyRnc")
    cantidad_encf_anulados: int = Field(alias="cantidadeNCFAnulados")
    detalle_anulacion: Optional[list[DetalleAnulacionRequestDto]] = Field(None, alias="detalleAnulacion")
    response: Optional[RespuestaAnulacionRango] = None
    status_code: int = Field(alias="statusCode")
    file_name: str = Field(alias="fileName")
    fecha_hora_anulacion_encf: datetime = Field(alias="fechaHoraAnulacioneNCF")
    created_on: datetime = Field(alias="createdOn")
    updated_on: datetime = Field(alias="updatedOn")
    created_by: str = Field(alias="createdBy")
    updated_by: str = Field(alias="updatedBy")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# Aprobacion comercial (ACECF)
# ---------------------------------------------------------------------------


class SendAcecfRequest(BaseModel):
    estado: EstadoType
    razon_social_comprador: Optional[str] = Field(None, alias="razonSocialComprador")
    rnc_comprador: str = Field(alias="rncComprador")
    comentarios: Optional[str] = None
    fecha_emision: Optional[date] = Field(None, alias="fechaEmision")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# Recepcion
# ---------------------------------------------------------------------------


class EcfReceptionRequestDto(BaseModel):
    message_id: UUID = Field(alias="messageId")
    tenant_id: UUID = Field(alias="tenantId")
    company_rnc: str = Field(alias="companyRnc")
    file_name: str = Field(alias="fileName")
    progress: int
    created_on: datetime = Field(alias="createdOn")
    updated_on: datetime = Field(alias="updatedOn")
    error_message: Optional[str] = Field(None, alias="errorMessage")
    encf: Optional[str] = None
    rnc_emisor: Optional[str] = Field(None, alias="rncEmisor")
    tipo_ecf: Optional[AllTipoECFTypes] = Field(None, alias="tipoEcf")
    result_internal_file_name: Optional[str] = Field(None, alias="resultInternalFileName")

    model_config = {"populate_by_name": True}


class AcecfReceptionRequestDto(BaseModel):
    message_id: UUID = Field(alias="messageId")
    tenant_id: UUID = Field(alias="tenantId")
    company_rnc: str = Field(alias="companyRnc")
    file_name: str = Field(alias="fileName")
    progress: int
    created_on: datetime = Field(alias="createdOn")
    updated_on: datetime = Field(alias="updatedOn")
    error_message: Optional[str] = Field(None, alias="errorMessage")
    encf: Optional[str] = None
    rnc_emisor: Optional[str] = Field(None, alias="rncEmisor")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# DGII consultation
# ---------------------------------------------------------------------------


class Directorio(BaseModel):
    nombre: Optional[str] = None
    rnc: Optional[str] = None
    url_recepcion: Optional[str] = Field(None, alias="urlRecepcion")
    url_aceptacion: Optional[str] = Field(None, alias="urlAceptacion")
    url_opcional: Optional[str] = Field(None, alias="urlOpcional")

    model_config = {"populate_by_name": True}


class RespuestaConsultaEstado(BaseModel):
    estado: Optional[str] = None
    rnc_emisor: Optional[str] = Field(None, alias="rncEmisor")
    rnc_comprador: Optional[str] = Field(None, alias="rncComprador")
    monto_total: Optional[float] = Field(None, alias="montoTotal")
    total_itbis: Optional[float] = Field(None, alias="totalITBIS")
    fecha_emision: Optional[str] = Field(None, alias="fechaEmision")
    fecha_firma: Optional[str] = Field(None, alias="fechaFirma")
    encf: Optional[str] = None
    codigo_seguridad: Optional[str] = Field(None, alias="codigoSeguridad")
    mensajes: Optional[list[Mensaje]] = None

    model_config = {"populate_by_name": True}


class RespuestaConsultaTrackId(BaseModel):
    track_id: Optional[str] = Field(None, alias="trackId")
    estado: Optional[str] = None
    mensajes: Optional[list[Mensaje]] = None

    model_config = {"populate_by_name": True}


class RespuestaConsultaRFCE(BaseModel):
    rfce_url: Optional[str] = Field(None, alias="rfceUrl")
    mensajes: Optional[list[Mensaje]] = None

    model_config = {"populate_by_name": True}


class RespuestaConsultaTimbre(BaseModel):
    url: Optional[str] = None
    mensajes: Optional[list[Mensaje]] = None


class RespuestaEstatusServicio(BaseModel):
    servicio: Optional[str] = None
    estatus: Optional[str] = None


class VentanaDeMantenimiento(BaseModel):
    ambiente: Optional[str] = None
    hora_inicio: Optional[str] = Field(None, alias="horaInicio")
    hora_fin: Optional[str] = Field(None, alias="horaFin")
    dias: Optional[list[str]] = None

    model_config = {"populate_by_name": True}


class RespuestaVentanaDeMantenimiento(BaseModel):
    ventanas: Optional[list[VentanaDeMantenimiento]] = None


# ---------------------------------------------------------------------------
# ApiKey
# ---------------------------------------------------------------------------


class NewCompanyApiKey(BaseModel):
    rnc: str
    name: Optional[str] = None


class Token(BaseModel):
    token: str


# ---------------------------------------------------------------------------
# Pagination wrappers
# ---------------------------------------------------------------------------


class PaginatedApiResult(BaseModel):
    """Generic paginated result. Use typed variants below."""

    total: int
    page: int
    limit: int
    next_page: Optional[int] = Field(None, alias="nextPage")
    previous_page: Optional[int] = Field(None, alias="previousPage")

    model_config = {"populate_by_name": True}


class PaginatedCompanyResponse(PaginatedApiResult):
    results: list[CompanyResponse]


class PaginatedEcfResponse(PaginatedApiResult):
    results: list[EcfResponse]


class PaginatedAnulacionListResponse(PaginatedApiResult):
    results: list[AnulacionListResponse]


class PaginatedEcfReceptionRequestDto(PaginatedApiResult):
    results: list[EcfReceptionRequestDto]


class PaginatedAcecfReceptionRequestDto(PaginatedApiResult):
    results: list[AcecfReceptionRequestDto]
