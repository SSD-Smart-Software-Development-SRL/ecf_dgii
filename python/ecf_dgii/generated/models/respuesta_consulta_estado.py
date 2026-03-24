from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RespuestaConsultaEstado")



@_attrs_define
class RespuestaConsultaEstado:
    """ Representa la respuesta del servicio de consulta de estado de e-CF.
    Este modelo contiene la información de validez y estado de un comprobante fiscal electrónico
    consultado a través del servicio web de consulta estado de la DGII.

        Example:
            {'codigo': 0, 'estado': 'estado', 'totalITBIS': 1.4658129805029452, 'codigoSeguridad': 'codigoSeguridad',
                'fechaFirma': 'fechaFirma', 'idExtranjero': 'idExtranjero', 'fechaEmision': 'fechaEmision', 'ncfElectronico':
                'ncfElectronico', 'montoTotal': 6.027456183070403, 'rncComprador': 'rncComprador', 'rncEmisor': 'rncEmisor'}

        Attributes:
            codigo (int | str | Unset): Código asociado al estado de validación del e-CF recibido.
                            Posibles valores:
                            * 0No encontrado - No se encontró el comprobante en los registros
                * 1Aceptado - El e-CF generado por el emisor fue aceptado y tiene validez fiscal
                * 2Rechazado - Corresponde a la nulidad del comprobante generado por el emisor
            estado (None | str | Unset): Estado de validación otorgado por Impuestos Internos al e-CF recibido.
                Descripción textual del estado del comprobante fiscal electrónico.
            rnc_emisor (None | str | Unset): Número de registro nacional del contribuyente que envió el e-CF.
                RNC del emisor del comprobante fiscal electrónico.
            ncf_electronico (None | str | Unset): Número de secuencia utilizada por el contribuyente en el e-CF.
                Número de comprobante fiscal electrónico (e-NCF) utilizado en la transacción.
            monto_total (float | None | str | Unset): Monto total extraído del e-CF recibido.
                Valor total de la transacción en pesos dominicanos.
            total_itbis (float | None | str | Unset): Total de ITBIS extraído del e-CF recibido.
                Monto total del Impuesto sobre Transferencias de Bienes Industrializados y Servicios.
            fecha_emision (None | str | Unset): Fecha de emisión extraída del e-CF recibido.
                Fecha en que fue emitido el comprobante fiscal electrónico.
            fecha_firma (None | str | Unset): Fecha de firma extraída del e-CF recibido.
                Fecha en que fue firmado digitalmente el comprobante fiscal electrónico.
            rnc_comprador (None | str | Unset): RNC del comprador extraído del e-CF recibido (si aplica).
                Número de registro nacional del contribuyente comprador, cuando corresponde.
            codigo_seguridad (None | str | Unset): Código de seguridad extraído de los primeros seis (6) dígitos del hash
                generado
                en el SignatureValue de la firma digital del e-CF recibido.
                Código de seguridad de 6 caracteres para validación del comprobante.
            id_extranjero (None | str | Unset): Identificación de extranjero extraída del e-CF recibido (si aplica).
                Número de identificación del comprador extranjero cuando corresponde.
     """

    codigo: int | str | Unset = UNSET
    estado: None | str | Unset = UNSET
    rnc_emisor: None | str | Unset = UNSET
    ncf_electronico: None | str | Unset = UNSET
    monto_total: float | None | str | Unset = UNSET
    total_itbis: float | None | str | Unset = UNSET
    fecha_emision: None | str | Unset = UNSET
    fecha_firma: None | str | Unset = UNSET
    rnc_comprador: None | str | Unset = UNSET
    codigo_seguridad: None | str | Unset = UNSET
    id_extranjero: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        codigo: int | str | Unset
        if isinstance(self.codigo, Unset):
            codigo = UNSET
        else:
            codigo = self.codigo

        estado: None | str | Unset
        if isinstance(self.estado, Unset):
            estado = UNSET
        else:
            estado = self.estado

        rnc_emisor: None | str | Unset
        if isinstance(self.rnc_emisor, Unset):
            rnc_emisor = UNSET
        else:
            rnc_emisor = self.rnc_emisor

        ncf_electronico: None | str | Unset
        if isinstance(self.ncf_electronico, Unset):
            ncf_electronico = UNSET
        else:
            ncf_electronico = self.ncf_electronico

        monto_total: float | None | str | Unset
        if isinstance(self.monto_total, Unset):
            monto_total = UNSET
        else:
            monto_total = self.monto_total

        total_itbis: float | None | str | Unset
        if isinstance(self.total_itbis, Unset):
            total_itbis = UNSET
        else:
            total_itbis = self.total_itbis

        fecha_emision: None | str | Unset
        if isinstance(self.fecha_emision, Unset):
            fecha_emision = UNSET
        else:
            fecha_emision = self.fecha_emision

        fecha_firma: None | str | Unset
        if isinstance(self.fecha_firma, Unset):
            fecha_firma = UNSET
        else:
            fecha_firma = self.fecha_firma

        rnc_comprador: None | str | Unset
        if isinstance(self.rnc_comprador, Unset):
            rnc_comprador = UNSET
        else:
            rnc_comprador = self.rnc_comprador

        codigo_seguridad: None | str | Unset
        if isinstance(self.codigo_seguridad, Unset):
            codigo_seguridad = UNSET
        else:
            codigo_seguridad = self.codigo_seguridad

        id_extranjero: None | str | Unset
        if isinstance(self.id_extranjero, Unset):
            id_extranjero = UNSET
        else:
            id_extranjero = self.id_extranjero


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if estado is not UNSET:
            field_dict["estado"] = estado
        if rnc_emisor is not UNSET:
            field_dict["rncEmisor"] = rnc_emisor
        if ncf_electronico is not UNSET:
            field_dict["ncfElectronico"] = ncf_electronico
        if monto_total is not UNSET:
            field_dict["montoTotal"] = monto_total
        if total_itbis is not UNSET:
            field_dict["totalITBIS"] = total_itbis
        if fecha_emision is not UNSET:
            field_dict["fechaEmision"] = fecha_emision
        if fecha_firma is not UNSET:
            field_dict["fechaFirma"] = fecha_firma
        if rnc_comprador is not UNSET:
            field_dict["rncComprador"] = rnc_comprador
        if codigo_seguridad is not UNSET:
            field_dict["codigoSeguridad"] = codigo_seguridad
        if id_extranjero is not UNSET:
            field_dict["idExtranjero"] = id_extranjero

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_codigo(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        codigo = _parse_codigo(d.pop("codigo", UNSET))


        def _parse_estado(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estado = _parse_estado(d.pop("estado", UNSET))


        def _parse_rnc_emisor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_emisor = _parse_rnc_emisor(d.pop("rncEmisor", UNSET))


        def _parse_ncf_electronico(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ncf_electronico = _parse_ncf_electronico(d.pop("ncfElectronico", UNSET))


        def _parse_monto_total(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_total = _parse_monto_total(d.pop("montoTotal", UNSET))


        def _parse_total_itbis(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_itbis = _parse_total_itbis(d.pop("totalITBIS", UNSET))


        def _parse_fecha_emision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fecha_emision = _parse_fecha_emision(d.pop("fechaEmision", UNSET))


        def _parse_fecha_firma(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fecha_firma = _parse_fecha_firma(d.pop("fechaFirma", UNSET))


        def _parse_rnc_comprador(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_comprador = _parse_rnc_comprador(d.pop("rncComprador", UNSET))


        def _parse_codigo_seguridad(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codigo_seguridad = _parse_codigo_seguridad(d.pop("codigoSeguridad", UNSET))


        def _parse_id_extranjero(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id_extranjero = _parse_id_extranjero(d.pop("idExtranjero", UNSET))


        respuesta_consulta_estado = cls(
            codigo=codigo,
            estado=estado,
            rnc_emisor=rnc_emisor,
            ncf_electronico=ncf_electronico,
            monto_total=monto_total,
            total_itbis=total_itbis,
            fecha_emision=fecha_emision,
            fecha_firma=fecha_firma,
            rnc_comprador=rnc_comprador,
            codigo_seguridad=codigo_seguridad,
            id_extranjero=id_extranjero,
        )


        respuesta_consulta_estado.additional_properties = d
        return respuesta_consulta_estado

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
