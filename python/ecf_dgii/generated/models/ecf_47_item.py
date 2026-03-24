from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_47_indicador_bieno_servicio_type import Ecf47IndicadorBienoServicioType
from ..models.ecf_47_indicador_facturacion_type import Ecf47IndicadorFacturacionType
from ..models.unidad_medida_type_type_1 import UnidadMedidaTypeType1
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_47_codigos_item import Ecf47CodigosItem
  from ..models.ecf_47_otra_moneda_detalle import Ecf47OtraMonedaDetalle
  from ..models.ecf_47_retencion import Ecf47Retencion





T = TypeVar("T", bound="Ecf47Item")



@_attrs_define
class Ecf47Item:
    """ 
        Example:
            {'numeroLinea': 5, 'indicadorFacturacion': 'NoFacturable_18Percent', 'nombreItem': 'nombreItem',
                'tablaCodigosItem': [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}, {'codigoItem': 'codigoItem',
                'tipoCodigo': 'tipoCodigo'}], 'cantidadItem': 2.3021358869347655, 'unidadMedida': '', 'retencion':
                {'montoISRRetenido': None, 'indicadorAgenteRetencionoPercepcion': 'Retencion'}, 'otraMonedaDetalle': '',
                'precioUnitarioItem': 7.061401241503109, 'indicadorBienoServicio': 'Bien', 'descripcionItem': 'descripcionItem',
                'montoItem': None}

        Attributes:
            numero_linea (int | str):
            indicador_facturacion (Ecf47IndicadorFacturacionType):
            retencion (Ecf47Retencion):  Example: {'montoISRRetenido': None, 'indicadorAgenteRetencionoPercepcion':
                'Retencion'}.
            nombre_item (str):
            indicador_bieno_servicio (Ecf47IndicadorBienoServicioType):
            cantidad_item (float | str):
            precio_unitario_item (float | str):
            monto_item (float | str):
            tabla_codigos_item (list[Ecf47CodigosItem] | None | Unset):
            descripcion_item (None | str | Unset):
            unidad_medida (None | UnidadMedidaTypeType1 | Unset):
            otra_moneda_detalle (Ecf47OtraMonedaDetalle | None | Unset):
     """

    numero_linea: int | str
    indicador_facturacion: Ecf47IndicadorFacturacionType
    retencion: Ecf47Retencion
    nombre_item: str
    indicador_bieno_servicio: Ecf47IndicadorBienoServicioType
    cantidad_item: float | str
    precio_unitario_item: float | str
    monto_item: float | str
    tabla_codigos_item: list[Ecf47CodigosItem] | None | Unset = UNSET
    descripcion_item: None | str | Unset = UNSET
    unidad_medida: None | UnidadMedidaTypeType1 | Unset = UNSET
    otra_moneda_detalle: Ecf47OtraMonedaDetalle | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_47_codigos_item import Ecf47CodigosItem
        from ..models.ecf_47_otra_moneda_detalle import Ecf47OtraMonedaDetalle
        from ..models.ecf_47_retencion import Ecf47Retencion
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

        otra_moneda_detalle: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda_detalle, Unset):
            otra_moneda_detalle = UNSET
        elif isinstance(self.otra_moneda_detalle, Ecf47OtraMonedaDetalle):
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
        if otra_moneda_detalle is not UNSET:
            field_dict["otraMonedaDetalle"] = otra_moneda_detalle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_47_codigos_item import Ecf47CodigosItem
        from ..models.ecf_47_otra_moneda_detalle import Ecf47OtraMonedaDetalle
        from ..models.ecf_47_retencion import Ecf47Retencion
        d = dict(src_dict)
        def _parse_numero_linea(data: object) -> int | str:
            return cast(int | str, data)

        numero_linea = _parse_numero_linea(d.pop("numeroLinea"))


        indicador_facturacion = Ecf47IndicadorFacturacionType(d.pop("indicadorFacturacion"))




        retencion = Ecf47Retencion.from_dict(d.pop("retencion"))




        nombre_item = d.pop("nombreItem")

        indicador_bieno_servicio = Ecf47IndicadorBienoServicioType(d.pop("indicadorBienoServicio"))




        def _parse_cantidad_item(data: object) -> float | str:
            return cast(float | str, data)

        cantidad_item = _parse_cantidad_item(d.pop("cantidadItem"))


        def _parse_precio_unitario_item(data: object) -> float | str:
            return cast(float | str, data)

        precio_unitario_item = _parse_precio_unitario_item(d.pop("precioUnitarioItem"))


        def _parse_monto_item(data: object) -> float | str:
            return cast(float | str, data)

        monto_item = _parse_monto_item(d.pop("montoItem"))


        def _parse_tabla_codigos_item(data: object) -> list[Ecf47CodigosItem] | None | Unset:
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
                    tabla_codigos_item_type_0_item = Ecf47CodigosItem.from_dict(tabla_codigos_item_type_0_item_data)



                    tabla_codigos_item_type_0.append(tabla_codigos_item_type_0_item)

                return tabla_codigos_item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf47CodigosItem] | None | Unset, data)

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


        def _parse_otra_moneda_detalle(data: object) -> Ecf47OtraMonedaDetalle | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_detalle_type_1 = Ecf47OtraMonedaDetalle.from_dict(data)



                return otra_moneda_detalle_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf47OtraMonedaDetalle | None | Unset, data)

        otra_moneda_detalle = _parse_otra_moneda_detalle(d.pop("otraMonedaDetalle", UNSET))


        ecf_47_item = cls(
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
            otra_moneda_detalle=otra_moneda_detalle,
        )


        ecf_47_item.additional_properties = d
        return ecf_47_item

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
