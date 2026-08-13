from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ecf_34_descuento_o_recargo import Ecf34DescuentoORecargo
    from ..models.ecf_34_encabezado import Ecf34Encabezado
    from ..models.ecf_34_informacion_referencia import Ecf34InformacionReferencia
    from ..models.ecf_34_item import Ecf34Item
    from ..models.ecf_34_pagina import Ecf34Pagina
    from ..models.ecf_34_subtotal import Ecf34Subtotal


T = TypeVar("T", bound="Ecf34ECF")


@_attrs_define
class Ecf34ECF:
    """
    Attributes:
        encabezado (Ecf34Encabezado):
        detalles_items (list[Ecf34Item]):
        informacion_referencia (Ecf34InformacionReferencia):
        subtotales (list[Ecf34Subtotal] | None | Unset):
        descuentos_o_recargos (list[Ecf34DescuentoORecargo] | None | Unset):
        paginacion (list[Ecf34Pagina] | None | Unset):
    """

    encabezado: Ecf34Encabezado
    detalles_items: list[Ecf34Item]
    informacion_referencia: Ecf34InformacionReferencia
    subtotales: list[Ecf34Subtotal] | None | Unset = UNSET
    descuentos_o_recargos: list[Ecf34DescuentoORecargo] | None | Unset = UNSET
    paginacion: list[Ecf34Pagina] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encabezado = self.encabezado.to_dict()

        detalles_items = []
        for detalles_items_item_data in self.detalles_items:
            detalles_items_item = detalles_items_item_data.to_dict()
            detalles_items.append(detalles_items_item)

        informacion_referencia = self.informacion_referencia.to_dict()

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

        descuentos_o_recargos: list[dict[str, Any]] | None | Unset
        if isinstance(self.descuentos_o_recargos, Unset):
            descuentos_o_recargos = UNSET
        elif isinstance(self.descuentos_o_recargos, list):
            descuentos_o_recargos = []
            for descuentos_o_recargos_type_1_item_data in self.descuentos_o_recargos:
                descuentos_o_recargos_type_1_item = descuentos_o_recargos_type_1_item_data.to_dict()
                descuentos_o_recargos.append(descuentos_o_recargos_type_1_item)

        else:
            descuentos_o_recargos = self.descuentos_o_recargos

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encabezado": encabezado,
                "detallesItems": detalles_items,
                "informacionReferencia": informacion_referencia,
            }
        )
        if subtotales is not UNSET:
            field_dict["subtotales"] = subtotales
        if descuentos_o_recargos is not UNSET:
            field_dict["descuentosORecargos"] = descuentos_o_recargos
        if paginacion is not UNSET:
            field_dict["paginacion"] = paginacion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_34_descuento_o_recargo import Ecf34DescuentoORecargo
        from ..models.ecf_34_encabezado import Ecf34Encabezado
        from ..models.ecf_34_informacion_referencia import Ecf34InformacionReferencia
        from ..models.ecf_34_item import Ecf34Item
        from ..models.ecf_34_pagina import Ecf34Pagina
        from ..models.ecf_34_subtotal import Ecf34Subtotal

        d = dict(src_dict)
        encabezado = Ecf34Encabezado.from_dict(d.pop("encabezado"))

        detalles_items = []
        _detalles_items = d.pop("detallesItems")
        for detalles_items_item_data in _detalles_items:
            detalles_items_item = Ecf34Item.from_dict(detalles_items_item_data)

            detalles_items.append(detalles_items_item)

        informacion_referencia = Ecf34InformacionReferencia.from_dict(d.pop("informacionReferencia"))

        def _parse_subtotales(data: object) -> list[Ecf34Subtotal] | None | Unset:
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
                    subtotales_type_1_item = Ecf34Subtotal.from_dict(subtotales_type_1_item_data)

                    subtotales_type_1.append(subtotales_type_1_item)

                return subtotales_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf34Subtotal] | None | Unset, data)

        subtotales = _parse_subtotales(d.pop("subtotales", UNSET))

        def _parse_descuentos_o_recargos(data: object) -> list[Ecf34DescuentoORecargo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                descuentos_o_recargos_type_1 = []
                _descuentos_o_recargos_type_1 = data
                for descuentos_o_recargos_type_1_item_data in _descuentos_o_recargos_type_1:
                    descuentos_o_recargos_type_1_item = Ecf34DescuentoORecargo.from_dict(
                        descuentos_o_recargos_type_1_item_data
                    )

                    descuentos_o_recargos_type_1.append(descuentos_o_recargos_type_1_item)

                return descuentos_o_recargos_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf34DescuentoORecargo] | None | Unset, data)

        descuentos_o_recargos = _parse_descuentos_o_recargos(d.pop("descuentosORecargos", UNSET))

        def _parse_paginacion(data: object) -> list[Ecf34Pagina] | None | Unset:
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
                    paginacion_type_1_item = Ecf34Pagina.from_dict(paginacion_type_1_item_data)

                    paginacion_type_1.append(paginacion_type_1_item)

                return paginacion_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf34Pagina] | None | Unset, data)

        paginacion = _parse_paginacion(d.pop("paginacion", UNSET))

        ecf_34ecf = cls(
            encabezado=encabezado,
            detalles_items=detalles_items,
            informacion_referencia=informacion_referencia,
            subtotales=subtotales,
            descuentos_o_recargos=descuentos_o_recargos,
            paginacion=paginacion,
        )

        ecf_34ecf.additional_properties = d
        return ecf_34ecf

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
