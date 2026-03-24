from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RespuestaAnulacionRango")



@_attrs_define
class RespuestaAnulacionRango:
    """ Respuesta de anulación de rango de secuencias de e-NCF.

    Representa la respuesta del servicio de anulación de rangos de secuencias de comprobantes
    fiscales electrónicos. Este modelo se utiliza para procesar la respuesta del servicio web
    de anulación de e-NCF de la DGII.

    Servicio Web:• Endpoint: /api/operaciones/anularrango• Método: POST• Formato de entrada: XML (formato ANECF)•
    Formato de respuesta: JSON o XMLValidaciones del Servicio:• Tipo de archivo válido (XML)• Firma del documento
    válida• Tipo de comprobante válido• Secuencias no utilizadas previamente• RNC autorizado para realizar
    transaccionesReferencia Oficial:• Descripción Técnica de Facturación Electrónica v1.6, Sección "Anulación de e-NCF"•
    Formato Anulación de e-NCF v1.0 - DGII

        Example:
            {'codigo': 1, 'rnc': 123456789, 'mensajes': ['Las secuencias fueron anuladas correctamente'], 'nombre': 'EMPRESA
                EJEMPLO SRL'}

        Attributes:
            rnc (None | str | Unset): Número de Registro Nacional del Contribuyente que envió la anulación.

                Corresponde al RNC del contribuyente que solicitó la anulación de las secuencias.
                Este valor debe coincidir con el RNC autorizado para realizar transacciones de anulación
                y debe estar registrado como Facturador Electrónico en la DGII. Example: 123456789.
            codigo (None | str | Unset): Código asociado al resultado de la validación de la anulación.

                Indica el código de estado del resultado de la operación de anulación.
                Los códigos proporcionan información sobre el éxito o fallo de la operación
                y los motivos específicos cuando hay errores. Example: 1.
            nombre (None | str | Unset): Razón social del contribuyente que realizó la anulación.

                Nombre o razón social del contribuyente asociado al RNC que solicitó la anulación.
                Este campo proporciona información adicional para identificación del contribuyente
                y corresponde al nombre registrado en la DGII. Example: EMPRESA EJEMPLO SRL.
            mensajes (list[str] | None | Unset): Mensajes asociados al resultado de la validación de la anulación.

                Array de mensajes que proporcionan información detallada sobre el resultado de la operación.
                Puede incluir mensajes de éxito, advertencias, o errores específicos que ocurrieron
                durante el proceso de validación y anulación de las secuencias. Example: ['Las secuencias fueron anuladas
                correctamente'].
     """

    rnc: None | str | Unset = UNSET
    codigo: None | str | Unset = UNSET
    nombre: None | str | Unset = UNSET
    mensajes: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rnc: None | str | Unset
        if isinstance(self.rnc, Unset):
            rnc = UNSET
        else:
            rnc = self.rnc

        codigo: None | str | Unset
        if isinstance(self.codigo, Unset):
            codigo = UNSET
        else:
            codigo = self.codigo

        nombre: None | str | Unset
        if isinstance(self.nombre, Unset):
            nombre = UNSET
        else:
            nombre = self.nombre

        mensajes: list[str] | None | Unset
        if isinstance(self.mensajes, Unset):
            mensajes = UNSET
        elif isinstance(self.mensajes, list):
            mensajes = self.mensajes


        else:
            mensajes = self.mensajes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rnc is not UNSET:
            field_dict["rnc"] = rnc
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if nombre is not UNSET:
            field_dict["nombre"] = nombre
        if mensajes is not UNSET:
            field_dict["mensajes"] = mensajes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_rnc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc = _parse_rnc(d.pop("rnc", UNSET))


        def _parse_codigo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codigo = _parse_codigo(d.pop("codigo", UNSET))


        def _parse_nombre(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nombre = _parse_nombre(d.pop("nombre", UNSET))


        def _parse_mensajes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mensajes_type_0 = cast(list[str], data)

                return mensajes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        mensajes = _parse_mensajes(d.pop("mensajes", UNSET))


        respuesta_anulacion_rango = cls(
            rnc=rnc,
            codigo=codigo,
            nombre=nombre,
            mensajes=mensajes,
        )


        respuesta_anulacion_rango.additional_properties = d
        return respuesta_anulacion_rango

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
