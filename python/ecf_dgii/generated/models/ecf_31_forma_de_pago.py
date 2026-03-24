from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_31_forma_pago_type import Ecf31FormaPagoType
from typing import cast






T = TypeVar("T", bound="Ecf31FormaDePago")



@_attrs_define
class Ecf31FormaDePago:
    """ 
        Example:
            {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}

        Attributes:
            forma_pago (Ecf31FormaPagoType):
            monto_pago (float | str):
     """

    forma_pago: Ecf31FormaPagoType
    monto_pago: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        forma_pago = self.forma_pago.value

        monto_pago: float | str
        monto_pago = self.monto_pago


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "formaPago": forma_pago,
            "montoPago": monto_pago,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forma_pago = Ecf31FormaPagoType(d.pop("formaPago"))




        def _parse_monto_pago(data: object) -> float | str:
            return cast(float | str, data)

        monto_pago = _parse_monto_pago(d.pop("montoPago"))


        ecf_31_forma_de_pago = cls(
            forma_pago=forma_pago,
            monto_pago=monto_pago,
        )


        ecf_31_forma_de_pago.additional_properties = d
        return ecf_31_forma_de_pago

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
