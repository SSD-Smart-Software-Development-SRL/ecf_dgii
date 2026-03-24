from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tipo_moneda_type_type_1 import TipoMonedaTypeType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf43OtraMoneda")



@_attrs_define
class Ecf43OtraMoneda:
    """ 
        Attributes:
            tipo_moneda (None | TipoMonedaTypeType1 | Unset):
            tipo_cambio (float | None | str | Unset):
            monto_exento_otra_moneda (float | None | str | Unset):
            monto_total_otra_moneda (float | None | str | Unset):
     """

    tipo_moneda: None | TipoMonedaTypeType1 | Unset = UNSET
    tipo_cambio: float | None | str | Unset = UNSET
    monto_exento_otra_moneda: float | None | str | Unset = UNSET
    monto_total_otra_moneda: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_moneda: None | str | Unset
        if isinstance(self.tipo_moneda, Unset):
            tipo_moneda = UNSET
        elif isinstance(self.tipo_moneda, TipoMonedaTypeType1):
            tipo_moneda = self.tipo_moneda.value
        else:
            tipo_moneda = self.tipo_moneda

        tipo_cambio: float | None | str | Unset
        if isinstance(self.tipo_cambio, Unset):
            tipo_cambio = UNSET
        else:
            tipo_cambio = self.tipo_cambio

        monto_exento_otra_moneda: float | None | str | Unset
        if isinstance(self.monto_exento_otra_moneda, Unset):
            monto_exento_otra_moneda = UNSET
        else:
            monto_exento_otra_moneda = self.monto_exento_otra_moneda

        monto_total_otra_moneda: float | None | str | Unset
        if isinstance(self.monto_total_otra_moneda, Unset):
            monto_total_otra_moneda = UNSET
        else:
            monto_total_otra_moneda = self.monto_total_otra_moneda


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tipo_moneda is not UNSET:
            field_dict["tipoMoneda"] = tipo_moneda
        if tipo_cambio is not UNSET:
            field_dict["tipoCambio"] = tipo_cambio
        if monto_exento_otra_moneda is not UNSET:
            field_dict["montoExentoOtraMoneda"] = monto_exento_otra_moneda
        if monto_total_otra_moneda is not UNSET:
            field_dict["montoTotalOtraMoneda"] = monto_total_otra_moneda

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_tipo_moneda(data: object) -> None | TipoMonedaTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_tipo_moneda_type_type_1 = TipoMonedaTypeType1(data)



                return componentsschemas_tipo_moneda_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TipoMonedaTypeType1 | Unset, data)

        tipo_moneda = _parse_tipo_moneda(d.pop("tipoMoneda", UNSET))


        def _parse_tipo_cambio(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        tipo_cambio = _parse_tipo_cambio(d.pop("tipoCambio", UNSET))


        def _parse_monto_exento_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_exento_otra_moneda = _parse_monto_exento_otra_moneda(d.pop("montoExentoOtraMoneda", UNSET))


        def _parse_monto_total_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_total_otra_moneda = _parse_monto_total_otra_moneda(d.pop("montoTotalOtraMoneda", UNSET))


        ecf_43_otra_moneda = cls(
            tipo_moneda=tipo_moneda,
            tipo_cambio=tipo_cambio,
            monto_exento_otra_moneda=monto_exento_otra_moneda,
            monto_total_otra_moneda=monto_total_otra_moneda,
        )


        ecf_43_otra_moneda.additional_properties = d
        return ecf_43_otra_moneda

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
