from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="CertificateResponse")



@_attrs_define
class CertificateResponse:
    """ 
        Example:
            {'serialNumber': 'serialNumber', 'createdBy': 'createdBy', 'subject': 'subject', 'notAfterUtc':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'rnc':
                'rnc', 'thumbprint': 'thumbprint', 'createdOn': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'issuer': 'issuer', 'notBeforeUtc':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}

        Attributes:
            thumbprint (str):
            subject (str):
            issuer (str):
            not_before_utc (datetime.datetime):
            not_after_utc (datetime.datetime):
            serial_number (str):
            rnc (None | str):
            created_on (datetime.datetime):
            created_by (str):
     """

    thumbprint: str
    subject: str
    issuer: str
    not_before_utc: datetime.datetime
    not_after_utc: datetime.datetime
    serial_number: str
    rnc: None | str
    created_on: datetime.datetime
    created_by: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        thumbprint = self.thumbprint

        subject = self.subject

        issuer = self.issuer

        not_before_utc = self.not_before_utc.isoformat()

        not_after_utc = self.not_after_utc.isoformat()

        serial_number = self.serial_number

        rnc: None | str
        rnc = self.rnc

        created_on = self.created_on.isoformat()

        created_by = self.created_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "thumbprint": thumbprint,
            "subject": subject,
            "issuer": issuer,
            "notBeforeUtc": not_before_utc,
            "notAfterUtc": not_after_utc,
            "serialNumber": serial_number,
            "rnc": rnc,
            "createdOn": created_on,
            "createdBy": created_by,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thumbprint = d.pop("thumbprint")

        subject = d.pop("subject")

        issuer = d.pop("issuer")

        not_before_utc = isoparse(d.pop("notBeforeUtc"))




        not_after_utc = isoparse(d.pop("notAfterUtc"))




        serial_number = d.pop("serialNumber")

        def _parse_rnc(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rnc = _parse_rnc(d.pop("rnc"))


        created_on = isoparse(d.pop("createdOn"))




        created_by = d.pop("createdBy")

        certificate_response = cls(
            thumbprint=thumbprint,
            subject=subject,
            issuer=issuer,
            not_before_utc=not_before_utc,
            not_after_utc=not_after_utc,
            serial_number=serial_number,
            rnc=rnc,
            created_on=created_on,
            created_by=created_by,
        )


        certificate_response.additional_properties = d
        return certificate_response

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
