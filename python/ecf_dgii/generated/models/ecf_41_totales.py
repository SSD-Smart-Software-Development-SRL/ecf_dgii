from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf41Totales")



@_attrs_define
class Ecf41Totales:
    """ 
        Example:
            {'montoPeriodo': 5.962133916683182, 'totalISRPercepcion': None, 'montoGravadoI3': None, 'montoGravadoI2': None,
                'montoAvancePago': None, 'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1': None, 'totalITBIS2': None,
                'totalITBISPercepcion': None, 'itbiS2': None, 'itbiS1': None, 'itbiS3': None, 'totalITBISRetenido': None,
                'totalITBIS': None, 'saldoAnterior': None, 'totalISRRetencion': None, 'montoExento': None, 'montoGravadoTotal':
                1.4658129805029452, 'valorPagar': None, 'montoTotal': None}

        Attributes:
            monto_total (float | str):
            monto_gravado_total (float | None | str | Unset):
            monto_gravado_i1 (float | None | str | Unset):
            monto_gravado_i2 (float | None | str | Unset):
            monto_gravado_i3 (float | None | str | Unset):
            monto_exento (float | None | str | Unset):
            itbi_s1 (int | None | str | Unset):
            itbi_s2 (int | None | str | Unset):
            itbi_s3 (int | None | str | Unset):
            total_itbis (float | None | str | Unset):
            total_itbis1 (float | None | str | Unset):
            total_itbis2 (float | None | str | Unset):
            total_itbis3 (float | None | str | Unset):
            monto_periodo (float | None | str | Unset):
            saldo_anterior (float | None | str | Unset):
            monto_avance_pago (float | None | str | Unset):
            valor_pagar (float | None | str | Unset):
            total_itbis_retenido (float | None | str | Unset):
            total_isr_retencion (float | None | str | Unset):
            total_itbis_percepcion (float | None | str | Unset):
            total_isr_percepcion (float | None | str | Unset):
     """

    monto_total: float | str
    monto_gravado_total: float | None | str | Unset = UNSET
    monto_gravado_i1: float | None | str | Unset = UNSET
    monto_gravado_i2: float | None | str | Unset = UNSET
    monto_gravado_i3: float | None | str | Unset = UNSET
    monto_exento: float | None | str | Unset = UNSET
    itbi_s1: int | None | str | Unset = UNSET
    itbi_s2: int | None | str | Unset = UNSET
    itbi_s3: int | None | str | Unset = UNSET
    total_itbis: float | None | str | Unset = UNSET
    total_itbis1: float | None | str | Unset = UNSET
    total_itbis2: float | None | str | Unset = UNSET
    total_itbis3: float | None | str | Unset = UNSET
    monto_periodo: float | None | str | Unset = UNSET
    saldo_anterior: float | None | str | Unset = UNSET
    monto_avance_pago: float | None | str | Unset = UNSET
    valor_pagar: float | None | str | Unset = UNSET
    total_itbis_retenido: float | None | str | Unset = UNSET
    total_isr_retencion: float | None | str | Unset = UNSET
    total_itbis_percepcion: float | None | str | Unset = UNSET
    total_isr_percepcion: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        monto_total: float | str
        monto_total = self.monto_total

        monto_gravado_total: float | None | str | Unset
        if isinstance(self.monto_gravado_total, Unset):
            monto_gravado_total = UNSET
        else:
            monto_gravado_total = self.monto_gravado_total

        monto_gravado_i1: float | None | str | Unset
        if isinstance(self.monto_gravado_i1, Unset):
            monto_gravado_i1 = UNSET
        else:
            monto_gravado_i1 = self.monto_gravado_i1

        monto_gravado_i2: float | None | str | Unset
        if isinstance(self.monto_gravado_i2, Unset):
            monto_gravado_i2 = UNSET
        else:
            monto_gravado_i2 = self.monto_gravado_i2

        monto_gravado_i3: float | None | str | Unset
        if isinstance(self.monto_gravado_i3, Unset):
            monto_gravado_i3 = UNSET
        else:
            monto_gravado_i3 = self.monto_gravado_i3

        monto_exento: float | None | str | Unset
        if isinstance(self.monto_exento, Unset):
            monto_exento = UNSET
        else:
            monto_exento = self.monto_exento

        itbi_s1: int | None | str | Unset
        if isinstance(self.itbi_s1, Unset):
            itbi_s1 = UNSET
        else:
            itbi_s1 = self.itbi_s1

        itbi_s2: int | None | str | Unset
        if isinstance(self.itbi_s2, Unset):
            itbi_s2 = UNSET
        else:
            itbi_s2 = self.itbi_s2

        itbi_s3: int | None | str | Unset
        if isinstance(self.itbi_s3, Unset):
            itbi_s3 = UNSET
        else:
            itbi_s3 = self.itbi_s3

        total_itbis: float | None | str | Unset
        if isinstance(self.total_itbis, Unset):
            total_itbis = UNSET
        else:
            total_itbis = self.total_itbis

        total_itbis1: float | None | str | Unset
        if isinstance(self.total_itbis1, Unset):
            total_itbis1 = UNSET
        else:
            total_itbis1 = self.total_itbis1

        total_itbis2: float | None | str | Unset
        if isinstance(self.total_itbis2, Unset):
            total_itbis2 = UNSET
        else:
            total_itbis2 = self.total_itbis2

        total_itbis3: float | None | str | Unset
        if isinstance(self.total_itbis3, Unset):
            total_itbis3 = UNSET
        else:
            total_itbis3 = self.total_itbis3

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

        total_itbis_retenido: float | None | str | Unset
        if isinstance(self.total_itbis_retenido, Unset):
            total_itbis_retenido = UNSET
        else:
            total_itbis_retenido = self.total_itbis_retenido

        total_isr_retencion: float | None | str | Unset
        if isinstance(self.total_isr_retencion, Unset):
            total_isr_retencion = UNSET
        else:
            total_isr_retencion = self.total_isr_retencion

        total_itbis_percepcion: float | None | str | Unset
        if isinstance(self.total_itbis_percepcion, Unset):
            total_itbis_percepcion = UNSET
        else:
            total_itbis_percepcion = self.total_itbis_percepcion

        total_isr_percepcion: float | None | str | Unset
        if isinstance(self.total_isr_percepcion, Unset):
            total_isr_percepcion = UNSET
        else:
            total_isr_percepcion = self.total_isr_percepcion


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "montoTotal": monto_total,
        })
        if monto_gravado_total is not UNSET:
            field_dict["montoGravadoTotal"] = monto_gravado_total
        if monto_gravado_i1 is not UNSET:
            field_dict["montoGravadoI1"] = monto_gravado_i1
        if monto_gravado_i2 is not UNSET:
            field_dict["montoGravadoI2"] = monto_gravado_i2
        if monto_gravado_i3 is not UNSET:
            field_dict["montoGravadoI3"] = monto_gravado_i3
        if monto_exento is not UNSET:
            field_dict["montoExento"] = monto_exento
        if itbi_s1 is not UNSET:
            field_dict["itbiS1"] = itbi_s1
        if itbi_s2 is not UNSET:
            field_dict["itbiS2"] = itbi_s2
        if itbi_s3 is not UNSET:
            field_dict["itbiS3"] = itbi_s3
        if total_itbis is not UNSET:
            field_dict["totalITBIS"] = total_itbis
        if total_itbis1 is not UNSET:
            field_dict["totalITBIS1"] = total_itbis1
        if total_itbis2 is not UNSET:
            field_dict["totalITBIS2"] = total_itbis2
        if total_itbis3 is not UNSET:
            field_dict["totalITBIS3"] = total_itbis3
        if monto_periodo is not UNSET:
            field_dict["montoPeriodo"] = monto_periodo
        if saldo_anterior is not UNSET:
            field_dict["saldoAnterior"] = saldo_anterior
        if monto_avance_pago is not UNSET:
            field_dict["montoAvancePago"] = monto_avance_pago
        if valor_pagar is not UNSET:
            field_dict["valorPagar"] = valor_pagar
        if total_itbis_retenido is not UNSET:
            field_dict["totalITBISRetenido"] = total_itbis_retenido
        if total_isr_retencion is not UNSET:
            field_dict["totalISRRetencion"] = total_isr_retencion
        if total_itbis_percepcion is not UNSET:
            field_dict["totalITBISPercepcion"] = total_itbis_percepcion
        if total_isr_percepcion is not UNSET:
            field_dict["totalISRPercepcion"] = total_isr_percepcion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_monto_total(data: object) -> float | str:
            return cast(float | str, data)

        monto_total = _parse_monto_total(d.pop("montoTotal"))


        def _parse_monto_gravado_total(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_gravado_total = _parse_monto_gravado_total(d.pop("montoGravadoTotal", UNSET))


        def _parse_monto_gravado_i1(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_gravado_i1 = _parse_monto_gravado_i1(d.pop("montoGravadoI1", UNSET))


        def _parse_monto_gravado_i2(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_gravado_i2 = _parse_monto_gravado_i2(d.pop("montoGravadoI2", UNSET))


        def _parse_monto_gravado_i3(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_gravado_i3 = _parse_monto_gravado_i3(d.pop("montoGravadoI3", UNSET))


        def _parse_monto_exento(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_exento = _parse_monto_exento(d.pop("montoExento", UNSET))


        def _parse_itbi_s1(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        itbi_s1 = _parse_itbi_s1(d.pop("itbiS1", UNSET))


        def _parse_itbi_s2(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        itbi_s2 = _parse_itbi_s2(d.pop("itbiS2", UNSET))


        def _parse_itbi_s3(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        itbi_s3 = _parse_itbi_s3(d.pop("itbiS3", UNSET))


        def _parse_total_itbis(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_itbis = _parse_total_itbis(d.pop("totalITBIS", UNSET))


        def _parse_total_itbis1(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_itbis1 = _parse_total_itbis1(d.pop("totalITBIS1", UNSET))


        def _parse_total_itbis2(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_itbis2 = _parse_total_itbis2(d.pop("totalITBIS2", UNSET))


        def _parse_total_itbis3(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_itbis3 = _parse_total_itbis3(d.pop("totalITBIS3", UNSET))


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


        def _parse_total_itbis_retenido(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_itbis_retenido = _parse_total_itbis_retenido(d.pop("totalITBISRetenido", UNSET))


        def _parse_total_isr_retencion(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_isr_retencion = _parse_total_isr_retencion(d.pop("totalISRRetencion", UNSET))


        def _parse_total_itbis_percepcion(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_itbis_percepcion = _parse_total_itbis_percepcion(d.pop("totalITBISPercepcion", UNSET))


        def _parse_total_isr_percepcion(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_isr_percepcion = _parse_total_isr_percepcion(d.pop("totalISRPercepcion", UNSET))


        ecf_41_totales = cls(
            monto_total=monto_total,
            monto_gravado_total=monto_gravado_total,
            monto_gravado_i1=monto_gravado_i1,
            monto_gravado_i2=monto_gravado_i2,
            monto_gravado_i3=monto_gravado_i3,
            monto_exento=monto_exento,
            itbi_s1=itbi_s1,
            itbi_s2=itbi_s2,
            itbi_s3=itbi_s3,
            total_itbis=total_itbis,
            total_itbis1=total_itbis1,
            total_itbis2=total_itbis2,
            total_itbis3=total_itbis3,
            monto_periodo=monto_periodo,
            saldo_anterior=saldo_anterior,
            monto_avance_pago=monto_avance_pago,
            valor_pagar=valor_pagar,
            total_itbis_retenido=total_itbis_retenido,
            total_isr_retencion=total_isr_retencion,
            total_itbis_percepcion=total_itbis_percepcion,
            total_isr_percepcion=total_isr_percepcion,
        )


        ecf_41_totales.additional_properties = d
        return ecf_41_totales

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
