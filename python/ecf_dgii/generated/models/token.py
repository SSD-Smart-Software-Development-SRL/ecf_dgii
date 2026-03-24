from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Token")



@_attrs_define
class Token:
    """ 
        Example:
            {'jwt': 'jwt', 'validFrom': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'validTo': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}

        Attributes:
            jwt (str):
            valid_from (datetime.datetime):
            valid_to (datetime.datetime):
     """

    jwt: str
    valid_from: datetime.datetime
    valid_to: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        jwt = self.jwt

        valid_from = self.valid_from.isoformat()

        valid_to = self.valid_to.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "jwt": jwt,
            "validFrom": valid_from,
            "validTo": valid_to,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        jwt = d.pop("jwt")

        valid_from = isoparse(d.pop("validFrom"))




        valid_to = isoparse(d.pop("validTo"))




        token = cls(
            jwt=jwt,
            valid_from=valid_from,
            valid_to=valid_to,
        )


        token.additional_properties = d
        return token

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
