from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.liquidacion_type_type_1 import LiquidacionTypeType1
from ..models.tipo_afiliacion_type_type_1 import TipoAfiliacionTypeType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf46Mineria")



@_attrs_define
class Ecf46Mineria:
    """ 
        Attributes:
            peso_neto_kilogramo (float | None | str | Unset):
            peso_neto_mineria (float | None | str | Unset):
            tipo_afiliacion (None | TipoAfiliacionTypeType1 | Unset):
            liquidacion (LiquidacionTypeType1 | None | Unset):
     """

    peso_neto_kilogramo: float | None | str | Unset = UNSET
    peso_neto_mineria: float | None | str | Unset = UNSET
    tipo_afiliacion: None | TipoAfiliacionTypeType1 | Unset = UNSET
    liquidacion: LiquidacionTypeType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        peso_neto_kilogramo: float | None | str | Unset
        if isinstance(self.peso_neto_kilogramo, Unset):
            peso_neto_kilogramo = UNSET
        else:
            peso_neto_kilogramo = self.peso_neto_kilogramo

        peso_neto_mineria: float | None | str | Unset
        if isinstance(self.peso_neto_mineria, Unset):
            peso_neto_mineria = UNSET
        else:
            peso_neto_mineria = self.peso_neto_mineria

        tipo_afiliacion: None | str | Unset
        if isinstance(self.tipo_afiliacion, Unset):
            tipo_afiliacion = UNSET
        elif isinstance(self.tipo_afiliacion, TipoAfiliacionTypeType1):
            tipo_afiliacion = self.tipo_afiliacion.value
        else:
            tipo_afiliacion = self.tipo_afiliacion

        liquidacion: None | str | Unset
        if isinstance(self.liquidacion, Unset):
            liquidacion = UNSET
        elif isinstance(self.liquidacion, LiquidacionTypeType1):
            liquidacion = self.liquidacion.value
        else:
            liquidacion = self.liquidacion


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if peso_neto_kilogramo is not UNSET:
            field_dict["pesoNetoKilogramo"] = peso_neto_kilogramo
        if peso_neto_mineria is not UNSET:
            field_dict["pesoNetoMineria"] = peso_neto_mineria
        if tipo_afiliacion is not UNSET:
            field_dict["tipoAfiliacion"] = tipo_afiliacion
        if liquidacion is not UNSET:
            field_dict["liquidacion"] = liquidacion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_peso_neto_kilogramo(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        peso_neto_kilogramo = _parse_peso_neto_kilogramo(d.pop("pesoNetoKilogramo", UNSET))


        def _parse_peso_neto_mineria(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        peso_neto_mineria = _parse_peso_neto_mineria(d.pop("pesoNetoMineria", UNSET))


        def _parse_tipo_afiliacion(data: object) -> None | TipoAfiliacionTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_tipo_afiliacion_type_type_1 = TipoAfiliacionTypeType1(data)



                return componentsschemas_tipo_afiliacion_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TipoAfiliacionTypeType1 | Unset, data)

        tipo_afiliacion = _parse_tipo_afiliacion(d.pop("tipoAfiliacion", UNSET))


        def _parse_liquidacion(data: object) -> LiquidacionTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_liquidacion_type_type_1 = LiquidacionTypeType1(data)



                return componentsschemas_liquidacion_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LiquidacionTypeType1 | None | Unset, data)

        liquidacion = _parse_liquidacion(d.pop("liquidacion", UNSET))


        ecf_46_mineria = cls(
            peso_neto_kilogramo=peso_neto_kilogramo,
            peso_neto_mineria=peso_neto_mineria,
            tipo_afiliacion=tipo_afiliacion,
            liquidacion=liquidacion,
        )


        ecf_46_mineria.additional_properties = d
        return ecf_46_mineria

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
