from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_41_tipo_descuento_recargo_type import Ecf41TipoDescuentoRecargoType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf41SubDescuento")



@_attrs_define
class Ecf41SubDescuento:
    """ 
        Example:
            {'tipoSubDescuento': '$', 'subDescuentoPorcentaje': 9.301444243932576, 'montoSubDescuento': None}

        Attributes:
            tipo_sub_descuento (Ecf41TipoDescuentoRecargoType):
            sub_descuento_porcentaje (float | None | str | Unset):
            monto_sub_descuento (float | None | str | Unset):
     """

    tipo_sub_descuento: Ecf41TipoDescuentoRecargoType
    sub_descuento_porcentaje: float | None | str | Unset = UNSET
    monto_sub_descuento: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_sub_descuento = self.tipo_sub_descuento.value

        sub_descuento_porcentaje: float | None | str | Unset
        if isinstance(self.sub_descuento_porcentaje, Unset):
            sub_descuento_porcentaje = UNSET
        else:
            sub_descuento_porcentaje = self.sub_descuento_porcentaje

        monto_sub_descuento: float | None | str | Unset
        if isinstance(self.monto_sub_descuento, Unset):
            monto_sub_descuento = UNSET
        else:
            monto_sub_descuento = self.monto_sub_descuento


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tipoSubDescuento": tipo_sub_descuento,
        })
        if sub_descuento_porcentaje is not UNSET:
            field_dict["subDescuentoPorcentaje"] = sub_descuento_porcentaje
        if monto_sub_descuento is not UNSET:
            field_dict["montoSubDescuento"] = monto_sub_descuento

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tipo_sub_descuento = Ecf41TipoDescuentoRecargoType(d.pop("tipoSubDescuento"))




        def _parse_sub_descuento_porcentaje(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_descuento_porcentaje = _parse_sub_descuento_porcentaje(d.pop("subDescuentoPorcentaje", UNSET))


        def _parse_monto_sub_descuento(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_sub_descuento = _parse_monto_sub_descuento(d.pop("montoSubDescuento", UNSET))


        ecf_41_sub_descuento = cls(
            tipo_sub_descuento=tipo_sub_descuento,
            sub_descuento_porcentaje=sub_descuento_porcentaje,
            monto_sub_descuento=monto_sub_descuento,
        )


        ecf_41_sub_descuento.additional_properties = d
        return ecf_41_sub_descuento

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
