from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="VentanaDeMantenimiento")



@_attrs_define
class VentanaDeMantenimiento:
    """ Representa información de ventana de mantenimiento para un ambiente específico.
    Contiene detalles sobre cuándo ocurrirá el mantenimiento programado.

        Example:
            {'horaFin': 'horaFin', 'ambiente': 'ambiente', 'dias': ['dias', 'dias'], 'horaInicio': 'horaInicio'}

        Attributes:
            ambiente (None | str | Unset): Nombre del ambiente donde aplica la ventana de mantenimiento.
                Valores posibles:
                - "PreCertificacion": Ambiente de pre-certificación
                - "Certificacion": Ambiente de certificación
                - "Produccion": Ambiente de producción
            hora_inicio (None | str | Unset): Hora de inicio de la ventana de mantenimiento.
                Formato: "H:MM AM/PM" (ejemplo: "9:00 AM", "1:00 PM")
            hora_fin (None | str | Unset): Hora de fin de la ventana de mantenimiento.
                Formato: "H:MM AM/PM" (ejemplo: "12:00 PM", "4:00 PM")
            dias (list[str] | None | Unset): Arreglo de fechas específicas cuando están programadas las ventanas de
                mantenimiento.
                Formato: "DD-MM-YYYY" (ejemplo: "06-08-2020", "20-08-2020")
     """

    ambiente: None | str | Unset = UNSET
    hora_inicio: None | str | Unset = UNSET
    hora_fin: None | str | Unset = UNSET
    dias: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ambiente: None | str | Unset
        if isinstance(self.ambiente, Unset):
            ambiente = UNSET
        else:
            ambiente = self.ambiente

        hora_inicio: None | str | Unset
        if isinstance(self.hora_inicio, Unset):
            hora_inicio = UNSET
        else:
            hora_inicio = self.hora_inicio

        hora_fin: None | str | Unset
        if isinstance(self.hora_fin, Unset):
            hora_fin = UNSET
        else:
            hora_fin = self.hora_fin

        dias: list[str] | None | Unset
        if isinstance(self.dias, Unset):
            dias = UNSET
        elif isinstance(self.dias, list):
            dias = self.dias


        else:
            dias = self.dias


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ambiente is not UNSET:
            field_dict["ambiente"] = ambiente
        if hora_inicio is not UNSET:
            field_dict["horaInicio"] = hora_inicio
        if hora_fin is not UNSET:
            field_dict["horaFin"] = hora_fin
        if dias is not UNSET:
            field_dict["dias"] = dias

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_ambiente(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ambiente = _parse_ambiente(d.pop("ambiente", UNSET))


        def _parse_hora_inicio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hora_inicio = _parse_hora_inicio(d.pop("horaInicio", UNSET))


        def _parse_hora_fin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hora_fin = _parse_hora_fin(d.pop("horaFin", UNSET))


        def _parse_dias(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dias_type_0 = cast(list[str], data)

                return dias_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        dias = _parse_dias(d.pop("dias", UNSET))


        ventana_de_mantenimiento = cls(
            ambiente=ambiente,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            dias=dias,
        )


        ventana_de_mantenimiento.additional_properties = d
        return ventana_de_mantenimiento

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
