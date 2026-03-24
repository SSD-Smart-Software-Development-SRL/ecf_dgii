from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ventana_de_mantenimiento import VentanaDeMantenimiento





T = TypeVar("T", bound="RespuestaVentanaDeMantenimiento")



@_attrs_define
class RespuestaVentanaDeMantenimiento:
    """ Modelo de respuesta que contiene información de ventanas de mantenimiento para todos los ambientes.
    Utilizado por el endpoint /api/estatusservicios/obtenerventanasmantenimiento.

        Example:
            {'ventanaMantenimientos': [{'horaFin': 'horaFin', 'ambiente': 'ambiente', 'dias': ['dias', 'dias'],
                'horaInicio': 'horaInicio'}, {'horaFin': 'horaFin', 'ambiente': 'ambiente', 'dias': ['dias', 'dias'],
                'horaInicio': 'horaInicio'}]}

        Attributes:
            ventana_mantenimientos (list[VentanaDeMantenimiento] | Unset): Arreglo de información de ventanas de
                mantenimiento para cada ambiente.
                Contiene períodos de mantenimiento programados cuando los servicios pueden no estar disponibles.
     """

    ventana_mantenimientos: list[VentanaDeMantenimiento] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ventana_de_mantenimiento import VentanaDeMantenimiento
        ventana_mantenimientos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ventana_mantenimientos, Unset):
            ventana_mantenimientos = []
            for ventana_mantenimientos_item_data in self.ventana_mantenimientos:
                ventana_mantenimientos_item = ventana_mantenimientos_item_data.to_dict()
                ventana_mantenimientos.append(ventana_mantenimientos_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ventana_mantenimientos is not UNSET:
            field_dict["ventanaMantenimientos"] = ventana_mantenimientos

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ventana_de_mantenimiento import VentanaDeMantenimiento
        d = dict(src_dict)
        _ventana_mantenimientos = d.pop("ventanaMantenimientos", UNSET)
        ventana_mantenimientos: list[VentanaDeMantenimiento] | Unset = UNSET
        if _ventana_mantenimientos is not UNSET:
            ventana_mantenimientos = []
            for ventana_mantenimientos_item_data in _ventana_mantenimientos:
                ventana_mantenimientos_item = VentanaDeMantenimiento.from_dict(ventana_mantenimientos_item_data)



                ventana_mantenimientos.append(ventana_mantenimientos_item)


        respuesta_ventana_de_mantenimiento = cls(
            ventana_mantenimientos=ventana_mantenimientos,
        )


        respuesta_ventana_de_mantenimiento.additional_properties = d
        return respuesta_ventana_de_mantenimiento

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
