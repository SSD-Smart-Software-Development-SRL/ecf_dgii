from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_41_descuento_o_recargo import Ecf41DescuentoORecargo
  from ..models.ecf_41_encabezado import Ecf41Encabezado
  from ..models.ecf_41_informacion_referencia import Ecf41InformacionReferencia
  from ..models.ecf_41_item import Ecf41Item
  from ..models.ecf_41_pagina import Ecf41Pagina
  from ..models.ecf_41_subtotal import Ecf41Subtotal





T = TypeVar("T", bound="Ecf41ECF")



@_attrs_define
class Ecf41ECF:
    """ 
        Example:
            {'detallesItems': [{'indicadorFacturacion': 'NoFacturable_18Percent', 'nombreItem': 'nombreItem',
                'tablaCodigosItem': [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}, {'codigoItem': 'codigoItem',
                'tipoCodigo': 'tipoCodigo'}], 'unidadMedida': '', 'otraMonedaDetalle': '', 'indicadorBienoServicio': 'Bien',
                'tablaSubRecargo': [{'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None},
                {'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None}], 'descripcionItem':
                'descripcionItem', 'descuentoMonto': None, 'fechaVencimientoItem': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroLinea': 5, 'recargoMonto': None,
                'cantidadItem': 2.3021358869347655, 'retencion': {'montoITBISRetenido': None, 'montoISRRetenido': None,
                'indicadorAgenteRetencionoPercepcion': 'Retencion'}, 'precioUnitarioItem': 7.061401241503109,
                'tablaSubDescuento': [{'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 9.301444243932576,
                'montoSubDescuento': None}, {'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 9.301444243932576,
                'montoSubDescuento': None}], 'montoItem': None, 'fechaElaboracion': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}, {'indicadorFacturacion': 'NoFacturable_18Percent',
                'nombreItem': 'nombreItem', 'tablaCodigosItem': [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'},
                {'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}], 'unidadMedida': '', 'otraMonedaDetalle': '',
                'indicadorBienoServicio': 'Bien', 'tablaSubRecargo': [{'subRecargoPorcentaje': None, 'tipoSubRecargo': None,
                'montoSubRecargo': None}, {'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None}],
                'descripcionItem': 'descripcionItem', 'descuentoMonto': None, 'fechaVencimientoItem': datetime.datetime(2000, 1,
                23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroLinea': 5, 'recargoMonto':
                None, 'cantidadItem': 2.3021358869347655, 'retencion': {'montoITBISRetenido': None, 'montoISRRetenido': None,
                'indicadorAgenteRetencionoPercepcion': 'Retencion'}, 'precioUnitarioItem': 7.061401241503109,
                'tablaSubDescuento': [{'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 9.301444243932576,
                'montoSubDescuento': None}, {'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 9.301444243932576,
                'montoSubDescuento': None}], 'montoItem': None, 'fechaElaboracion': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}], 'descuentosORecargos': [{'numeroLinea': None,
                'montoDescuentooRecargo': None, 'descripcionDescuentooRecargo': 'descripcionDescuentooRecargo',
                'indicadorFacturacionDescuentooRecargo': '', 'tipoAjuste': 'D', 'tipoValor': '', 'valorDescuentooRecargo': None,
                'montoDescuentooRecargoOtraMoneda': None}, {'numeroLinea': None, 'montoDescuentooRecargo': None,
                'descripcionDescuentooRecargo': 'descripcionDescuentooRecargo', 'indicadorFacturacionDescuentooRecargo': '',
                'tipoAjuste': 'D', 'tipoValor': '', 'valorDescuentooRecargo': None, 'montoDescuentooRecargoOtraMoneda': None}],
                'informacionReferencia': '', 'subtotales': [{'lineas': None, 'subTotalMontoGravadoI1': None, 'subTotaITBIS3':
                None, 'subTotalMontoGravadoTotal': None, 'subTotalMontoGravadoI3': None, 'subTotaITBIS2': None,
                'subTotalMontoGravadoI2': None, 'subTotaITBIS1': None, 'descripcionSubtotal': 'descripcionSubtotal',
                'subTotaITBIS': None, 'numeroSubTotal': None, 'subTotalImpuestoAdicional': None, 'montoSubTotal': None, 'orden':
                None, 'subTotalExento': None}, {'lineas': None, 'subTotalMontoGravadoI1': None, 'subTotaITBIS3': None,
                'subTotalMontoGravadoTotal': None, 'subTotalMontoGravadoI3': None, 'subTotaITBIS2': None,
                'subTotalMontoGravadoI2': None, 'subTotaITBIS1': None, 'descripcionSubtotal': 'descripcionSubtotal',
                'subTotaITBIS': None, 'numeroSubTotal': None, 'subTotalImpuestoAdicional': None, 'montoSubTotal': None, 'orden':
                None, 'subTotalExento': None}], 'encabezado': {'comprador': {'direccionComprador': 'direccionComprador',
                'correoComprador': 'correoComprador', 'responsablePago': 'responsablePago', 'informacionAdicionalComprador':
                'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador', 'provinciaComprador': '',
                'razonSocialComprador': 'razonSocialComprador', 'municipioComprador': '', 'rncComprador': 'rncComprador',
                'codigoInternoComprador': 'codigoInternoComprador'}, 'idDoc': {'fechaLimitePago': datetime.datetime(2000, 1, 23,
                4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroCuentaPago': 'numeroCuentaPago',
                'indicadorMontoGravado': '', 'encf': 'encf', 'tipoCuentaPago': '', 'bancoPago': 'bancoPago', 'tipoeCF':
                'FacturaDeCreditoFiscalElectronica', 'tipoPago': '', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'terminoPago': 'terminoPago', 'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'},
                {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version': 'Version1_0',
                'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'}, 'totales': {'montoPeriodo': 5.962133916683182,
                'totalISRPercepcion': None, 'montoGravadoI3': None, 'montoGravadoI2': None, 'montoAvancePago': None,
                'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1': None, 'totalITBIS2': None, 'totalITBISPercepcion':
                None, 'itbiS2': None, 'itbiS1': None, 'itbiS3': None, 'totalITBISRetenido': None, 'totalITBIS': None,
                'saldoAnterior': None, 'totalISRRetencion': None, 'montoExento': None, 'montoGravadoTotal': 1.4658129805029452,
                'valorPagar': None, 'montoTotal': None}}, 'paginacion': [{'subtotalItbis1Pagina': None, 'noLineaHasta': None,
                'subtotalMontoGravado2Pagina': None, 'subtotalMontoGravadoPagina': None, 'subtotalMontoGravado1Pagina': None,
                'noLineaDesde': None, 'subtotalItbisPagina': None, 'paginaNo': None, 'subtotalItbis3Pagina': None,
                'subtotalItbis2Pagina': None, 'montoSubtotalPagina': None, 'subtotalExentoPagina': None,
                'subtotalMontoGravado3Pagina': None}, {'subtotalItbis1Pagina': None, 'noLineaHasta': None,
                'subtotalMontoGravado2Pagina': None, 'subtotalMontoGravadoPagina': None, 'subtotalMontoGravado1Pagina': None,
                'noLineaDesde': None, 'subtotalItbisPagina': None, 'paginaNo': None, 'subtotalItbis3Pagina': None,
                'subtotalItbis2Pagina': None, 'montoSubtotalPagina': None, 'subtotalExentoPagina': None,
                'subtotalMontoGravado3Pagina': None}]}

        Attributes:
            encabezado (Ecf41Encabezado):  Example: {'comprador': {'direccionComprador': 'direccionComprador',
                'correoComprador': 'correoComprador', 'responsablePago': 'responsablePago', 'informacionAdicionalComprador':
                'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador', 'provinciaComprador': '',
                'razonSocialComprador': 'razonSocialComprador', 'municipioComprador': '', 'rncComprador': 'rncComprador',
                'codigoInternoComprador': 'codigoInternoComprador'}, 'idDoc': {'fechaLimitePago': datetime.datetime(2000, 1, 23,
                4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroCuentaPago': 'numeroCuentaPago',
                'indicadorMontoGravado': '', 'encf': 'encf', 'tipoCuentaPago': '', 'bancoPago': 'bancoPago', 'tipoeCF':
                'FacturaDeCreditoFiscalElectronica', 'tipoPago': '', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'terminoPago': 'terminoPago', 'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'},
                {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version': 'Version1_0',
                'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'}, 'totales': {'montoPeriodo': 5.962133916683182,
                'totalISRPercepcion': None, 'montoGravadoI3': None, 'montoGravadoI2': None, 'montoAvancePago': None,
                'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1': None, 'totalITBIS2': None, 'totalITBISPercepcion':
                None, 'itbiS2': None, 'itbiS1': None, 'itbiS3': None, 'totalITBISRetenido': None, 'totalITBIS': None,
                'saldoAnterior': None, 'totalISRRetencion': None, 'montoExento': None, 'montoGravadoTotal': 1.4658129805029452,
                'valorPagar': None, 'montoTotal': None}}.
            detalles_items (list[Ecf41Item]):
            subtotales (list[Ecf41Subtotal] | None | Unset):
            descuentos_o_recargos (list[Ecf41DescuentoORecargo] | None | Unset):
            paginacion (list[Ecf41Pagina] | None | Unset):
            informacion_referencia (Ecf41InformacionReferencia | None | Unset):
     """

    encabezado: Ecf41Encabezado
    detalles_items: list[Ecf41Item]
    subtotales: list[Ecf41Subtotal] | None | Unset = UNSET
    descuentos_o_recargos: list[Ecf41DescuentoORecargo] | None | Unset = UNSET
    paginacion: list[Ecf41Pagina] | None | Unset = UNSET
    informacion_referencia: Ecf41InformacionReferencia | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_41_descuento_o_recargo import Ecf41DescuentoORecargo
        from ..models.ecf_41_encabezado import Ecf41Encabezado
        from ..models.ecf_41_informacion_referencia import Ecf41InformacionReferencia
        from ..models.ecf_41_item import Ecf41Item
        from ..models.ecf_41_pagina import Ecf41Pagina
        from ..models.ecf_41_subtotal import Ecf41Subtotal
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
        elif isinstance(self.informacion_referencia, Ecf41InformacionReferencia):
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
        from ..models.ecf_41_descuento_o_recargo import Ecf41DescuentoORecargo
        from ..models.ecf_41_encabezado import Ecf41Encabezado
        from ..models.ecf_41_informacion_referencia import Ecf41InformacionReferencia
        from ..models.ecf_41_item import Ecf41Item
        from ..models.ecf_41_pagina import Ecf41Pagina
        from ..models.ecf_41_subtotal import Ecf41Subtotal
        d = dict(src_dict)
        encabezado = Ecf41Encabezado.from_dict(d.pop("encabezado"))




        detalles_items = []
        _detalles_items = d.pop("detallesItems")
        for detalles_items_item_data in (_detalles_items):
            detalles_items_item = Ecf41Item.from_dict(detalles_items_item_data)



            detalles_items.append(detalles_items_item)


        def _parse_subtotales(data: object) -> list[Ecf41Subtotal] | None | Unset:
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
                    subtotales_type_0_item = Ecf41Subtotal.from_dict(subtotales_type_0_item_data)



                    subtotales_type_0.append(subtotales_type_0_item)

                return subtotales_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf41Subtotal] | None | Unset, data)

        subtotales = _parse_subtotales(d.pop("subtotales", UNSET))


        def _parse_descuentos_o_recargos(data: object) -> list[Ecf41DescuentoORecargo] | None | Unset:
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
                    descuentos_o_recargos_type_0_item = Ecf41DescuentoORecargo.from_dict(descuentos_o_recargos_type_0_item_data)



                    descuentos_o_recargos_type_0.append(descuentos_o_recargos_type_0_item)

                return descuentos_o_recargos_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf41DescuentoORecargo] | None | Unset, data)

        descuentos_o_recargos = _parse_descuentos_o_recargos(d.pop("descuentosORecargos", UNSET))


        def _parse_paginacion(data: object) -> list[Ecf41Pagina] | None | Unset:
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
                    paginacion_type_0_item = Ecf41Pagina.from_dict(paginacion_type_0_item_data)



                    paginacion_type_0.append(paginacion_type_0_item)

                return paginacion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf41Pagina] | None | Unset, data)

        paginacion = _parse_paginacion(d.pop("paginacion", UNSET))


        def _parse_informacion_referencia(data: object) -> Ecf41InformacionReferencia | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                informacion_referencia_type_1 = Ecf41InformacionReferencia.from_dict(data)



                return informacion_referencia_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf41InformacionReferencia | None | Unset, data)

        informacion_referencia = _parse_informacion_referencia(d.pop("informacionReferencia", UNSET))


        ecf_41ecf = cls(
            encabezado=encabezado,
            detalles_items=detalles_items,
            subtotales=subtotales,
            descuentos_o_recargos=descuentos_o_recargos,
            paginacion=paginacion,
            informacion_referencia=informacion_referencia,
        )


        ecf_41ecf.additional_properties = d
        return ecf_41ecf

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
