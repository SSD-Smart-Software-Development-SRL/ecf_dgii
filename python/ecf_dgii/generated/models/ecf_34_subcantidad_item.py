from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.unidad_medida_type_type_1 import UnidadMedidaTypeType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf34SubcantidadItem")



@_attrs_define
class Ecf34SubcantidadItem:
    """ 
        Example:
            {'codigoSubcantidad': '', 'subcantidad': 3.616076749251911}

        Attributes:
            subcantidad (float | None | str | Unset):
            codigo_subcantidad (None | UnidadMedidaTypeType1 | Unset):
     """

    subcantidad: float | None | str | Unset = UNSET
    codigo_subcantidad: None | UnidadMedidaTypeType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        subcantidad: float | None | str | Unset
        if isinstance(self.subcantidad, Unset):
            subcantidad = UNSET
        else:
            subcantidad = self.subcantidad

        codigo_subcantidad: None | str | Unset
        if isinstance(self.codigo_subcantidad, Unset):
            codigo_subcantidad = UNSET
        elif isinstance(self.codigo_subcantidad, UnidadMedidaTypeType1):
            codigo_subcantidad = self.codigo_subcantidad.value
        else:
            codigo_subcantidad = self.codigo_subcantidad


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if subcantidad is not UNSET:
            field_dict["subcantidad"] = subcantidad
        if codigo_subcantidad is not UNSET:
            field_dict["codigoSubcantidad"] = codigo_subcantidad

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_subcantidad(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subcantidad = _parse_subcantidad(d.pop("subcantidad", UNSET))


        def _parse_codigo_subcantidad(data: object) -> None | UnidadMedidaTypeType1 | Unset:
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

        codigo_subcantidad = _parse_codigo_subcantidad(d.pop("codigoSubcantidad", UNSET))


        ecf_34_subcantidad_item = cls(
            subcantidad=subcantidad,
            codigo_subcantidad=codigo_subcantidad,
        )


        ecf_34_subcantidad_item.additional_properties = d
        return ecf_34_subcantidad_item

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
