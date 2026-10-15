from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyEnvironmentUrls")


@_attrs_define
class CompanyEnvironmentUrls:
    """
    Attributes:
        url_recepcion (str | Unset):
        url_aprobacion_comercial (str | Unset):
        url_autenticacion (str | Unset):
    """

    url_recepcion: str | Unset = UNSET
    url_aprobacion_comercial: str | Unset = UNSET
    url_autenticacion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url_recepcion = self.url_recepcion

        url_aprobacion_comercial = self.url_aprobacion_comercial

        url_autenticacion = self.url_autenticacion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url_recepcion is not UNSET:
            field_dict["urlRecepcion"] = url_recepcion
        if url_aprobacion_comercial is not UNSET:
            field_dict["urlAprobacionComercial"] = url_aprobacion_comercial
        if url_autenticacion is not UNSET:
            field_dict["urlAutenticacion"] = url_autenticacion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url_recepcion = d.pop("urlRecepcion", UNSET)

        url_aprobacion_comercial = d.pop("urlAprobacionComercial", UNSET)

        url_autenticacion = d.pop("urlAutenticacion", UNSET)

        company_environment_urls = cls(
            url_recepcion=url_recepcion,
            url_aprobacion_comercial=url_aprobacion_comercial,
            url_autenticacion=url_autenticacion,
        )

        company_environment_urls.additional_properties = d
        return company_environment_urls

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
