from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mensaje import Mensaje





T = TypeVar("T", bound="RespuestaConsultaRFCE")



@_attrs_define
class RespuestaConsultaRFCE:
    """ Representa la respuesta del servicio de Consulta de Resumen de Factura (RFCE) de la DGII.
    Este servicio permite validar la validez fiscal de un comprobante fiscal electrónico
    a través del RNC emisor, e-NCF y código de seguridad.

        Example:
            {'codigo': 'codigo', 'estado': 'estado', 'encf': 'encf', 'rnc': 'rnc', 'secuenciaUtilizada': True, 'mensajes':
                [{'codigo': 1, 'valor': 'El comprobante fue aceptado correctamente'}, {'codigo': 1, 'valor': 'El comprobante fue
                aceptado correctamente'}]}

        Attributes:
            rnc (None | str | Unset): Número de registro nacional del contribuyente que envió el e-CF.
                RNC del emisor del comprobante fiscal electrónico consultado.
            encf (str | Unset): Número de secuencia utilizada por el contribuyente en el ENCF.
                Número de comprobante fiscal electrónico (e-NCF) consultado.
            secuencia_utilizada (bool | Unset): Indica si el número de secuencia puede ser reutilizado.
                `true` si la secuencia NO puede reutilizarse (rechazado por motivos específicos);
                        `false` si la secuencia SÍ puede reutilizarse.
            codigo (None | str | Unset): Código asociado al estado de validación del e-CF recibido.
                Código numérico que indica el resultado de la validación:
                - 0: No encontrado
                - 1: Aceptado
                - 2: Rechazado
                - 4: Aceptado Condicional (solo para FC &lt; RD$ 250000.00)
            estado (None | str | Unset): Estado de validación otorgado por Impuestos Internos al e-CF recibido.
                Descripción textual del estado de validación del comprobante.
            mensajes (list[Mensaje] | None | Unset): Mensajes y códigos asociados al estado de validación del e-CF recibido.
                Array de mensajes que proporcionan detalles adicionales sobre la validación.
     """

    rnc: None | str | Unset = UNSET
    encf: str | Unset = UNSET
    secuencia_utilizada: bool | Unset = UNSET
    codigo: None | str | Unset = UNSET
    estado: None | str | Unset = UNSET
    mensajes: list[Mensaje] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mensaje import Mensaje
        rnc: None | str | Unset
        if isinstance(self.rnc, Unset):
            rnc = UNSET
        else:
            rnc = self.rnc

        encf = self.encf

        secuencia_utilizada = self.secuencia_utilizada

        codigo: None | str | Unset
        if isinstance(self.codigo, Unset):
            codigo = UNSET
        else:
            codigo = self.codigo

        estado: None | str | Unset
        if isinstance(self.estado, Unset):
            estado = UNSET
        else:
            estado = self.estado

        mensajes: list[dict[str, Any]] | None | Unset
        if isinstance(self.mensajes, Unset):
            mensajes = UNSET
        elif isinstance(self.mensajes, list):
            mensajes = []
            for mensajes_type_0_item_data in self.mensajes:
                mensajes_type_0_item = mensajes_type_0_item_data.to_dict()
                mensajes.append(mensajes_type_0_item)


        else:
            mensajes = self.mensajes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rnc is not UNSET:
            field_dict["rnc"] = rnc
        if encf is not UNSET:
            field_dict["encf"] = encf
        if secuencia_utilizada is not UNSET:
            field_dict["secuenciaUtilizada"] = secuencia_utilizada
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if estado is not UNSET:
            field_dict["estado"] = estado
        if mensajes is not UNSET:
            field_dict["mensajes"] = mensajes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mensaje import Mensaje
        d = dict(src_dict)
        def _parse_rnc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc = _parse_rnc(d.pop("rnc", UNSET))


        encf = d.pop("encf", UNSET)

        secuencia_utilizada = d.pop("secuenciaUtilizada", UNSET)

        def _parse_codigo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codigo = _parse_codigo(d.pop("codigo", UNSET))


        def _parse_estado(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estado = _parse_estado(d.pop("estado", UNSET))


        def _parse_mensajes(data: object) -> list[Mensaje] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mensajes_type_0 = []
                _mensajes_type_0 = data
                for mensajes_type_0_item_data in (_mensajes_type_0):
                    mensajes_type_0_item = Mensaje.from_dict(mensajes_type_0_item_data)



                    mensajes_type_0.append(mensajes_type_0_item)

                return mensajes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Mensaje] | None | Unset, data)

        mensajes = _parse_mensajes(d.pop("mensajes", UNSET))


        respuesta_consulta_rfce = cls(
            rnc=rnc,
            encf=encf,
            secuencia_utilizada=secuencia_utilizada,
            codigo=codigo,
            estado=estado,
            mensajes=mensajes,
        )


        respuesta_consulta_rfce.additional_properties = d
        return respuesta_consulta_rfce

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
