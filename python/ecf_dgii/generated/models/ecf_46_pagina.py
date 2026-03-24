from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf46Pagina")



@_attrs_define
class Ecf46Pagina:
    """ 
        Example:
            {'subtotalItbisPagina': None, 'noLineaHasta': None, 'subtotalMontoGravadoPagina': None, 'paginaNo': None,
                'subtotalItbis3Pagina': None, 'montoSubtotalPagina': None, 'subtotalMontoNoFacturablePagina': None,
                'noLineaDesde': None, 'subtotalMontoGravado3Pagina': None}

        Attributes:
            pagina_no (int | None | str | Unset):
            no_linea_desde (int | None | str | Unset):
            no_linea_hasta (int | None | str | Unset):
            subtotal_monto_gravado_pagina (float | None | str | Unset):
            subtotal_monto_gravado_3_pagina (float | None | str | Unset):
            subtotal_itbis_pagina (float | None | str | Unset):
            subtotal_itbis_3_pagina (float | None | str | Unset):
            monto_subtotal_pagina (float | None | str | Unset):
            subtotal_monto_no_facturable_pagina (float | None | str | Unset):
     """

    pagina_no: int | None | str | Unset = UNSET
    no_linea_desde: int | None | str | Unset = UNSET
    no_linea_hasta: int | None | str | Unset = UNSET
    subtotal_monto_gravado_pagina: float | None | str | Unset = UNSET
    subtotal_monto_gravado_3_pagina: float | None | str | Unset = UNSET
    subtotal_itbis_pagina: float | None | str | Unset = UNSET
    subtotal_itbis_3_pagina: float | None | str | Unset = UNSET
    monto_subtotal_pagina: float | None | str | Unset = UNSET
    subtotal_monto_no_facturable_pagina: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        pagina_no: int | None | str | Unset
        if isinstance(self.pagina_no, Unset):
            pagina_no = UNSET
        else:
            pagina_no = self.pagina_no

        no_linea_desde: int | None | str | Unset
        if isinstance(self.no_linea_desde, Unset):
            no_linea_desde = UNSET
        else:
            no_linea_desde = self.no_linea_desde

        no_linea_hasta: int | None | str | Unset
        if isinstance(self.no_linea_hasta, Unset):
            no_linea_hasta = UNSET
        else:
            no_linea_hasta = self.no_linea_hasta

        subtotal_monto_gravado_pagina: float | None | str | Unset
        if isinstance(self.subtotal_monto_gravado_pagina, Unset):
            subtotal_monto_gravado_pagina = UNSET
        else:
            subtotal_monto_gravado_pagina = self.subtotal_monto_gravado_pagina

        subtotal_monto_gravado_3_pagina: float | None | str | Unset
        if isinstance(self.subtotal_monto_gravado_3_pagina, Unset):
            subtotal_monto_gravado_3_pagina = UNSET
        else:
            subtotal_monto_gravado_3_pagina = self.subtotal_monto_gravado_3_pagina

        subtotal_itbis_pagina: float | None | str | Unset
        if isinstance(self.subtotal_itbis_pagina, Unset):
            subtotal_itbis_pagina = UNSET
        else:
            subtotal_itbis_pagina = self.subtotal_itbis_pagina

        subtotal_itbis_3_pagina: float | None | str | Unset
        if isinstance(self.subtotal_itbis_3_pagina, Unset):
            subtotal_itbis_3_pagina = UNSET
        else:
            subtotal_itbis_3_pagina = self.subtotal_itbis_3_pagina

        monto_subtotal_pagina: float | None | str | Unset
        if isinstance(self.monto_subtotal_pagina, Unset):
            monto_subtotal_pagina = UNSET
        else:
            monto_subtotal_pagina = self.monto_subtotal_pagina

        subtotal_monto_no_facturable_pagina: float | None | str | Unset
        if isinstance(self.subtotal_monto_no_facturable_pagina, Unset):
            subtotal_monto_no_facturable_pagina = UNSET
        else:
            subtotal_monto_no_facturable_pagina = self.subtotal_monto_no_facturable_pagina


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pagina_no is not UNSET:
            field_dict["paginaNo"] = pagina_no
        if no_linea_desde is not UNSET:
            field_dict["noLineaDesde"] = no_linea_desde
        if no_linea_hasta is not UNSET:
            field_dict["noLineaHasta"] = no_linea_hasta
        if subtotal_monto_gravado_pagina is not UNSET:
            field_dict["subtotalMontoGravadoPagina"] = subtotal_monto_gravado_pagina
        if subtotal_monto_gravado_3_pagina is not UNSET:
            field_dict["subtotalMontoGravado3Pagina"] = subtotal_monto_gravado_3_pagina
        if subtotal_itbis_pagina is not UNSET:
            field_dict["subtotalItbisPagina"] = subtotal_itbis_pagina
        if subtotal_itbis_3_pagina is not UNSET:
            field_dict["subtotalItbis3Pagina"] = subtotal_itbis_3_pagina
        if monto_subtotal_pagina is not UNSET:
            field_dict["montoSubtotalPagina"] = monto_subtotal_pagina
        if subtotal_monto_no_facturable_pagina is not UNSET:
            field_dict["subtotalMontoNoFacturablePagina"] = subtotal_monto_no_facturable_pagina

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_pagina_no(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        pagina_no = _parse_pagina_no(d.pop("paginaNo", UNSET))


        def _parse_no_linea_desde(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        no_linea_desde = _parse_no_linea_desde(d.pop("noLineaDesde", UNSET))


        def _parse_no_linea_hasta(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        no_linea_hasta = _parse_no_linea_hasta(d.pop("noLineaHasta", UNSET))


        def _parse_subtotal_monto_gravado_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_monto_gravado_pagina = _parse_subtotal_monto_gravado_pagina(d.pop("subtotalMontoGravadoPagina", UNSET))


        def _parse_subtotal_monto_gravado_3_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_monto_gravado_3_pagina = _parse_subtotal_monto_gravado_3_pagina(d.pop("subtotalMontoGravado3Pagina", UNSET))


        def _parse_subtotal_itbis_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_itbis_pagina = _parse_subtotal_itbis_pagina(d.pop("subtotalItbisPagina", UNSET))


        def _parse_subtotal_itbis_3_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_itbis_3_pagina = _parse_subtotal_itbis_3_pagina(d.pop("subtotalItbis3Pagina", UNSET))


        def _parse_monto_subtotal_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_subtotal_pagina = _parse_monto_subtotal_pagina(d.pop("montoSubtotalPagina", UNSET))


        def _parse_subtotal_monto_no_facturable_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_monto_no_facturable_pagina = _parse_subtotal_monto_no_facturable_pagina(d.pop("subtotalMontoNoFacturablePagina", UNSET))


        ecf_46_pagina = cls(
            pagina_no=pagina_no,
            no_linea_desde=no_linea_desde,
            no_linea_hasta=no_linea_hasta,
            subtotal_monto_gravado_pagina=subtotal_monto_gravado_pagina,
            subtotal_monto_gravado_3_pagina=subtotal_monto_gravado_3_pagina,
            subtotal_itbis_pagina=subtotal_itbis_pagina,
            subtotal_itbis_3_pagina=subtotal_itbis_3_pagina,
            monto_subtotal_pagina=monto_subtotal_pagina,
            subtotal_monto_no_facturable_pagina=subtotal_monto_no_facturable_pagina,
        )


        ecf_46_pagina.additional_properties = d
        return ecf_46_pagina

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
