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






T = TypeVar("T", bound="Ecf31Emisor")



@_attrs_define
class Ecf31Emisor:
    """ 
        Example:
            {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor', 'informacionAdicionalEmisor':
                'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000, 1, 23), 'provincia': '',
                'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor': 'correoEmisor', 'webSite':
                'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'], 'sucursal': 'sucursal',
                'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna': 'numeroFacturaInterna', 'nombreComercial':
                'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta': 'rutaVenta', 'codigoVendedor': 'codigoVendedor'}

        Attributes:
            rnc_emisor (str):
            razon_social_emisor (str):
            direccion_emisor (str):
            nombre_comercial (None | str | Unset):
            sucursal (None | str | Unset):
            municipio (None | ProvinciaMunicipioTypeType1 | Unset):
            provincia (None | ProvinciaMunicipioTypeType1 | Unset):
            tabla_telefono_emisor (list[str] | None | Unset):
            correo_emisor (None | str | Unset):
            web_site (None | str | Unset):
            actividad_economica (None | str | Unset):
            codigo_vendedor (None | str | Unset):
            numero_factura_interna (None | str | Unset):
            numero_pedido_interno (None | str | Unset):
            zona_venta (None | str | Unset):
            ruta_venta (None | str | Unset):
            informacion_adicional_emisor (None | str | Unset):
            fecha_emision (datetime.date | Unset):
     """

    rnc_emisor: str
    razon_social_emisor: str
    direccion_emisor: str
    nombre_comercial: None | str | Unset = UNSET
    sucursal: None | str | Unset = UNSET
    municipio: None | ProvinciaMunicipioTypeType1 | Unset = UNSET
    provincia: None | ProvinciaMunicipioTypeType1 | Unset = UNSET
    tabla_telefono_emisor: list[str] | None | Unset = UNSET
    correo_emisor: None | str | Unset = UNSET
    web_site: None | str | Unset = UNSET
    actividad_economica: None | str | Unset = UNSET
    codigo_vendedor: None | str | Unset = UNSET
    numero_factura_interna: None | str | Unset = UNSET
    numero_pedido_interno: None | str | Unset = UNSET
    zona_venta: None | str | Unset = UNSET
    ruta_venta: None | str | Unset = UNSET
    informacion_adicional_emisor: None | str | Unset = UNSET
    fecha_emision: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rnc_emisor = self.rnc_emisor

        razon_social_emisor = self.razon_social_emisor

        direccion_emisor = self.direccion_emisor

        nombre_comercial: None | str | Unset
        if isinstance(self.nombre_comercial, Unset):
            nombre_comercial = UNSET
        else:
            nombre_comercial = self.nombre_comercial

        sucursal: None | str | Unset
        if isinstance(self.sucursal, Unset):
            sucursal = UNSET
        else:
            sucursal = self.sucursal

        municipio: None | str | Unset
        if isinstance(self.municipio, Unset):
            municipio = UNSET
        elif isinstance(self.municipio, ProvinciaMunicipioTypeType1):
            municipio = self.municipio.value
        else:
            municipio = self.municipio

        provincia: None | str | Unset
        if isinstance(self.provincia, Unset):
            provincia = UNSET
        elif isinstance(self.provincia, ProvinciaMunicipioTypeType1):
            provincia = self.provincia.value
        else:
            provincia = self.provincia

        tabla_telefono_emisor: list[str] | None | Unset
        if isinstance(self.tabla_telefono_emisor, Unset):
            tabla_telefono_emisor = UNSET
        elif isinstance(self.tabla_telefono_emisor, list):
            tabla_telefono_emisor = self.tabla_telefono_emisor


        else:
            tabla_telefono_emisor = self.tabla_telefono_emisor

        correo_emisor: None | str | Unset
        if isinstance(self.correo_emisor, Unset):
            correo_emisor = UNSET
        else:
            correo_emisor = self.correo_emisor

        web_site: None | str | Unset
        if isinstance(self.web_site, Unset):
            web_site = UNSET
        else:
            web_site = self.web_site

        actividad_economica: None | str | Unset
        if isinstance(self.actividad_economica, Unset):
            actividad_economica = UNSET
        else:
            actividad_economica = self.actividad_economica

        codigo_vendedor: None | str | Unset
        if isinstance(self.codigo_vendedor, Unset):
            codigo_vendedor = UNSET
        else:
            codigo_vendedor = self.codigo_vendedor

        numero_factura_interna: None | str | Unset
        if isinstance(self.numero_factura_interna, Unset):
            numero_factura_interna = UNSET
        else:
            numero_factura_interna = self.numero_factura_interna

        numero_pedido_interno: None | str | Unset
        if isinstance(self.numero_pedido_interno, Unset):
            numero_pedido_interno = UNSET
        else:
            numero_pedido_interno = self.numero_pedido_interno

        zona_venta: None | str | Unset
        if isinstance(self.zona_venta, Unset):
            zona_venta = UNSET
        else:
            zona_venta = self.zona_venta

        ruta_venta: None | str | Unset
        if isinstance(self.ruta_venta, Unset):
            ruta_venta = UNSET
        else:
            ruta_venta = self.ruta_venta

        informacion_adicional_emisor: None | str | Unset
        if isinstance(self.informacion_adicional_emisor, Unset):
            informacion_adicional_emisor = UNSET
        else:
            informacion_adicional_emisor = self.informacion_adicional_emisor

        fecha_emision: str | Unset = UNSET
        if not isinstance(self.fecha_emision, Unset):
            fecha_emision = self.fecha_emision.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "rncEmisor": rnc_emisor,
            "razonSocialEmisor": razon_social_emisor,
            "direccionEmisor": direccion_emisor,
        })
        if nombre_comercial is not UNSET:
            field_dict["nombreComercial"] = nombre_comercial
        if sucursal is not UNSET:
            field_dict["sucursal"] = sucursal
        if municipio is not UNSET:
            field_dict["municipio"] = municipio
        if provincia is not UNSET:
            field_dict["provincia"] = provincia
        if tabla_telefono_emisor is not UNSET:
            field_dict["tablaTelefonoEmisor"] = tabla_telefono_emisor
        if correo_emisor is not UNSET:
            field_dict["correoEmisor"] = correo_emisor
        if web_site is not UNSET:
            field_dict["webSite"] = web_site
        if actividad_economica is not UNSET:
            field_dict["actividadEconomica"] = actividad_economica
        if codigo_vendedor is not UNSET:
            field_dict["codigoVendedor"] = codigo_vendedor
        if numero_factura_interna is not UNSET:
            field_dict["numeroFacturaInterna"] = numero_factura_interna
        if numero_pedido_interno is not UNSET:
            field_dict["numeroPedidoInterno"] = numero_pedido_interno
        if zona_venta is not UNSET:
            field_dict["zonaVenta"] = zona_venta
        if ruta_venta is not UNSET:
            field_dict["rutaVenta"] = ruta_venta
        if informacion_adicional_emisor is not UNSET:
            field_dict["informacionAdicionalEmisor"] = informacion_adicional_emisor
        if fecha_emision is not UNSET:
            field_dict["fechaEmision"] = fecha_emision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rnc_emisor = d.pop("rncEmisor")

        razon_social_emisor = d.pop("razonSocialEmisor")

        direccion_emisor = d.pop("direccionEmisor")

        def _parse_nombre_comercial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nombre_comercial = _parse_nombre_comercial(d.pop("nombreComercial", UNSET))


        def _parse_sucursal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sucursal = _parse_sucursal(d.pop("sucursal", UNSET))


        def _parse_municipio(data: object) -> None | ProvinciaMunicipioTypeType1 | Unset:
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

        municipio = _parse_municipio(d.pop("municipio", UNSET))


        def _parse_provincia(data: object) -> None | ProvinciaMunicipioTypeType1 | Unset:
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

        provincia = _parse_provincia(d.pop("provincia", UNSET))


        def _parse_tabla_telefono_emisor(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_telefono_emisor_type_0 = cast(list[str], data)

                return tabla_telefono_emisor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tabla_telefono_emisor = _parse_tabla_telefono_emisor(d.pop("tablaTelefonoEmisor", UNSET))


        def _parse_correo_emisor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        correo_emisor = _parse_correo_emisor(d.pop("correoEmisor", UNSET))


        def _parse_web_site(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        web_site = _parse_web_site(d.pop("webSite", UNSET))


        def _parse_actividad_economica(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actividad_economica = _parse_actividad_economica(d.pop("actividadEconomica", UNSET))


        def _parse_codigo_vendedor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codigo_vendedor = _parse_codigo_vendedor(d.pop("codigoVendedor", UNSET))


        def _parse_numero_factura_interna(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_factura_interna = _parse_numero_factura_interna(d.pop("numeroFacturaInterna", UNSET))


        def _parse_numero_pedido_interno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_pedido_interno = _parse_numero_pedido_interno(d.pop("numeroPedidoInterno", UNSET))


        def _parse_zona_venta(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zona_venta = _parse_zona_venta(d.pop("zonaVenta", UNSET))


        def _parse_ruta_venta(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ruta_venta = _parse_ruta_venta(d.pop("rutaVenta", UNSET))


        def _parse_informacion_adicional_emisor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        informacion_adicional_emisor = _parse_informacion_adicional_emisor(d.pop("informacionAdicionalEmisor", UNSET))


        _fecha_emision = d.pop("fechaEmision", UNSET)
        fecha_emision: datetime.date | Unset
        if isinstance(_fecha_emision,  Unset):
            fecha_emision = UNSET
        else:
            fecha_emision = isoparse(_fecha_emision).date()




        ecf_31_emisor = cls(
            rnc_emisor=rnc_emisor,
            razon_social_emisor=razon_social_emisor,
            direccion_emisor=direccion_emisor,
            nombre_comercial=nombre_comercial,
            sucursal=sucursal,
            municipio=municipio,
            provincia=provincia,
            tabla_telefono_emisor=tabla_telefono_emisor,
            correo_emisor=correo_emisor,
            web_site=web_site,
            actividad_economica=actividad_economica,
            codigo_vendedor=codigo_vendedor,
            numero_factura_interna=numero_factura_interna,
            numero_pedido_interno=numero_pedido_interno,
            zona_venta=zona_venta,
            ruta_venta=ruta_venta,
            informacion_adicional_emisor=informacion_adicional_emisor,
            fecha_emision=fecha_emision,
        )


        ecf_31_emisor.additional_properties = d
        return ecf_31_emisor

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
