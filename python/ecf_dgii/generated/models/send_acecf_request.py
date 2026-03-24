from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.estado_type import EstadoType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SendAcecfRequest")



@_attrs_define
class SendAcecfRequest:
    """ 
        Example:
            {'estadoType': 'ECFAceptado', 'detalleMotivoRechazo': 'detalleMotivoRechazo'}

        Attributes:
            detalle_motivo_rechazo (None | str | Unset):
            estado_type (EstadoType | Unset):
     """

    detalle_motivo_rechazo: None | str | Unset = UNSET
    estado_type: EstadoType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        detalle_motivo_rechazo: None | str | Unset
        if isinstance(self.detalle_motivo_rechazo, Unset):
            detalle_motivo_rechazo = UNSET
        else:
            detalle_motivo_rechazo = self.detalle_motivo_rechazo

        estado_type: str | Unset = UNSET
        if not isinstance(self.estado_type, Unset):
            estado_type = self.estado_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detalle_motivo_rechazo is not UNSET:
            field_dict["detalleMotivoRechazo"] = detalle_motivo_rechazo
        if estado_type is not UNSET:
            field_dict["estadoType"] = estado_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_detalle_motivo_rechazo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detalle_motivo_rechazo = _parse_detalle_motivo_rechazo(d.pop("detalleMotivoRechazo", UNSET))


        _estado_type = d.pop("estadoType", UNSET)
        estado_type: EstadoType | Unset
        if isinstance(_estado_type,  Unset):
            estado_type = UNSET
        else:
            estado_type = EstadoType(_estado_type)




        send_acecf_request = cls(
            detalle_motivo_rechazo=detalle_motivo_rechazo,
            estado_type=estado_type,
        )


        send_acecf_request.additional_properties = d
        return send_acecf_request

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
