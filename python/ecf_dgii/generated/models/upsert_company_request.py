from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpsertCompanyRequest")


@_attrs_define
class UpsertCompanyRequest:
    """
    Attributes:
        rnc (str):
        name (str):
        employee_count (None | str | Unset):
        estimated_invoices (None | str | Unset):
        legal_rep_first_name (None | str | Unset):
        legal_rep_last_name (None | str | Unset):
        address (None | str | Unset):
        certification_declared (bool | None | Unset):
        certification_status (None | str | Unset):
    """

    rnc: str
    name: str
    employee_count: None | str | Unset = UNSET
    estimated_invoices: None | str | Unset = UNSET
    legal_rep_first_name: None | str | Unset = UNSET
    legal_rep_last_name: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    certification_declared: bool | None | Unset = UNSET
    certification_status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rnc = self.rnc

        name = self.name

        employee_count: None | str | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        estimated_invoices: None | str | Unset
        if isinstance(self.estimated_invoices, Unset):
            estimated_invoices = UNSET
        else:
            estimated_invoices = self.estimated_invoices

        legal_rep_first_name: None | str | Unset
        if isinstance(self.legal_rep_first_name, Unset):
            legal_rep_first_name = UNSET
        else:
            legal_rep_first_name = self.legal_rep_first_name

        legal_rep_last_name: None | str | Unset
        if isinstance(self.legal_rep_last_name, Unset):
            legal_rep_last_name = UNSET
        else:
            legal_rep_last_name = self.legal_rep_last_name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        certification_declared: bool | None | Unset
        if isinstance(self.certification_declared, Unset):
            certification_declared = UNSET
        else:
            certification_declared = self.certification_declared

        certification_status: None | str | Unset
        if isinstance(self.certification_status, Unset):
            certification_status = UNSET
        else:
            certification_status = self.certification_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rnc": rnc,
                "name": name,
            }
        )
        if employee_count is not UNSET:
            field_dict["employeeCount"] = employee_count
        if estimated_invoices is not UNSET:
            field_dict["estimatedInvoices"] = estimated_invoices
        if legal_rep_first_name is not UNSET:
            field_dict["legalRepFirstName"] = legal_rep_first_name
        if legal_rep_last_name is not UNSET:
            field_dict["legalRepLastName"] = legal_rep_last_name
        if address is not UNSET:
            field_dict["address"] = address
        if certification_declared is not UNSET:
            field_dict["certificationDeclared"] = certification_declared
        if certification_status is not UNSET:
            field_dict["certificationStatus"] = certification_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rnc = d.pop("rnc")

        name = d.pop("name")

        def _parse_employee_count(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_count = _parse_employee_count(d.pop("employeeCount", UNSET))

        def _parse_estimated_invoices(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_invoices = _parse_estimated_invoices(d.pop("estimatedInvoices", UNSET))

        def _parse_legal_rep_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_rep_first_name = _parse_legal_rep_first_name(d.pop("legalRepFirstName", UNSET))

        def _parse_legal_rep_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_rep_last_name = _parse_legal_rep_last_name(d.pop("legalRepLastName", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_certification_declared(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        certification_declared = _parse_certification_declared(d.pop("certificationDeclared", UNSET))

        def _parse_certification_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certification_status = _parse_certification_status(d.pop("certificationStatus", UNSET))

        upsert_company_request = cls(
            rnc=rnc,
            name=name,
            employee_count=employee_count,
            estimated_invoices=estimated_invoices,
            legal_rep_first_name=legal_rep_first_name,
            legal_rep_last_name=legal_rep_last_name,
            address=address,
            certification_declared=certification_declared,
            certification_status=certification_status,
        )

        upsert_company_request.additional_properties = d
        return upsert_company_request

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
