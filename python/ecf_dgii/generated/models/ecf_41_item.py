from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_41_indicador_bieno_servicio_type import Ecf41IndicadorBienoServicioType
from ..models.ecf_41_indicador_facturacion_type import Ecf41IndicadorFacturacionType
from ..models.unidad_medida_type_type_1 import UnidadMedidaTypeType1
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.ecf_41_codigos_item import Ecf41CodigosItem
  from ..models.ecf_41_otra_moneda_detalle import Ecf41OtraMonedaDetalle
  from ..models.ecf_41_retencion import Ecf41Retencion
  from ..models.ecf_41_sub_descuento import Ecf41SubDescuento
  from ..models.ecf_41_sub_recargo import Ecf41SubRecargo





T = TypeVar("T", bound="Ecf41Item")



@_attrs_define
class Ecf41Item:
    """ 
        Example:
            {'indicadorFacturacion': 'NoFacturable_18Percent', 'nombreItem': 'nombreItem', 'tablaCodigosItem':
                [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}, {'codigoItem': 'codigoItem', 'tipoCodigo':
                'tipoCodigo'}], 'unidadMedida': '', 'otraMonedaDetalle': '', 'indicadorBienoServicio': 'Bien',
                'tablaSubRecargo': [{'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None},
                {'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None}], 'descripcionItem':
                'descripcionItem', 'descuentoMonto': None, 'fechaVencimientoItem': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroLinea': 5, 'recargoMonto': None,
                'cantidadItem': 2.3021358869347655, 'retencion': {'montoITBISRetenido': None, 'montoISRRetenido': None,
                'indicadorAgenteRetencionoPercepcion': 'Retencion'}, 'precioUnitarioItem': 7.061401241503109,
                'tablaSubDescuento': [{'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 9.301444243932576,
                'montoSubDescuento': None}, {'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 9.301444243932576,
                'montoSubDescuento': None}], 'montoItem': None, 'fechaElaboracion': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}

        Attributes:
            numero_linea (int | str):
            indicador_facturacion (Ecf41IndicadorFacturacionType):
            retencion (Ecf41Retencion):  Example: {'montoITBISRetenido': None, 'montoISRRetenido': None,
                'indicadorAgenteRetencionoPercepcion': 'Retencion'}.
            nombre_item (str):
            indicador_bieno_servicio (Ecf41IndicadorBienoServicioType):
            cantidad_item (float | str):
            precio_unitario_item (float | str):
            monto_item (float | str):
            tabla_codigos_item (list[Ecf41CodigosItem] | None | Unset):
            descripcion_item (None | str | Unset):
            unidad_medida (None | UnidadMedidaTypeType1 | Unset):
            fecha_elaboracion (datetime.datetime | None | Unset):
            fecha_vencimiento_item (datetime.datetime | None | Unset):
            descuento_monto (float | None | str | Unset):
            tabla_sub_descuento (list[Ecf41SubDescuento] | None | Unset):
            recargo_monto (float | None | str | Unset):
            tabla_sub_recargo (list[Ecf41SubRecargo] | None | Unset):
            otra_moneda_detalle (Ecf41OtraMonedaDetalle | None | Unset):
     """

    numero_linea: int | str
    indicador_facturacion: Ecf41IndicadorFacturacionType
    retencion: Ecf41Retencion
    nombre_item: str
    indicador_bieno_servicio: Ecf41IndicadorBienoServicioType
    cantidad_item: float | str
    precio_unitario_item: float | str
    monto_item: float | str
    tabla_codigos_item: list[Ecf41CodigosItem] | None | Unset = UNSET
    descripcion_item: None | str | Unset = UNSET
    unidad_medida: None | UnidadMedidaTypeType1 | Unset = UNSET
    fecha_elaboracion: datetime.datetime | None | Unset = UNSET
    fecha_vencimiento_item: datetime.datetime | None | Unset = UNSET
    descuento_monto: float | None | str | Unset = UNSET
    tabla_sub_descuento: list[Ecf41SubDescuento] | None | Unset = UNSET
    recargo_monto: float | None | str | Unset = UNSET
    tabla_sub_recargo: list[Ecf41SubRecargo] | None | Unset = UNSET
    otra_moneda_detalle: Ecf41OtraMonedaDetalle | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_41_codigos_item import Ecf41CodigosItem
        from ..models.ecf_41_otra_moneda_detalle import Ecf41OtraMonedaDetalle
        from ..models.ecf_41_retencion import Ecf41Retencion
        from ..models.ecf_41_sub_descuento import Ecf41SubDescuento
        from ..models.ecf_41_sub_recargo import Ecf41SubRecargo
        numero_linea: int | str
        numero_linea = self.numero_linea

        indicador_facturacion = self.indicador_facturacion.value

        retencion = self.retencion.to_dict()

        nombre_item = self.nombre_item

        indicador_bieno_servicio = self.indicador_bieno_servicio.value

        cantidad_item: float | str
        cantidad_item = self.cantidad_item

        precio_unitario_item: float | str
        precio_unitario_item = self.precio_unitario_item

        monto_item: float | str
        monto_item = self.monto_item

        tabla_codigos_item: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_codigos_item, Unset):
            tabla_codigos_item = UNSET
        elif isinstance(self.tabla_codigos_item, list):
            tabla_codigos_item = []
            for tabla_codigos_item_type_0_item_data in self.tabla_codigos_item:
                tabla_codigos_item_type_0_item = tabla_codigos_item_type_0_item_data.to_dict()
                tabla_codigos_item.append(tabla_codigos_item_type_0_item)


        else:
            tabla_codigos_item = self.tabla_codigos_item

        descripcion_item: None | str | Unset
        if isinstance(self.descripcion_item, Unset):
            descripcion_item = UNSET
        else:
            descripcion_item = self.descripcion_item

        unidad_medida: None | str | Unset
        if isinstance(self.unidad_medida, Unset):
            unidad_medida = UNSET
        elif isinstance(self.unidad_medida, UnidadMedidaTypeType1):
            unidad_medida = self.unidad_medida.value
        else:
            unidad_medida = self.unidad_medida

        fecha_elaboracion: None | str | Unset
        if isinstance(self.fecha_elaboracion, Unset):
            fecha_elaboracion = UNSET
        elif isinstance(self.fecha_elaboracion, datetime.datetime):
            fecha_elaboracion = self.fecha_elaboracion.isoformat()
        else:
            fecha_elaboracion = self.fecha_elaboracion

        fecha_vencimiento_item: None | str | Unset
        if isinstance(self.fecha_vencimiento_item, Unset):
            fecha_vencimiento_item = UNSET
        elif isinstance(self.fecha_vencimiento_item, datetime.datetime):
            fecha_vencimiento_item = self.fecha_vencimiento_item.isoformat()
        else:
            fecha_vencimiento_item = self.fecha_vencimiento_item

        descuento_monto: float | None | str | Unset
        if isinstance(self.descuento_monto, Unset):
            descuento_monto = UNSET
        else:
            descuento_monto = self.descuento_monto

        tabla_sub_descuento: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_sub_descuento, Unset):
            tabla_sub_descuento = UNSET
        elif isinstance(self.tabla_sub_descuento, list):
            tabla_sub_descuento = []
            for tabla_sub_descuento_type_0_item_data in self.tabla_sub_descuento:
                tabla_sub_descuento_type_0_item = tabla_sub_descuento_type_0_item_data.to_dict()
                tabla_sub_descuento.append(tabla_sub_descuento_type_0_item)


        else:
            tabla_sub_descuento = self.tabla_sub_descuento

        recargo_monto: float | None | str | Unset
        if isinstance(self.recargo_monto, Unset):
            recargo_monto = UNSET
        else:
            recargo_monto = self.recargo_monto

        tabla_sub_recargo: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_sub_recargo, Unset):
            tabla_sub_recargo = UNSET
        elif isinstance(self.tabla_sub_recargo, list):
            tabla_sub_recargo = []
            for tabla_sub_recargo_type_0_item_data in self.tabla_sub_recargo:
                tabla_sub_recargo_type_0_item = tabla_sub_recargo_type_0_item_data.to_dict()
                tabla_sub_recargo.append(tabla_sub_recargo_type_0_item)


        else:
            tabla_sub_recargo = self.tabla_sub_recargo

        otra_moneda_detalle: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda_detalle, Unset):
            otra_moneda_detalle = UNSET
        elif isinstance(self.otra_moneda_detalle, Ecf41OtraMonedaDetalle):
            otra_moneda_detalle = self.otra_moneda_detalle.to_dict()
        else:
            otra_moneda_detalle = self.otra_moneda_detalle


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "numeroLinea": numero_linea,
            "indicadorFacturacion": indicador_facturacion,
            "retencion": retencion,
            "nombreItem": nombre_item,
            "indicadorBienoServicio": indicador_bieno_servicio,
            "cantidadItem": cantidad_item,
            "precioUnitarioItem": precio_unitario_item,
            "montoItem": monto_item,
        })
        if tabla_codigos_item is not UNSET:
            field_dict["tablaCodigosItem"] = tabla_codigos_item
        if descripcion_item is not UNSET:
            field_dict["descripcionItem"] = descripcion_item
        if unidad_medida is not UNSET:
            field_dict["unidadMedida"] = unidad_medida
        if fecha_elaboracion is not UNSET:
            field_dict["fechaElaboracion"] = fecha_elaboracion
        if fecha_vencimiento_item is not UNSET:
            field_dict["fechaVencimientoItem"] = fecha_vencimiento_item
        if descuento_monto is not UNSET:
            field_dict["descuentoMonto"] = descuento_monto
        if tabla_sub_descuento is not UNSET:
            field_dict["tablaSubDescuento"] = tabla_sub_descuento
        if recargo_monto is not UNSET:
            field_dict["recargoMonto"] = recargo_monto
        if tabla_sub_recargo is not UNSET:
            field_dict["tablaSubRecargo"] = tabla_sub_recargo
        if otra_moneda_detalle is not UNSET:
            field_dict["otraMonedaDetalle"] = otra_moneda_detalle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_41_codigos_item import Ecf41CodigosItem
        from ..models.ecf_41_otra_moneda_detalle import Ecf41OtraMonedaDetalle
        from ..models.ecf_41_retencion import Ecf41Retencion
        from ..models.ecf_41_sub_descuento import Ecf41SubDescuento
        from ..models.ecf_41_sub_recargo import Ecf41SubRecargo
        d = dict(src_dict)
        def _parse_numero_linea(data: object) -> int | str:
            return cast(int | str, data)

        numero_linea = _parse_numero_linea(d.pop("numeroLinea"))


        indicador_facturacion = Ecf41IndicadorFacturacionType(d.pop("indicadorFacturacion"))




        retencion = Ecf41Retencion.from_dict(d.pop("retencion"))




        nombre_item = d.pop("nombreItem")

        indicador_bieno_servicio = Ecf41IndicadorBienoServicioType(d.pop("indicadorBienoServicio"))




        def _parse_cantidad_item(data: object) -> float | str:
            return cast(float | str, data)

        cantidad_item = _parse_cantidad_item(d.pop("cantidadItem"))


        def _parse_precio_unitario_item(data: object) -> float | str:
            return cast(float | str, data)

        precio_unitario_item = _parse_precio_unitario_item(d.pop("precioUnitarioItem"))


        def _parse_monto_item(data: object) -> float | str:
            return cast(float | str, data)

        monto_item = _parse_monto_item(d.pop("montoItem"))


        def _parse_tabla_codigos_item(data: object) -> list[Ecf41CodigosItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_codigos_item_type_0 = []
                _tabla_codigos_item_type_0 = data
                for tabla_codigos_item_type_0_item_data in (_tabla_codigos_item_type_0):
                    tabla_codigos_item_type_0_item = Ecf41CodigosItem.from_dict(tabla_codigos_item_type_0_item_data)



                    tabla_codigos_item_type_0.append(tabla_codigos_item_type_0_item)

                return tabla_codigos_item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf41CodigosItem] | None | Unset, data)

        tabla_codigos_item = _parse_tabla_codigos_item(d.pop("tablaCodigosItem", UNSET))


        def _parse_descripcion_item(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descripcion_item = _parse_descripcion_item(d.pop("descripcionItem", UNSET))


        def _parse_unidad_medida(data: object) -> None | UnidadMedidaTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_unidad_medida_type_type_1 = UnidadMedidaTypeType1(data)



                return componentsschemas_unidad_medida_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnidadMedidaTypeType1 | Unset, data)

        unidad_medida = _parse_unidad_medida(d.pop("unidadMedida", UNSET))


        def _parse_fecha_elaboracion(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_elaboracion_type_0 = isoparse(data)



                return fecha_elaboracion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_elaboracion = _parse_fecha_elaboracion(d.pop("fechaElaboracion", UNSET))


        def _parse_fecha_vencimiento_item(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_vencimiento_item_type_0 = isoparse(data)



                return fecha_vencimiento_item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_vencimiento_item = _parse_fecha_vencimiento_item(d.pop("fechaVencimientoItem", UNSET))


        def _parse_descuento_monto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        descuento_monto = _parse_descuento_monto(d.pop("descuentoMonto", UNSET))


        def _parse_tabla_sub_descuento(data: object) -> list[Ecf41SubDescuento] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_sub_descuento_type_0 = []
                _tabla_sub_descuento_type_0 = data
                for tabla_sub_descuento_type_0_item_data in (_tabla_sub_descuento_type_0):
                    tabla_sub_descuento_type_0_item = Ecf41SubDescuento.from_dict(tabla_sub_descuento_type_0_item_data)



                    tabla_sub_descuento_type_0.append(tabla_sub_descuento_type_0_item)

                return tabla_sub_descuento_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf41SubDescuento] | None | Unset, data)

        tabla_sub_descuento = _parse_tabla_sub_descuento(d.pop("tablaSubDescuento", UNSET))


        def _parse_recargo_monto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        recargo_monto = _parse_recargo_monto(d.pop("recargoMonto", UNSET))


        def _parse_tabla_sub_recargo(data: object) -> list[Ecf41SubRecargo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_sub_recargo_type_0 = []
                _tabla_sub_recargo_type_0 = data
                for tabla_sub_recargo_type_0_item_data in (_tabla_sub_recargo_type_0):
                    tabla_sub_recargo_type_0_item = Ecf41SubRecargo.from_dict(tabla_sub_recargo_type_0_item_data)



                    tabla_sub_recargo_type_0.append(tabla_sub_recargo_type_0_item)

                return tabla_sub_recargo_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf41SubRecargo] | None | Unset, data)

        tabla_sub_recargo = _parse_tabla_sub_recargo(d.pop("tablaSubRecargo", UNSET))


        def _parse_otra_moneda_detalle(data: object) -> Ecf41OtraMonedaDetalle | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_detalle_type_1 = Ecf41OtraMonedaDetalle.from_dict(data)



                return otra_moneda_detalle_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf41OtraMonedaDetalle | None | Unset, data)

        otra_moneda_detalle = _parse_otra_moneda_detalle(d.pop("otraMonedaDetalle", UNSET))


        ecf_41_item = cls(
            numero_linea=numero_linea,
            indicador_facturacion=indicador_facturacion,
            retencion=retencion,
            nombre_item=nombre_item,
            indicador_bieno_servicio=indicador_bieno_servicio,
            cantidad_item=cantidad_item,
            precio_unitario_item=precio_unitario_item,
            monto_item=monto_item,
            tabla_codigos_item=tabla_codigos_item,
            descripcion_item=descripcion_item,
            unidad_medida=unidad_medida,
            fecha_elaboracion=fecha_elaboracion,
            fecha_vencimiento_item=fecha_vencimiento_item,
            descuento_monto=descuento_monto,
            tabla_sub_descuento=tabla_sub_descuento,
            recargo_monto=recargo_monto,
            tabla_sub_recargo=tabla_sub_recargo,
            otra_moneda_detalle=otra_moneda_detalle,
        )


        ecf_41_item.additional_properties = d
        return ecf_41_item

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
