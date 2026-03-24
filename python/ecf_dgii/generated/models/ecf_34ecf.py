from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_34_descuento_o_recargo import Ecf34DescuentoORecargo
  from ..models.ecf_34_encabezado import Ecf34Encabezado
  from ..models.ecf_34_informacion_referencia import Ecf34InformacionReferencia
  from ..models.ecf_34_item import Ecf34Item
  from ..models.ecf_34_pagina import Ecf34Pagina
  from ..models.ecf_34_subtotal import Ecf34Subtotal





T = TypeVar("T", bound="Ecf34ECF")



@_attrs_define
class Ecf34ECF:
    """ 
        Example:
            {'detallesItems': [{'indicadorFacturacion': 'NoFacturable_18Percent', 'tablaImpuestoAdicional':
                [{'tipoImpuesto': '001'}, {'tipoImpuesto': '001'}], 'nombreItem': 'nombreItem', 'tablaSubcantidad':
                [{'codigoSubcantidad': '', 'subcantidad': 3.616076749251911}, {'codigoSubcantidad': '', 'subcantidad':
                3.616076749251911}], 'tablaCodigosItem': [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'},
                {'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}], 'otraMonedaDetalle': '', 'indicadorBienoServicio':
                'Bien', 'tablaSubRecargo': [{'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None},
                {'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None}], 'fechaVencimientoItem':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'numeroLinea': None, 'gradosAlcohol': None, 'tablaSubDescuento': [{'tipoSubDescuento': '$',
                'subDescuentoPorcentaje': None, 'montoSubDescuento': None}, {'tipoSubDescuento': '$', 'subDescuentoPorcentaje':
                None, 'montoSubDescuento': None}], 'montoItem': None, 'unidadMedida': '', 'mineria': '', 'descripcionItem':
                'descripcionItem', 'descuentoMonto': None, 'recargoMonto': None, 'cantidadItem': 9.301444243932576,
                'unidadReferencia': '', 'retencion': '', 'precioUnitarioReferencia': None, 'precioUnitarioItem':
                3.616076749251911, 'cantidadReferencia': None, 'fechaElaboracion': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}, {'indicadorFacturacion': 'NoFacturable_18Percent',
                'tablaImpuestoAdicional': [{'tipoImpuesto': '001'}, {'tipoImpuesto': '001'}], 'nombreItem': 'nombreItem',
                'tablaSubcantidad': [{'codigoSubcantidad': '', 'subcantidad': 3.616076749251911}, {'codigoSubcantidad': '',
                'subcantidad': 3.616076749251911}], 'tablaCodigosItem': [{'codigoItem': 'codigoItem', 'tipoCodigo':
                'tipoCodigo'}, {'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}], 'otraMonedaDetalle': '',
                'indicadorBienoServicio': 'Bien', 'tablaSubRecargo': [{'subRecargoPorcentaje': None, 'tipoSubRecargo': None,
                'montoSubRecargo': None}, {'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None}],
                'fechaVencimientoItem': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'numeroLinea': None, 'gradosAlcohol': None, 'tablaSubDescuento': [{'tipoSubDescuento': '$',
                'subDescuentoPorcentaje': None, 'montoSubDescuento': None}, {'tipoSubDescuento': '$', 'subDescuentoPorcentaje':
                None, 'montoSubDescuento': None}], 'montoItem': None, 'unidadMedida': '', 'mineria': '', 'descripcionItem':
                'descripcionItem', 'descuentoMonto': None, 'recargoMonto': None, 'cantidadItem': 9.301444243932576,
                'unidadReferencia': '', 'retencion': '', 'precioUnitarioReferencia': None, 'precioUnitarioItem':
                3.616076749251911, 'cantidadReferencia': None, 'fechaElaboracion': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}], 'descuentosORecargos': [{'numeroLinea': None,
                'montoDescuentooRecargo': None, 'descripcionDescuentooRecargo': 'descripcionDescuentooRecargo',
                'indicadorNorma1007': '', 'indicadorFacturacionDescuentooRecargo': '', 'tipoAjuste': 'D', 'tipoValor': '',
                'valorDescuentooRecargo': None, 'montoDescuentooRecargoOtraMoneda': None}, {'numeroLinea': None,
                'montoDescuentooRecargo': None, 'descripcionDescuentooRecargo': 'descripcionDescuentooRecargo',
                'indicadorNorma1007': '', 'indicadorFacturacionDescuentooRecargo': '', 'tipoAjuste': 'D', 'tipoValor': '',
                'valorDescuentooRecargo': None, 'montoDescuentooRecargoOtraMoneda': None}], 'informacionReferencia':
                {'razonModificacion': 'razonModificacion', 'rncOtroContribuyente': 'rncOtroContribuyente', 'codigoModificacion':
                'AnulaElNCFModificado', 'ncfModificado': 'ncfModificado', 'fechaNCFModificado': datetime.datetime(2000, 1, 23,
                4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}, 'subtotales': [{'lineas': None,
                'subTotalMontoGravadoI1': None, 'subTotaITBIS3': None, 'subTotalMontoGravadoTotal': None,
                'subTotalMontoGravadoI3': None, 'subTotaITBIS2': None, 'subTotalMontoGravadoI2': None, 'subTotaITBIS1': None,
                'descripcionSubtotal': 'descripcionSubtotal', 'subTotaITBIS': None, 'numeroSubTotal': None,
                'subTotalImpuestoAdicional': None, 'montoSubTotal': None, 'orden': None, 'subTotalExento': None}, {'lineas':
                None, 'subTotalMontoGravadoI1': None, 'subTotaITBIS3': None, 'subTotalMontoGravadoTotal': None,
                'subTotalMontoGravadoI3': None, 'subTotaITBIS2': None, 'subTotalMontoGravadoI2': None, 'subTotaITBIS1': None,
                'descripcionSubtotal': 'descripcionSubtotal', 'subTotaITBIS': None, 'numeroSubTotal': None,
                'subTotalImpuestoAdicional': None, 'montoSubTotal': None, 'orden': None, 'subTotalExento': None}], 'encabezado':
                {'transporte': '', 'informacionesAdicionales': '', 'comprador': '', 'idDoc': {'tipoIngresos': '01',
                'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'indicadorMontoGravado': '', 'encf': 'encf', 'fechaHasta': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'indicadorNotaCredito': 0, 'fechaDesde':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'indicadorEnvioDiferido': '', 'tipoeCF': 'FacturaDeCreditoFiscalElectronica', 'tipoPago': 'Contado',
                'totalPaginas': 6, 'indicadorServicioTodoIncluido': ''}, 'otraMoneda': '', 'version': 'Version1_0', 'emisor':
                {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor', 'informacionAdicionalEmisor':
                'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000, 1, 23), 'provincia': '',
                'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor': 'correoEmisor', 'webSite':
                'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'], 'sucursal': 'sucursal',
                'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna': 'numeroFacturaInterna', 'nombreComercial':
                'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta': 'rutaVenta', 'codigoVendedor': 'codigoVendedor'},
                'totales': {'montoPeriodo': None, 'totalISRPercepcion': None, 'montoGravadoI3': None, 'montoGravadoI2': None,
                'montoAvancePago': None, 'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1': None, 'totalITBIS2': None,
                'totalITBISPercepcion': None, 'itbiS2': None, 'montoImpuestoAdicional': 5.962133916683182, 'itbiS1': None,
                'itbiS3': None, 'totalITBISRetenido': None, 'totalITBIS': None, 'montoNoFacturable': 7.061401241503109,
                'impuestosAdicionales': [{'tipoImpuesto': '', 'montoImpuestoSelectivoConsumoAdvalorem': None,
                'tasaImpuestoAdicional': 5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None,
                'otrosImpuestosAdicionales': None}, {'tipoImpuesto': '', 'montoImpuestoSelectivoConsumoAdvalorem': None,
                'tasaImpuestoAdicional': 5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None,
                'otrosImpuestosAdicionales': None}], 'saldoAnterior': None, 'totalISRRetencion': None, 'montoExento': None,
                'montoGravadoTotal': 1.4658129805029452, 'valorPagar': None, 'montoTotal': 2.3021358869347655}}, 'paginacion':
                [{'subtotalItbis1Pagina': None, 'noLineaHasta': None, 'subtotalImpuestoAdicionalPagina': None,
                'subtotalMontoGravado2Pagina': None, 'subtotalMontoGravadoPagina': None, 'subtotalMontoNoFacturablePagina':
                None, 'subtotalMontoGravado1Pagina': None, 'subtotalImpuestoAdicional': '', 'noLineaDesde': None,
                'subtotalItbisPagina': None, 'paginaNo': None, 'subtotalItbis3Pagina': None, 'subtotalItbis2Pagina': None,
                'montoSubtotalPagina': None, 'subtotalExentoPagina': None, 'subtotalMontoGravado3Pagina': None},
                {'subtotalItbis1Pagina': None, 'noLineaHasta': None, 'subtotalImpuestoAdicionalPagina': None,
                'subtotalMontoGravado2Pagina': None, 'subtotalMontoGravadoPagina': None, 'subtotalMontoNoFacturablePagina':
                None, 'subtotalMontoGravado1Pagina': None, 'subtotalImpuestoAdicional': '', 'noLineaDesde': None,
                'subtotalItbisPagina': None, 'paginaNo': None, 'subtotalItbis3Pagina': None, 'subtotalItbis2Pagina': None,
                'montoSubtotalPagina': None, 'subtotalExentoPagina': None, 'subtotalMontoGravado3Pagina': None}]}

        Attributes:
            encabezado (Ecf34Encabezado):  Example: {'transporte': '', 'informacionesAdicionales': '', 'comprador': '',
                'idDoc': {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'indicadorMontoGravado': '', 'encf': 'encf',
                'fechaHasta': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'indicadorNotaCredito': 0, 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'indicadorEnvioDiferido': '', 'tipoeCF':
                'FacturaDeCreditoFiscalElectronica', 'tipoPago': 'Contado', 'totalPaginas': 6, 'indicadorServicioTodoIncluido':
                ''}, 'otraMoneda': '', 'version': 'Version1_0', 'emisor': {'direccionEmisor': 'direccionEmisor',
                'razonSocialEmisor': 'razonSocialEmisor', 'informacionAdicionalEmisor': 'informacionAdicionalEmisor',
                'municipio': '', 'fechaEmision': datetime.date(2000, 1, 23), 'provincia': '', 'actividadEconomica':
                'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor': 'correoEmisor', 'webSite': 'webSite',
                'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'], 'sucursal': 'sucursal',
                'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna': 'numeroFacturaInterna', 'nombreComercial':
                'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta': 'rutaVenta', 'codigoVendedor': 'codigoVendedor'},
                'totales': {'montoPeriodo': None, 'totalISRPercepcion': None, 'montoGravadoI3': None, 'montoGravadoI2': None,
                'montoAvancePago': None, 'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1': None, 'totalITBIS2': None,
                'totalITBISPercepcion': None, 'itbiS2': None, 'montoImpuestoAdicional': 5.962133916683182, 'itbiS1': None,
                'itbiS3': None, 'totalITBISRetenido': None, 'totalITBIS': None, 'montoNoFacturable': 7.061401241503109,
                'impuestosAdicionales': [{'tipoImpuesto': '', 'montoImpuestoSelectivoConsumoAdvalorem': None,
                'tasaImpuestoAdicional': 5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None,
                'otrosImpuestosAdicionales': None}, {'tipoImpuesto': '', 'montoImpuestoSelectivoConsumoAdvalorem': None,
                'tasaImpuestoAdicional': 5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None,
                'otrosImpuestosAdicionales': None}], 'saldoAnterior': None, 'totalISRRetencion': None, 'montoExento': None,
                'montoGravadoTotal': 1.4658129805029452, 'valorPagar': None, 'montoTotal': 2.3021358869347655}}.
            detalles_items (list[Ecf34Item]):
            informacion_referencia (Ecf34InformacionReferencia):  Example: {'razonModificacion': 'razonModificacion',
                'rncOtroContribuyente': 'rncOtroContribuyente', 'codigoModificacion': 'AnulaElNCFModificado', 'ncfModificado':
                'ncfModificado', 'fechaNCFModificado': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}.
            subtotales (list[Ecf34Subtotal] | None | Unset):
            descuentos_o_recargos (list[Ecf34DescuentoORecargo] | None | Unset):
            paginacion (list[Ecf34Pagina] | None | Unset):
     """

    encabezado: Ecf34Encabezado
    detalles_items: list[Ecf34Item]
    informacion_referencia: Ecf34InformacionReferencia
    subtotales: list[Ecf34Subtotal] | None | Unset = UNSET
    descuentos_o_recargos: list[Ecf34DescuentoORecargo] | None | Unset = UNSET
    paginacion: list[Ecf34Pagina] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_34_descuento_o_recargo import Ecf34DescuentoORecargo
        from ..models.ecf_34_encabezado import Ecf34Encabezado
        from ..models.ecf_34_informacion_referencia import Ecf34InformacionReferencia
        from ..models.ecf_34_item import Ecf34Item
        from ..models.ecf_34_pagina import Ecf34Pagina
        from ..models.ecf_34_subtotal import Ecf34Subtotal
        encabezado = self.encabezado.to_dict()

        detalles_items = []
        for detalles_items_item_data in self.detalles_items:
            detalles_items_item = detalles_items_item_data.to_dict()
            detalles_items.append(detalles_items_item)



        informacion_referencia = self.informacion_referencia.to_dict()

        subtotales: list[dict[str, Any]] | None | Unset
        if isinstance(self.subtotales, Unset):
            subtotales = UNSET
        elif isinstance(self.subtotales, list):
            subtotales = []
            for subtotales_type_0_item_data in self.subtotales:
                subtotales_type_0_item = subtotales_type_0_item_data.to_dict()
                subtotales.append(subtotales_type_0_item)


        else:
            subtotales = self.subtotales

        descuentos_o_recargos: list[dict[str, Any]] | None | Unset
        if isinstance(self.descuentos_o_recargos, Unset):
            descuentos_o_recargos = UNSET
        elif isinstance(self.descuentos_o_recargos, list):
            descuentos_o_recargos = []
            for descuentos_o_recargos_type_0_item_data in self.descuentos_o_recargos:
                descuentos_o_recargos_type_0_item = descuentos_o_recargos_type_0_item_data.to_dict()
                descuentos_o_recargos.append(descuentos_o_recargos_type_0_item)


        else:
            descuentos_o_recargos = self.descuentos_o_recargos

        paginacion: list[dict[str, Any]] | None | Unset
        if isinstance(self.paginacion, Unset):
            paginacion = UNSET
        elif isinstance(self.paginacion, list):
            paginacion = []
            for paginacion_type_0_item_data in self.paginacion:
                paginacion_type_0_item = paginacion_type_0_item_data.to_dict()
                paginacion.append(paginacion_type_0_item)


        else:
            paginacion = self.paginacion


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "encabezado": encabezado,
            "detallesItems": detalles_items,
            "informacionReferencia": informacion_referencia,
        })
        if subtotales is not UNSET:
            field_dict["subtotales"] = subtotales
        if descuentos_o_recargos is not UNSET:
            field_dict["descuentosORecargos"] = descuentos_o_recargos
        if paginacion is not UNSET:
            field_dict["paginacion"] = paginacion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_34_descuento_o_recargo import Ecf34DescuentoORecargo
        from ..models.ecf_34_encabezado import Ecf34Encabezado
        from ..models.ecf_34_informacion_referencia import Ecf34InformacionReferencia
        from ..models.ecf_34_item import Ecf34Item
        from ..models.ecf_34_pagina import Ecf34Pagina
        from ..models.ecf_34_subtotal import Ecf34Subtotal
        d = dict(src_dict)
        encabezado = Ecf34Encabezado.from_dict(d.pop("encabezado"))




        detalles_items = []
        _detalles_items = d.pop("detallesItems")
        for detalles_items_item_data in (_detalles_items):
            detalles_items_item = Ecf34Item.from_dict(detalles_items_item_data)



            detalles_items.append(detalles_items_item)


        informacion_referencia = Ecf34InformacionReferencia.from_dict(d.pop("informacionReferencia"))




        def _parse_subtotales(data: object) -> list[Ecf34Subtotal] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subtotales_type_0 = []
                _subtotales_type_0 = data
                for subtotales_type_0_item_data in (_subtotales_type_0):
                    subtotales_type_0_item = Ecf34Subtotal.from_dict(subtotales_type_0_item_data)



                    subtotales_type_0.append(subtotales_type_0_item)

                return subtotales_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf34Subtotal] | None | Unset, data)

        subtotales = _parse_subtotales(d.pop("subtotales", UNSET))


        def _parse_descuentos_o_recargos(data: object) -> list[Ecf34DescuentoORecargo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                descuentos_o_recargos_type_0 = []
                _descuentos_o_recargos_type_0 = data
                for descuentos_o_recargos_type_0_item_data in (_descuentos_o_recargos_type_0):
                    descuentos_o_recargos_type_0_item = Ecf34DescuentoORecargo.from_dict(descuentos_o_recargos_type_0_item_data)



                    descuentos_o_recargos_type_0.append(descuentos_o_recargos_type_0_item)

                return descuentos_o_recargos_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf34DescuentoORecargo] | None | Unset, data)

        descuentos_o_recargos = _parse_descuentos_o_recargos(d.pop("descuentosORecargos", UNSET))


        def _parse_paginacion(data: object) -> list[Ecf34Pagina] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                paginacion_type_0 = []
                _paginacion_type_0 = data
                for paginacion_type_0_item_data in (_paginacion_type_0):
                    paginacion_type_0_item = Ecf34Pagina.from_dict(paginacion_type_0_item_data)



                    paginacion_type_0.append(paginacion_type_0_item)

                return paginacion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf34Pagina] | None | Unset, data)

        paginacion = _parse_paginacion(d.pop("paginacion", UNSET))


        ecf_34ecf = cls(
            encabezado=encabezado,
            detalles_items=detalles_items,
            informacion_referencia=informacion_referencia,
            subtotales=subtotales,
            descuentos_o_recargos=descuentos_o_recargos,
            paginacion=paginacion,
        )


        ecf_34ecf.additional_properties = d
        return ecf_34ecf

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
