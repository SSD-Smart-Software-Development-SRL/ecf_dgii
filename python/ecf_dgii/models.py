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
    TipoAfiliacionType,
    TipoAjusteType,
    TipoCuentaPagoType,
    TipoDescuentoRecargoType,
    TipoeCFType,
    TipoIngresosValidationType,
    TipoMonedaType,
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
# ECF models (union of all per-type schemas Ecf31–Ecf47)
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
    encf: str = Field(alias="encf")
    fecha_vencimiento_secuencia: Optional[datetime] = Field(None, alias="fechaVencimientoSecuencia")
    indicador_envio_diferido: Optional[IndicadorEnvioDiferidoType] = Field(None, alias="indicadorEnvioDiferido")
    indicador_monto_gravado: Optional[IndicadorMontoGravadoType] = Field(None, alias="indicadorMontoGravado")
    indicador_servicio_todo_incluido: Optional[IndicadorServicioTodoIncluidoType] = Field(
        None, alias="indicadorServicioTodoIncluido"
    )
    indicador_nota_credito: Optional[int] = Field(None, alias="indicadorNotaCredito")
    tipo_ingresos: Optional[TipoIngresosValidationType] = Field(None, alias="tipoIngresos")
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
    codigo_vendedor: Optional[str] = Field(None, alias="codigoVendedor")
    numero_factura_interna: Optional[str] = Field(None, alias="numeroFacturaInterna")
    numero_pedido_interno: Optional[str] = Field(None, alias="numeroPedidoInterno")
    zona_venta: Optional[str] = Field(None, alias="zonaVenta")
    ruta_venta: Optional[str] = Field(None, alias="rutaVenta")
    informacion_adicional_emisor: Optional[str] = Field(None, alias="informacionAdicionalEmisor")
    fecha_emision: date = Field(alias="fechaEmision")

    model_config = {"populate_by_name": True}


class Comprador(BaseModel):
    rnc_comprador: Optional[str] = Field(None, alias="rncComprador")
    identificador_extranjero: Optional[str] = Field(None, alias="identificadorExtranjero")
    razon_social_comprador: Optional[str] = Field(None, alias="razonSocialComprador")
    contacto_comprador: Optional[str] = Field(None, alias="contactoComprador")
    correo_comprador: Optional[str] = Field(None, alias="correoComprador")
    direccion_comprador: Optional[str] = Field(None, alias="direccionComprador")
    municipio_comprador: Optional[ProvinciaMunicipioType] = Field(None, alias="municipioComprador")
    provincia_comprador: Optional[ProvinciaMunicipioType] = Field(None, alias="provinciaComprador")
    pais_comprador: Optional[str] = Field(None, alias="paisComprador")
    fecha_entrega: Optional[datetime] = Field(None, alias="fechaEntrega")
    contacto_entrega: Optional[str] = Field(None, alias="contactoEntrega")
    direccion_entrega: Optional[str] = Field(None, alias="direccionEntrega")
    telefono_adicional: Optional[str] = Field(None, alias="telefonoAdicional")
    fecha_orden_compra: Optional[datetime] = Field(None, alias="fechaOrdenCompra")
    numero_orden_compra: Optional[str] = Field(None, alias="numeroOrdenCompra")
    codigo_interno_comprador: Optional[str] = Field(None, alias="codigoInternoComprador")
    responsable_pago: Optional[str] = Field(None, alias="responsablePago")
    informacion_adicional_comprador: Optional[str] = Field(None, alias="informacionAdicionalComprador")

    model_config = {"populate_by_name": True}


