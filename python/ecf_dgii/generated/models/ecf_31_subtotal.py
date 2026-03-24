from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf31Subtotal")



@_attrs_define
class Ecf31Subtotal:
    """ 
        Example:
            {'lineas': None, 'subTotalMontoGravadoI1': None, 'subTotaITBIS3': None, 'subTotalMontoGravadoTotal': None,
                'subTotalMontoGravadoI3': None, 'subTotaITBIS2': None, 'subTotalMontoGravadoI2': None, 'subTotaITBIS1': None,
                'descripcionSubtotal': 'descripcionSubtotal', 'subTotaITBIS': None, 'numeroSubTotal': None,
                'subTotalImpuestoAdicional': None, 'montoSubTotal': None, 'orden': None, 'subTotalExento': None}

        Attributes:
            numero_sub_total (int | None | str | Unset):
            descripcion_subtotal (None | str | Unset):
            orden (int | None | str | Unset):
            sub_total_monto_gravado_total (float | None | str | Unset):
            sub_total_monto_gravado_i1 (float | None | str | Unset):
            sub_total_monto_gravado_i2 (float | None | str | Unset):
            sub_total_monto_gravado_i3 (float | None | str | Unset):
            sub_tota_itbis (float | None | str | Unset):
            sub_tota_itbis1 (float | None | str | Unset):
            sub_tota_itbis2 (float | None | str | Unset):
            sub_tota_itbis3 (float | None | str | Unset):
            sub_total_impuesto_adicional (float | None | str | Unset):
            sub_total_exento (float | None | str | Unset):
            monto_sub_total (float | None | str | Unset):
            lineas (int | None | str | Unset):
     """

    numero_sub_total: int | None | str | Unset = UNSET
    descripcion_subtotal: None | str | Unset = UNSET
    orden: int | None | str | Unset = UNSET
    sub_total_monto_gravado_total: float | None | str | Unset = UNSET
    sub_total_monto_gravado_i1: float | None | str | Unset = UNSET
    sub_total_monto_gravado_i2: float | None | str | Unset = UNSET
    sub_total_monto_gravado_i3: float | None | str | Unset = UNSET
    sub_tota_itbis: float | None | str | Unset = UNSET
    sub_tota_itbis1: float | None | str | Unset = UNSET
    sub_tota_itbis2: float | None | str | Unset = UNSET
    sub_tota_itbis3: float | None | str | Unset = UNSET
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

        sub_total_monto_gravado_total: float | None | str | Unset
        if isinstance(self.sub_total_monto_gravado_total, Unset):
            sub_total_monto_gravado_total = UNSET
        else:
            sub_total_monto_gravado_total = self.sub_total_monto_gravado_total

        sub_total_monto_gravado_i1: float | None | str | Unset
        if isinstance(self.sub_total_monto_gravado_i1, Unset):
            sub_total_monto_gravado_i1 = UNSET
        else:
            sub_total_monto_gravado_i1 = self.sub_total_monto_gravado_i1

        sub_total_monto_gravado_i2: float | None | str | Unset
        if isinstance(self.sub_total_monto_gravado_i2, Unset):
            sub_total_monto_gravado_i2 = UNSET
        else:
            sub_total_monto_gravado_i2 = self.sub_total_monto_gravado_i2

        sub_total_monto_gravado_i3: float | None | str | Unset
        if isinstance(self.sub_total_monto_gravado_i3, Unset):
            sub_total_monto_gravado_i3 = UNSET
        else:
            sub_total_monto_gravado_i3 = self.sub_total_monto_gravado_i3

        sub_tota_itbis: float | None | str | Unset
        if isinstance(self.sub_tota_itbis, Unset):
            sub_tota_itbis = UNSET
        else:
            sub_tota_itbis = self.sub_tota_itbis

        sub_tota_itbis1: float | None | str | Unset
        if isinstance(self.sub_tota_itbis1, Unset):
            sub_tota_itbis1 = UNSET
        else:
            sub_tota_itbis1 = self.sub_tota_itbis1

        sub_tota_itbis2: float | None | str | Unset
        if isinstance(self.sub_tota_itbis2, Unset):
            sub_tota_itbis2 = UNSET
        else:
            sub_tota_itbis2 = self.sub_tota_itbis2

        sub_tota_itbis3: float | None | str | Unset
        if isinstance(self.sub_tota_itbis3, Unset):
            sub_tota_itbis3 = UNSET
        else:
            sub_tota_itbis3 = self.sub_tota_itbis3

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
        if sub_total_monto_gravado_total is not UNSET:
            field_dict["subTotalMontoGravadoTotal"] = sub_total_monto_gravado_total
        if sub_total_monto_gravado_i1 is not UNSET:
            field_dict["subTotalMontoGravadoI1"] = sub_total_monto_gravado_i1
        if sub_total_monto_gravado_i2 is not UNSET:
            field_dict["subTotalMontoGravadoI2"] = sub_total_monto_gravado_i2
        if sub_total_monto_gravado_i3 is not UNSET:
            field_dict["subTotalMontoGravadoI3"] = sub_total_monto_gravado_i3
        if sub_tota_itbis is not UNSET:
            field_dict["subTotaITBIS"] = sub_tota_itbis
        if sub_tota_itbis1 is not UNSET:
            field_dict["subTotaITBIS1"] = sub_tota_itbis1
        if sub_tota_itbis2 is not UNSET:
            field_dict["subTotaITBIS2"] = sub_tota_itbis2
        if sub_tota_itbis3 is not UNSET:
            field_dict["subTotaITBIS3"] = sub_tota_itbis3
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


        def _parse_sub_total_monto_gravado_total(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_total_monto_gravado_total = _parse_sub_total_monto_gravado_total(d.pop("subTotalMontoGravadoTotal", UNSET))


        def _parse_sub_total_monto_gravado_i1(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_total_monto_gravado_i1 = _parse_sub_total_monto_gravado_i1(d.pop("subTotalMontoGravadoI1", UNSET))


        def _parse_sub_total_monto_gravado_i2(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_total_monto_gravado_i2 = _parse_sub_total_monto_gravado_i2(d.pop("subTotalMontoGravadoI2", UNSET))


        def _parse_sub_total_monto_gravado_i3(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_total_monto_gravado_i3 = _parse_sub_total_monto_gravado_i3(d.pop("subTotalMontoGravadoI3", UNSET))


        def _parse_sub_tota_itbis(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_tota_itbis = _parse_sub_tota_itbis(d.pop("subTotaITBIS", UNSET))


        def _parse_sub_tota_itbis1(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_tota_itbis1 = _parse_sub_tota_itbis1(d.pop("subTotaITBIS1", UNSET))


        def _parse_sub_tota_itbis2(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_tota_itbis2 = _parse_sub_tota_itbis2(d.pop("subTotaITBIS2", UNSET))


        def _parse_sub_tota_itbis3(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_tota_itbis3 = _parse_sub_tota_itbis3(d.pop("subTotaITBIS3", UNSET))


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


        ecf_31_subtotal = cls(
            numero_sub_total=numero_sub_total,
            descripcion_subtotal=descripcion_subtotal,
            orden=orden,
            sub_total_monto_gravado_total=sub_total_monto_gravado_total,
            sub_total_monto_gravado_i1=sub_total_monto_gravado_i1,
            sub_total_monto_gravado_i2=sub_total_monto_gravado_i2,
            sub_total_monto_gravado_i3=sub_total_monto_gravado_i3,
            sub_tota_itbis=sub_tota_itbis,
            sub_tota_itbis1=sub_tota_itbis1,
            sub_tota_itbis2=sub_tota_itbis2,
            sub_tota_itbis3=sub_tota_itbis3,
            sub_total_impuesto_adicional=sub_total_impuesto_adicional,
            sub_total_exento=sub_total_exento,
            monto_sub_total=monto_sub_total,
            lineas=lineas,
        )


        ecf_31_subtotal.additional_properties = d
        return ecf_31_subtotal

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
