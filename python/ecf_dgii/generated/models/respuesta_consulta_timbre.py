from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RespuestaConsultaTimbre")



@_attrs_define
class RespuestaConsultaTimbre:
    """ Representa la respuesta del servicio de Consulta Timbre Fiscal (QR) de la DGII.
    Este servicio permite validar la validez de un e-CF remitido exclusivamente por el servicio web
    de recepción de e-CF, a partir de los datos incluidos en el timbre de su representación impresa (RI).

        Example:
            {'razonSocial': 'razonSocial', 'estado': 'estado', 'encf': 'encf', 'rncEmisor': 'rncEmisor'}

        Attributes:
            rnc_emisor (None | str | Unset): Número de registro nacional del contribuyente que emitió el resumen de factura
                de consumo.
                RNC del emisor del comprobante fiscal electrónico consultado.
            razon_social (None | str | Unset): Razón social del contribuyente que emitió el resumen de factura de consumo.
                Nombre comercial o razón social del emisor del comprobante fiscal electrónico.
            encf (None | str | Unset): Número de secuencia utilizada por el contribuyente, extraído del resumen de factura
                de consumo.
                Número de comprobante fiscal electrónico (e-NCF) utilizado en la transacción.
            estado (None | str | Unset): Estado de validación otorgado por Impuestos Internos al resumen de factura de
                consumo recibido.
                Descripción textual del estado de validación del comprobante. Posibles valores:
                - "No fue encontrada la factura (e-CF)": El e-CF no se encontró en la base de datos de la DGII.
                - "Aceptado": Implica la validez del e-CF de la RI, incluyendo el aceptado condicional que corresponde
                  a que no cumplió en algún punto pero que no amerita el rechazo de este.
                - "Rechazado": Corresponde a que el e-CF de la RI le fue rechazado al emisor.
     """

    rnc_emisor: None | str | Unset = UNSET
    razon_social: None | str | Unset = UNSET
    encf: None | str | Unset = UNSET
    estado: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        rnc_emisor: None | str | Unset
        if isinstance(self.rnc_emisor, Unset):
            rnc_emisor = UNSET
        else:
            rnc_emisor = self.rnc_emisor

        razon_social: None | str | Unset
        if isinstance(self.razon_social, Unset):
            razon_social = UNSET
        else:
            razon_social = self.razon_social

        encf: None | str | Unset
        if isinstance(self.encf, Unset):
            encf = UNSET
        else:
            encf = self.encf

        estado: None | str | Unset
        if isinstance(self.estado, Unset):
            estado = UNSET
        else:
            estado = self.estado


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rnc_emisor is not UNSET:
            field_dict["rncEmisor"] = rnc_emisor
        if razon_social is not UNSET:
            field_dict["razonSocial"] = razon_social
        if encf is not UNSET:
            field_dict["encf"] = encf
        if estado is not UNSET:
            field_dict["estado"] = estado

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_rnc_emisor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_emisor = _parse_rnc_emisor(d.pop("rncEmisor", UNSET))


        def _parse_razon_social(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        razon_social = _parse_razon_social(d.pop("razonSocial", UNSET))


        def _parse_encf(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encf = _parse_encf(d.pop("encf", UNSET))


        def _parse_estado(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estado = _parse_estado(d.pop("estado", UNSET))


        respuesta_consulta_timbre = cls(
            rnc_emisor=rnc_emisor,
            razon_social=razon_social,
            encf=encf,
            estado=estado,
        )


        respuesta_consulta_timbre.additional_properties = d
        return respuesta_consulta_timbre

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