class InformacionesAdicionales(BaseModel):
    fecha_embarque: Optional[datetime] = Field(None, alias="fechaEmbarque")
    numero_embarque: Optional[str] = Field(None, alias="numeroEmbarque")
    numero_contenedor: Optional[str] = Field(None, alias="numeroContenedor")
    numero_referencia: Optional[str] = Field(None, alias="numeroReferencia")
    nombre_puerto_embarque: Optional[str] = Field(None, alias="nombrePuertoEmbarque")
    condiciones_entrega: Optional[str] = Field(None, alias="condicionesEntrega")
    total_fob: Optional[float] = Field(None, alias="totalFob")
    seguro: Optional[float] = None
    flete: Optional[float] = None
    otros_gastos: Optional[float] = Field(None, alias="otrosGastos")
    total_cif: Optional[float] = Field(None, alias="totalCif")
    regimen_aduanero: Optional[str] = Field(None, alias="regimenAduanero")
    nombre_puerto_salida: Optional[str] = Field(None, alias="nombrePuertoSalida")
    nombre_puerto_desembarque: Optional[str] = Field(None, alias="nombrePuertoDesembarque")
    peso_bruto: Optional[float] = Field(None, alias="pesoBruto")
    peso_neto: Optional[float] = Field(None, alias="pesoNeto")
    unidad_peso_bruto: Optional[UnidadMedidaType] = Field(None, alias="unidadPesoBruto")
    unidad_peso_neto: Optional[UnidadMedidaType] = Field(None, alias="unidadPesoNeto")
    cantidad_bulto: Optional[float] = Field(None, alias="cantidadBulto")
    unidad_bulto: Optional[UnidadMedidaType] = Field(None, alias="unidadBulto")
    volumen_bulto: Optional[float] = Field(None, alias="volumenBulto")
    unidad_volumen: Optional[UnidadMedidaType] = Field(None, alias="unidadVolumen")

    model_config = {"populate_by_name": True}


class Transporte(BaseModel):
    via_transporte: Optional[ViaTransporteType] = Field(None, alias="viaTransporte")
    pais_origen: Optional[str] = Field(None, alias="paisOrigen")
    direccion_destino: Optional[str] = Field(None, alias="direccionDestino")
    pais_destino: Optional[str] = Field(None, alias="paisDestino")
    rnc_identificacion_compania_transportista: Optional[str] = Field(
        None, alias="rncIdentificacionCompaniaTransportista"
    )
    nombre_compania_transportista: Optional[str] = Field(None, alias="nombreCompaniaTransportista")
    numero_viaje: Optional[str] = Field(None, alias="numeroViaje")
    conductor: Optional[str] = None
    documento_transporte: Optional[str] = Field(None, alias="documentoTransporte")
    ficha: Optional[str] = None
    placa: Optional[str] = None
    ruta_transporte: Optional[str] = Field(None, alias="rutaTransporte")
    zona_transporte: Optional[str] = Field(None, alias="zonaTransporte")
    numero_albaran: Optional[str] = Field(None, alias="numeroAlbaran")

    model_config = {"populate_by_name": True}


class ImpuestoAdicional(BaseModel):
    tipo_impuesto: CodificacionTipoImpuestosType = Field(alias="tipoImpuesto")

    model_config = {"populate_by_name": True}


class ImpuestoAdicional2(BaseModel):
    tipo_impuesto: CodificacionTipoImpuestosType = Field(alias="tipoImpuesto")
    tasa_impuesto_adicional: float = Field(alias="tasaImpuestoAdicional")
    monto_impuesto_selectivo_consumo_especifico: Optional[float] = Field(
        None, alias="montoImpuestoSelectivoConsumoEspecifico"
    )
    monto_impuesto_selectivo_consumo_advalorem: Optional[float] = Field(
        None, alias="montoImpuestoSelectivoConsumoAdvalorem"
    )
    otros_impuestos_adicionales: Optional[float] = Field(None, alias="otrosImpuestosAdicionales")

    model_config = {"populate_by_name": True}


