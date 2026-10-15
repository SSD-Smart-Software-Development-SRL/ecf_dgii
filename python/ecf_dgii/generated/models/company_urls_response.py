from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_environment_urls import CompanyEnvironmentUrls


T = TypeVar("T", bound="CompanyUrlsResponse")


@_attrs_define
class CompanyUrlsResponse:
    """
    Attributes:
        test (CompanyEnvironmentUrls | None | Unset):
        cert (CompanyEnvironmentUrls | None | Unset):
        prod (CompanyEnvironmentUrls | None | Unset):
    """

    test: CompanyEnvironmentUrls | None | Unset = UNSET
    cert: CompanyEnvironmentUrls | None | Unset = UNSET
    prod: CompanyEnvironmentUrls | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_environment_urls import CompanyEnvironmentUrls  # noqa: PLC0415

        test: dict[str, Any] | None | Unset
        if isinstance(self.test, Unset):
            test = UNSET
        elif isinstance(self.test, CompanyEnvironmentUrls):
            test = self.test.to_dict()
        else:
            test = self.test

        cert: dict[str, Any] | None | Unset
        if isinstance(self.cert, Unset):
            cert = UNSET
        elif isinstance(self.cert, CompanyEnvironmentUrls):
            cert = self.cert.to_dict()
        else:
            cert = self.cert

        prod: dict[str, Any] | None | Unset
        if isinstance(self.prod, Unset):
            prod = UNSET
        elif isinstance(self.prod, CompanyEnvironmentUrls):
            prod = self.prod.to_dict()
        else:
            prod = self.prod

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if test is not UNSET:
            field_dict["test"] = test
        if cert is not UNSET:
            field_dict["cert"] = cert
        if prod is not UNSET:
            field_dict["prod"] = prod

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_environment_urls import CompanyEnvironmentUrls  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_test(data: object) -> CompanyEnvironmentUrls | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                test_type_1 = CompanyEnvironmentUrls.from_dict(data)

                return test_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyEnvironmentUrls | None | Unset, data)

        test = _parse_test(d.pop("test", UNSET))

        def _parse_cert(data: object) -> CompanyEnvironmentUrls | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cert_type_1 = CompanyEnvironmentUrls.from_dict(data)

                return cert_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyEnvironmentUrls | None | Unset, data)

        cert = _parse_cert(d.pop("cert", UNSET))

        def _parse_prod(data: object) -> CompanyEnvironmentUrls | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prod_type_1 = CompanyEnvironmentUrls.from_dict(data)

                return prod_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyEnvironmentUrls | None | Unset, data)

        prod = _parse_prod(d.pop("prod", UNSET))

        company_urls_response = cls(
            test=test,
            cert=cert,
            prod=prod,
        )

        company_urls_response.additional_properties = d
        return company_urls_response

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
