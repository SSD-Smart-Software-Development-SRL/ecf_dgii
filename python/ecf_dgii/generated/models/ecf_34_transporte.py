from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf34Transporte")



@_attrs_define
class Ecf34Transporte:
    """ 
        Attributes:
            conductor (None | str | Unset):
            documento_transporte (None | str | Unset):
            ficha (None | str | Unset):
            placa (None | str | Unset):
            ruta_transporte (None | str | Unset):
            zona_transporte (None | str | Unset):
            numero_albaran (None | str | Unset):
     """

    conductor: None | str | Unset = UNSET
    documento_transporte: None | str | Unset = UNSET
    ficha: None | str | Unset = UNSET
    placa: None | str | Unset = UNSET
    ruta_transporte: None | str | Unset = UNSET
    zona_transporte: None | str | Unset = UNSET
    numero_albaran: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        conductor: None | str | Unset
        if isinstance(self.conductor, Unset):
            conductor = UNSET
        else:
            conductor = self.conductor

        documento_transporte: None | str | Unset
        if isinstance(self.documento_transporte, Unset):
            documento_transporte = UNSET
        else:
            documento_transporte = self.documento_transporte

        ficha: None | str | Unset
        if isinstance(self.ficha, Unset):
            ficha = UNSET
        else:
            ficha = self.ficha

        placa: None | str | Unset
        if isinstance(self.placa, Unset):
            placa = UNSET
        else:
            placa = self.placa

        ruta_transporte: None | str | Unset
        if isinstance(self.ruta_transporte, Unset):
            ruta_transporte = UNSET
        else:
            ruta_transporte = self.ruta_transporte

        zona_transporte: None | str | Unset
        if isinstance(self.zona_transporte, Unset):
            zona_transporte = UNSET
        else:
            zona_transporte = self.zona_transporte

        numero_albaran: None | str | Unset
        if isinstance(self.numero_albaran, Unset):
            numero_albaran = UNSET
        else:
            numero_albaran = self.numero_albaran


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if conductor is not UNSET:
            field_dict["conductor"] = conductor
        if documento_transporte is not UNSET:
            field_dict["documentoTransporte"] = documento_transporte
        if ficha is not UNSET:
            field_dict["ficha"] = ficha
        if placa is not UNSET:
            field_dict["placa"] = placa
        if ruta_transporte is not UNSET:
            field_dict["rutaTransporte"] = ruta_transporte
        if zona_transporte is not UNSET:
            field_dict["zonaTransporte"] = zona_transporte
        if numero_albaran is not UNSET:
            field_dict["numeroAlbaran"] = numero_albaran

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_conductor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conductor = _parse_conductor(d.pop("conductor", UNSET))


        def _parse_documento_transporte(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documento_transporte = _parse_documento_transporte(d.pop("documentoTransporte", UNSET))


        def _parse_ficha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ficha = _parse_ficha(d.pop("ficha", UNSET))


        def _parse_placa(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        placa = _parse_placa(d.pop("placa", UNSET))


        def _parse_ruta_transporte(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ruta_transporte = _parse_ruta_transporte(d.pop("rutaTransporte", UNSET))


        def _parse_zona_transporte(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zona_transporte = _parse_zona_transporte(d.pop("zonaTransporte", UNSET))


        def _parse_numero_albaran(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_albaran = _parse_numero_albaran(d.pop("numeroAlbaran", UNSET))


        ecf_34_transporte = cls(
            conductor=conductor,
            documento_transporte=documento_transporte,
            ficha=ficha,
            placa=placa,
            ruta_transporte=ruta_transporte,
            zona_transporte=zona_transporte,
            numero_albaran=numero_albaran,
        )


        ecf_34_transporte.additional_properties = d
        return ecf_34_transporte

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