class ImpuestoAdicionalOtraMoneda(BaseModel):
    tipo_impuesto_otra_moneda: CodificacionTipoImpuestosType = Field(alias="tipoImpuestoOtraMoneda")
    tasa_impuesto_adicional_otra_moneda: float = Field(alias="tasaImpuestoAdicionalOtraMoneda")
    monto_impuesto_selectivo_consumo_especifico_otra_moneda: Optional[float] = Field(
        None, alias="montoImpuestoSelectivoConsumoEspecificoOtraMoneda"
    )
    monto_impuesto_selectivo_consumo_advalorem_otra_moneda: Optional[float] = Field(
        None, alias="montoImpuestoSelectivoConsumoAdvaloremOtraMoneda"
    )
    otros_impuestos_adicionales_otra_moneda: Optional[float] = Field(
        None, alias="otrosImpuestosAdicionalesOtraMoneda"
    )

    model_config = {"populate_by_name": True}


class Totales(BaseModel):
    monto_gravado_total: Optional[float] = Field(None, alias="montoGravadoTotal")
    monto_gravado_i1: Optional[float] = Field(None, alias="montoGravadoI1")
    monto_gravado_i2: Optional[float] = Field(None, alias="montoGravadoI2")
    monto_gravado_i3: Optional[float] = Field(None, alias="montoGravadoI3")
    monto_exento: Optional[float] = Field(None, alias="montoExento")
    itbis1: Optional[int] = Field(None, alias="ITBIS1")
    itbis2: Optional[int] = Field(None, alias="ITBIS2")
    itbis3: Optional[int] = Field(None, alias="ITBIS3")
    total_itbis: Optional[float] = Field(None, alias="totalITBIS")
    total_itbis1: Optional[float] = Field(None, alias="totalITBIS1")
    total_itbis2: Optional[float] = Field(None, alias="totalITBIS2")
    total_itbis3: Optional[float] = Field(None, alias="totalITBIS3")
    monto_impuesto_adicional: Optional[float] = Field(None, alias="montoImpuestoAdicional")
    impuestos_adicionales: Optional[list[ImpuestoAdicional2]] = Field(None, alias="impuestosAdicionales")
    monto_total: float = Field(alias="montoTotal")
    monto_no_facturable: Optional[float] = Field(None, alias="montoNoFacturable")
    monto_periodo: Optional[float] = Field(None, alias="montoPeriodo")
    saldo_anterior: Optional[float] = Field(None, alias="saldoAnterior")
    monto_avance_pago: Optional[float] = Field(None, alias="montoAvancePago")
    valor_pagar: Optional[float] = Field(None, alias="valorPagar")
    total_itbis_retenido: Optional[float] = Field(None, alias="totalITBISRetenido")
    total_isr_retencion: Optional[float] = Field(None, alias="totalISRRetencion")
    total_itbis_percepcion: Optional[float] = Field(None, alias="totalITBISPercepcion")
    total_isr_percepcion: Optional[float] = Field(None, alias="totalISRPercepcion")

    model_config = {"populate_by_name": True}


class OtraMoneda(BaseModel):
    tipo_moneda: Optional[TipoMonedaType] = Field(None, alias="tipoMoneda")
    tipo_cambio: Optional[float] = Field(None, alias="tipoCambio")
    monto_gravado_total_otra_moneda: Optional[float] = Field(None, alias="montoGravadoTotalOtraMoneda")
    monto_gravado_1_otra_moneda: Optional[float] = Field(None, alias="montoGravado1OtraMoneda")
    monto_gravado_2_otra_moneda: Optional[float] = Field(None, alias="montoGravado2OtraMoneda")
    monto_gravado_3_otra_moneda: Optional[float] = Field(None, alias="montoGravado3OtraMoneda")
    monto_exento_otra_moneda: Optional[float] = Field(None, alias="montoExentoOtraMoneda")
    total_itbis_otra_moneda: Optional[float] = Field(None, alias="totalITBISOtraMoneda")
    total_itbis1_otra_moneda: Optional[float] = Field(None, alias="totalITBIS1OtraMoneda")
    total_itbis2_otra_moneda: Optional[float] = Field(None, alias="totalITBIS2OtraMoneda")
    total_itbis3_otra_moneda: Optional[float] = Field(None, alias="totalITBIS3OtraMoneda")
    monto_impuesto_adicional_otra_moneda: Optional[float] = Field(None, alias="montoImpuestoAdicionalOtraMoneda")
    impuestos_adicionales_otra_moneda: Optional[list[ImpuestoAdicionalOtraMoneda]] = Field(
        None, alias="impuestosAdicionalesOtraMoneda"
    )
    monto_total_otra_moneda: Optional[float] = Field(None, alias="montoTotalOtraMoneda")

    model_config = {"populate_by_name": True}


