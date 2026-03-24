from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_44_codificacion_tipo_impuestos_type import Ecf44CodificacionTipoImpuestosType
from typing import cast






T = TypeVar("T", bound="Ecf44ImpuestoAdicional2")



@_attrs_define
class Ecf44ImpuestoAdicional2:
    """ 
        Example:
            {'tipoImpuesto': '001', 'tasaImpuestoAdicional': 5.637376656633329, 'otrosImpuestosAdicionales':
                2.3021358869347655}

        Attributes:
            tipo_impuesto (Ecf44CodificacionTipoImpuestosType):
            tasa_impuesto_adicional (float | str):
            otros_impuestos_adicionales (float | str):
     """

    tipo_impuesto: Ecf44CodificacionTipoImpuestosType
    tasa_impuesto_adicional: float | str
    otros_impuestos_adicionales: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_impuesto = self.tipo_impuesto.value

        tasa_impuesto_adicional: float | str
        tasa_impuesto_adicional = self.tasa_impuesto_adicional

        otros_impuestos_adicionales: float | str
        otros_impuestos_adicionales = self.otros_impuestos_adicionales


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tipoImpuesto": tipo_impuesto,
            "tasaImpuestoAdicional": tasa_impuesto_adicional,
            "otrosImpuestosAdicionales": otros_impuestos_adicionales,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tipo_impuesto = Ecf44CodificacionTipoImpuestosType(d.pop("tipoImpuesto"))




        def _parse_tasa_impuesto_adicional(data: object) -> float | str:
            return cast(float | str, data)

        tasa_impuesto_adicional = _parse_tasa_impuesto_adicional(d.pop("tasaImpuestoAdicional"))


        def _parse_otros_impuestos_adicionales(data: object) -> float | str:
            return cast(float | str, data)

        otros_impuestos_adicionales = _parse_otros_impuestos_adicionales(d.pop("otrosImpuestosAdicionales"))


        ecf_44_impuesto_adicional_2 = cls(
            tipo_impuesto=tipo_impuesto,
            tasa_impuesto_adicional=tasa_impuesto_adicional,
            otros_impuestos_adicionales=otros_impuestos_adicionales,
        )


        ecf_44_impuesto_adicional_2.additional_properties = d
        return ecf_44_impuesto_adicional_2

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
