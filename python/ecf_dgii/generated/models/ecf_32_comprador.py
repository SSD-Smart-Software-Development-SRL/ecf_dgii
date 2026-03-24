from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provincia_municipio_type_type_1 import ProvinciaMunicipioTypeType1
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Ecf32Comprador")



@_attrs_define
class Ecf32Comprador:
    """ 
        Example:
            {'direccionComprador': 'direccionComprador', 'correoComprador': 'correoComprador', 'fechaOrdenCompra':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'responsablePago': 'responsablePago', 'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador',
                'identificadorExtranjero': 'identificadorExtranjero', 'municipioComprador': '', 'rncComprador': 'rncComprador',
                'codigoInternoComprador': 'codigoInternoComprador', 'direccionEntrega': 'direccionEntrega', 'numeroOrdenCompra':
                'numeroOrdenCompra', 'informacionAdicionalComprador': 'informacionAdicionalComprador', 'contactoComprador':
                'contactoComprador', 'contactoEntrega': 'contactoEntrega', 'fechaEntrega': datetime.datetime(2000, 1, 23, 4, 56,
                7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'telefonoAdicional': 'telefonoAdicional'}

        Attributes:
            rnc_comprador (None | str | Unset):
            identificador_extranjero (None | str | Unset):
            razon_social_comprador (None | str | Unset):
            contacto_comprador (None | str | Unset):
            correo_comprador (None | str | Unset):
            direccion_comprador (None | str | Unset):
            municipio_comprador (None | ProvinciaMunicipioTypeType1 | Unset):
            provincia_comprador (None | ProvinciaMunicipioTypeType1 | Unset):
            fecha_entrega (datetime.datetime | None | Unset):
            contacto_entrega (None | str | Unset):
            direccion_entrega (None | str | Unset):
            telefono_adicional (None | str | Unset):
            fecha_orden_compra (datetime.datetime | None | Unset):
            numero_orden_compra (None | str | Unset):
            codigo_interno_comprador (None | str | Unset):
            responsable_pago (None | str | Unset):
            informacion_adicional_comprador (None | str | Unset):
     """

    rnc_comprador: None | str | Unset = UNSET
    identificador_extranjero: None | str | Unset = UNSET
    razon_social_comprador: None | str | Unset = UNSET
    contacto_comprador: None | str | Unset = UNSET
    correo_comprador: None | str | Unset = UNSET
    direccion_comprador: None | str | Unset = UNSET
    municipio_comprador: None | ProvinciaMunicipioTypeType1 | Unset = UNSET
    provincia_comprador: None | ProvinciaMunicipioTypeType1 | Unset = UNSET
    fecha_entrega: datetime.datetime | None | Unset = UNSET
    contacto_entrega: None | str | Unset = UNSET
    direccion_entrega: None | str | Unset = UNSET
    telefono_adicional: None | str | Unset = UNSET
    fecha_orden_compra: datetime.datetime | None | Unset = UNSET
    numero_orden_compra: None | str | Unset = UNSET
    codigo_interno_comprador: None | str | Unset = UNSET
    responsable_pago: None | str | Unset = UNSET
    informacion_adicional_comprador: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rnc_comprador: None | str | Unset
        if isinstance(self.rnc_comprador, Unset):
            rnc_comprador = UNSET
        else:
            rnc_comprador = self.rnc_comprador

        identificador_extranjero: None | str | Unset
        if isinstance(self.identificador_extranjero, Unset):
            identificador_extranjero = UNSET
        else:
            identificador_extranjero = self.identificador_extranjero

        razon_social_comprador: None | str | Unset
        if isinstance(self.razon_social_comprador, Unset):
            razon_social_comprador = UNSET
        else:
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

        fecha_entrega: None | str | Unset
        if isinstance(self.fecha_entrega, Unset):
            fecha_entrega = UNSET
        elif isinstance(self.fecha_entrega, datetime.datetime):
            fecha_entrega = self.fecha_entrega.isoformat()
        else:
            fecha_entrega = self.fecha_entrega

        contacto_entrega: None | str | Unset
        if isinstance(self.contacto_entrega, Unset):
            contacto_entrega = UNSET
        else:
            contacto_entrega = self.contacto_entrega

        direccion_entrega: None | str | Unset
        if isinstance(self.direccion_entrega, Unset):
            direccion_entrega = UNSET
        else:
            direccion_entrega = self.direccion_entrega

        telefono_adicional: None | str | Unset
        if isinstance(self.telefono_adicional, Unset):
            telefono_adicional = UNSET
        else:
            telefono_adicional = self.telefono_adicional

        fecha_orden_compra: None | str | Unset
        if isinstance(self.fecha_orden_compra, Unset):
            fecha_orden_compra = UNSET
        elif isinstance(self.fecha_orden_compra, datetime.datetime):
            fecha_orden_compra = self.fecha_orden_compra.isoformat()
        else:
            fecha_orden_compra = self.fecha_orden_compra

        numero_orden_compra: None | str | Unset
        if isinstance(self.numero_orden_compra, Unset):
            numero_orden_compra = UNSET
        else:
            numero_orden_compra = self.numero_orden_compra

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
        })
        if rnc_comprador is not UNSET:
            field_dict["rncComprador"] = rnc_comprador
        if identificador_extranjero is not UNSET:
            field_dict["identificadorExtranjero"] = identificador_extranjero
        if razon_social_comprador is not UNSET:
            field_dict["razonSocialComprador"] = razon_social_comprador
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
        if fecha_entrega is not UNSET:
            field_dict["fechaEntrega"] = fecha_entrega
        if contacto_entrega is not UNSET:
            field_dict["contactoEntrega"] = contacto_entrega
        if direccion_entrega is not UNSET:
            field_dict["direccionEntrega"] = direccion_entrega
        if telefono_adicional is not UNSET:
            field_dict["telefonoAdicional"] = telefono_adicional
        if fecha_orden_compra is not UNSET:
            field_dict["fechaOrdenCompra"] = fecha_orden_compra
        if numero_orden_compra is not UNSET:
            field_dict["numeroOrdenCompra"] = numero_orden_compra
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
        def _parse_rnc_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_comprador = _parse_rnc_comprador(d.pop("rncComprador", UNSET))


        def _parse_identificador_extranjero(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identificador_extranjero = _parse_identificador_extranjero(d.pop("identificadorExtranjero", UNSET))


        def _parse_razon_social_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        razon_social_comprador = _parse_razon_social_comprador(d.pop("razonSocialComprador", UNSET))


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


        def _parse_fecha_entrega(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_entrega_type_0 = isoparse(data)



                return fecha_entrega_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_entrega = _parse_fecha_entrega(d.pop("fechaEntrega", UNSET))


        def _parse_contacto_entrega(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contacto_entrega = _parse_contacto_entrega(d.pop("contactoEntrega", UNSET))


        def _parse_direccion_entrega(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direccion_entrega = _parse_direccion_entrega(d.pop("direccionEntrega", UNSET))


        def _parse_telefono_adicional(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telefono_adicional = _parse_telefono_adicional(d.pop("telefonoAdicional", UNSET))


        def _parse_fecha_orden_compra(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_orden_compra_type_0 = isoparse(data)



                return fecha_orden_compra_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_orden_compra = _parse_fecha_orden_compra(d.pop("fechaOrdenCompra", UNSET))


        def _parse_numero_orden_compra(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_orden_compra = _parse_numero_orden_compra(d.pop("numeroOrdenCompra", UNSET))


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


        ecf_32_comprador = cls(
            rnc_comprador=rnc_comprador,
            identificador_extranjero=identificador_extranjero,
            razon_social_comprador=razon_social_comprador,
            contacto_comprador=contacto_comprador,
            correo_comprador=correo_comprador,
            direccion_comprador=direccion_comprador,
            municipio_comprador=municipio_comprador,
            provincia_comprador=provincia_comprador,
            fecha_entrega=fecha_entrega,
            contacto_entrega=contacto_entrega,
            direccion_entrega=direccion_entrega,
            telefono_adicional=telefono_adicional,
            fecha_orden_compra=fecha_orden_compra,
            numero_orden_compra=numero_orden_compra,
            codigo_interno_comprador=codigo_interno_comprador,
            responsable_pago=responsable_pago,
            informacion_adicional_comprador=informacion_adicional_comprador,
        )


        ecf_32_comprador.additional_properties = d
        return ecf_32_comprador

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
