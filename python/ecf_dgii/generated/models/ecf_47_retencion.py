from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_47_indicador_agente_retenciono_percepcion_type import Ecf47IndicadorAgenteRetencionoPercepcionType
from typing import cast






T = TypeVar("T", bound="Ecf47Retencion")



@_attrs_define
class Ecf47Retencion:
    """ 
        Example:
            {'montoISRRetenido': None, 'indicadorAgenteRetencionoPercepcion': 'Retencion'}

        Attributes:
            indicador_agente_retenciono_percepcion (Ecf47IndicadorAgenteRetencionoPercepcionType):
            monto_isr_retenido (float | str):
     """

    indicador_agente_retenciono_percepcion: Ecf47IndicadorAgenteRetencionoPercepcionType
    monto_isr_retenido: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        indicador_agente_retenciono_percepcion = self.indicador_agente_retenciono_percepcion.value

        monto_isr_retenido: float | str
        monto_isr_retenido = self.monto_isr_retenido


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "indicadorAgenteRetencionoPercepcion": indicador_agente_retenciono_percepcion,
            "montoISRRetenido": monto_isr_retenido,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indicador_agente_retenciono_percepcion = Ecf47IndicadorAgenteRetencionoPercepcionType(d.pop("indicadorAgenteRetencionoPercepcion"))




        def _parse_monto_isr_retenido(data: object) -> float | str:
            return cast(float | str, data)

        monto_isr_retenido = _parse_monto_isr_retenido(d.pop("montoISRRetenido"))


        ecf_47_retencion = cls(
            indicador_agente_retenciono_percepcion=indicador_agente_retenciono_percepcion,
            monto_isr_retenido=monto_isr_retenido,
        )


        ecf_47_retencion.additional_properties = d
        return ecf_47_retencion

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
