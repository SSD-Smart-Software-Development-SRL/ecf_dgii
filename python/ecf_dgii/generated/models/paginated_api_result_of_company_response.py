from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.company_response import CompanyResponse





T = TypeVar("T", bound="PaginatedApiResultOfCompanyResponse")



@_attrs_define
class PaginatedApiResultOfCompanyResponse:
    """ 
        Example:
            {'total': 0, 'previousPage': None, 'nextPageUri': 'https://openapi-generator.tech', 'nextPage': 6, 'values':
                [{'legalName': 'legalName', 'updatedBy': 'updatedBy', 'receptorId': 'receptorId', 'createdBy': 'createdBy',
                'rnc': 'rnc', 'name': 'name', 'tenantId': '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'updatedOn':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'createdOn': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00'))}, {'legalName': 'legalName', 'updatedBy': 'updatedBy', 'receptorId': 'receptorId', 'createdBy':
                'createdBy', 'rnc': 'rnc', 'name': 'name', 'tenantId': '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'updatedOn':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'createdOn': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00'))}], 'limit': None, 'page': None}

        Attributes:
            next_page_uri (None | str):
            values (list[CompanyResponse] | Unset):
            total (int | str | Unset):
            page (int | str | Unset):
            limit (int | str | Unset):
            next_page (int | None | str | Unset):
            previous_page (int | None | str | Unset):
     """

    next_page_uri: None | str
    values: list[CompanyResponse] | Unset = UNSET
    total: int | str | Unset = UNSET
    page: int | str | Unset = UNSET
    limit: int | str | Unset = UNSET
    next_page: int | None | str | Unset = UNSET
    previous_page: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_response import CompanyResponse
        next_page_uri: None | str
        next_page_uri = self.next_page_uri

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)



        total: int | str | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        page: int | str | Unset
        if isinstance(self.page, Unset):
            page = UNSET
        else:
            page = self.page

        limit: int | str | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        next_page: int | None | str | Unset
        if isinstance(self.next_page, Unset):
            next_page = UNSET
        else:
            next_page = self.next_page

        previous_page: int | None | str | Unset
        if isinstance(self.previous_page, Unset):
            previous_page = UNSET
        else:
            previous_page = self.previous_page


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "nextPageUri": next_page_uri,
        })
        if values is not UNSET:
            field_dict["values"] = values
        if total is not UNSET:
            field_dict["total"] = total
        if page is not UNSET:
            field_dict["page"] = page
        if limit is not UNSET:
            field_dict["limit"] = limit
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page
        if previous_page is not UNSET:
            field_dict["previousPage"] = previous_page

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_response import CompanyResponse
        d = dict(src_dict)
        def _parse_next_page_uri(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page_uri = _parse_next_page_uri(d.pop("nextPageUri"))


        _values = d.pop("values", UNSET)
        values: list[CompanyResponse] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = CompanyResponse.from_dict(values_item_data)



                values.append(values_item)


        def _parse_total(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        total = _parse_total(d.pop("total", UNSET))


        def _parse_page(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        page = _parse_page(d.pop("page", UNSET))


        def _parse_limit(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))


        def _parse_next_page(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        next_page = _parse_next_page(d.pop("nextPage", UNSET))


        def _parse_previous_page(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        previous_page = _parse_previous_page(d.pop("previousPage", UNSET))


        paginated_api_result_of_company_response = cls(
            next_page_uri=next_page_uri,
            values=values,
            total=total,
            page=page,
            limit=limit,
            next_page=next_page,
            previous_page=previous_page,
        )


        paginated_api_result_of_company_response.additional_properties = d
        return paginated_api_result_of_company_response

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
