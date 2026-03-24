from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf47Transporte")



@_attrs_define
class Ecf47Transporte:
    """ 
        Attributes:
            pais_destino (None | str | Unset):
     """

    pais_destino: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        pais_destino: None | str | Unset
        if isinstance(self.pais_destino, Unset):
            pais_destino = UNSET
        else:
            pais_destino = self.pais_destino


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pais_destino is not UNSET:
            field_dict["paisDestino"] = pais_destino

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_pais_destino(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pais_destino = _parse_pais_destino(d.pop("paisDestino", UNSET))


        ecf_47_transporte = cls(
            pais_destino=pais_destino,
        )


        ecf_47_transporte.additional_properties = d
        return ecf_47_transporte

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
