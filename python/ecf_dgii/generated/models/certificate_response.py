from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateResponse")


@_attrs_define
class CertificateResponse:
    """
    Attributes:
        thumbprint (str):
        subject (str):
        issuer (str):
        not_before_utc (datetime.datetime):
        not_after_utc (datetime.datetime):
        serial_number (str):
        created_on (datetime.datetime):
        created_by (str):
        rnc (None | str | Unset):
    """

    thumbprint: str
    subject: str
    issuer: str
    not_before_utc: datetime.datetime
    not_after_utc: datetime.datetime
    serial_number: str
    created_on: datetime.datetime
    created_by: str
    rnc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thumbprint = self.thumbprint

        subject = self.subject

        issuer = self.issuer

        not_before_utc = self.not_before_utc.isoformat()

        not_after_utc = self.not_after_utc.isoformat()

        serial_number = self.serial_number

        created_on = self.created_on.isoformat()

        created_by = self.created_by

        rnc: None | str | Unset
        if isinstance(self.rnc, Unset):
            rnc = UNSET
        else:
            rnc = self.rnc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thumbprint": thumbprint,
                "subject": subject,
                "issuer": issuer,
                "notBeforeUtc": not_before_utc,
                "notAfterUtc": not_after_utc,
                "serialNumber": serial_number,
                "createdOn": created_on,
                "createdBy": created_by,
            }
        )
        if rnc is not UNSET:
            field_dict["rnc"] = rnc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thumbprint = d.pop("thumbprint")

        subject = d.pop("subject")

        issuer = d.pop("issuer")

        not_before_utc = datetime.datetime.fromisoformat(d.pop("notBeforeUtc"))

        not_after_utc = datetime.datetime.fromisoformat(d.pop("notAfterUtc"))

        serial_number = d.pop("serialNumber")

        created_on = datetime.datetime.fromisoformat(d.pop("createdOn"))

        created_by = d.pop("createdBy")

        def _parse_rnc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc = _parse_rnc(d.pop("rnc", UNSET))

        certificate_response = cls(
            thumbprint=thumbprint,
            subject=subject,
            issuer=issuer,
            not_before_utc=not_before_utc,
            not_after_utc=not_after_utc,
            serial_number=serial_number,
            created_on=created_on,
            created_by=created_by,
            rnc=rnc,
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
