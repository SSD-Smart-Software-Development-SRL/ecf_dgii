from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="Ecf45CodigosItem")



@_attrs_define
class Ecf45CodigosItem:
    """ 
        Example:
            {'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}

        Attributes:
            tipo_codigo (str):
            codigo_item (str):
     """

    tipo_codigo: str
    codigo_item: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_codigo = self.tipo_codigo

        codigo_item = self.codigo_item


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tipoCodigo": tipo_codigo,
            "codigoItem": codigo_item,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tipo_codigo = d.pop("tipoCodigo")

        codigo_item = d.pop("codigoItem")

        ecf_45_codigos_item = cls(
            tipo_codigo=tipo_codigo,
            codigo_item=codigo_item,
        )


        ecf_45_codigos_item.additional_properties = d
        return ecf_45_codigos_item

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
