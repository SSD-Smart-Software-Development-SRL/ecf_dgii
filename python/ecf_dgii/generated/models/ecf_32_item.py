from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_32_indicador_bieno_servicio_type import Ecf32IndicadorBienoServicioType
from ..models.ecf_32_indicador_facturacion_type import Ecf32IndicadorFacturacionType
from ..models.unidad_medida_type_type_1 import UnidadMedidaTypeType1
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.ecf_32_codigos_item import Ecf32CodigosItem
  from ..models.ecf_32_impuesto_adicional import Ecf32ImpuestoAdicional
  from ..models.ecf_32_mineria import Ecf32Mineria
  from ..models.ecf_32_otra_moneda_detalle import Ecf32OtraMonedaDetalle
  from ..models.ecf_32_sub_descuento import Ecf32SubDescuento
  from ..models.ecf_32_sub_recargo import Ecf32SubRecargo
  from ..models.ecf_32_subcantidad_item import Ecf32SubcantidadItem





T = TypeVar("T", bound="Ecf32Item")



@_attrs_define
class Ecf32Item:
    """ 
        Example:
            {'indicadorFacturacion': 'NoFacturable_18Percent', 'tablaImpuestoAdicional': [{'tipoImpuesto': None},
                {'tipoImpuesto': None}], 'nombreItem': 'nombreItem', 'tablaSubcantidad': [{'codigoSubcantidad': '',
                'subcantidad': 3.616076749251911}, {'codigoSubcantidad': '', 'subcantidad': 3.616076749251911}],
                'tablaCodigosItem': [{'codigoItem': 'codigoItem', 'tipoCodigo': 'tipoCodigo'}, {'codigoItem': 'codigoItem',
                'tipoCodigo': 'tipoCodigo'}], 'unidadMedida': '', 'mineria': '', 'otraMonedaDetalle': '',
                'indicadorBienoServicio': 'Bien', 'tablaSubRecargo': [{'subRecargoPorcentaje': None, 'tipoSubRecargo': None,
                'montoSubRecargo': None}, {'subRecargoPorcentaje': None, 'tipoSubRecargo': None, 'montoSubRecargo': None}],
                'descripcionItem': 'descripcionItem', 'descuentoMonto': None, 'fechaVencimientoItem': datetime.datetime(2000, 1,
                23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroLinea': 7, 'recargoMonto':
                None, 'cantidadItem': 9.301444243932576, 'unidadReferencia': '', 'precioUnitarioReferencia': None,
                'precioUnitarioItem': 2.027123023002322, 'gradosAlcohol': 3.616076749251911, 'tablaSubDescuento':
                [{'tipoSubDescuento': '$', 'subDescuentoPorcentaje': None, 'montoSubDescuento': None}, {'tipoSubDescuento': '$',
                'subDescuentoPorcentaje': None, 'montoSubDescuento': None}], 'montoItem': None, 'cantidadReferencia': None,
                'fechaElaboracion': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00'))}

        Attributes:
            numero_linea (int | str):
            indicador_facturacion (Ecf32IndicadorFacturacionType):
            nombre_item (str):
            indicador_bieno_servicio (Ecf32IndicadorBienoServicioType):
            cantidad_item (float | str):
            precio_unitario_item (float | str):
            monto_item (float | str):
            tabla_codigos_item (list[Ecf32CodigosItem] | None | Unset):
            descripcion_item (None | str | Unset):
            unidad_medida (None | UnidadMedidaTypeType1 | Unset):
            cantidad_referencia (float | None | str | Unset):
            unidad_referencia (None | UnidadMedidaTypeType1 | Unset):
            tabla_subcantidad (list[Ecf32SubcantidadItem] | None | Unset):
            grados_alcohol (float | None | str | Unset):
            precio_unitario_referencia (float | None | str | Unset):
            fecha_elaboracion (datetime.datetime | None | Unset):
            fecha_vencimiento_item (datetime.datetime | None | Unset):
            mineria (Ecf32Mineria | None | Unset):
            descuento_monto (float | None | str | Unset):
            tabla_sub_descuento (list[Ecf32SubDescuento] | None | Unset):
            recargo_monto (float | None | str | Unset):
            tabla_sub_recargo (list[Ecf32SubRecargo] | None | Unset):
            tabla_impuesto_adicional (list[Ecf32ImpuestoAdicional] | None | Unset):
            otra_moneda_detalle (Ecf32OtraMonedaDetalle | None | Unset):
     """

    numero_linea: int | str
    indicador_facturacion: Ecf32IndicadorFacturacionType
    nombre_item: str
    indicador_bieno_servicio: Ecf32IndicadorBienoServicioType
    cantidad_item: float | str
    precio_unitario_item: float | str
    monto_item: float | str
    tabla_codigos_item: list[Ecf32CodigosItem] | None | Unset = UNSET
    descripcion_item: None | str | Unset = UNSET
    unidad_medida: None | UnidadMedidaTypeType1 | Unset = UNSET
    cantidad_referencia: float | None | str | Unset = UNSET
    unidad_referencia: None | UnidadMedidaTypeType1 | Unset = UNSET
    tabla_subcantidad: list[Ecf32SubcantidadItem] | None | Unset = UNSET
    grados_alcohol: float | None | str | Unset = UNSET
    precio_unitario_referencia: float | None | str | Unset = UNSET
    fecha_elaboracion: datetime.datetime | None | Unset = UNSET
    fecha_vencimiento_item: datetime.datetime | None | Unset = UNSET
    mineria: Ecf32Mineria | None | Unset = UNSET
    descuento_monto: float | None | str | Unset = UNSET
    tabla_sub_descuento: list[Ecf32SubDescuento] | None | Unset = UNSET
    recargo_monto: float | None | str | Unset = UNSET
    tabla_sub_recargo: list[Ecf32SubRecargo] | None | Unset = UNSET
    tabla_impuesto_adicional: list[Ecf32ImpuestoAdicional] | None | Unset = UNSET
    otra_moneda_detalle: Ecf32OtraMonedaDetalle | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_32_codigos_item import Ecf32CodigosItem
        from ..models.ecf_32_impuesto_adicional import Ecf32ImpuestoAdicional
        from ..models.ecf_32_mineria import Ecf32Mineria
        from ..models.ecf_32_otra_moneda_detalle import Ecf32OtraMonedaDetalle
        from ..models.ecf_32_sub_descuento import Ecf32SubDescuento
        from ..models.ecf_32_sub_recargo import Ecf32SubRecargo
        from ..models.ecf_32_subcantidad_item import Ecf32SubcantidadItem
        numero_linea: int | str
        numero_linea = self.numero_linea

        indicador_facturacion = self.indicador_facturacion.value

        nombre_item = self.nombre_item

        indicador_bieno_servicio = self.indicador_bieno_servicio.value

        cantidad_item: float | str
        cantidad_item = self.cantidad_item

        precio_unitario_item: float | str
        precio_unitario_item = self.precio_unitario_item

        monto_item: float | str
        monto_item = self.monto_item

        tabla_codigos_item: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_codigos_item, Unset):
            tabla_codigos_item = UNSET
        elif isinstance(self.tabla_codigos_item, list):
            tabla_codigos_item = []
            for tabla_codigos_item_type_0_item_data in self.tabla_codigos_item:
                tabla_codigos_item_type_0_item = tabla_codigos_item_type_0_item_data.to_dict()
                tabla_codigos_item.append(tabla_codigos_item_type_0_item)


        else:
            tabla_codigos_item = self.tabla_codigos_item

        descripcion_item: None | str | Unset
        if isinstance(self.descripcion_item, Unset):
            descripcion_item = UNSET
        else:
            descripcion_item = self.descripcion_item

        unidad_medida: None | str | Unset
        if isinstance(self.unidad_medida, Unset):
            unidad_medida = UNSET
        elif isinstance(self.unidad_medida, UnidadMedidaTypeType1):
            unidad_medida = self.unidad_medida.value
        else:
            unidad_medida = self.unidad_medida

        cantidad_referencia: float | None | str | Unset
        if isinstance(self.cantidad_referencia, Unset):
            cantidad_referencia = UNSET
        else:
            cantidad_referencia = self.cantidad_referencia

        unidad_referencia: None | str | Unset
        if isinstance(self.unidad_referencia, Unset):
            unidad_referencia = UNSET
        elif isinstance(self.unidad_referencia, UnidadMedidaTypeType1):
            unidad_referencia = self.unidad_referencia.value
        else:
            unidad_referencia = self.unidad_referencia

        tabla_subcantidad: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_subcantidad, Unset):
            tabla_subcantidad = UNSET
        elif isinstance(self.tabla_subcantidad, list):
            tabla_subcantidad = []
            for tabla_subcantidad_type_0_item_data in self.tabla_subcantidad:
                tabla_subcantidad_type_0_item = tabla_subcantidad_type_0_item_data.to_dict()
                tabla_subcantidad.append(tabla_subcantidad_type_0_item)


        else:
            tabla_subcantidad = self.tabla_subcantidad

        grados_alcohol: float | None | str | Unset
        if isinstance(self.grados_alcohol, Unset):
            grados_alcohol = UNSET
        else:
            grados_alcohol = self.grados_alcohol

        precio_unitario_referencia: float | None | str | Unset
        if isinstance(self.precio_unitario_referencia, Unset):
            precio_unitario_referencia = UNSET
        else:
            precio_unitario_referencia = self.precio_unitario_referencia

        fecha_elaboracion: None | str | Unset
        if isinstance(self.fecha_elaboracion, Unset):
            fecha_elaboracion = UNSET
        elif isinstance(self.fecha_elaboracion, datetime.datetime):
            fecha_elaboracion = self.fecha_elaboracion.isoformat()
        else:
            fecha_elaboracion = self.fecha_elaboracion

        fecha_vencimiento_item: None | str | Unset
        if isinstance(self.fecha_vencimiento_item, Unset):
            fecha_vencimiento_item = UNSET
        elif isinstance(self.fecha_vencimiento_item, datetime.datetime):
            fecha_vencimiento_item = self.fecha_vencimiento_item.isoformat()
        else:
            fecha_vencimiento_item = self.fecha_vencimiento_item

        mineria: dict[str, Any] | None | Unset
        if isinstance(self.mineria, Unset):
            mineria = UNSET
        elif isinstance(self.mineria, Ecf32Mineria):
            mineria = self.mineria.to_dict()
        else:
            mineria = self.mineria

        descuento_monto: float | None | str | Unset
        if isinstance(self.descuento_monto, Unset):
            descuento_monto = UNSET
        else:
            descuento_monto = self.descuento_monto

        tabla_sub_descuento: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_sub_descuento, Unset):
            tabla_sub_descuento = UNSET
        elif isinstance(self.tabla_sub_descuento, list):
            tabla_sub_descuento = []
            for tabla_sub_descuento_type_0_item_data in self.tabla_sub_descuento:
                tabla_sub_descuento_type_0_item = tabla_sub_descuento_type_0_item_data.to_dict()
                tabla_sub_descuento.append(tabla_sub_descuento_type_0_item)


        else:
            tabla_sub_descuento = self.tabla_sub_descuento

        recargo_monto: float | None | str | Unset
        if isinstance(self.recargo_monto, Unset):
            recargo_monto = UNSET
        else:
            recargo_monto = self.recargo_monto

        tabla_sub_recargo: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_sub_recargo, Unset):
            tabla_sub_recargo = UNSET
        elif isinstance(self.tabla_sub_recargo, list):
            tabla_sub_recargo = []
            for tabla_sub_recargo_type_0_item_data in self.tabla_sub_recargo:
                tabla_sub_recargo_type_0_item = tabla_sub_recargo_type_0_item_data.to_dict()
                tabla_sub_recargo.append(tabla_sub_recargo_type_0_item)


        else:
            tabla_sub_recargo = self.tabla_sub_recargo

        tabla_impuesto_adicional: list[dict[str, Any]] | None | Unset
        if isinstance(self.tabla_impuesto_adicional, Unset):
            tabla_impuesto_adicional = UNSET
        elif isinstance(self.tabla_impuesto_adicional, list):
            tabla_impuesto_adicional = []
            for tabla_impuesto_adicional_type_0_item_data in self.tabla_impuesto_adicional:
                tabla_impuesto_adicional_type_0_item = tabla_impuesto_adicional_type_0_item_data.to_dict()
                tabla_impuesto_adicional.append(tabla_impuesto_adicional_type_0_item)


        else:
            tabla_impuesto_adicional = self.tabla_impuesto_adicional

        otra_moneda_detalle: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda_detalle, Unset):
            otra_moneda_detalle = UNSET
        elif isinstance(self.otra_moneda_detalle, Ecf32OtraMonedaDetalle):
            otra_moneda_detalle = self.otra_moneda_detalle.to_dict()
        else:
            otra_moneda_detalle = self.otra_moneda_detalle


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "numeroLinea": numero_linea,
            "indicadorFacturacion": indicador_facturacion,
            "nombreItem": nombre_item,
            "indicadorBienoServicio": indicador_bieno_servicio,
            "cantidadItem": cantidad_item,
            "precioUnitarioItem": precio_unitario_item,
            "montoItem": monto_item,
        })
        if tabla_codigos_item is not UNSET:
            field_dict["tablaCodigosItem"] = tabla_codigos_item
        if descripcion_item is not UNSET:
            field_dict["descripcionItem"] = descripcion_item
        if unidad_medida is not UNSET:
            field_dict["unidadMedida"] = unidad_medida
        if cantidad_referencia is not UNSET:
            field_dict["cantidadReferencia"] = cantidad_referencia
        if unidad_referencia is not UNSET:
            field_dict["unidadReferencia"] = unidad_referencia
        if tabla_subcantidad is not UNSET:
            field_dict["tablaSubcantidad"] = tabla_subcantidad
        if grados_alcohol is not UNSET:
            field_dict["gradosAlcohol"] = grados_alcohol
        if precio_unitario_referencia is not UNSET:
            field_dict["precioUnitarioReferencia"] = precio_unitario_referencia
        if fecha_elaboracion is not UNSET:
            field_dict["fechaElaboracion"] = fecha_elaboracion
        if fecha_vencimiento_item is not UNSET:
            field_dict["fechaVencimientoItem"] = fecha_vencimiento_item
        if mineria is not UNSET:
            field_dict["mineria"] = mineria
        if descuento_monto is not UNSET:
            field_dict["descuentoMonto"] = descuento_monto
        if tabla_sub_descuento is not UNSET:
            field_dict["tablaSubDescuento"] = tabla_sub_descuento
        if recargo_monto is not UNSET:
            field_dict["recargoMonto"] = recargo_monto
        if tabla_sub_recargo is not UNSET:
            field_dict["tablaSubRecargo"] = tabla_sub_recargo
        if tabla_impuesto_adicional is not UNSET:
            field_dict["tablaImpuestoAdicional"] = tabla_impuesto_adicional
        if otra_moneda_detalle is not UNSET:
            field_dict["otraMonedaDetalle"] = otra_moneda_detalle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_32_codigos_item import Ecf32CodigosItem
        from ..models.ecf_32_impuesto_adicional import Ecf32ImpuestoAdicional
        from ..models.ecf_32_mineria import Ecf32Mineria
        from ..models.ecf_32_otra_moneda_detalle import Ecf32OtraMonedaDetalle
        from ..models.ecf_32_sub_descuento import Ecf32SubDescuento
        from ..models.ecf_32_sub_recargo import Ecf32SubRecargo
        from ..models.ecf_32_subcantidad_item import Ecf32SubcantidadItem
        d = dict(src_dict)
        def _parse_numero_linea(data: object) -> int | str:
            return cast(int | str, data)

        numero_linea = _parse_numero_linea(d.pop("numeroLinea"))


        indicador_facturacion = Ecf32IndicadorFacturacionType(d.pop("indicadorFacturacion"))




        nombre_item = d.pop("nombreItem")

        indicador_bieno_servicio = Ecf32IndicadorBienoServicioType(d.pop("indicadorBienoServicio"))




        def _parse_cantidad_item(data: object) -> float | str:
            return cast(float | str, data)

        cantidad_item = _parse_cantidad_item(d.pop("cantidadItem"))


        def _parse_precio_unitario_item(data: object) -> float | str:
            return cast(float | str, data)

        precio_unitario_item = _parse_precio_unitario_item(d.pop("precioUnitarioItem"))


        def _parse_monto_item(data: object) -> float | str:
            return cast(float | str, data)

        monto_item = _parse_monto_item(d.pop("montoItem"))


        def _parse_tabla_codigos_item(data: object) -> list[Ecf32CodigosItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_codigos_item_type_0 = []
                _tabla_codigos_item_type_0 = data
                for tabla_codigos_item_type_0_item_data in (_tabla_codigos_item_type_0):
                    tabla_codigos_item_type_0_item = Ecf32CodigosItem.from_dict(tabla_codigos_item_type_0_item_data)



                    tabla_codigos_item_type_0.append(tabla_codigos_item_type_0_item)

                return tabla_codigos_item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf32CodigosItem] | None | Unset, data)

        tabla_codigos_item = _parse_tabla_codigos_item(d.pop("tablaCodigosItem", UNSET))


        def _parse_descripcion_item(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descripcion_item = _parse_descripcion_item(d.pop("descripcionItem", UNSET))


        def _parse_unidad_medida(data: object) -> None | UnidadMedidaTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_unidad_medida_type_type_1 = UnidadMedidaTypeType1(data)



                return componentsschemas_unidad_medida_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnidadMedidaTypeType1 | Unset, data)

        unidad_medida = _parse_unidad_medida(d.pop("unidadMedida", UNSET))


        def _parse_cantidad_referencia(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        cantidad_referencia = _parse_cantidad_referencia(d.pop("cantidadReferencia", UNSET))


        def _parse_unidad_referencia(data: object) -> None | UnidadMedidaTypeType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_unidad_medida_type_type_1 = UnidadMedidaTypeType1(data)



                return componentsschemas_unidad_medida_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UnidadMedidaTypeType1 | Unset, data)

        unidad_referencia = _parse_unidad_referencia(d.pop("unidadReferencia", UNSET))


        def _parse_tabla_subcantidad(data: object) -> list[Ecf32SubcantidadItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_subcantidad_type_0 = []
                _tabla_subcantidad_type_0 = data
                for tabla_subcantidad_type_0_item_data in (_tabla_subcantidad_type_0):
                    tabla_subcantidad_type_0_item = Ecf32SubcantidadItem.from_dict(tabla_subcantidad_type_0_item_data)



                    tabla_subcantidad_type_0.append(tabla_subcantidad_type_0_item)

                return tabla_subcantidad_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf32SubcantidadItem] | None | Unset, data)

        tabla_subcantidad = _parse_tabla_subcantidad(d.pop("tablaSubcantidad", UNSET))


        def _parse_grados_alcohol(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        grados_alcohol = _parse_grados_alcohol(d.pop("gradosAlcohol", UNSET))


        def _parse_precio_unitario_referencia(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        precio_unitario_referencia = _parse_precio_unitario_referencia(d.pop("precioUnitarioReferencia", UNSET))


        def _parse_fecha_elaboracion(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_elaboracion_type_0 = isoparse(data)



                return fecha_elaboracion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_elaboracion = _parse_fecha_elaboracion(d.pop("fechaElaboracion", UNSET))


        def _parse_fecha_vencimiento_item(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_vencimiento_item_type_0 = isoparse(data)



                return fecha_vencimiento_item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_vencimiento_item = _parse_fecha_vencimiento_item(d.pop("fechaVencimientoItem", UNSET))


        def _parse_mineria(data: object) -> Ecf32Mineria | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mineria_type_1 = Ecf32Mineria.from_dict(data)



                return mineria_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf32Mineria | None | Unset, data)

        mineria = _parse_mineria(d.pop("mineria", UNSET))


        def _parse_descuento_monto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        descuento_monto = _parse_descuento_monto(d.pop("descuentoMonto", UNSET))


        def _parse_tabla_sub_descuento(data: object) -> list[Ecf32SubDescuento] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_sub_descuento_type_0 = []
                _tabla_sub_descuento_type_0 = data
                for tabla_sub_descuento_type_0_item_data in (_tabla_sub_descuento_type_0):
                    tabla_sub_descuento_type_0_item = Ecf32SubDescuento.from_dict(tabla_sub_descuento_type_0_item_data)



                    tabla_sub_descuento_type_0.append(tabla_sub_descuento_type_0_item)

                return tabla_sub_descuento_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf32SubDescuento] | None | Unset, data)

        tabla_sub_descuento = _parse_tabla_sub_descuento(d.pop("tablaSubDescuento", UNSET))


        def _parse_recargo_monto(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        recargo_monto = _parse_recargo_monto(d.pop("recargoMonto", UNSET))


        def _parse_tabla_sub_recargo(data: object) -> list[Ecf32SubRecargo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_sub_recargo_type_0 = []
                _tabla_sub_recargo_type_0 = data
                for tabla_sub_recargo_type_0_item_data in (_tabla_sub_recargo_type_0):
                    tabla_sub_recargo_type_0_item = Ecf32SubRecargo.from_dict(tabla_sub_recargo_type_0_item_data)



                    tabla_sub_recargo_type_0.append(tabla_sub_recargo_type_0_item)

                return tabla_sub_recargo_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf32SubRecargo] | None | Unset, data)

        tabla_sub_recargo = _parse_tabla_sub_recargo(d.pop("tablaSubRecargo", UNSET))


        def _parse_tabla_impuesto_adicional(data: object) -> list[Ecf32ImpuestoAdicional] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tabla_impuesto_adicional_type_0 = []
                _tabla_impuesto_adicional_type_0 = data
                for tabla_impuesto_adicional_type_0_item_data in (_tabla_impuesto_adicional_type_0):
                    tabla_impuesto_adicional_type_0_item = Ecf32ImpuestoAdicional.from_dict(tabla_impuesto_adicional_type_0_item_data)



                    tabla_impuesto_adicional_type_0.append(tabla_impuesto_adicional_type_0_item)

                return tabla_impuesto_adicional_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Ecf32ImpuestoAdicional] | None | Unset, data)

        tabla_impuesto_adicional = _parse_tabla_impuesto_adicional(d.pop("tablaImpuestoAdicional", UNSET))


        def _parse_otra_moneda_detalle(data: object) -> Ecf32OtraMonedaDetalle | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_detalle_type_1 = Ecf32OtraMonedaDetalle.from_dict(data)



                return otra_moneda_detalle_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf32OtraMonedaDetalle | None | Unset, data)

        otra_moneda_detalle = _parse_otra_moneda_detalle(d.pop("otraMonedaDetalle", UNSET))


        ecf_32_item = cls(
            numero_linea=numero_linea,
            indicador_facturacion=indicador_facturacion,
            nombre_item=nombre_item,
            indicador_bieno_servicio=indicador_bieno_servicio,
            cantidad_item=cantidad_item,
            precio_unitario_item=precio_unitario_item,
            monto_item=monto_item,
            tabla_codigos_item=tabla_codigos_item,
            descripcion_item=descripcion_item,
            unidad_medida=unidad_medida,
            cantidad_referencia=cantidad_referencia,
            unidad_referencia=unidad_referencia,
            tabla_subcantidad=tabla_subcantidad,
            grados_alcohol=grados_alcohol,
            precio_unitario_referencia=precio_unitario_referencia,
            fecha_elaboracion=fecha_elaboracion,
            fecha_vencimiento_item=fecha_vencimiento_item,
            mineria=mineria,
            descuento_monto=descuento_monto,
            tabla_sub_descuento=tabla_sub_descuento,
            recargo_monto=recargo_monto,
            tabla_sub_recargo=tabla_sub_recargo,
            tabla_impuesto_adicional=tabla_impuesto_adicional,
            otra_moneda_detalle=otra_moneda_detalle,
        )


        ecf_32_item.additional_properties = d
        return ecf_32_item

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
