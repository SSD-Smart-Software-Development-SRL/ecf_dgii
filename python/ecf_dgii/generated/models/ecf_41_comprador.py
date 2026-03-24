from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provincia_municipio_type_type_1 import ProvinciaMunicipioTypeType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf41Comprador")



@_attrs_define
class Ecf41Comprador:
    """ 
        Example:
            {'direccionComprador': 'direccionComprador', 'correoComprador': 'correoComprador', 'responsablePago':
                'responsablePago', 'informacionAdicionalComprador': 'informacionAdicionalComprador', 'contactoComprador':
                'contactoComprador', 'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador',
                'municipioComprador': '', 'rncComprador': 'rncComprador', 'codigoInternoComprador': 'codigoInternoComprador'}

        Attributes:
            rnc_comprador (str):
            razon_social_comprador (str):
            contacto_comprador (None | str | Unset):
            correo_comprador (None | str | Unset):
            direccion_comprador (None | str | Unset):
            municipio_comprador (None | ProvinciaMunicipioTypeType1 | Unset):
            provincia_comprador (None | ProvinciaMunicipioTypeType1 | Unset):
            codigo_interno_comprador (None | str | Unset):
            responsable_pago (None | str | Unset):
            informacion_adicional_comprador (None | str | Unset):
     """

    rnc_comprador: str
    razon_social_comprador: str
    contacto_comprador: None | str | Unset = UNSET
    correo_comprador: None | str | Unset = UNSET
    direccion_comprador: None | str | Unset = UNSET
    municipio_comprador: None | ProvinciaMunicipioTypeType1 | Unset = UNSET
    provincia_comprador: None | ProvinciaMunicipioTypeType1 | Unset = UNSET
    codigo_interno_comprador: None | str | Unset = UNSET
    responsable_pago: None | str | Unset = UNSET
    informacion_adicional_comprador: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rnc_comprador = self.rnc_comprador

        razon_social_comprador = self.razon_social_comprador

        contacto_comprador: None | str | Unset
        if isinstance(self.contacto_comprador, Unset):
            contacto_comprador = UNSET
        else:
            contacto_comprador = self.contacto_comprador

        correo_comprador: None | str | Unset
        if isinstance(self.correo_comprador, Unset):
            correo_comprador = UNSET
        else:
            correo_comprador = self.correo_comprador

        direccion_comprador: None | str | Unset
        if isinstance(self.direccion_comprador, Unset):
            direccion_comprador = UNSET
        else:
            direccion_comprador = self.direccion_comprador

        municipio_comprador: None | str | Unset
        if isinstance(self.municipio_comprador, Unset):
            municipio_comprador = UNSET
        elif isinstance(self.municipio_comprador, ProvinciaMunicipioTypeType1):
            municipio_comprador = self.municipio_comprador.value
        else:
            municipio_comprador = self.municipio_comprador

        provincia_comprador: None | str | Unset
        if isinstance(self.provincia_comprador, Unset):
            provincia_comprador = UNSET
        elif isinstance(self.provincia_comprador, ProvinciaMunicipioTypeType1):
            provincia_comprador = self.provincia_comprador.value
        else:
            provincia_comprador = self.provincia_comprador

        codigo_interno_comprador: None | str | Unset
        if isinstance(self.codigo_interno_comprador, Unset):
            codigo_interno_comprador = UNSET
        else:
            codigo_interno_comprador = self.codigo_interno_comprador

        responsable_pago: None | str | Unset
        if isinstance(self.responsable_pago, Unset):
            responsable_pago = UNSET
        else:
            responsable_pago = self.responsable_pago

        informacion_adicional_comprador: None | str | Unset
        if isinstance(self.informacion_adicional_comprador, Unset):
            informacion_adicional_comprador = UNSET
        else:
            informacion_adicional_comprador = self.informacion_adicional_comprador


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rncComprador": rnc_comprador,
            "razonSocialComprador": razon_social_comprador,
        })
        if contacto_comprador is not UNSET:
            field_dict["contactoComprador"] = contacto_comprador
        if correo_comprador is not UNSET:
            field_dict["correoComprador"] = correo_comprador
        if direccion_comprador is not UNSET:
            field_dict["direccionComprador"] = direccion_comprador
        if municipio_comprador is not UNSET:
            field_dict["municipioComprador"] = municipio_comprador
        if provincia_comprador is not UNSET:
            field_dict["provinciaComprador"] = provincia_comprador
        if codigo_interno_comprador is not UNSET:
            field_dict["codigoInternoComprador"] = codigo_interno_comprador
        if responsable_pago is not UNSET:
            field_dict["responsablePago"] = responsable_pago
        if informacion_adicional_comprador is not UNSET:
            field_dict["informacionAdicionalComprador"] = informacion_adicional_comprador

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rnc_comprador = d.pop("rncComprador")

        razon_social_comprador = d.pop("razonSocialComprador")

        def _parse_contacto_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contacto_comprador = _parse_contacto_comprador(d.pop("contactoComprador", UNSET))


        def _parse_correo_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        correo_comprador = _parse_correo_comprador(d.pop("correoComprador", UNSET))


        def _parse_direccion_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direccion_comprador = _parse_direccion_comprador(d.pop("direccionComprador", UNSET))


        def _parse_municipio_comprador(data: object) -> None | ProvinciaMunicipioTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_provincia_municipio_type_type_1 = ProvinciaMunicipioTypeType1(data)



                return componentsschemas_provincia_municipio_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProvinciaMunicipioTypeType1 | Unset, data)

        municipio_comprador = _parse_municipio_comprador(d.pop("municipioComprador", UNSET))


        def _parse_provincia_comprador(data: object) -> None | ProvinciaMunicipioTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_provincia_municipio_type_type_1 = ProvinciaMunicipioTypeType1(data)



                return componentsschemas_provincia_municipio_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProvinciaMunicipioTypeType1 | Unset, data)

        provincia_comprador = _parse_provincia_comprador(d.pop("provinciaComprador", UNSET))


        def _parse_codigo_interno_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codigo_interno_comprador = _parse_codigo_interno_comprador(d.pop("codigoInternoComprador", UNSET))


        def _parse_responsable_pago(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsable_pago = _parse_responsable_pago(d.pop("responsablePago", UNSET))


        def _parse_informacion_adicional_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        informacion_adicional_comprador = _parse_informacion_adicional_comprador(d.pop("informacionAdicionalComprador", UNSET))


        ecf_41_comprador = cls(
            rnc_comprador=rnc_comprador,
            razon_social_comprador=razon_social_comprador,
            contacto_comprador=contacto_comprador,
            correo_comprador=correo_comprador,
            direccion_comprador=direccion_comprador,
            municipio_comprador=municipio_comprador,
            provincia_comprador=provincia_comprador,
            codigo_interno_comprador=codigo_interno_comprador,
            responsable_pago=responsable_pago,
            informacion_adicional_comprador=informacion_adicional_comprador,
        )


        ecf_41_comprador.additional_properties = d
        return ecf_41_comprador

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
