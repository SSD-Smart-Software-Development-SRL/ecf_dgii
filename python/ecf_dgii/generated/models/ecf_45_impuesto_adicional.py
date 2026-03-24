from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_45_codificacion_tipo_impuestos_type import Ecf45CodificacionTipoImpuestosType






T = TypeVar("T", bound="Ecf45ImpuestoAdicional")



@_attrs_define
class Ecf45ImpuestoAdicional:
    """ 
        Example:
            {'tipoImpuesto': None}

        Attributes:
            tipo_impuesto (Ecf45CodificacionTipoImpuestosType):
     """

    tipo_impuesto: Ecf45CodificacionTipoImpuestosType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_impuesto = self.tipo_impuesto.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tipoImpuesto": tipo_impuesto,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tipo_impuesto = Ecf45CodificacionTipoImpuestosType(d.pop("tipoImpuesto"))




        ecf_45_impuesto_adicional = cls(
            tipo_impuesto=tipo_impuesto,
        )


        ecf_45_impuesto_adicional.additional_properties = d
        return ecf_45_impuesto_adicional

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
