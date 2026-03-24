from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.via_transporte_type_type_1 import ViaTransporteTypeType1
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Ecf46Transporte")



@_attrs_define
class Ecf46Transporte:
    """ 
        Attributes:
            via_transporte (None | Unset | ViaTransporteTypeType1):
            pais_origen (None | str | Unset):
            direccion_destino (None | str | Unset):
            pais_destino (None | str | Unset):
            rnc_identificacion_compania_transportista (None | str | Unset):
            nombre_compania_transportista (None | str | Unset):
            numero_viaje (None | str | Unset):
            conductor (None | str | Unset):
            documento_transporte (None | str | Unset):
            ficha (None | str | Unset):
            placa (None | str | Unset):
            ruta_transporte (None | str | Unset):
            zona_transporte (None | str | Unset):
            numero_albaran (None | str | Unset):
     """

    via_transporte: None | Unset | ViaTransporteTypeType1 = UNSET
    pais_origen: None | str | Unset = UNSET
    direccion_destino: None | str | Unset = UNSET
    pais_destino: None | str | Unset = UNSET
    rnc_identificacion_compania_transportista: None | str | Unset = UNSET
    nombre_compania_transportista: None | str | Unset = UNSET
    numero_viaje: None | str | Unset = UNSET
    conductor: None | str | Unset = UNSET
    documento_transporte: None | str | Unset = UNSET
    ficha: None | str | Unset = UNSET
    placa: None | str | Unset = UNSET
    ruta_transporte: None | str | Unset = UNSET
    zona_transporte: None | str | Unset = UNSET
    numero_albaran: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        via_transporte: None | str | Unset
        if isinstance(self.via_transporte, Unset):
            via_transporte = UNSET
        elif isinstance(self.via_transporte, ViaTransporteTypeType1):
            via_transporte = self.via_transporte.value
        else:
            via_transporte = self.via_transporte

        pais_origen: None | str | Unset
        if isinstance(self.pais_origen, Unset):
            pais_origen = UNSET
        else:
            pais_origen = self.pais_origen

        direccion_destino: None | str | Unset
        if isinstance(self.direccion_destino, Unset):
            direccion_destino = UNSET
        else:
            direccion_destino = self.direccion_destino

        pais_destino: None | str | Unset
        if isinstance(self.pais_destino, Unset):
            pais_destino = UNSET
        else:
            pais_destino = self.pais_destino

        rnc_identificacion_compania_transportista: None | str | Unset
        if isinstance(self.rnc_identificacion_compania_transportista, Unset):
            rnc_identificacion_compania_transportista = UNSET
        else:
            rnc_identificacion_compania_transportista = self.rnc_identificacion_compania_transportista

        nombre_compania_transportista: None | str | Unset
        if isinstance(self.nombre_compania_transportista, Unset):
            nombre_compania_transportista = UNSET
        else:
            nombre_compania_transportista = self.nombre_compania_transportista

        numero_viaje: None | str | Unset
        if isinstance(self.numero_viaje, Unset):
            numero_viaje = UNSET
        else:
            numero_viaje = self.numero_viaje

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
        if via_transporte is not UNSET:
            field_dict["viaTransporte"] = via_transporte
        if pais_origen is not UNSET:
            field_dict["paisOrigen"] = pais_origen
        if direccion_destino is not UNSET:
            field_dict["direccionDestino"] = direccion_destino
        if pais_destino is not UNSET:
            field_dict["paisDestino"] = pais_destino
        if rnc_identificacion_compania_transportista is not UNSET:
            field_dict["rncIdentificacionCompaniaTransportista"] = rnc_identificacion_compania_transportista
        if nombre_compania_transportista is not UNSET:
            field_dict["nombreCompaniaTransportista"] = nombre_compania_transportista
        if numero_viaje is not UNSET:
            field_dict["numeroViaje"] = numero_viaje
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
        def _parse_via_transporte(data: object) -> None | Unset | ViaTransporteTypeType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_via_transporte_type_type_1 = ViaTransporteTypeType1(data)



                return componentsschemas_via_transporte_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ViaTransporteTypeType1, data)

        via_transporte = _parse_via_transporte(d.pop("viaTransporte", UNSET))


        def _parse_pais_origen(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pais_origen = _parse_pais_origen(d.pop("paisOrigen", UNSET))


        def _parse_direccion_destino(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direccion_destino = _parse_direccion_destino(d.pop("direccionDestino", UNSET))


        def _parse_pais_destino(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pais_destino = _parse_pais_destino(d.pop("paisDestino", UNSET))


        def _parse_rnc_identificacion_compania_transportista(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_identificacion_compania_transportista = _parse_rnc_identificacion_compania_transportista(d.pop("rncIdentificacionCompaniaTransportista", UNSET))


        def _parse_nombre_compania_transportista(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nombre_compania_transportista = _parse_nombre_compania_transportista(d.pop("nombreCompaniaTransportista", UNSET))


        def _parse_numero_viaje(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_viaje = _parse_numero_viaje(d.pop("numeroViaje", UNSET))


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


        ecf_46_transporte = cls(
            via_transporte=via_transporte,
            pais_origen=pais_origen,
            direccion_destino=direccion_destino,
            pais_destino=pais_destino,
            rnc_identificacion_compania_transportista=rnc_identificacion_compania_transportista,
            nombre_compania_transportista=nombre_compania_transportista,
            numero_viaje=numero_viaje,
            conductor=conductor,
            documento_transporte=documento_transporte,
            ficha=ficha,
            placa=placa,
            ruta_transporte=ruta_transporte,
            zona_transporte=zona_transporte,
            numero_albaran=numero_albaran,
        )


        ecf_46_transporte.additional_properties = d
        return ecf_46_transporte

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
