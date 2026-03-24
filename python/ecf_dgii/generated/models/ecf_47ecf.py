from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_47_encabezado import Ecf47Encabezado
  from ..models.ecf_47_informacion_referencia import Ecf47InformacionReferencia
  from ..models.ecf_47_item import Ecf47Item
  from ..models.ecf_47_pagina import Ecf47Pagina
  from ..models.ecf_47_subtotal import Ecf47Subtotal





T = TypeVar("T", bound="Ecf47ECF")



@_attrs_define
class Ecf47ECF:
    """ 
        Example:
            {'detallesItems': [{'numeroLinea': 5, 'indicadorFacturacion': 'NoFacturable_18Percent', 'nombreItem':
                'nombreItem', 'tablaCodigosItem': [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}, {'codigoItem':
                'codigoItem', 'tipoCodigo': 'tipoCodigo'}], 'cantidadItem': 2.3021358869347655, 'unidadMedida': '', 'retencion':
                {'montoISRRetenido': None, 'indicadorAgenteRetencionoPercepcion': 'Retencion'}, 'otraMonedaDetalle': '',
                'precioUnitarioItem': 7.061401241503109, 'indicadorBienoServicio': 'Bien', 'descripcionItem': 'descripcionItem',
                'montoItem': None}, {'numeroLinea': 5, 'indicadorFacturacion': 'NoFacturable_18Percent', 'nombreItem':
                'nombreItem', 'tablaCodigosItem': [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}, {'codigoItem':
                'codigoItem', 'tipoCodigo': 'tipoCodigo'}], 'cantidadItem': 2.3021358869347655, 'unidadMedida': '', 'retencion':
                {'montoISRRetenido': None, 'indicadorAgenteRetencionoPercepcion': 'Retencion'}, 'otraMonedaDetalle': '',
                'precioUnitarioItem': 7.061401241503109, 'indicadorBienoServicio': 'Bien', 'descripcionItem': 'descripcionItem',
                'montoItem': None}], 'informacionReferencia': '', 'subtotales': [{'lineas': None, 'descripcionSubtotal':
                'descripcionSubtotal', 'numeroSubTotal': None, 'montoSubTotal': None, 'orden': None, 'subTotalExento': None},
                {'lineas': None, 'descripcionSubtotal': 'descripcionSubtotal', 'numeroSubTotal': None, 'montoSubTotal': None,
                'orden': None, 'subTotalExento': None}], 'encabezado': {'transporte': '', 'comprador': '', 'idDoc':
                {'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'encf': 'encf', 'fechaHasta': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoCuentaPago': '', 'fechaDesde':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF':
                'FacturaDeCreditoFiscalElectronica', 'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago',
                'bancoPago': 'bancoPago', 'tipoPago': '', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago':
                0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version': 'Version1_0', 'emisor':
                {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor', 'informacionAdicionalEmisor':
                'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000, 1, 23), 'provincia': '',
                'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor': 'correoEmisor', 'webSite':
                'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'], 'sucursal': 'sucursal',
                'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna': 'numeroFacturaInterna', 'nombreComercial':
                'nombreComercial'}, 'totales': {'montoPeriodo': 5.962133916683182, 'saldoAnterior': None, 'montoAvancePago':
                None, 'totalISRRetencion': None, 'montoExento': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None}},
                'paginacion': [{'noLineaHasta': None, 'paginaNo': None, 'montoSubtotalPagina': None, 'subtotalExentoPagina':
                None, 'noLineaDesde': None}, {'noLineaHasta': None, 'paginaNo': None, 'montoSubtotalPagina': None,
                'subtotalExentoPagina': None, 'noLineaDesde': None}]}

        Attributes:
            encabezado (Ecf47Encabezado):  Example: {'transporte': '', 'comprador': '', 'idDoc': {'fechaLimitePago':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf':
                'encf', 'fechaHasta': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'bancoPago': 'bancoPago', 'tipoPago': '',
                'totalPaginas': 6, 'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tablaFormasPago': [{'montoPago':
                0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]},
                'otraMoneda': '', 'version': 'Version1_0', 'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor':
                'razonSocialEmisor', 'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '',
                'fechaEmision': datetime.date(2000, 1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica',
                'rncEmisor': 'rncEmisor', 'correoEmisor': 'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor':
                ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'], 'sucursal': 'sucursal', 'numeroPedidoInterno':
                'numeroPedidoInterno', 'numeroFacturaInterna': 'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'},
                'totales': {'montoPeriodo': 5.962133916683182, 'saldoAnterior': None, 'montoAvancePago': None,
                'totalISRRetencion': None, 'montoExento': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None}}.
            detalles_items (list[Ecf47Item]):
            subtotales (list[Ecf47Subtotal] | None | Unset):
            paginacion (list[Ecf47Pagina] | None | Unset):
            informacion_referencia (Ecf47InformacionReferencia | None | Unset):
     """

    encabezado: Ecf47Encabezado
    detalles_items: list[Ecf47Item]
    subtotales: list[Ecf47Subtotal] | None | Unset = UNSET
    paginacion: list[Ecf47Pagina] | None | Unset = UNSET
    informacion_referencia: Ecf47InformacionReferencia | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_47_encabezado import Ecf47Encabezado
        from ..models.ecf_47_informacion_referencia import Ecf47InformacionReferencia
        from ..models.ecf_47_item import Ecf47Item
        from ..models.ecf_47_pagina import Ecf47Pagina
        from ..models.ecf_47_subtotal import Ecf47Subtotal
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
        elif isinstance(self.informacion_referencia, Ecf47InformacionReferencia):
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
        if paginacion is not UNSET:
            field_dict["paginacion"] = paginacion
        if informacion_referencia is not UNSET:
            field_dict["informacionReferencia"] = informacion_referencia

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_47_encabezado import Ecf47Encabezado
        from ..models.ecf_47_informacion_referencia import Ecf47InformacionReferencia
        from ..models.ecf_47_item import Ecf47Item
        from ..models.ecf_47_pagina import Ecf47Pagina
        from ..models.ecf_47_subtotal import Ecf47Subtotal
        d = dict(src_dict)
        encabezado = Ecf47Encabezado.from_dict(d.pop("encabezado"))




        detalles_items = []
        _detalles_items = d.pop("detallesItems")
        for detalles_items_item_data in (_detalles_items):
            detalles_items_item = Ecf47Item.from_dict(detalles_items_item_data)



            detalles_items.append(detalles_items_item)


        def _parse_subtotales(data: object) -> list[Ecf47Subtotal] | None | Unset:
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
                    subtotales_type_0_item = Ecf47Subtotal.from_dict(subtotales_type_0_item_data)



                    subtotales_type_0.append(subtotales_type_0_item)

                return subtotales_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf47Subtotal] | None | Unset, data)

        subtotales = _parse_subtotales(d.pop("subtotales", UNSET))


        def _parse_paginacion(data: object) -> list[Ecf47Pagina] | None | Unset:
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
                    paginacion_type_0_item = Ecf47Pagina.from_dict(paginacion_type_0_item_data)



                    paginacion_type_0.append(paginacion_type_0_item)

                return paginacion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf47Pagina] | None | Unset, data)

        paginacion = _parse_paginacion(d.pop("paginacion", UNSET))


        def _parse_informacion_referencia(data: object) -> Ecf47InformacionReferencia | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                informacion_referencia_type_1 = Ecf47InformacionReferencia.from_dict(data)



                return informacion_referencia_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf47InformacionReferencia | None | Unset, data)

        informacion_referencia = _parse_informacion_referencia(d.pop("informacionReferencia", UNSET))


        ecf_47ecf = cls(
            encabezado=encabezado,
            detalles_items=detalles_items,
            subtotales=subtotales,
            paginacion=paginacion,
            informacion_referencia=informacion_referencia,
        )


        ecf_47ecf.additional_properties = d
        return ecf_47ecf

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
