from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_44_impuesto_adicional_2 import Ecf44ImpuestoAdicional2





T = TypeVar("T", bound="Ecf44Totales")



@_attrs_define
class Ecf44Totales:
    """ 
        Example:
            {'montoNoFacturable': 7.061401241503109, 'montoPeriodo': None, 'impuestosAdicionales': [{'tipoImpuesto': '001',
                'tasaImpuestoAdicional': 5.637376656633329, 'otrosImpuestosAdicionales': 2.3021358869347655}, {'tipoImpuesto':
                '001', 'tasaImpuestoAdicional': 5.637376656633329, 'otrosImpuestosAdicionales': 2.3021358869347655}],
                'saldoAnterior': None, 'montoAvancePago': None, 'montoExento': 1.4658129805029452, 'valorPagar': None,
                'montoImpuestoAdicional': 5.962133916683182, 'montoTotal': None}

        Attributes:
            monto_total (float | str):
            monto_exento (float | None | str | Unset):
            monto_impuesto_adicional (float | None | str | Unset):
            impuestos_adicionales (list[Ecf44ImpuestoAdicional2] | None | Unset):
            monto_no_facturable (float | None | str | Unset):
            monto_periodo (float | None | str | Unset):
            saldo_anterior (float | None | str | Unset):
            monto_avance_pago (float | None | str | Unset):
            valor_pagar (float | None | str | Unset):
     """

    monto_total: float | str
    monto_exento: float | None | str | Unset = UNSET
    monto_impuesto_adicional: float | None | str | Unset = UNSET
    impuestos_adicionales: list[Ecf44ImpuestoAdicional2] | None | Unset = UNSET
    monto_no_facturable: float | None | str | Unset = UNSET
    monto_periodo: float | None | str | Unset = UNSET
    saldo_anterior: float | None | str | Unset = UNSET
    monto_avance_pago: float | None | str | Unset = UNSET
    valor_pagar: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_44_impuesto_adicional_2 import Ecf44ImpuestoAdicional2
        monto_total: float | str
        monto_total = self.monto_total

        monto_exento: float | None | str | Unset
        if isinstance(self.monto_exento, Unset):
            monto_exento = UNSET
        else:
            monto_exento = self.monto_exento

        monto_impuesto_adicional: float | None | str | Unset
        if isinstance(self.monto_impuesto_adicional, Unset):
            monto_impuesto_adicional = UNSET
        else:
            monto_impuesto_adicional = self.monto_impuesto_adicional

        impuestos_adicionales: list[dict[str, Any]] | None | Unset
        if isinstance(self.impuestos_adicionales, Unset):
            impuestos_adicionales = UNSET
        elif isinstance(self.impuestos_adicionales, list):
            impuestos_adicionales = []
            for impuestos_adicionales_type_0_item_data in self.impuestos_adicionales:
                impuestos_adicionales_type_0_item = impuestos_adicionales_type_0_item_data.to_dict()
                impuestos_adicionales.append(impuestos_adicionales_type_0_item)


        else:
            impuestos_adicionales = self.impuestos_adicionales

        monto_no_facturable: float | None | str | Unset
        if isinstance(self.monto_no_facturable, Unset):
            monto_no_facturable = UNSET
        else:
            monto_no_facturable = self.monto_no_facturable

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "montoTotal": monto_total,
        })
        if monto_exento is not UNSET:
            field_dict["montoExento"] = monto_exento
        if monto_impuesto_adicional is not UNSET:
            field_dict["montoImpuestoAdicional"] = monto_impuesto_adicional
        if impuestos_adicionales is not UNSET:
            field_dict["impuestosAdicionales"] = impuestos_adicionales
        if monto_no_facturable is not UNSET:
            field_dict["montoNoFacturable"] = monto_no_facturable
        if monto_periodo is not UNSET:
            field_dict["montoPeriodo"] = monto_periodo
        if saldo_anterior is not UNSET:
            field_dict["saldoAnterior"] = saldo_anterior
        if monto_avance_pago is not UNSET:
            field_dict["montoAvancePago"] = monto_avance_pago
        if valor_pagar is not UNSET:
            field_dict["valorPagar"] = valor_pagar

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_44_impuesto_adicional_2 import Ecf44ImpuestoAdicional2
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


        def _parse_monto_impuesto_adicional(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_impuesto_adicional = _parse_monto_impuesto_adicional(d.pop("montoImpuestoAdicional", UNSET))


        def _parse_impuestos_adicionales(data: object) -> list[Ecf44ImpuestoAdicional2] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                impuestos_adicionales_type_0 = []
                _impuestos_adicionales_type_0 = data
                for impuestos_adicionales_type_0_item_data in (_impuestos_adicionales_type_0):
                    impuestos_adicionales_type_0_item = Ecf44ImpuestoAdicional2.from_dict(impuestos_adicionales_type_0_item_data)



                    impuestos_adicionales_type_0.append(impuestos_adicionales_type_0_item)

                return impuestos_adicionales_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf44ImpuestoAdicional2] | None | Unset, data)

        impuestos_adicionales = _parse_impuestos_adicionales(d.pop("impuestosAdicionales", UNSET))


        def _parse_monto_no_facturable(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_no_facturable = _parse_monto_no_facturable(d.pop("montoNoFacturable", UNSET))


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


        ecf_44_totales = cls(
            monto_total=monto_total,
            monto_exento=monto_exento,
            monto_impuesto_adicional=monto_impuesto_adicional,
            impuestos_adicionales=impuestos_adicionales,
            monto_no_facturable=monto_no_facturable,
            monto_periodo=monto_periodo,
            saldo_anterior=saldo_anterior,
            monto_avance_pago=monto_avance_pago,
            valor_pagar=valor_pagar,
        )


        ecf_44_totales.additional_properties = d
        return ecf_44_totales

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
