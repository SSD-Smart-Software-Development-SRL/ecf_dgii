from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_34_codigo_modificacion_type import Ecf34CodigoModificacionType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Ecf34InformacionReferencia")



@_attrs_define
class Ecf34InformacionReferencia:
    """ 
        Example:
            {'razonModificacion': 'razonModificacion', 'rncOtroContribuyente': 'rncOtroContribuyente', 'codigoModificacion':
                'AnulaElNCFModificado', 'ncfModificado': 'ncfModificado', 'fechaNCFModificado': datetime.datetime(2000, 1, 23,
                4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}

        Attributes:
            ncf_modificado (str):
            codigo_modificacion (Ecf34CodigoModificacionType):
            rnc_otro_contribuyente (None | str | Unset):
            fecha_ncf_modificado (datetime.datetime | Unset):
            razon_modificacion (None | str | Unset):
     """

    ncf_modificado: str
    codigo_modificacion: Ecf34CodigoModificacionType
    rnc_otro_contribuyente: None | str | Unset = UNSET
    fecha_ncf_modificado: datetime.datetime | Unset = UNSET
    razon_modificacion: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ncf_modificado = self.ncf_modificado

        codigo_modificacion = self.codigo_modificacion.value

        rnc_otro_contribuyente: None | str | Unset
        if isinstance(self.rnc_otro_contribuyente, Unset):
            rnc_otro_contribuyente = UNSET
        else:
            rnc_otro_contribuyente = self.rnc_otro_contribuyente

        fecha_ncf_modificado: str | Unset = UNSET
        if not isinstance(self.fecha_ncf_modificado, Unset):
            fecha_ncf_modificado = self.fecha_ncf_modificado.isoformat()

        razon_modificacion: None | str | Unset
        if isinstance(self.razon_modificacion, Unset):
            razon_modificacion = UNSET
        else:
            razon_modificacion = self.razon_modificacion


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ncfModificado": ncf_modificado,
            "codigoModificacion": codigo_modificacion,
        })
        if rnc_otro_contribuyente is not UNSET:
            field_dict["rncOtroContribuyente"] = rnc_otro_contribuyente
        if fecha_ncf_modificado is not UNSET:
            field_dict["fechaNCFModificado"] = fecha_ncf_modificado
        if razon_modificacion is not UNSET:
            field_dict["razonModificacion"] = razon_modificacion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ncf_modificado = d.pop("ncfModificado")

        codigo_modificacion = Ecf34CodigoModificacionType(d.pop("codigoModificacion"))




        def _parse_rnc_otro_contribuyente(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_otro_contribuyente = _parse_rnc_otro_contribuyente(d.pop("rncOtroContribuyente", UNSET))


        _fecha_ncf_modificado = d.pop("fechaNCFModificado", UNSET)
        fecha_ncf_modificado: datetime.datetime | Unset
        if isinstance(_fecha_ncf_modificado,  Unset):
            fecha_ncf_modificado = UNSET
        else:
            fecha_ncf_modificado = isoparse(_fecha_ncf_modificado)




        def _parse_razon_modificacion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        razon_modificacion = _parse_razon_modificacion(d.pop("razonModificacion", UNSET))


        ecf_34_informacion_referencia = cls(
            ncf_modificado=ncf_modificado,
            codigo_modificacion=codigo_modificacion,
            rnc_otro_contribuyente=rnc_otro_contribuyente,
            fecha_ncf_modificado=fecha_ncf_modificado,
            razon_modificacion=razon_modificacion,
        )


        ecf_34_informacion_referencia.additional_properties = d
        return ecf_34_informacion_referencia

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
