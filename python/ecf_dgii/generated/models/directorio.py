from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Directorio")



@_attrs_define
class Directorio:
    """ Representa una entrada del directorio para contribuyentes electrónicos en el sistema de facturación electrónica
    de la República Dominicana. Este modelo contiene las URLs de servicios que los contribuyentes electrónicos
    deben proporcionar para la comunicación entre contribuyentes.

        Example:
            {'urlRecepcion': 'urlRecepcion', 'urlAceptacion': 'urlAceptacion', 'rnc': 'rnc', 'urlOpcional': 'urlOpcional',
                'nombre': 'nombre'}

        Attributes:
            nombre (None | str | Unset): Obtiene el nombre legal o razón social del contribuyente electrónico.
                La razón social registrada tal como aparece en el registro oficial del contribuyente.
                Este campo es requerido y debe coincidir con el nombre de la entidad legal del contribuyente.
            rnc (None | str | Unset): Obtiene el Número de Registro Nacional del Contribuyente (RNC) del contribuyente
                electrónico.
                Un número de 9 dígitos que identifica de forma única al contribuyente en el sistema tributario
                de la República Dominicana. Este campo es requerido y debe tener un formato de RNC válido.
            url_recepcion (None | str | Unset): Obtiene la URL del servicio de recepción de facturas electrónicas.
                La URL completa donde otros contribuyentes pueden enviar facturas electrónicas (e-CF) a este contribuyente.
                Debe seguir el formato estándar: https://host/ambiente/nombreservicio/fe/recepcion/api/ecf
                Este campo es obligatorio para todos los contribuyentes electrónicos.
            url_aceptacion (None | str | Unset): Obtiene la URL del servicio de aprobación comercial.
                La URL completa donde otros contribuyentes pueden enviar aprobaciones comerciales para facturas recibidas.
                Debe seguir el formato estándar: https://host/ambiente/nombreservicio/fe/aprobacioncomercial/api/ecf
                Este campo es obligatorio para todos los contribuyentes electrónicos.
            url_opcional (None | str | Unset): Obtiene la URL del servicio opcional de autenticación.
                La URL base del servicio de autenticación, si es implementado por el contribuyente.
                Debe seguir el formato estándar: https://host/ambiente/nombreservicio/fe/autenticacion/api/
                Este campo es opcional pero recomendado para mayor seguridad.
     """

    nombre: None | str | Unset = UNSET
    rnc: None | str | Unset = UNSET
    url_recepcion: None | str | Unset = UNSET
    url_aceptacion: None | str | Unset = UNSET
    url_opcional: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        nombre: None | str | Unset
        if isinstance(self.nombre, Unset):
            nombre = UNSET
        else:
            nombre = self.nombre

        rnc: None | str | Unset
        if isinstance(self.rnc, Unset):
            rnc = UNSET
        else:
            rnc = self.rnc

        url_recepcion: None | str | Unset
        if isinstance(self.url_recepcion, Unset):
            url_recepcion = UNSET
        else:
            url_recepcion = self.url_recepcion

        url_aceptacion: None | str | Unset
        if isinstance(self.url_aceptacion, Unset):
            url_aceptacion = UNSET
        else:
            url_aceptacion = self.url_aceptacion

        url_opcional: None | str | Unset
        if isinstance(self.url_opcional, Unset):
            url_opcional = UNSET
        else:
            url_opcional = self.url_opcional


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if nombre is not UNSET:
            field_dict["nombre"] = nombre
        if rnc is not UNSET:
            field_dict["rnc"] = rnc
        if url_recepcion is not UNSET:
            field_dict["urlRecepcion"] = url_recepcion
        if url_aceptacion is not UNSET:
            field_dict["urlAceptacion"] = url_aceptacion
        if url_opcional is not UNSET:
            field_dict["urlOpcional"] = url_opcional

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_nombre(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nombre = _parse_nombre(d.pop("nombre", UNSET))


        def _parse_rnc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc = _parse_rnc(d.pop("rnc", UNSET))


        def _parse_url_recepcion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_recepcion = _parse_url_recepcion(d.pop("urlRecepcion", UNSET))


        def _parse_url_aceptacion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_aceptacion = _parse_url_aceptacion(d.pop("urlAceptacion", UNSET))


        def _parse_url_opcional(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_opcional = _parse_url_opcional(d.pop("urlOpcional", UNSET))


        directorio = cls(
            nombre=nombre,
            rnc=rnc,
            url_recepcion=url_recepcion,
            url_aceptacion=url_aceptacion,
            url_opcional=url_opcional,
        )


        directorio.additional_properties = d
        return directorio

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
