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






T = TypeVar("T", bound="CompanyResponse")



@_attrs_define
class CompanyResponse:
    """ 
        Example:
            {'legalName': 'legalName', 'updatedBy': 'updatedBy', 'receptorId': 'receptorId', 'createdBy': 'createdBy',
                'rnc': 'rnc', 'name': 'name', 'tenantId': '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'updatedOn':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'createdOn': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00'))}

        Attributes:
            rnc (str | Unset):
            legal_name (str | Unset):
            name (str | Unset):
            created_on (datetime.datetime | Unset):
            updated_on (datetime.datetime | Unset):
            created_by (str | Unset):
            updated_by (str | Unset):
            tenant_id (UUID | Unset):
            receptor_id (str | Unset):
     """

    rnc: str | Unset = UNSET
    legal_name: str | Unset = UNSET
    name: str | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    receptor_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rnc = self.rnc

        legal_name = self.legal_name

        name = self.name

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        created_by = self.created_by

        updated_by = self.updated_by

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)

        receptor_id = self.receptor_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rnc is not UNSET:
            field_dict["rnc"] = rnc
        if legal_name is not UNSET:
            field_dict["legalName"] = legal_name
        if name is not UNSET:
            field_dict["name"] = name
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if updated_on is not UNSET:
            field_dict["updatedOn"] = updated_on
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if receptor_id is not UNSET:
            field_dict["receptorId"] = receptor_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rnc = d.pop("rnc", UNSET)

        legal_name = d.pop("legalName", UNSET)

        name = d.pop("name", UNSET)

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




        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        _tenant_id = d.pop("tenantId", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id,  Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)




        receptor_id = d.pop("receptorId", UNSET)

        company_response = cls(
            rnc=rnc,
            legal_name=legal_name,
            name=name,
            created_on=created_on,
            updated_on=updated_on,
            created_by=created_by,
            updated_by=updated_by,
            tenant_id=tenant_id,
            receptor_id=receptor_id,
        )


        company_response.additional_properties = d
        return company_response

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