class Encabezado(BaseModel):
    version: VersionType
    id_doc: IdDoc = Field(alias="idDoc")
    emisor: Emisor
    comprador: Optional[Comprador] = None
    informaciones_adicionales: Optional[InformacionesAdicionales] = Field(None, alias="informacionesAdicionales")
    transporte: Optional[Transporte] = None
    totales: Totales
    otra_moneda: Optional[OtraMoneda] = Field(None, alias="otraMoneda")

    model_config = {"populate_by_name": True}


class Retencion(BaseModel):
    indicador_agente_retencion_o_percepcion: Optional[IndicadorAgenteRetencionoPercepcionType] = Field(
        None, alias="indicadorAgenteRetencionoPercepcion"
    )
    monto_itbis_retenido: Optional[float] = Field(None, alias="montoITBISRetenido")
    monto_isr_retenido: Optional[float] = Field(None, alias="montoISRRetenido")

    model_config = {"populate_by_name": True}


class OtraMonedaDetalle(BaseModel):
    precio_otra_moneda: Optional[float] = Field(None, alias="precioOtraMoneda")
    descuento_otra_moneda: Optional[float] = Field(None, alias="descuentoOtraMoneda")
    recargo_otra_moneda: Optional[float] = Field(None, alias="recargoOtraMoneda")
    monto_item_otra_moneda: Optional[float] = Field(None, alias="montoItemOtraMoneda")

    model_config = {"populate_by_name": True}


class SubcantidadItem(BaseModel):
    subcantidad: Optional[float] = None
    codigo_subcantidad: Optional[UnidadMedidaType] = Field(None, alias="codigoSubcantidad")

    model_config = {"populate_by_name": True}


class SubDescuento(BaseModel):
    tipo_sub_descuento: TipoDescuentoRecargoType = Field(alias="tipoSubDescuento")
    sub_descuento_porcentaje: Optional[float] = Field(None, alias="subDescuentoPorcentaje")
    monto_sub_descuento: Optional[float] = Field(None, alias="montoSubDescuento")

    model_config = {"populate_by_name": True}


class SubRecargo(BaseModel):
    tipo_sub_recargo: TipoDescuentoRecargoType = Field(alias="tipoSubRecargo")
    sub_recargo_porcentaje: Optional[float] = Field(None, alias="subRecargoPorcentaje")
    monto_sub_recargo: Optional[float] = Field(None, alias="montoSubRecargo")

    model_config = {"populate_by_name": True}


class Mineria(BaseModel):
    peso_neto_kilogramo: Optional[float] = Field(None, alias="pesoNetoKilogramo")
    peso_neto_mineria: Optional[float] = Field(None, alias="pesoNetoMineria")
    tipo_afiliacion: Optional[TipoAfiliacionType] = Field(None, alias="tipoAfiliacion")
    liquidacion: Optional[LiquidacionType] = None

    model_config = {"populate_by_name": True}


