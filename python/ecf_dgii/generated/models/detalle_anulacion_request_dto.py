from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_type import ECFType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.secuencia_request_dto import SecuenciaRequestDto





T = TypeVar("T", bound="DetalleAnulacionRequestDto")



@_attrs_define
class DetalleAnulacionRequestDto:
    """ 
        Example:
            {'secuencias': [{'hastaEncf': 'hastaEncf', 'desdeEncf': 'desdeEncf'}, {'hastaEncf': 'hastaEncf', 'desdeEncf':
                'desdeEncf'}], 'cantidadeNcfAnulados': None, 'tipoEcf': 'ECF31', 'noLinea': [None, None]}

        Attributes:
            tipo_ecf (ECFType | Unset):
            cantidade_ncf_anulados (int | str | Unset):
            no_linea (list[int | str] | Unset):
            secuencias (list[SecuenciaRequestDto] | Unset):
     """

    tipo_ecf: ECFType | Unset = UNSET
    cantidade_ncf_anulados: int | str | Unset = UNSET
    no_linea: list[int | str] | Unset = UNSET
    secuencias: list[SecuenciaRequestDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.secuencia_request_dto import SecuenciaRequestDto
        tipo_ecf: str | Unset = UNSET
        if not isinstance(self.tipo_ecf, Unset):
            tipo_ecf = self.tipo_ecf.value


        cantidade_ncf_anulados: int | str | Unset
        if isinstance(self.cantidade_ncf_anulados, Unset):
            cantidade_ncf_anulados = UNSET
        else:
            cantidade_ncf_anulados = self.cantidade_ncf_anulados

        no_linea: list[int | str] | Unset = UNSET
        if not isinstance(self.no_linea, Unset):
            no_linea = []
            for no_linea_item_data in self.no_linea:
                no_linea_item: int | str
                no_linea_item = no_linea_item_data
                no_linea.append(no_linea_item)



        secuencias: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secuencias, Unset):
            secuencias = []
            for secuencias_item_data in self.secuencias:
                secuencias_item = secuencias_item_data.to_dict()
                secuencias.append(secuencias_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tipo_ecf is not UNSET:
            field_dict["tipoEcf"] = tipo_ecf
        if cantidade_ncf_anulados is not UNSET:
            field_dict["cantidadeNcfAnulados"] = cantidade_ncf_anulados
        if no_linea is not UNSET:
            field_dict["noLinea"] = no_linea
        if secuencias is not UNSET:
            field_dict["secuencias"] = secuencias

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secuencia_request_dto import SecuenciaRequestDto
        d = dict(src_dict)
        _tipo_ecf = d.pop("tipoEcf", UNSET)
        tipo_ecf: ECFType | Unset
        if isinstance(_tipo_ecf,  Unset):
            tipo_ecf = UNSET
        else:
            tipo_ecf = ECFType(_tipo_ecf)




        def _parse_cantidade_ncf_anulados(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        cantidade_ncf_anulados = _parse_cantidade_ncf_anulados(d.pop("cantidadeNcfAnulados", UNSET))


        _no_linea = d.pop("noLinea", UNSET)
        no_linea: list[int | str] | Unset = UNSET
        if _no_linea is not UNSET:
            no_linea = []
            for no_linea_item_data in _no_linea:
                def _parse_no_linea_item(data: object) -> int | str:
                    return cast(int | str, data)

                no_linea_item = _parse_no_linea_item(no_linea_item_data)

                no_linea.append(no_linea_item)


        _secuencias = d.pop("secuencias", UNSET)
        secuencias: list[SecuenciaRequestDto] | Unset = UNSET
        if _secuencias is not UNSET:
            secuencias = []
            for secuencias_item_data in _secuencias:
                secuencias_item = SecuenciaRequestDto.from_dict(secuencias_item_data)



                secuencias.append(secuencias_item)


        detalle_anulacion_request_dto = cls(
            tipo_ecf=tipo_ecf,
            cantidade_ncf_anulados=cantidade_ncf_anulados,
            no_linea=no_linea,
            secuencias=secuencias,
        )


        detalle_anulacion_request_dto.additional_properties = d
        return detalle_anulacion_request_dto

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
