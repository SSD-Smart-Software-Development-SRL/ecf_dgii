from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.codificacion_tipo_impuestos_type_type_1 import CodificacionTipoImpuestosTypeType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf44ImpuestoAdicionalOtraMoneda")



@_attrs_define
class Ecf44ImpuestoAdicionalOtraMoneda:
    """ 
        Attributes:
            tipo_impuesto_otra_moneda (CodificacionTipoImpuestosTypeType1 | None | Unset):
            tasa_impuesto_adicional_otra_moneda (float | None | str | Unset):
            otros_impuestos_adicionales_otra_moneda (float | None | str | Unset):
     """

    tipo_impuesto_otra_moneda: CodificacionTipoImpuestosTypeType1 | None | Unset = UNSET
    tasa_impuesto_adicional_otra_moneda: float | None | str | Unset = UNSET
    otros_impuestos_adicionales_otra_moneda: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_impuesto_otra_moneda: None | str | Unset
        if isinstance(self.tipo_impuesto_otra_moneda, Unset):
            tipo_impuesto_otra_moneda = UNSET
        elif isinstance(self.tipo_impuesto_otra_moneda, CodificacionTipoImpuestosTypeType1):
            tipo_impuesto_otra_moneda = self.tipo_impuesto_otra_moneda.value
        else:
            tipo_impuesto_otra_moneda = self.tipo_impuesto_otra_moneda

        tasa_impuesto_adicional_otra_moneda: float | None | str | Unset
        if isinstance(self.tasa_impuesto_adicional_otra_moneda, Unset):
            tasa_impuesto_adicional_otra_moneda = UNSET
        else:
            tasa_impuesto_adicional_otra_moneda = self.tasa_impuesto_adicional_otra_moneda

        otros_impuestos_adicionales_otra_moneda: float | None | str | Unset
        if isinstance(self.otros_impuestos_adicionales_otra_moneda, Unset):
            otros_impuestos_adicionales_otra_moneda = UNSET
        else:
            otros_impuestos_adicionales_otra_moneda = self.otros_impuestos_adicionales_otra_moneda


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tipo_impuesto_otra_moneda is not UNSET:
            field_dict["tipoImpuestoOtraMoneda"] = tipo_impuesto_otra_moneda
        if tasa_impuesto_adicional_otra_moneda is not UNSET:
            field_dict["tasaImpuestoAdicionalOtraMoneda"] = tasa_impuesto_adicional_otra_moneda
        if otros_impuestos_adicionales_otra_moneda is not UNSET:
            field_dict["otrosImpuestosAdicionalesOtraMoneda"] = otros_impuestos_adicionales_otra_moneda

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_tipo_impuesto_otra_moneda(data: object) -> CodificacionTipoImpuestosTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_codificacion_tipo_impuestos_type_type_1 = CodificacionTipoImpuestosTypeType1(data)



                return componentsschemas_codificacion_tipo_impuestos_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CodificacionTipoImpuestosTypeType1 | None | Unset, data)

        tipo_impuesto_otra_moneda = _parse_tipo_impuesto_otra_moneda(d.pop("tipoImpuestoOtraMoneda", UNSET))


        def _parse_tasa_impuesto_adicional_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        tasa_impuesto_adicional_otra_moneda = _parse_tasa_impuesto_adicional_otra_moneda(d.pop("tasaImpuestoAdicionalOtraMoneda", UNSET))


        def _parse_otros_impuestos_adicionales_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        otros_impuestos_adicionales_otra_moneda = _parse_otros_impuestos_adicionales_otra_moneda(d.pop("otrosImpuestosAdicionalesOtraMoneda", UNSET))


        ecf_44_impuesto_adicional_otra_moneda = cls(
            tipo_impuesto_otra_moneda=tipo_impuesto_otra_moneda,
            tasa_impuesto_adicional_otra_moneda=tasa_impuesto_adicional_otra_moneda,
            otros_impuestos_adicionales_otra_moneda=otros_impuestos_adicionales_otra_moneda,
        )


        ecf_44_impuesto_adicional_otra_moneda.additional_properties = d
        return ecf_44_impuesto_adicional_otra_moneda

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