class Item(BaseModel):
    numero_linea: int = Field(alias="numeroLinea")
    tabla_codigos_item: Optional[list[CodigosItem]] = Field(None, alias="tablaCodigosItem")
    indicador_facturacion: IndicadorFacturacionType = Field(alias="indicadorFacturacion")
    retencion: Optional[Retencion] = None
    nombre_item: str = Field(alias="nombreItem")
    indicador_bien_o_servicio: IndicadorBienoServicioType = Field(alias="indicadorBienoServicio")
    descripcion_item: Optional[str] = Field(None, alias="descripcionItem")
    cantidad_item: float = Field(alias="cantidadItem")
    unidad_medida: Optional[UnidadMedidaType] = Field(None, alias="unidadMedida")
    cantidad_referencia: Optional[float] = Field(None, alias="cantidadReferencia")
    unidad_referencia: Optional[UnidadMedidaType] = Field(None, alias="unidadReferencia")
    tabla_subcantidad: Optional[list[SubcantidadItem]] = Field(None, alias="tablaSubcantidad")
    grados_alcohol: Optional[float] = Field(None, alias="gradosAlcohol")
    precio_unitario_referencia: Optional[float] = Field(None, alias="precioUnitarioReferencia")
    fecha_elaboracion: Optional[datetime] = Field(None, alias="fechaElaboracion")
    fecha_vencimiento_item: Optional[datetime] = Field(None, alias="fechaVencimientoItem")
    precio_unitario_item: float = Field(alias="precioUnitarioItem")
    descuento_monto: Optional[float] = Field(None, alias="descuentoMonto")
    tabla_sub_descuento: Optional[list[SubDescuento]] = Field(None, alias="tablaSubDescuento")
    recargo_monto: Optional[float] = Field(None, alias="recargoMonto")
    tabla_sub_recargo: Optional[list[SubRecargo]] = Field(None, alias="tablaSubRecargo")
    tabla_impuesto_adicional: Optional[list[ImpuestoAdicional]] = Field(None, alias="tablaImpuestoAdicional")
    mineria: Optional[Mineria] = None
    otra_moneda_detalle: Optional[OtraMonedaDetalle] = Field(None, alias="otraMonedaDetalle")
    monto_item: float = Field(alias="montoItem")

    model_config = {"populate_by_name": True}


class DescuentoORecargo(BaseModel):
    numero_linea: int = Field(alias="numeroLinea")
    tipo_ajuste: TipoAjusteType = Field(alias="tipoAjuste")
    indicador_norma_1007: Optional[IndicadorNorma1007Type] = Field(None, alias="indicadorNorma1007")
    descripcion_descuento_o_recargo: Optional[str] = Field(None, alias="descripcionDescuentooRecargo")
    tipo_valor: Optional[TipoDescuentoRecargoType] = Field(None, alias="tipoValor")
    valor_descuento_o_recargo: Optional[float] = Field(None, alias="valorDescuentooRecargo")
    monto_descuento_o_recargo: Optional[float] = Field(None, alias="montoDescuentooRecargo")
    monto_descuento_o_recargo_otra_moneda: Optional[float] = Field(
        None, alias="montoDescuentooRecargoOtraMoneda"
    )
    indicador_facturacion_descuento_o_recargo: Optional[IndicadorFacturacionDRType] = Field(
        None, alias="indicadorFacturacionDescuentooRecargo"
    )

    model_config = {"populate_by_name": True}


class SubtotalImpuestoAdicional(BaseModel):
    subtotal_impuesto_selectivo_consumo_especifico_pagina: Optional[float] = Field(
        None, alias="subtotalImpuestoSelectivoConsumoEspecificoPagina"
    )
    subtotal_otros_impuesto: Optional[float] = Field(None, alias="subtotalOtrosImpuesto")

    model_config = {"populate_by_name": True}


