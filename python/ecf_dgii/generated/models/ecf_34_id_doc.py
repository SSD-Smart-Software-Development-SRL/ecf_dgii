from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_34_tipo_ingresos_validation_type import Ecf34TipoIngresosValidationType
from ..models.ecf_34_tipo_pago_type import Ecf34TipoPagoType
from ..models.indicador_envio_diferido_type_type_1 import IndicadorEnvioDiferidoTypeType1
from ..models.indicador_monto_gravado_type_type_1 import IndicadorMontoGravadoTypeType1
from ..models.indicador_servicio_todo_incluido_type_type_1 import IndicadorServicioTodoIncluidoTypeType1
from ..models.tipoe_cf_type import TipoeCFType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="Ecf34IdDoc")



@_attrs_define
class Ecf34IdDoc:
    """ 
        Example:
            {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'indicadorMontoGravado': '', 'encf': 'encf',
                'fechaHasta': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'indicadorNotaCredito': 0, 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'indicadorEnvioDiferido': '', 'tipoeCF':
                'FacturaDeCreditoFiscalElectronica', 'tipoPago': 'Contado', 'totalPaginas': 6, 'indicadorServicioTodoIncluido':
                ''}

        Attributes:
            tipoe_cf (TipoeCFType):
            encf (str):
            indicador_nota_credito (int | str):
            tipo_ingresos (Ecf34TipoIngresosValidationType):
            tipo_pago (Ecf34TipoPagoType):
            indicador_envio_diferido (IndicadorEnvioDiferidoTypeType1 | None | Unset):
            indicador_monto_gravado (IndicadorMontoGravadoTypeType1 | None | Unset):
            indicador_servicio_todo_incluido (IndicadorServicioTodoIncluidoTypeType1 | None | Unset):
            fecha_limite_pago (datetime.datetime | None | Unset):
            fecha_desde (datetime.datetime | None | Unset):
            fecha_hasta (datetime.datetime | None | Unset):
            total_paginas (int | None | str | Unset):
     """

    tipoe_cf: TipoeCFType
    encf: str
    indicador_nota_credito: int | str
    tipo_ingresos: Ecf34TipoIngresosValidationType
    tipo_pago: Ecf34TipoPagoType
    indicador_envio_diferido: IndicadorEnvioDiferidoTypeType1 | None | Unset = UNSET
    indicador_monto_gravado: IndicadorMontoGravadoTypeType1 | None | Unset = UNSET
    indicador_servicio_todo_incluido: IndicadorServicioTodoIncluidoTypeType1 | None | Unset = UNSET
    fecha_limite_pago: datetime.datetime | None | Unset = UNSET
    fecha_desde: datetime.datetime | None | Unset = UNSET
    fecha_hasta: datetime.datetime | None | Unset = UNSET
    total_paginas: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tipoe_cf = self.tipoe_cf.value

        encf = self.encf

        indicador_nota_credito: int | str
        indicador_nota_credito = self.indicador_nota_credito

        tipo_ingresos = self.tipo_ingresos.value

        tipo_pago = self.tipo_pago.value

        indicador_envio_diferido: None | str | Unset
        if isinstance(self.indicador_envio_diferido, Unset):
            indicador_envio_diferido = UNSET
        elif isinstance(self.indicador_envio_diferido, IndicadorEnvioDiferidoTypeType1):
            indicador_envio_diferido = self.indicador_envio_diferido.value
        else:
            indicador_envio_diferido = self.indicador_envio_diferido

        indicador_monto_gravado: None | str | Unset
        if isinstance(self.indicador_monto_gravado, Unset):
            indicador_monto_gravado = UNSET
        elif isinstance(self.indicador_monto_gravado, IndicadorMontoGravadoTypeType1):
            indicador_monto_gravado = self.indicador_monto_gravado.value
        else:
            indicador_monto_gravado = self.indicador_monto_gravado

        indicador_servicio_todo_incluido: None | str | Unset
        if isinstance(self.indicador_servicio_todo_incluido, Unset):
            indicador_servicio_todo_incluido = UNSET
        elif isinstance(self.indicador_servicio_todo_incluido, IndicadorServicioTodoIncluidoTypeType1):
            indicador_servicio_todo_incluido = self.indicador_servicio_todo_incluido.value
        else:
            indicador_servicio_todo_incluido = self.indicador_servicio_todo_incluido

        fecha_limite_pago: None | str | Unset
        if isinstance(self.fecha_limite_pago, Unset):
            fecha_limite_pago = UNSET
        elif isinstance(self.fecha_limite_pago, datetime.datetime):
            fecha_limite_pago = self.fecha_limite_pago.isoformat()
        else:
            fecha_limite_pago = self.fecha_limite_pago

        fecha_desde: None | str | Unset
        if isinstance(self.fecha_desde, Unset):
            fecha_desde = UNSET
        elif isinstance(self.fecha_desde, datetime.datetime):
            fecha_desde = self.fecha_desde.isoformat()
        else:
            fecha_desde = self.fecha_desde

        fecha_hasta: None | str | Unset
        if isinstance(self.fecha_hasta, Unset):
            fecha_hasta = UNSET
        elif isinstance(self.fecha_hasta, datetime.datetime):
            fecha_hasta = self.fecha_hasta.isoformat()
        else:
            fecha_hasta = self.fecha_hasta

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
            "indicadorNotaCredito": indicador_nota_credito,
            "tipoIngresos": tipo_ingresos,
            "tipoPago": tipo_pago,
        })
        if indicador_envio_diferido is not UNSET:
            field_dict["indicadorEnvioDiferido"] = indicador_envio_diferido
        if indicador_monto_gravado is not UNSET:
            field_dict["indicadorMontoGravado"] = indicador_monto_gravado
        if indicador_servicio_todo_incluido is not UNSET:
            field_dict["indicadorServicioTodoIncluido"] = indicador_servicio_todo_incluido
        if fecha_limite_pago is not UNSET:
            field_dict["fechaLimitePago"] = fecha_limite_pago
        if fecha_desde is not UNSET:
            field_dict["fechaDesde"] = fecha_desde
        if fecha_hasta is not UNSET:
            field_dict["fechaHasta"] = fecha_hasta
        if total_paginas is not UNSET:
            field_dict["totalPaginas"] = total_paginas

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tipoe_cf = TipoeCFType(d.pop("tipoeCF"))




        encf = d.pop("encf")

        def _parse_indicador_nota_credito(data: object) -> int | str:
            return cast(int | str, data)

        indicador_nota_credito = _parse_indicador_nota_credito(d.pop("indicadorNotaCredito"))


        tipo_ingresos = Ecf34TipoIngresosValidationType(d.pop("tipoIngresos"))




        tipo_pago = Ecf34TipoPagoType(d.pop("tipoPago"))




        def _parse_indicador_envio_diferido(data: object) -> IndicadorEnvioDiferidoTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_indicador_envio_diferido_type_type_1 = IndicadorEnvioDiferidoTypeType1(data)



                return componentsschemas_indicador_envio_diferido_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IndicadorEnvioDiferidoTypeType1 | None | Unset, data)

        indicador_envio_diferido = _parse_indicador_envio_diferido(d.pop("indicadorEnvioDiferido", UNSET))


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


        def _parse_indicador_servicio_todo_incluido(data: object) -> IndicadorServicioTodoIncluidoTypeType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_indicador_servicio_todo_incluido_type_type_1 = IndicadorServicioTodoIncluidoTypeType1(data)



                return componentsschemas_indicador_servicio_todo_incluido_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IndicadorServicioTodoIncluidoTypeType1 | None | Unset, data)

        indicador_servicio_todo_incluido = _parse_indicador_servicio_todo_incluido(d.pop("indicadorServicioTodoIncluido", UNSET))


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


        def _parse_fecha_desde(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_desde_type_0 = isoparse(data)



                return fecha_desde_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_desde = _parse_fecha_desde(d.pop("fechaDesde", UNSET))


        def _parse_fecha_hasta(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_hasta_type_0 = isoparse(data)



                return fecha_hasta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_hasta = _parse_fecha_hasta(d.pop("fechaHasta", UNSET))


        def _parse_total_paginas(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        total_paginas = _parse_total_paginas(d.pop("totalPaginas", UNSET))


        ecf_34_id_doc = cls(
            tipoe_cf=tipoe_cf,
            encf=encf,
            indicador_nota_credito=indicador_nota_credito,
            tipo_ingresos=tipo_ingresos,
            tipo_pago=tipo_pago,
            indicador_envio_diferido=indicador_envio_diferido,
            indicador_monto_gravado=indicador_monto_gravado,
            indicador_servicio_todo_incluido=indicador_servicio_todo_incluido,
            fecha_limite_pago=fecha_limite_pago,
            fecha_desde=fecha_desde,
            fecha_hasta=fecha_hasta,
            total_paginas=total_paginas,
        )


        ecf_34_id_doc.additional_properties = d
        return ecf_34_id_doc

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
