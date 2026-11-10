from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackingDetalle")


@_attrs_define
class TrackingDetalle:
    """
    Attributes:
        track_id (None | str | Unset):
        estado (None | str | Unset):
        fecha_recepcion (None | str | Unset):
    """

    track_id: None | str | Unset = UNSET
    estado: None | str | Unset = UNSET
    fecha_recepcion: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        track_id: None | str | Unset
        if isinstance(self.track_id, Unset):
            track_id = UNSET
        else:
            track_id = self.track_id

        estado: None | str | Unset
        if isinstance(self.estado, Unset):
            estado = UNSET
        else:
            estado = self.estado

        fecha_recepcion: None | str | Unset
        if isinstance(self.fecha_recepcion, Unset):
            fecha_recepcion = UNSET
        else:
            fecha_recepcion = self.fecha_recepcion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if track_id is not UNSET:
            field_dict["trackId"] = track_id
        if estado is not UNSET:
            field_dict["estado"] = estado
        if fecha_recepcion is not UNSET:
            field_dict["fechaRecepcion"] = fecha_recepcion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_track_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        track_id = _parse_track_id(d.pop("trackId", UNSET))

        def _parse_estado(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estado = _parse_estado(d.pop("estado", UNSET))

        def _parse_fecha_recepcion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fecha_recepcion = _parse_fecha_recepcion(d.pop("fechaRecepcion", UNSET))

        tracking_detalle = cls(
            track_id=track_id,
            estado=estado,
            fecha_recepcion=fecha_recepcion,
        )

        tracking_detalle.additional_properties = d
        return tracking_detalle

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
