from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf47Comprador")



@_attrs_define
class Ecf47Comprador:
    """ 
        Attributes:
            identificador_extranjero (None | str | Unset):
            razon_social_comprador (None | str | Unset):
     """

    identificador_extranjero: None | str | Unset = UNSET
    razon_social_comprador: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        identificador_extranjero: None | str | Unset
        if isinstance(self.identificador_extranjero, Unset):
            identificador_extranjero = UNSET
        else:
            identificador_extranjero = self.identificador_extranjero

        razon_social_comprador: None | str | Unset
        if isinstance(self.razon_social_comprador, Unset):
            razon_social_comprador = UNSET
        else:
            razon_social_comprador = self.razon_social_comprador


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if identificador_extranjero is not UNSET:
            field_dict["identificadorExtranjero"] = identificador_extranjero
        if razon_social_comprador is not UNSET:
            field_dict["razonSocialComprador"] = razon_social_comprador

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_identificador_extranjero(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identificador_extranjero = _parse_identificador_extranjero(d.pop("identificadorExtranjero", UNSET))


        def _parse_razon_social_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        razon_social_comprador = _parse_razon_social_comprador(d.pop("razonSocialComprador", UNSET))


        ecf_47_comprador = cls(
            identificador_extranjero=identificador_extranjero,
            razon_social_comprador=razon_social_comprador,
        )


        ecf_47_comprador.additional_properties = d
        return ecf_47_comprador

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
