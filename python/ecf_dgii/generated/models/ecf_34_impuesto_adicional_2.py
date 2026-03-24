from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.codificacion_tipo_impuestos_type_type_1 import CodificacionTipoImpuestosTypeType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf34ImpuestoAdicional2")



@_attrs_define
class Ecf34ImpuestoAdicional2:
    """ 
        Example:
            {'tipoImpuesto': '', 'montoImpuestoSelectivoConsumoAdvalorem': None, 'tasaImpuestoAdicional': 5.637376656633329,
                'montoImpuestoSelectivoConsumoEspecifico': None, 'otrosImpuestosAdicionales': None}

        Attributes:
            tipo_impuesto (CodificacionTipoImpuestosTypeType1 | None | Unset):
            tasa_impuesto_adicional (float | None | str | Unset):
            monto_impuesto_selectivo_consumo_especifico (float | None | str | Unset):
            monto_impuesto_selectivo_consumo_advalorem (float | None | str | Unset):
            otros_impuestos_adicionales (float | None | str | Unset):
     """

    tipo_impuesto: CodificacionTipoImpuestosTypeType1 | None | Unset = UNSET
    tasa_impuesto_adicional: float | None | str | Unset = UNSET
    monto_impuesto_selectivo_consumo_especifico: float | None | str | Unset = UNSET
    monto_impuesto_selectivo_consumo_advalorem: float | None | str | Unset = UNSET
    otros_impuestos_adicionales: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_impuesto: None | str | Unset
        if isinstance(self.tipo_impuesto, Unset):
            tipo_impuesto = UNSET
        elif isinstance(self.tipo_impuesto, CodificacionTipoImpuestosTypeType1):
            tipo_impuesto = self.tipo_impuesto.value
        else:
            tipo_impuesto = self.tipo_impuesto

        tasa_impuesto_adicional: float | None | str | Unset
        if isinstance(self.tasa_impuesto_adicional, Unset):
            tasa_impuesto_adicional = UNSET
        else:
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
        })
        if tipo_impuesto is not UNSET:
            field_dict["tipoImpuesto"] = tipo_impuesto
        if tasa_impuesto_adicional is not UNSET:
            field_dict["tasaImpuestoAdicional"] = tasa_impuesto_adicional
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
        def _parse_tipo_impuesto(data: object) -> CodificacionTipoImpuestosTypeType1 | None | Unset:
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

        tipo_impuesto = _parse_tipo_impuesto(d.pop("tipoImpuesto", UNSET))


        def _parse_tasa_impuesto_adicional(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        tasa_impuesto_adicional = _parse_tasa_impuesto_adicional(d.pop("tasaImpuestoAdicional", UNSET))


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


        ecf_34_impuesto_adicional_2 = cls(
            tipo_impuesto=tipo_impuesto,
            tasa_impuesto_adicional=tasa_impuesto_adicional,
            monto_impuesto_selectivo_consumo_especifico=monto_impuesto_selectivo_consumo_especifico,
            monto_impuesto_selectivo_consumo_advalorem=monto_impuesto_selectivo_consumo_advalorem,
            otros_impuestos_adicionales=otros_impuestos_adicionales,
        )


        ecf_34_impuesto_adicional_2.additional_properties = d
        return ecf_34_impuesto_adicional_2

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
