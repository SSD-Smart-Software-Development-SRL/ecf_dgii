from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_44_descuento_o_recargo import Ecf44DescuentoORecargo
  from ..models.ecf_44_encabezado import Ecf44Encabezado
  from ..models.ecf_44_informacion_referencia import Ecf44InformacionReferencia
  from ..models.ecf_44_item import Ecf44Item
  from ..models.ecf_44_pagina import Ecf44Pagina
  from ..models.ecf_44_subtotal import Ecf44Subtotal





T = TypeVar("T", bound="Ecf44ECF")



@_attrs_define
class Ecf44ECF:
    """ 
        Example:
            {'detallesItems': [{'indicadorFacturacion': 'NoFacturable_18Percent', 'tablaImpuestoAdicional':
                [{'tipoImpuesto': None}, {'tipoImpuesto': None}], 'nombreItem': 'nombreItem', 'tablaCodigosItem':
                [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}, {'codigoItem': 'codigoItem', 'tipoCodigo':
                'tipoCodigo'}], 'unidadMedida': '', 'otraMonedaDetalle': '', 'indicadorBienoServicio': 'Bien',
                'tablaSubRecargo': [{'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None},
                {'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None}], 'descripcionItem':
                'descripcionItem', 'descuentoMonto': None, 'fechaVencimientoItem': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroLinea': 9, 'recargoMonto': None,
                'cantidadItem': None, 'precioUnitarioItem': 3.616076749251911, 'tablaSubDescuento': [{'tipoSubDescuento': '$',
                'subDescuentoPorcentaje': 2.027123023002322, 'montoSubDescuento': None}, {'tipoSubDescuento': '$',
                'subDescuentoPorcentaje': 2.027123023002322, 'montoSubDescuento': None}], 'montoItem': None, 'fechaElaboracion':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))},
                {'indicadorFacturacion': 'NoFacturable_18Percent', 'tablaImpuestoAdicional': [{'tipoImpuesto': None},
                {'tipoImpuesto': None}], 'nombreItem': 'nombreItem', 'tablaCodigosItem': [{'codigoItem': 'codigoItem',
                'tipoCodigo': 'tipoCodigo'}, {'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}], 'unidadMedida': '',
                'otraMonedaDetalle': '', 'indicadorBienoServicio': 'Bien', 'tablaSubRecargo': [{'subRecargoPorcentaje': None,
                'tipoSubRecargo': None, 'montoSubRecargo': None}, {'subRecargoPorcentaje': None, 'tipoSubRecargo': None,
                'montoSubRecargo': None}], 'descripcionItem': 'descripcionItem', 'descuentoMonto': None, 'fechaVencimientoItem':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'numeroLinea': 9, 'recargoMonto': None, 'cantidadItem': None, 'precioUnitarioItem': 3.616076749251911,
                'tablaSubDescuento': [{'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 2.027123023002322,
                'montoSubDescuento': None}, {'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 2.027123023002322,
                'montoSubDescuento': None}], 'montoItem': None, 'fechaElaboracion': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}], 'descuentosORecargos': [{'numeroLinea': None,
                'montoDescuentooRecargo': None, 'descripcionDescuentooRecargo': 'descripcionDescuentooRecargo',
                'indicadorFacturacionDescuentooRecargo': '', 'tipoAjuste': 'D', 'tipoValor': '', 'valorDescuentooRecargo': None,
                'montoDescuentooRecargoOtraMoneda': None}, {'numeroLinea': None, 'montoDescuentooRecargo': None,
                'descripcionDescuentooRecargo': 'descripcionDescuentooRecargo', 'indicadorFacturacionDescuentooRecargo': '',
                'tipoAjuste': 'D', 'tipoValor': '', 'valorDescuentooRecargo': None, 'montoDescuentooRecargoOtraMoneda': None}],
                'informacionReferencia': '', 'subtotales': [{'lineas': None, 'descripcionSubtotal': 'descripcionSubtotal',
                'numeroSubTotal': None, 'subTotalImpuestoAdicional': None, 'montoSubTotal': None, 'orden': None,
                'subTotalExento': None}, {'lineas': None, 'descripcionSubtotal': 'descripcionSubtotal', 'numeroSubTotal': None,
                'subTotalImpuestoAdicional': None, 'montoSubTotal': None, 'orden': None, 'subTotalExento': None}], 'encabezado':
                {'transporte': '', 'informacionesAdicionales': '', 'comprador': {'direccionComprador': 'direccionComprador',
                'correoComprador': 'correoComprador', 'fechaOrdenCompra': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'responsablePago': 'responsablePago',
                'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador', 'identificadorExtranjero':
                'identificadorExtranjero', 'municipioComprador': '', 'rncComprador': 'rncComprador', 'codigoInternoComprador':
                'codigoInternoComprador', 'direccionEntrega': 'direccionEntrega', 'numeroOrdenCompra': 'numeroOrdenCompra',
                'informacionAdicionalComprador': 'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador',
                'contactoEntrega': 'contactoEntrega', 'fechaEntrega': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'telefonoAdicional': 'telefonoAdicional'}, 'idDoc':
                {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'bancoPago': 'bancoPago',
                'indicadorEnvioDiferido': '', 'tipoPago': 'Contado', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'indicadorServicioTodoIncluido': '', 'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago':
                'Efectivo'}, {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version':
                'Version1_0', 'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta':
                'rutaVenta', 'codigoVendedor': 'codigoVendedor'}, 'totales': {'montoNoFacturable': 7.061401241503109,
                'montoPeriodo': None, 'impuestosAdicionales': [{'tipoImpuesto': '001', 'tasaImpuestoAdicional':
                5.637376656633329, 'otrosImpuestosAdicionales': 2.3021358869347655}, {'tipoImpuesto': '001',
                'tasaImpuestoAdicional': 5.637376656633329, 'otrosImpuestosAdicionales': 2.3021358869347655}], 'saldoAnterior':
                None, 'montoAvancePago': None, 'montoExento': 1.4658129805029452, 'valorPagar': None, 'montoImpuestoAdicional':
                5.962133916683182, 'montoTotal': None}}, 'paginacion': [{'noLineaHasta': None,
                'subtotalImpuestoAdicionalPagina': None, 'paginaNo': None, 'montoSubtotalPagina': None,
                'subtotalMontoNoFacturablePagina': None, 'subtotalExentoPagina': None, 'subtotalImpuestoAdicional': '',
                'noLineaDesde': None}, {'noLineaHasta': None, 'subtotalImpuestoAdicionalPagina': None, 'paginaNo': None,
                'montoSubtotalPagina': None, 'subtotalMontoNoFacturablePagina': None, 'subtotalExentoPagina': None,
                'subtotalImpuestoAdicional': '', 'noLineaDesde': None}]}

        Attributes:
            encabezado (Ecf44Encabezado):  Example: {'transporte': '', 'informacionesAdicionales': '', 'comprador':
                {'direccionComprador': 'direccionComprador', 'correoComprador': 'correoComprador', 'fechaOrdenCompra':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'responsablePago': 'responsablePago', 'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador',
                'identificadorExtranjero': 'identificadorExtranjero', 'municipioComprador': '', 'rncComprador': 'rncComprador',
                'codigoInternoComprador': 'codigoInternoComprador', 'direccionEntrega': 'direccionEntrega', 'numeroOrdenCompra':
                'numeroOrdenCompra', 'informacionAdicionalComprador': 'informacionAdicionalComprador', 'contactoComprador':
                'contactoComprador', 'contactoEntrega': 'contactoEntrega', 'fechaEntrega': datetime.datetime(2000, 1, 23, 4, 56,
                7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'telefonoAdicional': 'telefonoAdicional'},
                'idDoc': {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'bancoPago': 'bancoPago',
                'indicadorEnvioDiferido': '', 'tipoPago': 'Contado', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'indicadorServicioTodoIncluido': '', 'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago':
                'Efectivo'}, {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version':
                'Version1_0', 'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta':
                'rutaVenta', 'codigoVendedor': 'codigoVendedor'}, 'totales': {'montoNoFacturable': 7.061401241503109,
                'montoPeriodo': None, 'impuestosAdicionales': [{'tipoImpuesto': '001', 'tasaImpuestoAdicional':
                5.637376656633329, 'otrosImpuestosAdicionales': 2.3021358869347655}, {'tipoImpuesto': '001',
                'tasaImpuestoAdicional': 5.637376656633329, 'otrosImpuestosAdicionales': 2.3021358869347655}], 'saldoAnterior':
                None, 'montoAvancePago': None, 'montoExento': 1.4658129805029452, 'valorPagar': None, 'montoImpuestoAdicional':
                5.962133916683182, 'montoTotal': None}}.
            detalles_items (list[Ecf44Item]):
            subtotales (list[Ecf44Subtotal] | None | Unset):
            descuentos_o_recargos (list[Ecf44DescuentoORecargo] | None | Unset):
            paginacion (list[Ecf44Pagina] | None | Unset):
            informacion_referencia (Ecf44InformacionReferencia | None | Unset):
     """

    encabezado: Ecf44Encabezado
    detalles_items: list[Ecf44Item]
    subtotales: list[Ecf44Subtotal] | None | Unset = UNSET
    descuentos_o_recargos: list[Ecf44DescuentoORecargo] | None | Unset = UNSET
    paginacion: list[Ecf44Pagina] | None | Unset = UNSET
    informacion_referencia: Ecf44InformacionReferencia | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_44_descuento_o_recargo import Ecf44DescuentoORecargo
        from ..models.ecf_44_encabezado import Ecf44Encabezado
        from ..models.ecf_44_informacion_referencia import Ecf44InformacionReferencia
        from ..models.ecf_44_item import Ecf44Item
        from ..models.ecf_44_pagina import Ecf44Pagina
        from ..models.ecf_44_subtotal import Ecf44Subtotal
        encabezado = self.encabezado.to_dict()

        detalles_items = []
        for detalles_items_item_data in self.detalles_items:
            detalles_items_item = detalles_items_item_data.to_dict()
            detalles_items.append(detalles_items_item)



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

        informacion_referencia: dict[str, Any] | None | Unset
        if isinstance(self.informacion_referencia, Unset):
            informacion_referencia = UNSET
        elif isinstance(self.informacion_referencia, Ecf44InformacionReferencia):
            informacion_referencia = self.informacion_referencia.to_dict()
        else:
            informacion_referencia = self.informacion_referencia


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "encabezado": encabezado,
            "detallesItems": detalles_items,
        })
        if subtotales is not UNSET:
            field_dict["subtotales"] = subtotales
        if descuentos_o_recargos is not UNSET:
            field_dict["descuentosORecargos"] = descuentos_o_recargos
        if paginacion is not UNSET:
            field_dict["paginacion"] = paginacion
        if informacion_referencia is not UNSET:
            field_dict["informacionReferencia"] = informacion_referencia

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_44_descuento_o_recargo import Ecf44DescuentoORecargo
        from ..models.ecf_44_encabezado import Ecf44Encabezado
        from ..models.ecf_44_informacion_referencia import Ecf44InformacionReferencia
        from ..models.ecf_44_item import Ecf44Item
        from ..models.ecf_44_pagina import Ecf44Pagina
        from ..models.ecf_44_subtotal import Ecf44Subtotal
        d = dict(src_dict)
        encabezado = Ecf44Encabezado.from_dict(d.pop("encabezado"))




        detalles_items = []
        _detalles_items = d.pop("detallesItems")
        for detalles_items_item_data in (_detalles_items):
            detalles_items_item = Ecf44Item.from_dict(detalles_items_item_data)



            detalles_items.append(detalles_items_item)


        def _parse_subtotales(data: object) -> list[Ecf44Subtotal] | None | Unset:
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
                    subtotales_type_0_item = Ecf44Subtotal.from_dict(subtotales_type_0_item_data)



                    subtotales_type_0.append(subtotales_type_0_item)

                return subtotales_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf44Subtotal] | None | Unset, data)

        subtotales = _parse_subtotales(d.pop("subtotales", UNSET))


        def _parse_descuentos_o_recargos(data: object) -> list[Ecf44DescuentoORecargo] | None | Unset:
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
                    descuentos_o_recargos_type_0_item = Ecf44DescuentoORecargo.from_dict(descuentos_o_recargos_type_0_item_data)



                    descuentos_o_recargos_type_0.append(descuentos_o_recargos_type_0_item)

                return descuentos_o_recargos_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf44DescuentoORecargo] | None | Unset, data)

        descuentos_o_recargos = _parse_descuentos_o_recargos(d.pop("descuentosORecargos", UNSET))


        def _parse_paginacion(data: object) -> list[Ecf44Pagina] | None | Unset:
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
                    paginacion_type_0_item = Ecf44Pagina.from_dict(paginacion_type_0_item_data)



                    paginacion_type_0.append(paginacion_type_0_item)

                return paginacion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf44Pagina] | None | Unset, data)

        paginacion = _parse_paginacion(d.pop("paginacion", UNSET))


        def _parse_informacion_referencia(data: object) -> Ecf44InformacionReferencia | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                informacion_referencia_type_1 = Ecf44InformacionReferencia.from_dict(data)



                return informacion_referencia_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf44InformacionReferencia | None | Unset, data)

        informacion_referencia = _parse_informacion_referencia(d.pop("informacionReferencia", UNSET))


        ecf_44ecf = cls(
            encabezado=encabezado,
            detalles_items=detalles_items,
            subtotales=subtotales,
            descuentos_o_recargos=descuentos_o_recargos,
            paginacion=paginacion,
            informacion_referencia=informacion_referencia,
        )


        ecf_44ecf.additional_properties = d
        return ecf_44ecf

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
