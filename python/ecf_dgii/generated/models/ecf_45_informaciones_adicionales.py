from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.unidad_medida_type_type_1 import UnidadMedidaTypeType1
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Ecf45InformacionesAdicionales")



@_attrs_define
class Ecf45InformacionesAdicionales:
    """ 
        Attributes:
            fecha_embarque (datetime.datetime | None | Unset):
            numero_embarque (None | str | Unset):
            numero_contenedor (None | str | Unset):
            numero_referencia (None | str | Unset):
            peso_bruto (float | None | str | Unset):
            peso_neto (float | None | str | Unset):
            unidad_peso_bruto (None | UnidadMedidaTypeType1 | Unset):
            unidad_peso_neto (None | UnidadMedidaTypeType1 | Unset):
            cantidad_bulto (float | None | str | Unset):
            unidad_bulto (None | UnidadMedidaTypeType1 | Unset):
            volumen_bulto (float | None | str | Unset):
            unidad_volumen (None | UnidadMedidaTypeType1 | Unset):
     """

    fecha_embarque: datetime.datetime | None | Unset = UNSET
    numero_embarque: None | str | Unset = UNSET
    numero_contenedor: None | str | Unset = UNSET
    numero_referencia: None | str | Unset = UNSET
    peso_bruto: float | None | str | Unset = UNSET
    peso_neto: float | None | str | Unset = UNSET
    unidad_peso_bruto: None | UnidadMedidaTypeType1 | Unset = UNSET
    unidad_peso_neto: None | UnidadMedidaTypeType1 | Unset = UNSET
    cantidad_bulto: float | None | str | Unset = UNSET
    unidad_bulto: None | UnidadMedidaTypeType1 | Unset = UNSET
    volumen_bulto: float | None | str | Unset = UNSET
    unidad_volumen: None | UnidadMedidaTypeType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        fecha_embarque: None | str | Unset
        if isinstance(self.fecha_embarque, Unset):
            fecha_embarque = UNSET
        elif isinstance(self.fecha_embarque, datetime.datetime):
            fecha_embarque = self.fecha_embarque.isoformat()
        else:
            fecha_embarque = self.fecha_embarque

        numero_embarque: None | str | Unset
        if isinstance(self.numero_embarque, Unset):
            numero_embarque = UNSET
        else:
            numero_embarque = self.numero_embarque

        numero_contenedor: None | str | Unset
        if isinstance(self.numero_contenedor, Unset):
            numero_contenedor = UNSET
        else:
            numero_contenedor = self.numero_contenedor

        numero_referencia: None | str | Unset
        if isinstance(self.numero_referencia, Unset):
            numero_referencia = UNSET
        else:
            numero_referencia = self.numero_referencia

        peso_bruto: float | None | str | Unset
        if isinstance(self.peso_bruto, Unset):
            peso_bruto = UNSET
        else:
            peso_bruto = self.peso_bruto

        peso_neto: float | None | str | Unset
        if isinstance(self.peso_neto, Unset):
            peso_neto = UNSET
        else:
            peso_neto = self.peso_neto

        unidad_peso_bruto: None | str | Unset
        if isinstance(self.unidad_peso_bruto, Unset):
            unidad_peso_bruto = UNSET
        elif isinstance(self.unidad_peso_bruto, UnidadMedidaTypeType1):
            unidad_peso_bruto = self.unidad_peso_bruto.value
        else:
            unidad_peso_bruto = self.unidad_peso_bruto

        unidad_peso_neto: None | str | Unset
        if isinstance(self.unidad_peso_neto, Unset):
            unidad_peso_neto = UNSET
        elif isinstance(self.unidad_peso_neto, UnidadMedidaTypeType1):
            unidad_peso_neto = self.unidad_peso_neto.value
        else:
            unidad_peso_neto = self.unidad_peso_neto

        cantidad_bulto: float | None | str | Unset
        if isinstance(self.cantidad_bulto, Unset):
            cantidad_bulto = UNSET
        else:
            cantidad_bulto = self.cantidad_bulto

        unidad_bulto: None | str | Unset
        if isinstance(self.unidad_bulto, Unset):
            unidad_bulto = UNSET
        elif isinstance(self.unidad_bulto, UnidadMedidaTypeType1):
            unidad_bulto = self.unidad_bulto.value
        else:
            unidad_bulto = self.unidad_bulto

        volumen_bulto: float | None | str | Unset
        if isinstance(self.volumen_bulto, Unset):
            volumen_bulto = UNSET
        else:
            volumen_bulto = self.volumen_bulto

        unidad_volumen: None | str | Unset
        if isinstance(self.unidad_volumen, Unset):
            unidad_volumen = UNSET
        elif isinstance(self.unidad_volumen, UnidadMedidaTypeType1):
            unidad_volumen = self.unidad_volumen.value
        else:
            unidad_volumen = self.unidad_volumen


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fecha_embarque is not UNSET:
            field_dict["fechaEmbarque"] = fecha_embarque
        if numero_embarque is not UNSET:
            field_dict["numeroEmbarque"] = numero_embarque
        if numero_contenedor is not UNSET:
            field_dict["numeroContenedor"] = numero_contenedor
        if numero_referencia is not UNSET:
            field_dict["numeroReferencia"] = numero_referencia
        if peso_bruto is not UNSET:
            field_dict["pesoBruto"] = peso_bruto
        if peso_neto is not UNSET:
            field_dict["pesoNeto"] = peso_neto
        if unidad_peso_bruto is not UNSET:
            field_dict["unidadPesoBruto"] = unidad_peso_bruto
        if unidad_peso_neto is not UNSET:
            field_dict["unidadPesoNeto"] = unidad_peso_neto
        if cantidad_bulto is not UNSET:
            field_dict["cantidadBulto"] = cantidad_bulto
        if unidad_bulto is not UNSET:
            field_dict["unidadBulto"] = unidad_bulto
        if volumen_bulto is not UNSET:
            field_dict["volumenBulto"] = volumen_bulto
        if unidad_volumen is not UNSET:
            field_dict["unidadVolumen"] = unidad_volumen

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_fecha_embarque(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_embarque_type_0 = isoparse(data)



                return fecha_embarque_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_embarque = _parse_fecha_embarque(d.pop("fechaEmbarque", UNSET))


        def _parse_numero_embarque(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_embarque = _parse_numero_embarque(d.pop("numeroEmbarque", UNSET))


        def _parse_numero_contenedor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_contenedor = _parse_numero_contenedor(d.pop("numeroContenedor", UNSET))


        def _parse_numero_referencia(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_referencia = _parse_numero_referencia(d.pop("numeroReferencia", UNSET))


        def _parse_peso_bruto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        peso_bruto = _parse_peso_bruto(d.pop("pesoBruto", UNSET))


        def _parse_peso_neto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        peso_neto = _parse_peso_neto(d.pop("pesoNeto", UNSET))


        def _parse_unidad_peso_bruto(data: object) -> None | UnidadMedidaTypeType1 | Unset:
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

        unidad_peso_bruto = _parse_unidad_peso_bruto(d.pop("unidadPesoBruto", UNSET))


        def _parse_unidad_peso_neto(data: object) -> None | UnidadMedidaTypeType1 | Unset:
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

        unidad_peso_neto = _parse_unidad_peso_neto(d.pop("unidadPesoNeto", UNSET))


        def _parse_cantidad_bulto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        cantidad_bulto = _parse_cantidad_bulto(d.pop("cantidadBulto", UNSET))


        def _parse_unidad_bulto(data: object) -> None | UnidadMedidaTypeType1 | Unset:
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

        unidad_bulto = _parse_unidad_bulto(d.pop("unidadBulto", UNSET))


        def _parse_volumen_bulto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        volumen_bulto = _parse_volumen_bulto(d.pop("volumenBulto", UNSET))


        def _parse_unidad_volumen(data: object) -> None | UnidadMedidaTypeType1 | Unset:
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

        unidad_volumen = _parse_unidad_volumen(d.pop("unidadVolumen", UNSET))


        ecf_45_informaciones_adicionales = cls(
            fecha_embarque=fecha_embarque,
            numero_embarque=numero_embarque,
            numero_contenedor=numero_contenedor,
            numero_referencia=numero_referencia,
            peso_bruto=peso_bruto,
            peso_neto=peso_neto,
            unidad_peso_bruto=unidad_peso_bruto,
            unidad_peso_neto=unidad_peso_neto,
            cantidad_bulto=cantidad_bulto,
            unidad_bulto=unidad_bulto,
            volumen_bulto=volumen_bulto,
            unidad_volumen=unidad_volumen,
        )


        ecf_45_informaciones_adicionales.additional_properties = d
        return ecf_45_informaciones_adicionales

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
