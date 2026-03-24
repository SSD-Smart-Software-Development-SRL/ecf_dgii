from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Mensaje")



@_attrs_define
class Mensaje:
    """ Representa un mensaje asociado al estado de validación de un comprobante fiscal electrónico (e-CF).
    Este modelo se utiliza en las respuestas de consulta de resultado para proporcionar información
    detallada sobre el estado de procesamiento y cualquier mensaje relacionado.

        Example:
            {'codigo': 1, 'valor': 'El comprobante fue aceptado correctamente'}

        Attributes:
            valor (None | str | Unset): Obtiene el valor textual del mensaje que describe el estado o resultado de la
                validación.
                El texto descriptivo del mensaje. Puede ser null si no hay mensaje disponible. Example: El comprobante fue
                aceptado correctamente.
            codigo (int | str | Unset): Obtiene el código numérico que identifica el tipo de mensaje o estado.
                Un código entero que categoriza el mensaje. Los valores típicos incluyen:
                - 0: No encontrado
                - 1: Aceptado
                - 2: Rechazado
                - 3: En Proceso
                - 4: Aceptado Condicional Example: 1.
     """

    valor: None | str | Unset = UNSET
    codigo: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        valor: None | str | Unset
        if isinstance(self.valor, Unset):
            valor = UNSET
        else:
            valor = self.valor

        codigo: int | str | Unset
        if isinstance(self.codigo, Unset):
            codigo = UNSET
        else:
            codigo = self.codigo


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if valor is not UNSET:
            field_dict["valor"] = valor
        if codigo is not UNSET:
            field_dict["codigo"] = codigo

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_valor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        valor = _parse_valor(d.pop("valor", UNSET))


        def _parse_codigo(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        codigo = _parse_codigo(d.pop("codigo", UNSET))


        mensaje = cls(
            valor=valor,
            codigo=codigo,
        )


        mensaje.additional_properties = d
        return mensaje

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
