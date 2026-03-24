from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_31_tipo_descuento_recargo_type import Ecf31TipoDescuentoRecargoType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf31SubRecargo")



@_attrs_define
class Ecf31SubRecargo:
    """ 
        Example:
            {'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None}

        Attributes:
            tipo_sub_recargo (Ecf31TipoDescuentoRecargoType):
            sub_recargo_porcentaje (float | None | str | Unset):
            monto_sub_recargo (float | None | str | Unset):
     """

    tipo_sub_recargo: Ecf31TipoDescuentoRecargoType
    sub_recargo_porcentaje: float | None | str | Unset = UNSET
    monto_sub_recargo: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipo_sub_recargo = self.tipo_sub_recargo.value

        sub_recargo_porcentaje: float | None | str | Unset
        if isinstance(self.sub_recargo_porcentaje, Unset):
            sub_recargo_porcentaje = UNSET
        else:
            sub_recargo_porcentaje = self.sub_recargo_porcentaje

        monto_sub_recargo: float | None | str | Unset
        if isinstance(self.monto_sub_recargo, Unset):
            monto_sub_recargo = UNSET
        else:
            monto_sub_recargo = self.monto_sub_recargo


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tipoSubRecargo": tipo_sub_recargo,
        })
        if sub_recargo_porcentaje is not UNSET:
            field_dict["subRecargoPorcentaje"] = sub_recargo_porcentaje
        if monto_sub_recargo is not UNSET:
            field_dict["montoSubRecargo"] = monto_sub_recargo

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tipo_sub_recargo = Ecf31TipoDescuentoRecargoType(d.pop("tipoSubRecargo"))




        def _parse_sub_recargo_porcentaje(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sub_recargo_porcentaje = _parse_sub_recargo_porcentaje(d.pop("subRecargoPorcentaje", UNSET))


        def _parse_monto_sub_recargo(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_sub_recargo = _parse_monto_sub_recargo(d.pop("montoSubRecargo", UNSET))


        ecf_31_sub_recargo = cls(
            tipo_sub_recargo=tipo_sub_recargo,
            sub_recargo_porcentaje=sub_recargo_porcentaje,
            monto_sub_recargo=monto_sub_recargo,
        )


        ecf_31_sub_recargo.additional_properties = d
        return ecf_31_sub_recargo

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
