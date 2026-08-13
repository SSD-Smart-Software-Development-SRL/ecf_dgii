from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyResponse")


@_attrs_define
class CompanyResponse:
    """
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
        url_recepcion (None | str | Unset):
        url_aprobacion_comercial (None | str | Unset):
        url_autenticacion (None | str | Unset):
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
    url_recepcion: None | str | Unset = UNSET
    url_aprobacion_comercial: None | str | Unset = UNSET
    url_autenticacion: None | str | Unset = UNSET
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

        url_recepcion: None | str | Unset
        if isinstance(self.url_recepcion, Unset):
            url_recepcion = UNSET
        else:
            url_recepcion = self.url_recepcion

        url_aprobacion_comercial: None | str | Unset
        if isinstance(self.url_aprobacion_comercial, Unset):
            url_aprobacion_comercial = UNSET
        else:
            url_aprobacion_comercial = self.url_aprobacion_comercial

        url_autenticacion: None | str | Unset
        if isinstance(self.url_autenticacion, Unset):
            url_autenticacion = UNSET
        else:
            url_autenticacion = self.url_autenticacion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        rnc = d.pop("rnc", UNSET)

        legal_name = d.pop("legalName", UNSET)

        name = d.pop("name", UNSET)

        _created_on = d.pop("createdOn", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = datetime.datetime.fromisoformat(_created_on)

        _updated_on = d.pop("updatedOn", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on, Unset):
            updated_on = UNSET
        else:
            updated_on = datetime.datetime.fromisoformat(_updated_on)

        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        _tenant_id = d.pop("tenantId", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)

        receptor_id = d.pop("receptorId", UNSET)

        def _parse_url_recepcion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_recepcion = _parse_url_recepcion(d.pop("urlRecepcion", UNSET))

        def _parse_url_aprobacion_comercial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_aprobacion_comercial = _parse_url_aprobacion_comercial(d.pop("urlAprobacionComercial", UNSET))

        def _parse_url_autenticacion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_autenticacion = _parse_url_autenticacion(d.pop("urlAutenticacion", UNSET))

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
            url_recepcion=url_recepcion,
            url_aprobacion_comercial=url_aprobacion_comercial,
            url_autenticacion=url_autenticacion,
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
