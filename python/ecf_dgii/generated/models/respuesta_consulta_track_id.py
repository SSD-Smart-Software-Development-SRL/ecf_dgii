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





T = TypeVar("T", bound="RespuestaConsultaTrackId")



@_attrs_define
class RespuestaConsultaTrackId:
    """ Representa la respuesta del servicio de consulta de resultado de comprobantes fiscales electrónicos (e-CF).
    Este modelo contiene la información completa sobre el estado de procesamiento y validación de un e-CF
    que fue enviado previamente mediante el servicio de recepción.

        Example:
            {'codigo': '1', 'estado': 'Aceptado', 'encf': 'E310000000001', 'trackId': 'ddddd', 'rnc': '131880738',
                'secuenciaUtilizada': False, 'mensajes': [{'codigo': 1, 'valor': 'El comprobante fue aceptado correctamente'},
                {'codigo': 1, 'valor': 'El comprobante fue aceptado correctamente'}], 'fechaRecepcion': datetime.datetime(2020,
                12, 17, 11, 19, 6)}

        Attributes:
            track_id (None | str | Unset): Obtiene el número único generado por Impuestos Internos para identificar un e-CF
                recibido.
                Este identificador se obtiene como respuesta del servicio de recepción de e-CF.
                El identificador único del track. Puede ser null si no está disponible. Example: ddddd.
            codigo (None | str | Unset): Obtiene el código asociado al estado de validación del e-CF recibido.
                Un código que indica el resultado de la validación. Los valores típicos son:
                - "0": No encontrado
                - "1": Aceptado
                - "2": Rechazado
                - "3": En Proceso
                - "4": Aceptado Condicional Example: 1.
            estado (None | str | Unset): Obtiene el estado de validación otorgado por Impuestos Internos al e-CF recibido.
                Descripción textual del estado. Puede incluir valores como:
                - "No encontrado": No se encontró el trackid en los registros
                - "Aceptado": Implica la validez del e-CF
                - "Rechazado": Implica la nulidad del comprobante para fines tributarios
                - "En Proceso": El comprobante aún no ha sido validado
                - "Aceptado Condicional": El comprobante no cumplió en algún punto pero no ameritó el rechazo Example: Aceptado.
            rnc (None | str | Unset): Obtiene el número de registro nacional del contribuyente que envió el e-CF.
                El RNC del emisor del comprobante. Puede ser null si no está disponible. Example: 131880738.
            encf (None | str | Unset): Obtiene el número de secuencia utilizada por el contribuyente en el e-CF.
                El número de comprobante fiscal electrónico (e-NCF). Puede ser null si no está disponible. Example:
                E310000000001.
            secuencia_utilizada (bool | Unset): Indica si el número de secuencia puede ser reutilizada en otro e-CF.
                True si la secuencia puede reutilizarse, False si no puede reutilizarse.

                Este parámetro permite dar a conocer si el número de secuencia que fue recibido
                por Impuestos Internos puede reutilizarse en otro Comprobante Fiscal Electrónico (e-CF)
                en el escenario de que el resultado de la validación haya sido "Rechazado" por los siguientes motivos:
                - Certificado y/o firma inválida
                - Estructura del comprobante (XML) no es válida
                - Firmante del comprobante fiscal electrónico no corresponde a un delegado autorizado
                - El e-NCF no está autorizado para el RNC Emisor
                - El e-NCF autorizado se encuentra vencido
                - El RNC Emisor no corresponde a un emisor electrónico
                - El RNC Emisor no existe o no se encuentra activo
            fecha_recepcion (None | str | Unset): Obtiene la fecha en la cual Impuestos Internos recibió el e-CF.
                La fecha de recepción del comprobante. Puede ser null si no está disponible.
                El formato típico es ISO 8601 o un formato de fecha legible. Example: 2020-12-17 11:19:06.
            mensajes (list[Mensaje] | None | Unset): Obtiene los mensajes asociados al estado de validación del e-CF
                recibido.
                Un array de mensajes que proporcionan información detallada sobre el estado
                de validación. Puede ser null si no hay mensajes disponibles.
     """

    track_id: None | str | Unset = UNSET
    codigo: None | str | Unset = UNSET
    estado: None | str | Unset = UNSET
    rnc: None | str | Unset = UNSET
    encf: None | str | Unset = UNSET
    secuencia_utilizada: bool | Unset = UNSET
    fecha_recepcion: None | str | Unset = UNSET
    mensajes: list[Mensaje] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mensaje import Mensaje
        track_id: None | str | Unset
        if isinstance(self.track_id, Unset):
            track_id = UNSET
        else:
            track_id = self.track_id

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

        rnc: None | str | Unset
        if isinstance(self.rnc, Unset):
            rnc = UNSET
        else:
            rnc = self.rnc

        encf: None | str | Unset
        if isinstance(self.encf, Unset):
            encf = UNSET
        else:
            encf = self.encf

        secuencia_utilizada = self.secuencia_utilizada

        fecha_recepcion: None | str | Unset
        if isinstance(self.fecha_recepcion, Unset):
            fecha_recepcion = UNSET
        else:
            fecha_recepcion = self.fecha_recepcion

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
        if track_id is not UNSET:
            field_dict["trackId"] = track_id
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if estado is not UNSET:
            field_dict["estado"] = estado
        if rnc is not UNSET:
            field_dict["rnc"] = rnc
        if encf is not UNSET:
            field_dict["encf"] = encf
        if secuencia_utilizada is not UNSET:
            field_dict["secuenciaUtilizada"] = secuencia_utilizada
        if fecha_recepcion is not UNSET:
            field_dict["fechaRecepcion"] = fecha_recepcion
        if mensajes is not UNSET:
            field_dict["mensajes"] = mensajes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mensaje import Mensaje
        d = dict(src_dict)
        def _parse_track_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        track_id = _parse_track_id(d.pop("trackId", UNSET))


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


        def _parse_rnc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc = _parse_rnc(d.pop("rnc", UNSET))


        def _parse_encf(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encf = _parse_encf(d.pop("encf", UNSET))


        secuencia_utilizada = d.pop("secuenciaUtilizada", UNSET)

        def _parse_fecha_recepcion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fecha_recepcion = _parse_fecha_recepcion(d.pop("fechaRecepcion", UNSET))


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


        respuesta_consulta_track_id = cls(
            track_id=track_id,
            codigo=codigo,
            estado=estado,
            rnc=rnc,
            encf=encf,
            secuencia_utilizada=secuencia_utilizada,
            fecha_recepcion=fecha_recepcion,
            mensajes=mensajes,
        )


        respuesta_consulta_track_id.additional_properties = d
        return respuesta_consulta_track_id

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
