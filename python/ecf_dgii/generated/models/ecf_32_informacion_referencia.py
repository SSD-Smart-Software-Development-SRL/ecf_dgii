from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.codigo_modificacion_type_type_1 import CodigoModificacionTypeType1
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Ecf32InformacionReferencia")



@_attrs_define
class Ecf32InformacionReferencia:
    """ 
        Attributes:
            ncf_modificado (None | str | Unset):
            rnc_otro_contribuyente (None | str | Unset):
            fecha_ncf_modificado (datetime.datetime | None | Unset):
            codigo_modificacion (CodigoModificacionTypeType1 | None | Unset):
     """

    ncf_modificado: None | str | Unset = UNSET
    rnc_otro_contribuyente: None | str | Unset = UNSET
    fecha_ncf_modificado: datetime.datetime | None | Unset = UNSET
    codigo_modificacion: CodigoModificacionTypeType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ncf_modificado: None | str | Unset
        if isinstance(self.ncf_modificado, Unset):
            ncf_modificado = UNSET
        else:
            ncf_modificado = self.ncf_modificado

        rnc_otro_contribuyente: None | str | Unset
        if isinstance(self.rnc_otro_contribuyente, Unset):
            rnc_otro_contribuyente = UNSET
        else:
            rnc_otro_contribuyente = self.rnc_otro_contribuyente

        fecha_ncf_modificado: None | str | Unset
        if isinstance(self.fecha_ncf_modificado, Unset):
            fecha_ncf_modificado = UNSET
        elif isinstance(self.fecha_ncf_modificado, datetime.datetime):
            fecha_ncf_modificado = self.fecha_ncf_modificado.isoformat()
        else:
            fecha_ncf_modificado = self.fecha_ncf_modificado

        codigo_modificacion: None | str | Unset
        if isinstance(self.codigo_modificacion, Unset):
            codigo_modificacion = UNSET
        elif isinstance(self.codigo_modificacion, CodigoModificacionTypeType1):
            codigo_modificacion = self.codigo_modificacion.value
        else:
            codigo_modificacion = self.codigo_modificacion


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ncf_modificado is not UNSET:
            field_dict["ncfModificado"] = ncf_modificado
        if rnc_otro_contribuyente is not UNSET:
            field_dict["rncOtroContribuyente"] = rnc_otro_contribuyente
        if fecha_ncf_modificado is not UNSET:
            field_dict["fechaNCFModificado"] = fecha_ncf_modificado
        if codigo_modificacion is not UNSET:
            field_dict["codigoModificacion"] = codigo_modificacion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_ncf_modificado(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ncf_modificado = _parse_ncf_modificado(d.pop("ncfModificado", UNSET))


        def _parse_rnc_otro_contribuyente(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_otro_contribuyente = _parse_rnc_otro_contribuyente(d.pop("rncOtroContribuyente", UNSET))


        def _parse_fecha_ncf_modificado(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_ncf_modificado_type_0 = isoparse(data)



                return fecha_ncf_modificado_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_ncf_modificado = _parse_fecha_ncf_modificado(d.pop("fechaNCFModificado", UNSET))


        def _parse_codigo_modificacion(data: object) -> CodigoModificacionTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_codigo_modificacion_type_type_1 = CodigoModificacionTypeType1(data)



                return componentsschemas_codigo_modificacion_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CodigoModificacionTypeType1 | None | Unset, data)

        codigo_modificacion = _parse_codigo_modificacion(d.pop("codigoModificacion", UNSET))


        ecf_32_informacion_referencia = cls(
            ncf_modificado=ncf_modificado,
            rnc_otro_contribuyente=rnc_otro_contribuyente,
            fecha_ncf_modificado=fecha_ncf_modificado,
            codigo_modificacion=codigo_modificacion,
        )


        ecf_32_informacion_referencia.additional_properties = d
        return ecf_32_informacion_referencia

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
