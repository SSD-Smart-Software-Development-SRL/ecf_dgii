from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_33_subtotal_impuesto_adicional import Ecf33SubtotalImpuestoAdicional





T = TypeVar("T", bound="Ecf33Pagina")



@_attrs_define
class Ecf33Pagina:
    """ 
        Example:
            {'subtotalItbis1Pagina': None, 'noLineaHasta': None, 'subtotalImpuestoAdicionalPagina': None,
                'subtotalMontoGravado2Pagina': None, 'subtotalMontoGravadoPagina': None, 'subtotalMontoNoFacturablePagina':
                None, 'subtotalMontoGravado1Pagina': None, 'subtotalImpuestoAdicional': '', 'noLineaDesde': None,
                'subtotalItbisPagina': None, 'paginaNo': None, 'subtotalItbis3Pagina': None, 'subtotalItbis2Pagina': None,
                'montoSubtotalPagina': None, 'subtotalExentoPagina': None, 'subtotalMontoGravado3Pagina': None}

        Attributes:
            pagina_no (int | None | str | Unset):
            no_linea_desde (int | None | str | Unset):
            no_linea_hasta (int | None | str | Unset):
            subtotal_monto_gravado_pagina (float | None | str | Unset):
            subtotal_monto_gravado_1_pagina (float | None | str | Unset):
            subtotal_monto_gravado_2_pagina (float | None | str | Unset):
            subtotal_monto_gravado_3_pagina (float | None | str | Unset):
            subtotal_exento_pagina (float | None | str | Unset):
            subtotal_itbis_pagina (float | None | str | Unset):
            subtotal_itbis_1_pagina (float | None | str | Unset):
            subtotal_itbis_2_pagina (float | None | str | Unset):
            subtotal_itbis_3_pagina (float | None | str | Unset):
            subtotal_impuesto_adicional_pagina (float | None | str | Unset):
            subtotal_impuesto_adicional (Ecf33SubtotalImpuestoAdicional | None | Unset):
            monto_subtotal_pagina (float | None | str | Unset):
            subtotal_monto_no_facturable_pagina (float | None | str | Unset):
     """

    pagina_no: int | None | str | Unset = UNSET
    no_linea_desde: int | None | str | Unset = UNSET
    no_linea_hasta: int | None | str | Unset = UNSET
    subtotal_monto_gravado_pagina: float | None | str | Unset = UNSET
    subtotal_monto_gravado_1_pagina: float | None | str | Unset = UNSET
    subtotal_monto_gravado_2_pagina: float | None | str | Unset = UNSET
    subtotal_monto_gravado_3_pagina: float | None | str | Unset = UNSET
    subtotal_exento_pagina: float | None | str | Unset = UNSET
    subtotal_itbis_pagina: float | None | str | Unset = UNSET
    subtotal_itbis_1_pagina: float | None | str | Unset = UNSET
    subtotal_itbis_2_pagina: float | None | str | Unset = UNSET
    subtotal_itbis_3_pagina: float | None | str | Unset = UNSET
    subtotal_impuesto_adicional_pagina: float | None | str | Unset = UNSET
    subtotal_impuesto_adicional: Ecf33SubtotalImpuestoAdicional | None | Unset = UNSET
    monto_subtotal_pagina: float | None | str | Unset = UNSET
    subtotal_monto_no_facturable_pagina: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_33_subtotal_impuesto_adicional import Ecf33SubtotalImpuestoAdicional
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

        subtotal_monto_gravado_1_pagina: float | None | str | Unset
        if isinstance(self.subtotal_monto_gravado_1_pagina, Unset):
            subtotal_monto_gravado_1_pagina = UNSET
        else:
            subtotal_monto_gravado_1_pagina = self.subtotal_monto_gravado_1_pagina

        subtotal_monto_gravado_2_pagina: float | None | str | Unset
        if isinstance(self.subtotal_monto_gravado_2_pagina, Unset):
            subtotal_monto_gravado_2_pagina = UNSET
        else:
            subtotal_monto_gravado_2_pagina = self.subtotal_monto_gravado_2_pagina

        subtotal_monto_gravado_3_pagina: float | None | str | Unset
        if isinstance(self.subtotal_monto_gravado_3_pagina, Unset):
            subtotal_monto_gravado_3_pagina = UNSET
        else:
            subtotal_monto_gravado_3_pagina = self.subtotal_monto_gravado_3_pagina

        subtotal_exento_pagina: float | None | str | Unset
        if isinstance(self.subtotal_exento_pagina, Unset):
            subtotal_exento_pagina = UNSET
        else:
            subtotal_exento_pagina = self.subtotal_exento_pagina

        subtotal_itbis_pagina: float | None | str | Unset
        if isinstance(self.subtotal_itbis_pagina, Unset):
            subtotal_itbis_pagina = UNSET
        else:
            subtotal_itbis_pagina = self.subtotal_itbis_pagina

        subtotal_itbis_1_pagina: float | None | str | Unset
        if isinstance(self.subtotal_itbis_1_pagina, Unset):
            subtotal_itbis_1_pagina = UNSET
        else:
            subtotal_itbis_1_pagina = self.subtotal_itbis_1_pagina

        subtotal_itbis_2_pagina: float | None | str | Unset
        if isinstance(self.subtotal_itbis_2_pagina, Unset):
            subtotal_itbis_2_pagina = UNSET
        else:
            subtotal_itbis_2_pagina = self.subtotal_itbis_2_pagina

        subtotal_itbis_3_pagina: float | None | str | Unset
        if isinstance(self.subtotal_itbis_3_pagina, Unset):
            subtotal_itbis_3_pagina = UNSET
        else:
            subtotal_itbis_3_pagina = self.subtotal_itbis_3_pagina

        subtotal_impuesto_adicional_pagina: float | None | str | Unset
        if isinstance(self.subtotal_impuesto_adicional_pagina, Unset):
            subtotal_impuesto_adicional_pagina = UNSET
        else:
            subtotal_impuesto_adicional_pagina = self.subtotal_impuesto_adicional_pagina

        subtotal_impuesto_adicional: dict[str, Any] | None | Unset
        if isinstance(self.subtotal_impuesto_adicional, Unset):
            subtotal_impuesto_adicional = UNSET
        elif isinstance(self.subtotal_impuesto_adicional, Ecf33SubtotalImpuestoAdicional):
            subtotal_impuesto_adicional = self.subtotal_impuesto_adicional.to_dict()
        else:
            subtotal_impuesto_adicional = self.subtotal_impuesto_adicional

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
        if subtotal_monto_gravado_1_pagina is not UNSET:
            field_dict["subtotalMontoGravado1Pagina"] = subtotal_monto_gravado_1_pagina
        if subtotal_monto_gravado_2_pagina is not UNSET:
            field_dict["subtotalMontoGravado2Pagina"] = subtotal_monto_gravado_2_pagina
        if subtotal_monto_gravado_3_pagina is not UNSET:
            field_dict["subtotalMontoGravado3Pagina"] = subtotal_monto_gravado_3_pagina
        if subtotal_exento_pagina is not UNSET:
            field_dict["subtotalExentoPagina"] = subtotal_exento_pagina
        if subtotal_itbis_pagina is not UNSET:
            field_dict["subtotalItbisPagina"] = subtotal_itbis_pagina
        if subtotal_itbis_1_pagina is not UNSET:
            field_dict["subtotalItbis1Pagina"] = subtotal_itbis_1_pagina
        if subtotal_itbis_2_pagina is not UNSET:
            field_dict["subtotalItbis2Pagina"] = subtotal_itbis_2_pagina
        if subtotal_itbis_3_pagina is not UNSET:
            field_dict["subtotalItbis3Pagina"] = subtotal_itbis_3_pagina
        if subtotal_impuesto_adicional_pagina is not UNSET:
            field_dict["subtotalImpuestoAdicionalPagina"] = subtotal_impuesto_adicional_pagina
        if subtotal_impuesto_adicional is not UNSET:
            field_dict["subtotalImpuestoAdicional"] = subtotal_impuesto_adicional
        if monto_subtotal_pagina is not UNSET:
            field_dict["montoSubtotalPagina"] = monto_subtotal_pagina
        if subtotal_monto_no_facturable_pagina is not UNSET:
            field_dict["subtotalMontoNoFacturablePagina"] = subtotal_monto_no_facturable_pagina

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_33_subtotal_impuesto_adicional import Ecf33SubtotalImpuestoAdicional
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


        def _parse_subtotal_monto_gravado_1_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_monto_gravado_1_pagina = _parse_subtotal_monto_gravado_1_pagina(d.pop("subtotalMontoGravado1Pagina", UNSET))


        def _parse_subtotal_monto_gravado_2_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_monto_gravado_2_pagina = _parse_subtotal_monto_gravado_2_pagina(d.pop("subtotalMontoGravado2Pagina", UNSET))


        def _parse_subtotal_monto_gravado_3_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_monto_gravado_3_pagina = _parse_subtotal_monto_gravado_3_pagina(d.pop("subtotalMontoGravado3Pagina", UNSET))


        def _parse_subtotal_exento_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_exento_pagina = _parse_subtotal_exento_pagina(d.pop("subtotalExentoPagina", UNSET))


        def _parse_subtotal_itbis_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_itbis_pagina = _parse_subtotal_itbis_pagina(d.pop("subtotalItbisPagina", UNSET))


        def _parse_subtotal_itbis_1_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_itbis_1_pagina = _parse_subtotal_itbis_1_pagina(d.pop("subtotalItbis1Pagina", UNSET))


        def _parse_subtotal_itbis_2_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_itbis_2_pagina = _parse_subtotal_itbis_2_pagina(d.pop("subtotalItbis2Pagina", UNSET))


        def _parse_subtotal_itbis_3_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_itbis_3_pagina = _parse_subtotal_itbis_3_pagina(d.pop("subtotalItbis3Pagina", UNSET))


        def _parse_subtotal_impuesto_adicional_pagina(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        subtotal_impuesto_adicional_pagina = _parse_subtotal_impuesto_adicional_pagina(d.pop("subtotalImpuestoAdicionalPagina", UNSET))


        def _parse_subtotal_impuesto_adicional(data: object) -> Ecf33SubtotalImpuestoAdicional | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subtotal_impuesto_adicional_type_1 = Ecf33SubtotalImpuestoAdicional.from_dict(data)



                return subtotal_impuesto_adicional_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf33SubtotalImpuestoAdicional | None | Unset, data)

        subtotal_impuesto_adicional = _parse_subtotal_impuesto_adicional(d.pop("subtotalImpuestoAdicional", UNSET))


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


        ecf_33_pagina = cls(
            pagina_no=pagina_no,
            no_linea_desde=no_linea_desde,
            no_linea_hasta=no_linea_hasta,
            subtotal_monto_gravado_pagina=subtotal_monto_gravado_pagina,
            subtotal_monto_gravado_1_pagina=subtotal_monto_gravado_1_pagina,
            subtotal_monto_gravado_2_pagina=subtotal_monto_gravado_2_pagina,
            subtotal_monto_gravado_3_pagina=subtotal_monto_gravado_3_pagina,
            subtotal_exento_pagina=subtotal_exento_pagina,
            subtotal_itbis_pagina=subtotal_itbis_pagina,
            subtotal_itbis_1_pagina=subtotal_itbis_1_pagina,
            subtotal_itbis_2_pagina=subtotal_itbis_2_pagina,
            subtotal_itbis_3_pagina=subtotal_itbis_3_pagina,
            subtotal_impuesto_adicional_pagina=subtotal_impuesto_adicional_pagina,
            subtotal_impuesto_adicional=subtotal_impuesto_adicional,
            monto_subtotal_pagina=monto_subtotal_pagina,
            subtotal_monto_no_facturable_pagina=subtotal_monto_no_facturable_pagina,
        )


        ecf_33_pagina.additional_properties = d
        return ecf_33_pagina

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
