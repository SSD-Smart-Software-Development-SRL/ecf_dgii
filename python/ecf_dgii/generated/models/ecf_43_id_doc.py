from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tipo_pago_type_type_1 import TipoPagoTypeType1
from ..models.tipoe_cf_type import TipoeCFType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Ecf43IdDoc")



@_attrs_define
class Ecf43IdDoc:
    """ 
        Example:
            {'encf': 'encf', 'tipoeCF': 'FacturaDeCreditoFiscalElectronica', 'tipoPago': '', 'totalPaginas': 0,
                'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}

        Attributes:
            tipoe_cf (TipoeCFType):
            encf (str):
            fecha_vencimiento_secuencia (datetime.datetime | Unset):
            tipo_pago (None | TipoPagoTypeType1 | Unset):
            total_paginas (int | None | str | Unset):
     """

    tipoe_cf: TipoeCFType
    encf: str
    fecha_vencimiento_secuencia: datetime.datetime | Unset = UNSET
    tipo_pago: None | TipoPagoTypeType1 | Unset = UNSET
    total_paginas: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipoe_cf = self.tipoe_cf.value

        encf = self.encf

        fecha_vencimiento_secuencia: str | Unset = UNSET
        if not isinstance(self.fecha_vencimiento_secuencia, Unset):
            fecha_vencimiento_secuencia = self.fecha_vencimiento_secuencia.isoformat()

        tipo_pago: None | str | Unset
        if isinstance(self.tipo_pago, Unset):
            tipo_pago = UNSET
        elif isinstance(self.tipo_pago, TipoPagoTypeType1):
            tipo_pago = self.tipo_pago.value
        else:
            tipo_pago = self.tipo_pago

        total_paginas: int | None | str | Unset
        if isinstance(self.total_paginas, Unset):
            total_paginas = UNSET
        else:
            total_paginas = self.total_paginas


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tipoeCF": tipoe_cf,
            "encf": encf,
        })
        if fecha_vencimiento_secuencia is not UNSET:
            field_dict["fechaVencimientoSecuencia"] = fecha_vencimiento_secuencia
        if tipo_pago is not UNSET:
            field_dict["tipoPago"] = tipo_pago
        if total_paginas is not UNSET:
            field_dict["totalPaginas"] = total_paginas

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tipoe_cf = TipoeCFType(d.pop("tipoeCF"))




        encf = d.pop("encf")

        _fecha_vencimiento_secuencia = d.pop("fechaVencimientoSecuencia", UNSET)
        fecha_vencimiento_secuencia: datetime.datetime | Unset
        if isinstance(_fecha_vencimiento_secuencia,  Unset):
            fecha_vencimiento_secuencia = UNSET
        else:
            fecha_vencimiento_secuencia = isoparse(_fecha_vencimiento_secuencia)




        def _parse_tipo_pago(data: object) -> None | TipoPagoTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_tipo_pago_type_type_1 = TipoPagoTypeType1(data)



                return componentsschemas_tipo_pago_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TipoPagoTypeType1 | Unset, data)

        tipo_pago = _parse_tipo_pago(d.pop("tipoPago", UNSET))


        def _parse_total_paginas(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        total_paginas = _parse_total_paginas(d.pop("totalPaginas", UNSET))


        ecf_43_id_doc = cls(
            tipoe_cf=tipoe_cf,
            encf=encf,
            fecha_vencimiento_secuencia=fecha_vencimiento_secuencia,
            tipo_pago=tipo_pago,
            total_paginas=total_paginas,
        )


        ecf_43_id_doc.additional_properties = d
        return ecf_43_id_doc

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
