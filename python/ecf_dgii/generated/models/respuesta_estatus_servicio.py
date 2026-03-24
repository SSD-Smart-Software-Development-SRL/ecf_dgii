from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RespuestaEstatusServicio")



@_attrs_define
class RespuestaEstatusServicio:
    """ Modelo de respuesta que representa el estado de un servicio específico de facturación electrónica en un ambiente
    específico.
    Utilizado por el endpoint /api/estatusservicios/obtenerestatus.

        Example:
            {'servicio': 'servicio', 'ambiente': 'ambiente', 'status': 'status'}

        Attributes:
            servicio (None | str | Unset): Nombre del servicio de facturación electrónica.
                Valores posibles incluyen:
                - "Autenticación"
                - "Recepción"
                - "Consulta Resultado"
                - "Consulta Estado"
                - "Consulta Directorio"
                - "Consulta TrackIds"
                - "Aprobación Comercial"
                - "Anulación Rangos"
                - "Recepción FC"
            status (None | str | Unset): Estado actual del servicio.
                Valores posibles:
                - "Disponible": El servicio está disponible y operativo
                - "No Disponible": El servicio no está disponible (probablemente en mantenimiento)
            ambiente (None | str | Unset): Ambiente donde opera el servicio.
                Valores posibles:
                - "PreCertificacion": Ambiente de pre-certificación
                - "Certificacion": Ambiente de certificación
                - "Produccion": Ambiente de producción
     """

    servicio: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    ambiente: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        servicio: None | str | Unset
        if isinstance(self.servicio, Unset):
            servicio = UNSET
        else:
            servicio = self.servicio

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        ambiente: None | str | Unset
        if isinstance(self.ambiente, Unset):
            ambiente = UNSET
        else:
            ambiente = self.ambiente


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if servicio is not UNSET:
            field_dict["servicio"] = servicio
        if status is not UNSET:
            field_dict["status"] = status
        if ambiente is not UNSET:
            field_dict["ambiente"] = ambiente

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_servicio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        servicio = _parse_servicio(d.pop("servicio", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_ambiente(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ambiente = _parse_ambiente(d.pop("ambiente", UNSET))


        respuesta_estatus_servicio = cls(
            servicio=servicio,
            status=status,
            ambiente=ambiente,
        )


        respuesta_estatus_servicio.additional_properties = d
        return respuesta_estatus_servicio

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
