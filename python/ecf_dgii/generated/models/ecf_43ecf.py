from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ecf_43_encabezado import Ecf43Encabezado
    from ..models.ecf_43_informacion_referencia import Ecf43InformacionReferencia
    from ..models.ecf_43_item import Ecf43Item
    from ..models.ecf_43_pagina import Ecf43Pagina
    from ..models.ecf_43_subtotal import Ecf43Subtotal


T = TypeVar("T", bound="Ecf43ECF")


@_attrs_define
class Ecf43ECF:
    """
    Attributes:
        encabezado (Ecf43Encabezado):
        detalles_items (list[Ecf43Item]):
        subtotales (list[Ecf43Subtotal] | None | Unset):
        paginacion (list[Ecf43Pagina] | None | Unset):
        informacion_referencia (Ecf43InformacionReferencia | None | Unset):
    """

    encabezado: Ecf43Encabezado
    detalles_items: list[Ecf43Item]
    subtotales: list[Ecf43Subtotal] | None | Unset = UNSET
    paginacion: list[Ecf43Pagina] | None | Unset = UNSET
    informacion_referencia: Ecf43InformacionReferencia | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_43_informacion_referencia import Ecf43InformacionReferencia

        encabezado = self.encabezado.to_dict()

        detalles_items = []
        for detalles_items_item_data in self.detalles_items:
            detalles_items_item = detalles_items_item_data.to_dict()
            detalles_items.append(detalles_items_item)

        subtotales: list[dict[str, Any]] | None | Unset
        if isinstance(self.subtotales, Unset):
            subtotales = UNSET
        elif isinstance(self.subtotales, list):
            subtotales = []
            for subtotales_type_1_item_data in self.subtotales:
                subtotales_type_1_item = subtotales_type_1_item_data.to_dict()
                subtotales.append(subtotales_type_1_item)

        else:
            subtotales = self.subtotales

        paginacion: list[dict[str, Any]] | None | Unset
        if isinstance(self.paginacion, Unset):
            paginacion = UNSET
        elif isinstance(self.paginacion, list):
            paginacion = []
            for paginacion_type_1_item_data in self.paginacion:
                paginacion_type_1_item = paginacion_type_1_item_data.to_dict()
                paginacion.append(paginacion_type_1_item)

        else:
            paginacion = self.paginacion

        informacion_referencia: dict[str, Any] | None | Unset
        if isinstance(self.informacion_referencia, Unset):
            informacion_referencia = UNSET
        elif isinstance(self.informacion_referencia, Ecf43InformacionReferencia):
            informacion_referencia = self.informacion_referencia.to_dict()
        else:
            informacion_referencia = self.informacion_referencia

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encabezado": encabezado,
                "detallesItems": detalles_items,
            }
        )
        if subtotales is not UNSET:
            field_dict["subtotales"] = subtotales
        if paginacion is not UNSET:
            field_dict["paginacion"] = paginacion
        if informacion_referencia is not UNSET:
            field_dict["informacionReferencia"] = informacion_referencia

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_43_encabezado import Ecf43Encabezado
        from ..models.ecf_43_informacion_referencia import Ecf43InformacionReferencia
        from ..models.ecf_43_item import Ecf43Item
        from ..models.ecf_43_pagina import Ecf43Pagina
        from ..models.ecf_43_subtotal import Ecf43Subtotal

        d = dict(src_dict)
        encabezado = Ecf43Encabezado.from_dict(d.pop("encabezado"))

        detalles_items = []
        _detalles_items = d.pop("detallesItems")
        for detalles_items_item_data in _detalles_items:
            detalles_items_item = Ecf43Item.from_dict(detalles_items_item_data)

            detalles_items.append(detalles_items_item)

        def _parse_subtotales(data: object) -> list[Ecf43Subtotal] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subtotales_type_1 = []
                _subtotales_type_1 = data
                for subtotales_type_1_item_data in _subtotales_type_1:
                    subtotales_type_1_item = Ecf43Subtotal.from_dict(subtotales_type_1_item_data)

                    subtotales_type_1.append(subtotales_type_1_item)

                return subtotales_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf43Subtotal] | None | Unset, data)

        subtotales = _parse_subtotales(d.pop("subtotales", UNSET))

        def _parse_paginacion(data: object) -> list[Ecf43Pagina] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                paginacion_type_1 = []
                _paginacion_type_1 = data
                for paginacion_type_1_item_data in _paginacion_type_1:
                    paginacion_type_1_item = Ecf43Pagina.from_dict(paginacion_type_1_item_data)

                    paginacion_type_1.append(paginacion_type_1_item)

                return paginacion_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf43Pagina] | None | Unset, data)

        paginacion = _parse_paginacion(d.pop("paginacion", UNSET))

        def _parse_informacion_referencia(data: object) -> Ecf43InformacionReferencia | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                informacion_referencia_type_1 = Ecf43InformacionReferencia.from_dict(data)

                return informacion_referencia_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf43InformacionReferencia | None | Unset, data)

        informacion_referencia = _parse_informacion_referencia(d.pop("informacionReferencia", UNSET))

        ecf_43ecf = cls(
            encabezado=encabezado,
            detalles_items=detalles_items,
            subtotales=subtotales,
            paginacion=paginacion,
            informacion_referencia=informacion_referencia,
        )

        ecf_43ecf.additional_properties = d
        return ecf_43ecf

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