class Subtotal(BaseModel):
    numero_subtotal: Optional[int] = Field(None, alias="numeroSubTotal")
    descripcion_subtotal: Optional[str] = Field(None, alias="descripcionSubtotal")
    orden: Optional[int] = None
    sub_total_monto_gravado_total: Optional[float] = Field(None, alias="subTotalMontoGravadoTotal")
    sub_total_monto_gravado_i1: Optional[float] = Field(None, alias="subTotalMontoGravadoI1")
    sub_total_monto_gravado_i2: Optional[float] = Field(None, alias="subTotalMontoGravadoI2")
    sub_total_monto_gravado_i3: Optional[float] = Field(None, alias="subTotalMontoGravadoI3")
    sub_tota_itbis: Optional[float] = Field(None, alias="subTotaITBIS")
    sub_tota_itbis1: Optional[float] = Field(None, alias="subTotaITBIS1")
    sub_tota_itbis2: Optional[float] = Field(None, alias="subTotaITBIS2")
    sub_tota_itbis3: Optional[float] = Field(None, alias="subTotaITBIS3")
    sub_total_impuesto_adicional: Optional[float] = Field(None, alias="subTotalImpuestoAdicional")
    sub_total_exento: Optional[float] = Field(None, alias="subTotalExento")
    monto_subtotal: Optional[float] = Field(None, alias="montoSubTotal")
    lineas: Optional[int] = None

    model_config = {"populate_by_name": True}


class Pagina(BaseModel):
    pagina_no: Optional[int] = Field(None, alias="paginaNo")
    no_linea_desde: Optional[int] = Field(None, alias="noLineaDesde")
    no_linea_hasta: Optional[int] = Field(None, alias="noLineaHasta")
    subtotal_monto_gravado_pagina: Optional[float] = Field(None, alias="subtotalMontoGravadoPagina")
    subtotal_monto_gravado_1_pagina: Optional[float] = Field(None, alias="subtotalMontoGravado1Pagina")
    subtotal_monto_gravado_2_pagina: Optional[float] = Field(None, alias="subtotalMontoGravado2Pagina")
    subtotal_monto_gravado_3_pagina: Optional[float] = Field(None, alias="subtotalMontoGravado3Pagina")
    subtotal_exento_pagina: Optional[float] = Field(None, alias="subtotalExentoPagina")
    subtotal_itbis_pagina: Optional[float] = Field(None, alias="subtotalItbisPagina")
    subtotal_itbis1_pagina: Optional[float] = Field(None, alias="subtotalItbis1Pagina")
    subtotal_itbis2_pagina: Optional[float] = Field(None, alias="subtotalItbis2Pagina")
    subtotal_itbis3_pagina: Optional[float] = Field(None, alias="subtotalItbis3Pagina")
    subtotal_impuesto_adicional_pagina: Optional[float] = Field(None, alias="subtotalImpuestoAdicionalPagina")
    subtotal_impuesto_adicional: Optional[SubtotalImpuestoAdicional] = Field(None, alias="subtotalImpuestoAdicional")
    monto_subtotal_pagina: Optional[float] = Field(None, alias="montoSubtotalPagina")
    subtotal_monto_no_facturable_pagina: Optional[float] = Field(None, alias="subtotalMontoNoFacturablePagina")

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
    descuentos_o_recargos: Optional[list[DescuentoORecargo]] = Field(None, alias="descuentosORecargos")
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
    desde_encf: str = Field(alias="desdeEncf")
    hasta_encf: str = Field(alias="hastaEncf")

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
    rnc: Optional[str] = None
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    mensajes: Optional[list[Mensaje]] = None


