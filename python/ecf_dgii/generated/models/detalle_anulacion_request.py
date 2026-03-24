from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_type import ECFType
from typing import cast

if TYPE_CHECKING:
  from ..models.secuencia_request import SecuenciaRequest





T = TypeVar("T", bound="DetalleAnulacionRequest")



@_attrs_define
class DetalleAnulacionRequest:
    """ 
        Example:
            {'secuencias': [{'hastaEncf': 'hastaEncf', 'desdeEncf': 'desdeEncf'}, {'hastaEncf': 'hastaEncf', 'desdeEncf':
                'desdeEncf'}], 'cantidadeNcfAnulados': None, 'tipoEcf': 'ECF31', 'noLinea': [None, None]}

        Attributes:
            tipo_ecf (ECFType):
            cantidade_ncf_anulados (int | str):
            no_linea (list[int | str]):
            secuencias (list[SecuenciaRequest]):
     """

    tipo_ecf: ECFType
    cantidade_ncf_anulados: int | str
    no_linea: list[int | str]
    secuencias: list[SecuenciaRequest]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.secuencia_request import SecuenciaRequest
        tipo_ecf = self.tipo_ecf.value

        cantidade_ncf_anulados: int | str
        cantidade_ncf_anulados = self.cantidade_ncf_anulados

        no_linea = []
        for no_linea_item_data in self.no_linea:
            no_linea_item: int | str
            no_linea_item = no_linea_item_data
            no_linea.append(no_linea_item)



        secuencias = []
        for secuencias_item_data in self.secuencias:
            secuencias_item = secuencias_item_data.to_dict()
            secuencias.append(secuencias_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tipoEcf": tipo_ecf,
            "cantidadeNcfAnulados": cantidade_ncf_anulados,
            "noLinea": no_linea,
            "secuencias": secuencias,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secuencia_request import SecuenciaRequest
        d = dict(src_dict)
        tipo_ecf = ECFType(d.pop("tipoEcf"))




        def _parse_cantidade_ncf_anulados(data: object) -> int | str:
            return cast(int | str, data)

        cantidade_ncf_anulados = _parse_cantidade_ncf_anulados(d.pop("cantidadeNcfAnulados"))


        no_linea = []
        _no_linea = d.pop("noLinea")
        for no_linea_item_data in (_no_linea):
            def _parse_no_linea_item(data: object) -> int | str:
                return cast(int | str, data)

            no_linea_item = _parse_no_linea_item(no_linea_item_data)

            no_linea.append(no_linea_item)


        secuencias = []
        _secuencias = d.pop("secuencias")
        for secuencias_item_data in (_secuencias):
            secuencias_item = SecuenciaRequest.from_dict(secuencias_item_data)



            secuencias.append(secuencias_item)


        detalle_anulacion_request = cls(
            tipo_ecf=tipo_ecf,
            cantidade_ncf_anulados=cantidade_ncf_anulados,
            no_linea=no_linea,
            secuencias=secuencias,
        )


        detalle_anulacion_request.additional_properties = d
        return detalle_anulacion_request

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
