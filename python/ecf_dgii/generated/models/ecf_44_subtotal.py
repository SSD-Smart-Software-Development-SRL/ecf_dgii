from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf44Subtotal")



@_attrs_define
class Ecf44Subtotal:
    """ 
        Example:
            {'lineas': None, 'descripcionSubtotal': 'descripcionSubtotal', 'numeroSubTotal': None,
                'subTotalImpuestoAdicional': None, 'montoSubTotal': None, 'orden': None, 'subTotalExento': None}

        Attributes:
            numero_sub_total (int | None | str | Unset):
            descripcion_subtotal (None | str | Unset):
            orden (int | None | str | Unset):
            sub_total_impuesto_adicional (float | None | str | Unset):
            sub_total_exento (float | None | str | Unset):
            monto_sub_total (float | None | str | Unset):
            lineas (int | None | str | Unset):
     """

    numero_sub_total: int | None | str | Unset = UNSET
    descripcion_subtotal: None | str | Unset = UNSET
    orden: int | None | str | Unset = UNSET
    sub_total_impuesto_adicional: float | None | str | Unset = UNSET
    sub_total_exento: float | None | str | Unset = UNSET
    monto_sub_total: float | None | str | Unset = UNSET
    lineas: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        numero_sub_total: int | None | str | Unset
        if isinstance(self.numero_sub_total, Unset):
            numero_sub_total = UNSET
        else:
            numero_sub_total = self.numero_sub_total

        descripcion_subtotal: None | str | Unset
        if isinstance(self.descripcion_subtotal, Unset):
            descripcion_subtotal = UNSET
        else:
            descripcion_subtotal = self.descripcion_subtotal

        orden: int | None | str | Unset
        if isinstance(self.orden, Unset):
            orden = UNSET
        else:
            orden = self.orden

        sub_total_impuesto_adicional: float | None | str | Unset
        if isinstance(self.sub_total_impuesto_adicional, Unset):
            sub_total_impuesto_adicional = UNSET
        else:
            sub_total_impuesto_adicional = self.sub_total_impuesto_adicional

        sub_total_exento: float | None | str | Unset
        if isinstance(self.sub_total_exento, Unset):
            sub_total_exento = UNSET
        else:
            sub_total_exento = self.sub_total_exento

        monto_sub_total: float | None | str | Unset
        if isinstance(self.monto_sub_total, Unset):
            monto_sub_total = UNSET
        else:
            monto_sub_total = self.monto_sub_total

        lineas: int | None | str | Unset
        if isinstance(self.lineas, Unset):
            lineas = UNSET
        else:
            lineas = self.lineas


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if numero_sub_total is not UNSET:
            field_dict["numeroSubTotal"] = numero_sub_total
        if descripcion_subtotal is not UNSET:
            field_dict["descripcionSubtotal"] = descripcion_subtotal
        if orden is not UNSET:
            field_dict["orden"] = orden
        if sub_total_impuesto_adicional is not UNSET:
            field_dict["subTotalImpuestoAdicional"] = sub_total_impuesto_adicional
        if sub_total_exento is not UNSET:
            field_dict["subTotalExento"] = sub_total_exento
        if monto_sub_total is not UNSET:
            field_dict["montoSubTotal"] = monto_sub_total
        if lineas is not UNSET:
            field_dict["lineas"] = lineas

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_numero_sub_total(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        numero_sub_total = _parse_numero_sub_total(d.pop("numeroSubTotal", UNSET))


        def _parse_descripcion_subtotal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descripcion_subtotal = _parse_descripcion_subtotal(d.pop("descripcionSubtotal", UNSET))


        def _parse_orden(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        orden = _parse_orden(d.pop("orden", UNSET))


        def _parse_sub_total_impuesto_adicional(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_total_impuesto_adicional = _parse_sub_total_impuesto_adicional(d.pop("subTotalImpuestoAdicional", UNSET))


        def _parse_sub_total_exento(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_total_exento = _parse_sub_total_exento(d.pop("subTotalExento", UNSET))


        def _parse_monto_sub_total(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_sub_total = _parse_monto_sub_total(d.pop("montoSubTotal", UNSET))


        def _parse_lineas(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        lineas = _parse_lineas(d.pop("lineas", UNSET))


        ecf_44_subtotal = cls(
            numero_sub_total=numero_sub_total,
            descripcion_subtotal=descripcion_subtotal,
            orden=orden,
            sub_total_impuesto_adicional=sub_total_impuesto_adicional,
            sub_total_exento=sub_total_exento,
            monto_sub_total=monto_sub_total,
            lineas=lineas,
        )


        ecf_44_subtotal.additional_properties = d
        return ecf_44_subtotal

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
