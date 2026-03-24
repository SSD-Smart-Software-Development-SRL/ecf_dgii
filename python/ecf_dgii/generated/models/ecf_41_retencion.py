from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_41_indicador_agente_retenciono_percepcion_type import Ecf41IndicadorAgenteRetencionoPercepcionType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf41Retencion")



@_attrs_define
class Ecf41Retencion:
    """ 
        Example:
            {'montoITBISRetenido': None, 'montoISRRetenido': None, 'indicadorAgenteRetencionoPercepcion': 'Retencion'}

        Attributes:
            indicador_agente_retenciono_percepcion (Ecf41IndicadorAgenteRetencionoPercepcionType):
            monto_itbis_retenido (float | None | str | Unset):
            monto_isr_retenido (float | None | str | Unset):
     """

    indicador_agente_retenciono_percepcion: Ecf41IndicadorAgenteRetencionoPercepcionType
    monto_itbis_retenido: float | None | str | Unset = UNSET
    monto_isr_retenido: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        indicador_agente_retenciono_percepcion = self.indicador_agente_retenciono_percepcion.value

        monto_itbis_retenido: float | None | str | Unset
        if isinstance(self.monto_itbis_retenido, Unset):
            monto_itbis_retenido = UNSET
        else:
            monto_itbis_retenido = self.monto_itbis_retenido

        monto_isr_retenido: float | None | str | Unset
        if isinstance(self.monto_isr_retenido, Unset):
            monto_isr_retenido = UNSET
        else:
            monto_isr_retenido = self.monto_isr_retenido


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "indicadorAgenteRetencionoPercepcion": indicador_agente_retenciono_percepcion,
        })
        if monto_itbis_retenido is not UNSET:
            field_dict["montoITBISRetenido"] = monto_itbis_retenido
        if monto_isr_retenido is not UNSET:
            field_dict["montoISRRetenido"] = monto_isr_retenido

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indicador_agente_retenciono_percepcion = Ecf41IndicadorAgenteRetencionoPercepcionType(d.pop("indicadorAgenteRetencionoPercepcion"))




        def _parse_monto_itbis_retenido(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_itbis_retenido = _parse_monto_itbis_retenido(d.pop("montoITBISRetenido", UNSET))


        def _parse_monto_isr_retenido(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        monto_isr_retenido = _parse_monto_isr_retenido(d.pop("montoISRRetenido", UNSET))


        ecf_41_retencion = cls(
            indicador_agente_retenciono_percepcion=indicador_agente_retenciono_percepcion,
            monto_itbis_retenido=monto_itbis_retenido,
            monto_isr_retenido=monto_isr_retenido,
        )


        ecf_41_retencion.additional_properties = d
        return ecf_41_retencion

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
