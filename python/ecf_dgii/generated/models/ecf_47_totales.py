from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf47Totales")



@_attrs_define
class Ecf47Totales:
    """ 
        Example:
            {'montoPeriodo': 5.962133916683182, 'saldoAnterior': None, 'montoAvancePago': None, 'totalISRRetencion': None,
                'montoExento': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None}

        Attributes:
            monto_total (float | str):
            monto_exento (float | None | str | Unset):
            monto_periodo (float | None | str | Unset):
            saldo_anterior (float | None | str | Unset):
            monto_avance_pago (float | None | str | Unset):
            valor_pagar (float | None | str | Unset):
            total_isr_retencion (float | None | str | Unset):
     """

    monto_total: float | str
    monto_exento: float | None | str | Unset = UNSET
    monto_periodo: float | None | str | Unset = UNSET
    saldo_anterior: float | None | str | Unset = UNSET
    monto_avance_pago: float | None | str | Unset = UNSET
    valor_pagar: float | None | str | Unset = UNSET
    total_isr_retencion: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        monto_total: float | str
        monto_total = self.monto_total

        monto_exento: float | None | str | Unset
        if isinstance(self.monto_exento, Unset):
            monto_exento = UNSET
        else:
            monto_exento = self.monto_exento

        monto_periodo: float | None | str | Unset
        if isinstance(self.monto_periodo, Unset):
            monto_periodo = UNSET
        else:
            monto_periodo = self.monto_periodo

        saldo_anterior: float | None | str | Unset
        if isinstance(self.saldo_anterior, Unset):
            saldo_anterior = UNSET
        else:
            saldo_anterior = self.saldo_anterior

        monto_avance_pago: float | None | str | Unset
        if isinstance(self.monto_avance_pago, Unset):
            monto_avance_pago = UNSET
        else:
            monto_avance_pago = self.monto_avance_pago

        valor_pagar: float | None | str | Unset
        if isinstance(self.valor_pagar, Unset):
            valor_pagar = UNSET
        else:
            valor_pagar = self.valor_pagar

        total_isr_retencion: float | None | str | Unset
        if isinstance(self.total_isr_retencion, Unset):
            total_isr_retencion = UNSET
        else:
            total_isr_retencion = self.total_isr_retencion


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "montoTotal": monto_total,
        })
        if monto_exento is not UNSET:
            field_dict["montoExento"] = monto_exento
        if monto_periodo is not UNSET:
            field_dict["montoPeriodo"] = monto_periodo
        if saldo_anterior is not UNSET:
            field_dict["saldoAnterior"] = saldo_anterior
        if monto_avance_pago is not UNSET:
            field_dict["montoAvancePago"] = monto_avance_pago
        if valor_pagar is not UNSET:
            field_dict["valorPagar"] = valor_pagar
        if total_isr_retencion is not UNSET:
            field_dict["totalISRRetencion"] = total_isr_retencion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_monto_total(data: object) -> float | str:
            return cast(float | str, data)

        monto_total = _parse_monto_total(d.pop("montoTotal"))


        def _parse_monto_exento(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_exento = _parse_monto_exento(d.pop("montoExento", UNSET))


        def _parse_monto_periodo(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_periodo = _parse_monto_periodo(d.pop("montoPeriodo", UNSET))


        def _parse_saldo_anterior(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        saldo_anterior = _parse_saldo_anterior(d.pop("saldoAnterior", UNSET))


        def _parse_monto_avance_pago(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_avance_pago = _parse_monto_avance_pago(d.pop("montoAvancePago", UNSET))


        def _parse_valor_pagar(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        valor_pagar = _parse_valor_pagar(d.pop("valorPagar", UNSET))


        def _parse_total_isr_retencion(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_isr_retencion = _parse_total_isr_retencion(d.pop("totalISRRetencion", UNSET))


        ecf_47_totales = cls(
            monto_total=monto_total,
            monto_exento=monto_exento,
            monto_periodo=monto_periodo,
            saldo_anterior=saldo_anterior,
            monto_avance_pago=monto_avance_pago,
            valor_pagar=valor_pagar,
            total_isr_retencion=total_isr_retencion,
        )


        ecf_47_totales.additional_properties = d
        return ecf_47_totales

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
