from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpsertCompanyRequest")



@_attrs_define
class UpsertCompanyRequest:
    """ 
        Example:
            {'legalName': 'legalName', 'rnc': 'rnc', 'name': 'name'}

        Attributes:
            rnc (str):
            legal_name (str):
            name (str):
     """

    rnc: str
    legal_name: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rnc = self.rnc

        legal_name = self.legal_name

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rnc": rnc,
            "legalName": legal_name,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rnc = d.pop("rnc")

        legal_name = d.pop("legalName")

        name = d.pop("name")

        upsert_company_request = cls(
            rnc=rnc,
            legal_name=legal_name,
            name=name,
        )


        upsert_company_request.additional_properties = d
        return upsert_company_request

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
