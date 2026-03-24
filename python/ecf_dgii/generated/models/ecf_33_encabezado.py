from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_33_version_type import Ecf33VersionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_33_comprador import Ecf33Comprador
  from ..models.ecf_33_emisor import Ecf33Emisor
  from ..models.ecf_33_id_doc import Ecf33IdDoc
  from ..models.ecf_33_informaciones_adicionales import Ecf33InformacionesAdicionales
  from ..models.ecf_33_otra_moneda import Ecf33OtraMoneda
  from ..models.ecf_33_totales import Ecf33Totales
  from ..models.ecf_33_transporte import Ecf33Transporte





T = TypeVar("T", bound="Ecf33Encabezado")



@_attrs_define
class Ecf33Encabezado:
    """ 
        Example:
            {'transporte': '', 'informacionesAdicionales': '', 'comprador': '', 'idDoc': {'tipoIngresos': '01',
                'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'encf': 'encf', 'fechaHasta': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoCuentaPago': '', 'fechaDesde':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF':
                'FacturaDeCreditoFiscalElectronica', 'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago',
                'indicadorMontoGravado': '', 'bancoPago': 'bancoPago', 'indicadorEnvioDiferido': '', 'tipoPago': 'Contado',
                'totalPaginas': 6, 'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'indicadorServicioTodoIncluido': '',
                'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago':
                0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version': 'Version1_0', 'emisor':
                {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor', 'informacionAdicionalEmisor':
                'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000, 1, 23), 'provincia': '',
                'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor': 'correoEmisor', 'webSite':
                'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'], 'sucursal': 'sucursal',
                'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna': 'numeroFacturaInterna', 'nombreComercial':
                'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta': 'rutaVenta', 'codigoVendedor': 'codigoVendedor'},
                'totales': {'montoPeriodo': None, 'totalISRPercepcion': None, 'montoGravadoI3': None, 'montoGravadoI2': None,
                'montoAvancePago': None, 'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1': None, 'totalITBIS2': None,
                'totalITBISPercepcion': None, 'itbiS2': None, 'montoImpuestoAdicional': 5.962133916683182, 'itbiS1': None,
                'itbiS3': None, 'totalITBISRetenido': None, 'totalITBIS': None, 'montoNoFacturable': 2.3021358869347655,
                'impuestosAdicionales': [{'tipoImpuesto': '001', 'montoImpuestoSelectivoConsumoAdvalorem': None,
                'tasaImpuestoAdicional': 5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None,
                'otrosImpuestosAdicionales': None}, {'tipoImpuesto': '001', 'montoImpuestoSelectivoConsumoAdvalorem': None,
                'tasaImpuestoAdicional': 5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None,
                'otrosImpuestosAdicionales': None}], 'saldoAnterior': None, 'totalISRRetencion': None, 'montoExento': None,
                'montoGravadoTotal': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None}}

        Attributes:
            version (Ecf33VersionType):
            id_doc (Ecf33IdDoc):  Example: {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56,
                7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'indicadorMontoGravado': '', 'bancoPago':
                'bancoPago', 'indicadorEnvioDiferido': '', 'tipoPago': 'Contado', 'totalPaginas': 6,
                'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'indicadorServicioTodoIncluido': '',
                'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago':
                0.8008281904610115, 'formaPago': 'Efectivo'}]}.
            emisor (Ecf33Emisor):  Example: {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta':
                'rutaVenta', 'codigoVendedor': 'codigoVendedor'}.
            totales (Ecf33Totales):  Example: {'montoPeriodo': None, 'totalISRPercepcion': None, 'montoGravadoI3': None,
                'montoGravadoI2': None, 'montoAvancePago': None, 'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1':
                None, 'totalITBIS2': None, 'totalITBISPercepcion': None, 'itbiS2': None, 'montoImpuestoAdicional':
                5.962133916683182, 'itbiS1': None, 'itbiS3': None, 'totalITBISRetenido': None, 'totalITBIS': None,
                'montoNoFacturable': 2.3021358869347655, 'impuestosAdicionales': [{'tipoImpuesto': '001',
                'montoImpuestoSelectivoConsumoAdvalorem': None, 'tasaImpuestoAdicional': 5.637376656633329,
                'montoImpuestoSelectivoConsumoEspecifico': None, 'otrosImpuestosAdicionales': None}, {'tipoImpuesto': '001',
                'montoImpuestoSelectivoConsumoAdvalorem': None, 'tasaImpuestoAdicional': 5.637376656633329,
                'montoImpuestoSelectivoConsumoEspecifico': None, 'otrosImpuestosAdicionales': None}], 'saldoAnterior': None,
                'totalISRRetencion': None, 'montoExento': None, 'montoGravadoTotal': 1.4658129805029452, 'valorPagar': None,
                'montoTotal': None}.
            comprador (Ecf33Comprador | None | Unset):
            informaciones_adicionales (Ecf33InformacionesAdicionales | None | Unset):
            transporte (Ecf33Transporte | None | Unset):
            otra_moneda (Ecf33OtraMoneda | None | Unset):
     """

    version: Ecf33VersionType
    id_doc: Ecf33IdDoc
    emisor: Ecf33Emisor
    totales: Ecf33Totales
    comprador: Ecf33Comprador | None | Unset = UNSET
    informaciones_adicionales: Ecf33InformacionesAdicionales | None | Unset = UNSET
    transporte: Ecf33Transporte | None | Unset = UNSET
    otra_moneda: Ecf33OtraMoneda | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_33_comprador import Ecf33Comprador
        from ..models.ecf_33_emisor import Ecf33Emisor
        from ..models.ecf_33_id_doc import Ecf33IdDoc
        from ..models.ecf_33_informaciones_adicionales import Ecf33InformacionesAdicionales
        from ..models.ecf_33_otra_moneda import Ecf33OtraMoneda
        from ..models.ecf_33_totales import Ecf33Totales
        from ..models.ecf_33_transporte import Ecf33Transporte
        version = self.version.value

        id_doc = self.id_doc.to_dict()

        emisor = self.emisor.to_dict()

        totales = self.totales.to_dict()

        comprador: dict[str, Any] | None | Unset
        if isinstance(self.comprador, Unset):
            comprador = UNSET
        elif isinstance(self.comprador, Ecf33Comprador):
            comprador = self.comprador.to_dict()
        else:
            comprador = self.comprador

        informaciones_adicionales: dict[str, Any] | None | Unset
        if isinstance(self.informaciones_adicionales, Unset):
            informaciones_adicionales = UNSET
        elif isinstance(self.informaciones_adicionales, Ecf33InformacionesAdicionales):
            informaciones_adicionales = self.informaciones_adicionales.to_dict()
        else:
            informaciones_adicionales = self.informaciones_adicionales

        transporte: dict[str, Any] | None | Unset
        if isinstance(self.transporte, Unset):
            transporte = UNSET
        elif isinstance(self.transporte, Ecf33Transporte):
            transporte = self.transporte.to_dict()
        else:
            transporte = self.transporte

        otra_moneda: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda, Unset):
            otra_moneda = UNSET
        elif isinstance(self.otra_moneda, Ecf33OtraMoneda):
            otra_moneda = self.otra_moneda.to_dict()
        else:
            otra_moneda = self.otra_moneda


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "version": version,
            "idDoc": id_doc,
            "emisor": emisor,
            "totales": totales,
        })
        if comprador is not UNSET:
            field_dict["comprador"] = comprador
        if informaciones_adicionales is not UNSET:
            field_dict["informacionesAdicionales"] = informaciones_adicionales
        if transporte is not UNSET:
            field_dict["transporte"] = transporte
        if otra_moneda is not UNSET:
            field_dict["otraMoneda"] = otra_moneda

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_33_comprador import Ecf33Comprador
        from ..models.ecf_33_emisor import Ecf33Emisor
        from ..models.ecf_33_id_doc import Ecf33IdDoc
        from ..models.ecf_33_informaciones_adicionales import Ecf33InformacionesAdicionales
        from ..models.ecf_33_otra_moneda import Ecf33OtraMoneda
        from ..models.ecf_33_totales import Ecf33Totales
        from ..models.ecf_33_transporte import Ecf33Transporte
        d = dict(src_dict)
        version = Ecf33VersionType(d.pop("version"))




        id_doc = Ecf33IdDoc.from_dict(d.pop("idDoc"))




        emisor = Ecf33Emisor.from_dict(d.pop("emisor"))




        totales = Ecf33Totales.from_dict(d.pop("totales"))




        def _parse_comprador(data: object) -> Ecf33Comprador | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                comprador_type_1 = Ecf33Comprador.from_dict(data)



                return comprador_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf33Comprador | None | Unset, data)

        comprador = _parse_comprador(d.pop("comprador", UNSET))


        def _parse_informaciones_adicionales(data: object) -> Ecf33InformacionesAdicionales | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                informaciones_adicionales_type_1 = Ecf33InformacionesAdicionales.from_dict(data)



                return informaciones_adicionales_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf33InformacionesAdicionales | None | Unset, data)

        informaciones_adicionales = _parse_informaciones_adicionales(d.pop("informacionesAdicionales", UNSET))


        def _parse_transporte(data: object) -> Ecf33Transporte | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transporte_type_1 = Ecf33Transporte.from_dict(data)



                return transporte_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf33Transporte | None | Unset, data)

        transporte = _parse_transporte(d.pop("transporte", UNSET))


        def _parse_otra_moneda(data: object) -> Ecf33OtraMoneda | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_type_1 = Ecf33OtraMoneda.from_dict(data)



                return otra_moneda_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf33OtraMoneda | None | Unset, data)

        otra_moneda = _parse_otra_moneda(d.pop("otraMoneda", UNSET))


        ecf_33_encabezado = cls(
            version=version,
            id_doc=id_doc,
            emisor=emisor,
            totales=totales,
            comprador=comprador,
            informaciones_adicionales=informaciones_adicionales,
            transporte=transporte,
            otra_moneda=otra_moneda,
        )


        ecf_33_encabezado.additional_properties = d
        return ecf_33_encabezado

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
