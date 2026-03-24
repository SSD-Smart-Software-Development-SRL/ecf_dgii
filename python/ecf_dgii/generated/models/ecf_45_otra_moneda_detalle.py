from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf45OtraMonedaDetalle")



@_attrs_define
class Ecf45OtraMonedaDetalle:
    """ 
        Attributes:
            precio_otra_moneda (float | None | str | Unset):
            descuento_otra_moneda (float | None | str | Unset):
            recargo_otra_moneda (float | None | str | Unset):
            monto_item_otra_moneda (float | None | str | Unset):
     """

    precio_otra_moneda: float | None | str | Unset = UNSET
    descuento_otra_moneda: float | None | str | Unset = UNSET
    recargo_otra_moneda: float | None | str | Unset = UNSET
    monto_item_otra_moneda: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        precio_otra_moneda: float | None | str | Unset
        if isinstance(self.precio_otra_moneda, Unset):
            precio_otra_moneda = UNSET
        else:
            precio_otra_moneda = self.precio_otra_moneda

        descuento_otra_moneda: float | None | str | Unset
        if isinstance(self.descuento_otra_moneda, Unset):
            descuento_otra_moneda = UNSET
        else:
            descuento_otra_moneda = self.descuento_otra_moneda

        recargo_otra_moneda: float | None | str | Unset
        if isinstance(self.recargo_otra_moneda, Unset):
            recargo_otra_moneda = UNSET
        else:
            recargo_otra_moneda = self.recargo_otra_moneda

        monto_item_otra_moneda: float | None | str | Unset
        if isinstance(self.monto_item_otra_moneda, Unset):
            monto_item_otra_moneda = UNSET
        else:
            monto_item_otra_moneda = self.monto_item_otra_moneda


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if precio_otra_moneda is not UNSET:
            field_dict["precioOtraMoneda"] = precio_otra_moneda
        if descuento_otra_moneda is not UNSET:
            field_dict["descuentoOtraMoneda"] = descuento_otra_moneda
        if recargo_otra_moneda is not UNSET:
            field_dict["recargoOtraMoneda"] = recargo_otra_moneda
        if monto_item_otra_moneda is not UNSET:
            field_dict["montoItemOtraMoneda"] = monto_item_otra_moneda

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_precio_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        precio_otra_moneda = _parse_precio_otra_moneda(d.pop("precioOtraMoneda", UNSET))


        def _parse_descuento_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        descuento_otra_moneda = _parse_descuento_otra_moneda(d.pop("descuentoOtraMoneda", UNSET))


        def _parse_recargo_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        recargo_otra_moneda = _parse_recargo_otra_moneda(d.pop("recargoOtraMoneda", UNSET))


        def _parse_monto_item_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_item_otra_moneda = _parse_monto_item_otra_moneda(d.pop("montoItemOtraMoneda", UNSET))


        ecf_45_otra_moneda_detalle = cls(
            precio_otra_moneda=precio_otra_moneda,
            descuento_otra_moneda=descuento_otra_moneda,
            recargo_otra_moneda=recargo_otra_moneda,
            monto_item_otra_moneda=monto_item_otra_moneda,
        )


        ecf_45_otra_moneda_detalle.additional_properties = d
        return ecf_45_otra_moneda_detalle

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