class SecuenciaRequestDto(BaseModel):
    desde_encf: Optional[str] = Field(None, alias="desdeEncf")
    hasta_encf: Optional[str] = Field(None, alias="hastaEncf")

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
    detalle_motivo_rechazo: Optional[str] = Field(None, alias="detalleMotivoRechazo")
    estado_type: EstadoType = Field(alias="estadoType")

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
    codigo: Optional[int] = None
    estado: Optional[str] = None
    rnc_emisor: Optional[str] = Field(None, alias="rncEmisor")
    ncf_electronico: Optional[str] = Field(None, alias="ncfElectronico")
    monto_total: Optional[float] = Field(None, alias="montoTotal")
    total_itbis: Optional[float] = Field(None, alias="totalITBIS")
    fecha_emision: Optional[str] = Field(None, alias="fechaEmision")
    fecha_firma: Optional[str] = Field(None, alias="fechaFirma")
    rnc_comprador: Optional[str] = Field(None, alias="rncComprador")
    codigo_seguridad: Optional[str] = Field(None, alias="codigoSeguridad")
    id_extranjero: Optional[str] = Field(None, alias="idExtranjero")

    model_config = {"populate_by_name": True}


class RespuestaConsultaTrackId(BaseModel):
    track_id: Optional[str] = Field(None, alias="trackId")
    codigo: Optional[str] = None
    estado: Optional[str] = None
    rnc: Optional[str] = None
    encf: Optional[str] = None
    secuencia_utilizada: Optional[bool] = Field(None, alias="secuenciaUtilizada")
    fecha_recepcion: Optional[str] = Field(None, alias="fechaRecepcion")
    mensajes: Optional[list[Mensaje]] = None

    model_config = {"populate_by_name": True}


class RespuestaConsultaRFCE(BaseModel):
    rnc: Optional[str] = None
    encf: Optional[str] = None
    secuencia_utilizada: Optional[bool] = Field(None, alias="secuenciaUtilizada")
    codigo: Optional[str] = None
    estado: Optional[str] = None
    mensajes: Optional[list[Mensaje]] = None

    model_config = {"populate_by_name": True}


class RespuestaConsultaTimbre(BaseModel):
    rnc_emisor: Optional[str] = Field(None, alias="rncEmisor")
    razon_social: Optional[str] = Field(None, alias="razonSocial")
    encf: Optional[str] = None
    estado: Optional[str] = None

    model_config = {"populate_by_name": True}


class RespuestaEstatusServicio(BaseModel):
    servicio: Optional[str] = None
    status: Optional[str] = None
    ambiente: Optional[str] = None


class VentanaDeMantenimiento(BaseModel):
    ambiente: Optional[str] = None
    hora_inicio: Optional[str] = Field(None, alias="horaInicio")
    hora_fin: Optional[str] = Field(None, alias="horaFin")
    dias: Optional[list[str]] = None

    model_config = {"populate_by_name": True}


class RespuestaVentanaDeMantenimiento(BaseModel):
    ventana_mantenimientos: Optional[list[VentanaDeMantenimiento]] = Field(None, alias="ventanaMantenimientos")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# ApiKey
# ---------------------------------------------------------------------------


class NewCompanyApiKey(BaseModel):
    rnc: str


class Token(BaseModel):
    jwt: str
    valid_from: datetime = Field(alias="validFrom")
    valid_to: datetime = Field(alias="validTo")

    model_config = {"populate_by_name": True}


# ---------------------------------------------------------------------------
# Pagination wrappers
# ---------------------------------------------------------------------------


class PaginatedApiResult(BaseModel):
    """Generic paginated result. Use typed variants below."""

    next_page_uri: Optional[str] = Field(None, alias="nextPageUri")
    total: int
    page: int
    limit: int
    next_page: Optional[int] = Field(None, alias="nextPage")
    previous_page: Optional[int] = Field(None, alias="previousPage")

    model_config = {"populate_by_name": True}


class PaginatedCompanyResponse(PaginatedApiResult):
    values: list[CompanyResponse]


class PaginatedEcfResponse(PaginatedApiResult):
    values: list[EcfResponse]


class PaginatedAnulacionListResponse(PaginatedApiResult):
    values: list[AnulacionListResponse]


class PaginatedEcfReceptionRequestDto(PaginatedApiResult):
    values: list[EcfReceptionRequestDto]


class PaginatedAcecfReceptionRequestDto(PaginatedApiResult):
    values: list[AcecfReceptionRequestDto]
