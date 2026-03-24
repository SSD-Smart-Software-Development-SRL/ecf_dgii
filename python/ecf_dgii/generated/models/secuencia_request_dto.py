from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SecuenciaRequestDto")



@_attrs_define
class SecuenciaRequestDto:
    """ 
        Example:
            {'hastaEncf': 'hastaEncf', 'desdeEncf': 'desdeEncf'}

        Attributes:
            desde_encf (str | Unset):
            hasta_encf (str | Unset):
     """

    desde_encf: str | Unset = UNSET
    hasta_encf: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        desde_encf = self.desde_encf

        hasta_encf = self.hasta_encf


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if desde_encf is not UNSET:
            field_dict["desdeEncf"] = desde_encf
        if hasta_encf is not UNSET:
            field_dict["hastaEncf"] = hasta_encf

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        desde_encf = d.pop("desdeEncf", UNSET)

        hasta_encf = d.pop("hastaEncf", UNSET)

        secuencia_request_dto = cls(
            desde_encf=desde_encf,
            hasta_encf=hasta_encf,
        )


        secuencia_request_dto.additional_properties = d
        return secuencia_request_dto

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
