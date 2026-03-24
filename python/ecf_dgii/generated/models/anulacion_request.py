from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.detalle_anulacion_request import DetalleAnulacionRequest





T = TypeVar("T", bound="AnulacionRequest")



@_attrs_define
class AnulacionRequest:
    """ 
        Example:
            {'cantidaDeNcfAnulados': 0, 'detalleAnulacion': [{'secuencias': [{'hastaEncf': 'hastaEncf', 'desdeEncf':
                'desdeEncf'}, {'hastaEncf': 'hastaEncf', 'desdeEncf': 'desdeEncf'}], 'cantidadeNcfAnulados': None, 'tipoEcf':
                'ECF31', 'noLinea': [None, None]}, {'secuencias': [{'hastaEncf': 'hastaEncf', 'desdeEncf': 'desdeEncf'},
                {'hastaEncf': 'hastaEncf', 'desdeEncf': 'desdeEncf'}], 'cantidadeNcfAnulados': None, 'tipoEcf': 'ECF31',
                'noLinea': [None, None]}]}

        Attributes:
            cantida_de_ncf_anulados (int | str):
            detalle_anulacion (list[DetalleAnulacionRequest]):
     """

    cantida_de_ncf_anulados: int | str
    detalle_anulacion: list[DetalleAnulacionRequest]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.detalle_anulacion_request import DetalleAnulacionRequest
        cantida_de_ncf_anulados: int | str
        cantida_de_ncf_anulados = self.cantida_de_ncf_anulados

        detalle_anulacion = []
        for detalle_anulacion_item_data in self.detalle_anulacion:
            detalle_anulacion_item = detalle_anulacion_item_data.to_dict()
            detalle_anulacion.append(detalle_anulacion_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cantidaDeNcfAnulados": cantida_de_ncf_anulados,
            "detalleAnulacion": detalle_anulacion,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.detalle_anulacion_request import DetalleAnulacionRequest
        d = dict(src_dict)
        def _parse_cantida_de_ncf_anulados(data: object) -> int | str:
            return cast(int | str, data)

        cantida_de_ncf_anulados = _parse_cantida_de_ncf_anulados(d.pop("cantidaDeNcfAnulados"))


        detalle_anulacion = []
        _detalle_anulacion = d.pop("detalleAnulacion")
        for detalle_anulacion_item_data in (_detalle_anulacion):
            detalle_anulacion_item = DetalleAnulacionRequest.from_dict(detalle_anulacion_item_data)



            detalle_anulacion.append(detalle_anulacion_item)


        anulacion_request = cls(
            cantida_de_ncf_anulados=cantida_de_ncf_anulados,
            detalle_anulacion=detalle_anulacion,
        )


        anulacion_request.additional_properties = d
        return anulacion_request

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
