from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcecfSummaryDto")


@_attrs_define
class AcecfSummaryDto:
    """
    Attributes:
        acecf_id (UUID | Unset):
        estado (int | str | Unset):
        detalle_motivo_rechazo (None | str | Unset):
        fecha_hora_aprobacion_comercial (datetime.datetime | Unset):
        file_name (None | str | Unset):
        created_on (datetime.datetime | Unset):
        progress (int | str | Unset): Lifecycle progress (Pending / Building / DirectorioResolved / SendingToEmisor /
            SentToEmisor / Completed / Failed).
        error_message (None | str | Unset): Last failure reason when Progress = Failed.
        receptor_http_status (int | None | str | Unset): HTTP status code from the receptor (set after SendingToEmisor).
        dgii_codigo_response (None | str | Unset):
        dgii_estado_response (None | str | Unset):
        dgii_mensajes_response (None | str | Unset):
    """

    acecf_id: UUID | Unset = UNSET
    estado: int | str | Unset = UNSET
    detalle_motivo_rechazo: None | str | Unset = UNSET
    fecha_hora_aprobacion_comercial: datetime.datetime | Unset = UNSET
    file_name: None | str | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    progress: int | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    receptor_http_status: int | None | str | Unset = UNSET
    dgii_codigo_response: None | str | Unset = UNSET
    dgii_estado_response: None | str | Unset = UNSET
    dgii_mensajes_response: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acecf_id: str | Unset = UNSET
        if not isinstance(self.acecf_id, Unset):
            acecf_id = str(self.acecf_id)

        estado: int | str | Unset
        if isinstance(self.estado, Unset):
            estado = UNSET
        else:
            estado = self.estado

        detalle_motivo_rechazo: None | str | Unset
        if isinstance(self.detalle_motivo_rechazo, Unset):
            detalle_motivo_rechazo = UNSET
        else:
            detalle_motivo_rechazo = self.detalle_motivo_rechazo

        fecha_hora_aprobacion_comercial: str | Unset = UNSET
        if not isinstance(self.fecha_hora_aprobacion_comercial, Unset):
            fecha_hora_aprobacion_comercial = self.fecha_hora_aprobacion_comercial.isoformat()

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        progress: int | str | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        receptor_http_status: int | None | str | Unset
        if isinstance(self.receptor_http_status, Unset):
            receptor_http_status = UNSET
        else:
            receptor_http_status = self.receptor_http_status

        dgii_codigo_response: None | str | Unset
        if isinstance(self.dgii_codigo_response, Unset):
            dgii_codigo_response = UNSET
        else:
            dgii_codigo_response = self.dgii_codigo_response

        dgii_estado_response: None | str | Unset
        if isinstance(self.dgii_estado_response, Unset):
            dgii_estado_response = UNSET
        else:
            dgii_estado_response = self.dgii_estado_response

        dgii_mensajes_response: None | str | Unset
        if isinstance(self.dgii_mensajes_response, Unset):
            dgii_mensajes_response = UNSET
        else:
            dgii_mensajes_response = self.dgii_mensajes_response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acecf_id is not UNSET:
            field_dict["acecfId"] = acecf_id
        if estado is not UNSET:
            field_dict["estado"] = estado
        if detalle_motivo_rechazo is not UNSET:
            field_dict["detalleMotivoRechazo"] = detalle_motivo_rechazo
        if fecha_hora_aprobacion_comercial is not UNSET:
            field_dict["fechaHoraAprobacionComercial"] = fecha_hora_aprobacion_comercial
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if progress is not UNSET:
            field_dict["progress"] = progress
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if receptor_http_status is not UNSET:
            field_dict["receptorHttpStatus"] = receptor_http_status
        if dgii_codigo_response is not UNSET:
            field_dict["dgiiCodigoResponse"] = dgii_codigo_response
        if dgii_estado_response is not UNSET:
            field_dict["dgiiEstadoResponse"] = dgii_estado_response
        if dgii_mensajes_response is not UNSET:
            field_dict["dgiiMensajesResponse"] = dgii_mensajes_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _acecf_id = d.pop("acecfId", UNSET)
        acecf_id: UUID | Unset
        if isinstance(_acecf_id, Unset):
            acecf_id = UNSET
        else:
            acecf_id = UUID(_acecf_id)

        def _parse_estado(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        estado = _parse_estado(d.pop("estado", UNSET))

        def _parse_detalle_motivo_rechazo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detalle_motivo_rechazo = _parse_detalle_motivo_rechazo(d.pop("detalleMotivoRechazo", UNSET))

        _fecha_hora_aprobacion_comercial = d.pop("fechaHoraAprobacionComercial", UNSET)
        fecha_hora_aprobacion_comercial: datetime.datetime | Unset
        if isinstance(_fecha_hora_aprobacion_comercial, Unset):
            fecha_hora_aprobacion_comercial = UNSET
        else:
            fecha_hora_aprobacion_comercial = datetime.datetime.fromisoformat(_fecha_hora_aprobacion_comercial)

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        _created_on = d.pop("createdOn", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = datetime.datetime.fromisoformat(_created_on)

        def _parse_progress(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        progress = _parse_progress(d.pop("progress", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))

        def _parse_receptor_http_status(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        receptor_http_status = _parse_receptor_http_status(d.pop("receptorHttpStatus", UNSET))

        def _parse_dgii_codigo_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dgii_codigo_response = _parse_dgii_codigo_response(d.pop("dgiiCodigoResponse", UNSET))

        def _parse_dgii_estado_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dgii_estado_response = _parse_dgii_estado_response(d.pop("dgiiEstadoResponse", UNSET))

        def _parse_dgii_mensajes_response(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dgii_mensajes_response = _parse_dgii_mensajes_response(d.pop("dgiiMensajesResponse", UNSET))

        acecf_summary_dto = cls(
            acecf_id=acecf_id,
            estado=estado,
            detalle_motivo_rechazo=detalle_motivo_rechazo,
            fecha_hora_aprobacion_comercial=fecha_hora_aprobacion_comercial,
            file_name=file_name,
            created_on=created_on,
            progress=progress,
            error_message=error_message,
            receptor_http_status=receptor_http_status,
            dgii_codigo_response=dgii_codigo_response,
            dgii_estado_response=dgii_estado_response,
            dgii_mensajes_response=dgii_mensajes_response,
        )

        acecf_summary_dto.additional_properties = d
        return acecf_summary_dto

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
