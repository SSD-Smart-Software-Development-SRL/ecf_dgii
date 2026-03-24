from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="AcecfReceptionRequestDto")



@_attrs_define
class AcecfReceptionRequestDto:
    """ 
        Example:
            {'fileName': 'fileName', 'companyRnc': 'companyRnc', 'encf': 'encf', 'tenantId':
                '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'errorMessage': 'errorMessage', 'messageId':
                '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'progress': 0, 'updatedOn': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'createdOn': datetime.datetime(2000, 1, 23, 4, 56,
                7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'rncEmisor': 'rncEmisor'}

        Attributes:
            message_id (UUID | Unset):
            tenant_id (UUID | Unset):
            company_rnc (str | Unset):
            file_name (str | Unset):
            progress (int | str | Unset):
            created_on (datetime.datetime | Unset):
            updated_on (datetime.datetime | Unset):
            error_message (None | str | Unset):
            encf (None | str | Unset):
            rnc_emisor (None | str | Unset):
     """

    message_id: UUID | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    company_rnc: str | Unset = UNSET
    file_name: str | Unset = UNSET
    progress: int | str | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    error_message: None | str | Unset = UNSET
    encf: None | str | Unset = UNSET
    rnc_emisor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message_id: str | Unset = UNSET
        if not isinstance(self.message_id, Unset):
            message_id = str(self.message_id)

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)

        company_rnc = self.company_rnc

        file_name = self.file_name

        progress: int | str | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        encf: None | str | Unset
        if isinstance(self.encf, Unset):
            encf = UNSET
        else:
            encf = self.encf

        rnc_emisor: None | str | Unset
        if isinstance(self.rnc_emisor, Unset):
            rnc_emisor = UNSET
        else:
            rnc_emisor = self.rnc_emisor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if company_rnc is not UNSET:
            field_dict["companyRnc"] = company_rnc
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if progress is not UNSET:
            field_dict["progress"] = progress
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if updated_on is not UNSET:
            field_dict["updatedOn"] = updated_on
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if encf is not UNSET:
            field_dict["encf"] = encf
        if rnc_emisor is not UNSET:
            field_dict["rncEmisor"] = rnc_emisor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _message_id = d.pop("messageId", UNSET)
        message_id: UUID | Unset
        if isinstance(_message_id,  Unset):
            message_id = UNSET
        else:
            message_id = UUID(_message_id)




        _tenant_id = d.pop("tenantId", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id,  Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)




        company_rnc = d.pop("companyRnc", UNSET)

        file_name = d.pop("fileName", UNSET)

        def _parse_progress(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        progress = _parse_progress(d.pop("progress", UNSET))


        _created_on = d.pop("createdOn", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on,  Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)




        _updated_on = d.pop("updatedOn", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on,  Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)




        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))


        def _parse_encf(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encf = _parse_encf(d.pop("encf", UNSET))


        def _parse_rnc_emisor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_emisor = _parse_rnc_emisor(d.pop("rncEmisor", UNSET))


        acecf_reception_request_dto = cls(
            message_id=message_id,
            tenant_id=tenant_id,
            company_rnc=company_rnc,
            file_name=file_name,
            progress=progress,
            created_on=created_on,
            updated_on=updated_on,
            error_message=error_message,
            encf=encf,
            rnc_emisor=rnc_emisor,
        )


        acecf_reception_request_dto.additional_properties = d
        return acecf_reception_request_dto

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
