from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_34_tipo_ajuste_type import Ecf34TipoAjusteType
from ..models.indicador_facturacion_dr_type_type_1 import IndicadorFacturacionDRTypeType1
from ..models.indicador_norma_1007_type_type_1 import IndicadorNorma1007TypeType1
from ..models.tipo_descuento_recargo_type_type_1 import TipoDescuentoRecargoTypeType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf34DescuentoORecargo")



@_attrs_define
class Ecf34DescuentoORecargo:
    """ 
        Example:
            {'numeroLinea': None, 'montoDescuentooRecargo': None, 'descripcionDescuentooRecargo':
                'descripcionDescuentooRecargo', 'indicadorNorma1007': '', 'indicadorFacturacionDescuentooRecargo': '',
                'tipoAjuste': 'D', 'tipoValor': '', 'valorDescuentooRecargo': None, 'montoDescuentooRecargoOtraMoneda': None}

        Attributes:
            numero_linea (int | str):
            tipo_ajuste (Ecf34TipoAjusteType):
            indicador_norma_1007 (IndicadorNorma1007TypeType1 | None | Unset):
            descripcion_descuentoo_recargo (None | str | Unset):
            tipo_valor (None | TipoDescuentoRecargoTypeType1 | Unset):
            valor_descuentoo_recargo (float | None | str | Unset):
            monto_descuentoo_recargo (float | None | str | Unset):
            monto_descuentoo_recargo_otra_moneda (float | None | str | Unset):
            indicador_facturacion_descuentoo_recargo (IndicadorFacturacionDRTypeType1 | None | Unset):
     """

    numero_linea: int | str
    tipo_ajuste: Ecf34TipoAjusteType
    indicador_norma_1007: IndicadorNorma1007TypeType1 | None | Unset = UNSET
    descripcion_descuentoo_recargo: None | str | Unset = UNSET
    tipo_valor: None | TipoDescuentoRecargoTypeType1 | Unset = UNSET
    valor_descuentoo_recargo: float | None | str | Unset = UNSET
    monto_descuentoo_recargo: float | None | str | Unset = UNSET
    monto_descuentoo_recargo_otra_moneda: float | None | str | Unset = UNSET
    indicador_facturacion_descuentoo_recargo: IndicadorFacturacionDRTypeType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        numero_linea: int | str
        numero_linea = self.numero_linea

        tipo_ajuste = self.tipo_ajuste.value

        indicador_norma_1007: None | str | Unset
        if isinstance(self.indicador_norma_1007, Unset):
            indicador_norma_1007 = UNSET
        elif isinstance(self.indicador_norma_1007, IndicadorNorma1007TypeType1):
            indicador_norma_1007 = self.indicador_norma_1007.value
        else:
            indicador_norma_1007 = self.indicador_norma_1007

        descripcion_descuentoo_recargo: None | str | Unset
        if isinstance(self.descripcion_descuentoo_recargo, Unset):
            descripcion_descuentoo_recargo = UNSET
        else:
            descripcion_descuentoo_recargo = self.descripcion_descuentoo_recargo

        tipo_valor: None | str | Unset
        if isinstance(self.tipo_valor, Unset):
            tipo_valor = UNSET
        elif isinstance(self.tipo_valor, TipoDescuentoRecargoTypeType1):
            tipo_valor = self.tipo_valor.value
        else:
            tipo_valor = self.tipo_valor

        valor_descuentoo_recargo: float | None | str | Unset
        if isinstance(self.valor_descuentoo_recargo, Unset):
            valor_descuentoo_recargo = UNSET
        else:
            valor_descuentoo_recargo = self.valor_descuentoo_recargo

        monto_descuentoo_recargo: float | None | str | Unset
        if isinstance(self.monto_descuentoo_recargo, Unset):
            monto_descuentoo_recargo = UNSET
        else:
            monto_descuentoo_recargo = self.monto_descuentoo_recargo

        monto_descuentoo_recargo_otra_moneda: float | None | str | Unset
        if isinstance(self.monto_descuentoo_recargo_otra_moneda, Unset):
            monto_descuentoo_recargo_otra_moneda = UNSET
        else:
            monto_descuentoo_recargo_otra_moneda = self.monto_descuentoo_recargo_otra_moneda

        indicador_facturacion_descuentoo_recargo: None | str | Unset
        if isinstance(self.indicador_facturacion_descuentoo_recargo, Unset):
            indicador_facturacion_descuentoo_recargo = UNSET
        elif isinstance(self.indicador_facturacion_descuentoo_recargo, IndicadorFacturacionDRTypeType1):
            indicador_facturacion_descuentoo_recargo = self.indicador_facturacion_descuentoo_recargo.value
        else:
            indicador_facturacion_descuentoo_recargo = self.indicador_facturacion_descuentoo_recargo


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "numeroLinea": numero_linea,
            "tipoAjuste": tipo_ajuste,
        })
        if indicador_norma_1007 is not UNSET:
            field_dict["indicadorNorma1007"] = indicador_norma_1007
        if descripcion_descuentoo_recargo is not UNSET:
            field_dict["descripcionDescuentooRecargo"] = descripcion_descuentoo_recargo
        if tipo_valor is not UNSET:
            field_dict["tipoValor"] = tipo_valor
        if valor_descuentoo_recargo is not UNSET:
            field_dict["valorDescuentooRecargo"] = valor_descuentoo_recargo
        if monto_descuentoo_recargo is not UNSET:
            field_dict["montoDescuentooRecargo"] = monto_descuentoo_recargo
        if monto_descuentoo_recargo_otra_moneda is not UNSET:
            field_dict["montoDescuentooRecargoOtraMoneda"] = monto_descuentoo_recargo_otra_moneda
        if indicador_facturacion_descuentoo_recargo is not UNSET:
            field_dict["indicadorFacturacionDescuentooRecargo"] = indicador_facturacion_descuentoo_recargo

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_numero_linea(data: object) -> int | str:
            return cast(int | str, data)

        numero_linea = _parse_numero_linea(d.pop("numeroLinea"))


        tipo_ajuste = Ecf34TipoAjusteType(d.pop("tipoAjuste"))




        def _parse_indicador_norma_1007(data: object) -> IndicadorNorma1007TypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_indicador_norma_1007_type_type_1 = IndicadorNorma1007TypeType1(data)



                return componentsschemas_indicador_norma_1007_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IndicadorNorma1007TypeType1 | None | Unset, data)

        indicador_norma_1007 = _parse_indicador_norma_1007(d.pop("indicadorNorma1007", UNSET))


        def _parse_descripcion_descuentoo_recargo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descripcion_descuentoo_recargo = _parse_descripcion_descuentoo_recargo(d.pop("descripcionDescuentooRecargo", UNSET))


        def _parse_tipo_valor(data: object) -> None | TipoDescuentoRecargoTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_tipo_descuento_recargo_type_type_1 = TipoDescuentoRecargoTypeType1(data)



                return componentsschemas_tipo_descuento_recargo_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TipoDescuentoRecargoTypeType1 | Unset, data)

        tipo_valor = _parse_tipo_valor(d.pop("tipoValor", UNSET))


        def _parse_valor_descuentoo_recargo(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        valor_descuentoo_recargo = _parse_valor_descuentoo_recargo(d.pop("valorDescuentooRecargo", UNSET))


        def _parse_monto_descuentoo_recargo(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_descuentoo_recargo = _parse_monto_descuentoo_recargo(d.pop("montoDescuentooRecargo", UNSET))


        def _parse_monto_descuentoo_recargo_otra_moneda(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_descuentoo_recargo_otra_moneda = _parse_monto_descuentoo_recargo_otra_moneda(d.pop("montoDescuentooRecargoOtraMoneda", UNSET))


        def _parse_indicador_facturacion_descuentoo_recargo(data: object) -> IndicadorFacturacionDRTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_indicador_facturacion_dr_type_type_1 = IndicadorFacturacionDRTypeType1(data)



                return componentsschemas_indicador_facturacion_dr_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IndicadorFacturacionDRTypeType1 | None | Unset, data)

        indicador_facturacion_descuentoo_recargo = _parse_indicador_facturacion_descuentoo_recargo(d.pop("indicadorFacturacionDescuentooRecargo", UNSET))


        ecf_34_descuento_o_recargo = cls(
            numero_linea=numero_linea,
            tipo_ajuste=tipo_ajuste,
            indicador_norma_1007=indicador_norma_1007,
            descripcion_descuentoo_recargo=descripcion_descuentoo_recargo,
            tipo_valor=tipo_valor,
            valor_descuentoo_recargo=valor_descuentoo_recargo,
            monto_descuentoo_recargo=monto_descuentoo_recargo,
            monto_descuentoo_recargo_otra_moneda=monto_descuentoo_recargo_otra_moneda,
            indicador_facturacion_descuentoo_recargo=indicador_facturacion_descuentoo_recargo,
        )


        ecf_34_descuento_o_recargo.additional_properties = d
        return ecf_34_descuento_o_recargo

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
