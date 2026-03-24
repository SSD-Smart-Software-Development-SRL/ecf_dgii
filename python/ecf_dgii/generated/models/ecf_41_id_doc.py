from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.indicador_monto_gravado_type_type_1 import IndicadorMontoGravadoTypeType1
from ..models.tipo_cuenta_pago_type_type_1 import TipoCuentaPagoTypeType1
from ..models.tipo_pago_type_type_1 import TipoPagoTypeType1
from ..models.tipoe_cf_type import TipoeCFType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.ecf_41_forma_de_pago import Ecf41FormaDePago





T = TypeVar("T", bound="Ecf41IdDoc")



@_attrs_define
class Ecf41IdDoc:
    """ 
        Example:
            {'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'numeroCuentaPago': 'numeroCuentaPago', 'indicadorMontoGravado': '', 'encf': 'encf',
                'tipoCuentaPago': '', 'bancoPago': 'bancoPago', 'tipoeCF': 'FacturaDeCreditoFiscalElectronica', 'tipoPago': '',
                'totalPaginas': 6, 'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'terminoPago': 'terminoPago', 'tablaFormasPago':
                [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago': 0.8008281904610115, 'formaPago':
                'Efectivo'}]}

        Attributes:
            tipoe_cf (TipoeCFType):
            encf (str):
            fecha_vencimiento_secuencia (datetime.datetime | Unset):
            indicador_monto_gravado (IndicadorMontoGravadoTypeType1 | None | Unset):
            tipo_pago (None | TipoPagoTypeType1 | Unset):
            fecha_limite_pago (datetime.datetime | None | Unset):
            termino_pago (None | str | Unset):
            tabla_formas_pago (list[Ecf41FormaDePago] | None | Unset):
            tipo_cuenta_pago (None | TipoCuentaPagoTypeType1 | Unset):
            numero_cuenta_pago (None | str | Unset):
            banco_pago (None | str | Unset):
            total_paginas (int | None | str | Unset):
     """

    tipoe_cf: TipoeCFType
    encf: str
    fecha_vencimiento_secuencia: datetime.datetime | Unset = UNSET
    indicador_monto_gravado: IndicadorMontoGravadoTypeType1 | None | Unset = UNSET
    tipo_pago: None | TipoPagoTypeType1 | Unset = UNSET
    fecha_limite_pago: datetime.datetime | None | Unset = UNSET
    termino_pago: None | str | Unset = UNSET
    tabla_formas_pago: list[Ecf41FormaDePago] | None | Unset = UNSET
    tipo_cuenta_pago: None | TipoCuentaPagoTypeType1 | Unset = UNSET
    numero_cuenta_pago: None | str | Unset = UNSET
    banco_pago: None | str | Unset = UNSET
    total_paginas: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_41_forma_de_pago import Ecf41FormaDePago
        tipoe_cf = self.tipoe_cf.value

        encf = self.encf

        fecha_vencimiento_secuencia: str | Unset = UNSET
        if not isinstance(self.fecha_vencimiento_secuencia, Unset):
            fecha_vencimiento_secuencia = self.fecha_vencimiento_secuencia.isoformat()

        indicador_monto_gravado: None | str | Unset
        if isinstance(self.indicador_monto_gravado, Unset):
            indicador_monto_gravado = UNSET
        elif isinstance(self.indicador_monto_gravado, IndicadorMontoGravadoTypeType1):
            indicador_monto_gravado = self.indicador_monto_gravado.value
        else:
            indicador_monto_gravado = self.indicador_monto_gravado

        tipo_pago: None | str | Unset
        if isinstance(self.tipo_pago, Unset):
            tipo_pago = UNSET
        elif isinstance(self.tipo_pago, TipoPagoTypeType1):
            tipo_pago = self.tipo_pago.value
        else:
            tipo_pago = self.tipo_pago

        fecha_limite_pago: None | str | Unset
        if isinstance(self.fecha_limite_pago, Unset):
            fecha_limite_pago = UNSET
        elif isinstance(self.fecha_limite_pago, datetime.datetime):
            fecha_limite_pago = self.fecha_limite_pago.isoformat()
        else:
            fecha_limite_pago = self.fecha_limite_pago

        termino_pago: None | str | Unset
        if isinstance(self.termino_pago, Unset):
            termino_pago = UNSET
        else:
            termino_pago = self.termino_pago

        tabla_formas_pago: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_formas_pago, Unset):
            tabla_formas_pago = UNSET
        elif isinstance(self.tabla_formas_pago, list):
            tabla_formas_pago = []
            for tabla_formas_pago_type_0_item_data in self.tabla_formas_pago:
                tabla_formas_pago_type_0_item = tabla_formas_pago_type_0_item_data.to_dict()
                tabla_formas_pago.append(tabla_formas_pago_type_0_item)


        else:
            tabla_formas_pago = self.tabla_formas_pago

        tipo_cuenta_pago: None | str | Unset
        if isinstance(self.tipo_cuenta_pago, Unset):
            tipo_cuenta_pago = UNSET
        elif isinstance(self.tipo_cuenta_pago, TipoCuentaPagoTypeType1):
            tipo_cuenta_pago = self.tipo_cuenta_pago.value
        else:
            tipo_cuenta_pago = self.tipo_cuenta_pago

        numero_cuenta_pago: None | str | Unset
        if isinstance(self.numero_cuenta_pago, Unset):
            numero_cuenta_pago = UNSET
        else:
            numero_cuenta_pago = self.numero_cuenta_pago

        banco_pago: None | str | Unset
        if isinstance(self.banco_pago, Unset):
            banco_pago = UNSET
        else:
            banco_pago = self.banco_pago

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
        if indicador_monto_gravado is not UNSET:
            field_dict["indicadorMontoGravado"] = indicador_monto_gravado
        if tipo_pago is not UNSET:
            field_dict["tipoPago"] = tipo_pago
        if fecha_limite_pago is not UNSET:
            field_dict["fechaLimitePago"] = fecha_limite_pago
        if termino_pago is not UNSET:
            field_dict["terminoPago"] = termino_pago
        if tabla_formas_pago is not UNSET:
            field_dict["tablaFormasPago"] = tabla_formas_pago
        if tipo_cuenta_pago is not UNSET:
            field_dict["tipoCuentaPago"] = tipo_cuenta_pago
        if numero_cuenta_pago is not UNSET:
            field_dict["numeroCuentaPago"] = numero_cuenta_pago
        if banco_pago is not UNSET:
            field_dict["bancoPago"] = banco_pago
        if total_paginas is not UNSET:
            field_dict["totalPaginas"] = total_paginas

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_41_forma_de_pago import Ecf41FormaDePago
        d = dict(src_dict)
        tipoe_cf = TipoeCFType(d.pop("tipoeCF"))




        encf = d.pop("encf")

        _fecha_vencimiento_secuencia = d.pop("fechaVencimientoSecuencia", UNSET)
        fecha_vencimiento_secuencia: datetime.datetime | Unset
        if isinstance(_fecha_vencimiento_secuencia,  Unset):
            fecha_vencimiento_secuencia = UNSET
        else:
            fecha_vencimiento_secuencia = isoparse(_fecha_vencimiento_secuencia)




        def _parse_indicador_monto_gravado(data: object) -> IndicadorMontoGravadoTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_indicador_monto_gravado_type_type_1 = IndicadorMontoGravadoTypeType1(data)



                return componentsschemas_indicador_monto_gravado_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IndicadorMontoGravadoTypeType1 | None | Unset, data)

        indicador_monto_gravado = _parse_indicador_monto_gravado(d.pop("indicadorMontoGravado", UNSET))


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


        def _parse_fecha_limite_pago(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_limite_pago_type_0 = isoparse(data)



                return fecha_limite_pago_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_limite_pago = _parse_fecha_limite_pago(d.pop("fechaLimitePago", UNSET))


        def _parse_termino_pago(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        termino_pago = _parse_termino_pago(d.pop("terminoPago", UNSET))


        def _parse_tabla_formas_pago(data: object) -> list[Ecf41FormaDePago] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_formas_pago_type_0 = []
                _tabla_formas_pago_type_0 = data
                for tabla_formas_pago_type_0_item_data in (_tabla_formas_pago_type_0):
                    tabla_formas_pago_type_0_item = Ecf41FormaDePago.from_dict(tabla_formas_pago_type_0_item_data)



                    tabla_formas_pago_type_0.append(tabla_formas_pago_type_0_item)

                return tabla_formas_pago_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf41FormaDePago] | None | Unset, data)

        tabla_formas_pago = _parse_tabla_formas_pago(d.pop("tablaFormasPago", UNSET))


        def _parse_tipo_cuenta_pago(data: object) -> None | TipoCuentaPagoTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_tipo_cuenta_pago_type_type_1 = TipoCuentaPagoTypeType1(data)



                return componentsschemas_tipo_cuenta_pago_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TipoCuentaPagoTypeType1 | Unset, data)

        tipo_cuenta_pago = _parse_tipo_cuenta_pago(d.pop("tipoCuentaPago", UNSET))


        def _parse_numero_cuenta_pago(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        numero_cuenta_pago = _parse_numero_cuenta_pago(d.pop("numeroCuentaPago", UNSET))


        def _parse_banco_pago(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        banco_pago = _parse_banco_pago(d.pop("bancoPago", UNSET))


        def _parse_total_paginas(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        total_paginas = _parse_total_paginas(d.pop("totalPaginas", UNSET))


        ecf_41_id_doc = cls(
            tipoe_cf=tipoe_cf,
            encf=encf,
            fecha_vencimiento_secuencia=fecha_vencimiento_secuencia,
            indicador_monto_gravado=indicador_monto_gravado,
            tipo_pago=tipo_pago,
            fecha_limite_pago=fecha_limite_pago,
            termino_pago=termino_pago,
            tabla_formas_pago=tabla_formas_pago,
            tipo_cuenta_pago=tipo_cuenta_pago,
            numero_cuenta_pago=numero_cuenta_pago,
            banco_pago=banco_pago,
            total_paginas=total_paginas,
        )


        ecf_41_id_doc.additional_properties = d
        return ecf_41_id_doc

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
