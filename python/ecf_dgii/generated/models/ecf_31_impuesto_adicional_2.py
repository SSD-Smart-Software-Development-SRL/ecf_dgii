from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_31_codificacion_tipo_impuestos_type import Ecf31CodificacionTipoImpuestosType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf31ImpuestoAdicional2")



@_attrs_define
class Ecf31ImpuestoAdicional2:
    """ 
        Example:
            {'tipoImpuesto': '001', 'montoImpuestoSelectivoConsumoAdvalorem': None, 'tasaImpuestoAdicional':
                5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None, 'otrosImpuestosAdicionales': None}

        Attributes:
            tipo_impuesto (Ecf31CodificacionTipoImpuestosType):
            tasa_impuesto_adicional (float | str):
            monto_impuesto_selectivo_consumo_especifico (float | None | str | Unset):
            monto_impuesto_selectivo_consumo_advalorem (float | None | str | Unset):
            otros_impuestos_adicionales (float | None | str | Unset):
     """

    tipo_impuesto: Ecf31CodificacionTipoImpuestosType
    tasa_impuesto_adicional: float | str
    monto_impuesto_selectivo_consumo_especifico: float | None | str | Unset = UNSET
    monto_impuesto_selectivo_consumo_advalorem: float | None | str | Unset = UNSET
    otros_impuestos_adicionales: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_impuesto = self.tipo_impuesto.value

        tasa_impuesto_adicional: float | str
        tasa_impuesto_adicional = self.tasa_impuesto_adicional

        monto_impuesto_selectivo_consumo_especifico: float | None | str | Unset
        if isinstance(self.monto_impuesto_selectivo_consumo_especifico, Unset):
            monto_impuesto_selectivo_consumo_especifico = UNSET
        else:
            monto_impuesto_selectivo_consumo_especifico = self.monto_impuesto_selectivo_consumo_especifico

        monto_impuesto_selectivo_consumo_advalorem: float | None | str | Unset
        if isinstance(self.monto_impuesto_selectivo_consumo_advalorem, Unset):
            monto_impuesto_selectivo_consumo_advalorem = UNSET
        else:
            monto_impuesto_selectivo_consumo_advalorem = self.monto_impuesto_selectivo_consumo_advalorem

        otros_impuestos_adicionales: float | None | str | Unset
        if isinstance(self.otros_impuestos_adicionales, Unset):
            otros_impuestos_adicionales = UNSET
        else:
            otros_impuestos_adicionales = self.otros_impuestos_adicionales


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tipoImpuesto": tipo_impuesto,
            "tasaImpuestoAdicional": tasa_impuesto_adicional,
        })
        if monto_impuesto_selectivo_consumo_especifico is not UNSET:
            field_dict["montoImpuestoSelectivoConsumoEspecifico"] = monto_impuesto_selectivo_consumo_especifico
        if monto_impuesto_selectivo_consumo_advalorem is not UNSET:
            field_dict["montoImpuestoSelectivoConsumoAdvalorem"] = monto_impuesto_selectivo_consumo_advalorem
        if otros_impuestos_adicionales is not UNSET:
            field_dict["otrosImpuestosAdicionales"] = otros_impuestos_adicionales

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tipo_impuesto = Ecf31CodificacionTipoImpuestosType(d.pop("tipoImpuesto"))




        def _parse_tasa_impuesto_adicional(data: object) -> float | str:
            return cast(float | str, data)

        tasa_impuesto_adicional = _parse_tasa_impuesto_adicional(d.pop("tasaImpuestoAdicional"))


        def _parse_monto_impuesto_selectivo_consumo_especifico(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_impuesto_selectivo_consumo_especifico = _parse_monto_impuesto_selectivo_consumo_especifico(d.pop("montoImpuestoSelectivoConsumoEspecifico", UNSET))


        def _parse_monto_impuesto_selectivo_consumo_advalorem(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_impuesto_selectivo_consumo_advalorem = _parse_monto_impuesto_selectivo_consumo_advalorem(d.pop("montoImpuestoSelectivoConsumoAdvalorem", UNSET))


        def _parse_otros_impuestos_adicionales(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        otros_impuestos_adicionales = _parse_otros_impuestos_adicionales(d.pop("otrosImpuestosAdicionales", UNSET))


        ecf_31_impuesto_adicional_2 = cls(
            tipo_impuesto=tipo_impuesto,
            tasa_impuesto_adicional=tasa_impuesto_adicional,
            monto_impuesto_selectivo_consumo_especifico=monto_impuesto_selectivo_consumo_especifico,
            monto_impuesto_selectivo_consumo_advalorem=monto_impuesto_selectivo_consumo_advalorem,
            otros_impuestos_adicionales=otros_impuestos_adicionales,
        )


        ecf_31_impuesto_adicional_2.additional_properties = d
        return ecf_31_impuesto_adicional_2

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
