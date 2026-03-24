from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf44SubtotalImpuestoAdicional")



@_attrs_define
class Ecf44SubtotalImpuestoAdicional:
    """ 
        Attributes:
            subtotal_otros_impuesto (float | None | str | Unset):
     """

    subtotal_otros_impuesto: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        subtotal_otros_impuesto: float | None | str | Unset
        if isinstance(self.subtotal_otros_impuesto, Unset):
            subtotal_otros_impuesto = UNSET
        else:
            subtotal_otros_impuesto = self.subtotal_otros_impuesto


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if subtotal_otros_impuesto is not UNSET:
            field_dict["subtotalOtrosImpuesto"] = subtotal_otros_impuesto

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_subtotal_otros_impuesto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_otros_impuesto = _parse_subtotal_otros_impuesto(d.pop("subtotalOtrosImpuesto", UNSET))


        ecf_44_subtotal_impuesto_adicional = cls(
            subtotal_otros_impuesto=subtotal_otros_impuesto,
        )


        ecf_44_subtotal_impuesto_adicional.additional_properties = d
        return ecf_44_subtotal_impuesto_adicional

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
