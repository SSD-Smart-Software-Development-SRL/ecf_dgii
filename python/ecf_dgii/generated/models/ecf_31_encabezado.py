from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_31_version_type import Ecf31VersionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_31_comprador import Ecf31Comprador
  from ..models.ecf_31_emisor import Ecf31Emisor
  from ..models.ecf_31_id_doc import Ecf31IdDoc
  from ..models.ecf_31_informaciones_adicionales import Ecf31InformacionesAdicionales
  from ..models.ecf_31_otra_moneda import Ecf31OtraMoneda
  from ..models.ecf_31_totales import Ecf31Totales
  from ..models.ecf_31_transporte import Ecf31Transporte





T = TypeVar("T", bound="Ecf31Encabezado")



@_attrs_define
class Ecf31Encabezado:
    """ 
        Example:
            {'transporte': '', 'informacionesAdicionales': '', 'comprador': {'direccionComprador': 'direccionComprador',
                'correoComprador': 'correoComprador', 'fechaOrdenCompra': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'responsablePago': 'responsablePago',
                'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador', 'municipioComprador': '',
                'rncComprador': 'rncComprador', 'codigoInternoComprador': 'codigoInternoComprador', 'direccionEntrega':
                'direccionEntrega', 'numeroOrdenCompra': 'numeroOrdenCompra', 'informacionAdicionalComprador':
                'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador', 'contactoEntrega': 'contactoEntrega',
                'fechaEntrega': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'telefonoAdicional': 'telefonoAdicional'}, 'idDoc': {'tipoIngresos': '01', 'fechaLimitePago':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf':
                'encf', 'fechaHasta': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'indicadorMontoGravado': '', 'bancoPago':
                'bancoPago', 'indicadorEnvioDiferido': '', 'tipoPago': 'Contado', 'totalPaginas': 6,
                'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
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
            version (Ecf31VersionType):
            id_doc (Ecf31IdDoc):  Example: {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56,
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
            emisor (Ecf31Emisor):  Example: {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta':
                'rutaVenta', 'codigoVendedor': 'codigoVendedor'}.
            comprador (Ecf31Comprador):  Example: {'direccionComprador': 'direccionComprador', 'correoComprador':
                'correoComprador', 'fechaOrdenCompra': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'responsablePago': 'responsablePago',
                'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador', 'municipioComprador': '',
                'rncComprador': 'rncComprador', 'codigoInternoComprador': 'codigoInternoComprador', 'direccionEntrega':
                'direccionEntrega', 'numeroOrdenCompra': 'numeroOrdenCompra', 'informacionAdicionalComprador':
                'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador', 'contactoEntrega': 'contactoEntrega',
                'fechaEntrega': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'telefonoAdicional': 'telefonoAdicional'}.
            totales (Ecf31Totales):  Example: {'montoPeriodo': None, 'totalISRPercepcion': None, 'montoGravadoI3': None,
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
            informaciones_adicionales (Ecf31InformacionesAdicionales | None | Unset):
            transporte (Ecf31Transporte | None | Unset):
            otra_moneda (Ecf31OtraMoneda | None | Unset):
     """

    version: Ecf31VersionType
    id_doc: Ecf31IdDoc
    emisor: Ecf31Emisor
    comprador: Ecf31Comprador
    totales: Ecf31Totales
    informaciones_adicionales: Ecf31InformacionesAdicionales | None | Unset = UNSET
    transporte: Ecf31Transporte | None | Unset = UNSET
    otra_moneda: Ecf31OtraMoneda | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_31_comprador import Ecf31Comprador
        from ..models.ecf_31_emisor import Ecf31Emisor
        from ..models.ecf_31_id_doc import Ecf31IdDoc
        from ..models.ecf_31_informaciones_adicionales import Ecf31InformacionesAdicionales
        from ..models.ecf_31_otra_moneda import Ecf31OtraMoneda
        from ..models.ecf_31_totales import Ecf31Totales
        from ..models.ecf_31_transporte import Ecf31Transporte
        version = self.version.value

        id_doc = self.id_doc.to_dict()

        emisor = self.emisor.to_dict()

        comprador = self.comprador.to_dict()

        totales = self.totales.to_dict()

        informaciones_adicionales: dict[str, Any] | None | Unset
        if isinstance(self.informaciones_adicionales, Unset):
            informaciones_adicionales = UNSET
        elif isinstance(self.informaciones_adicionales, Ecf31InformacionesAdicionales):
            informaciones_adicionales = self.informaciones_adicionales.to_dict()
        else:
            informaciones_adicionales = self.informaciones_adicionales

        transporte: dict[str, Any] | None | Unset
        if isinstance(self.transporte, Unset):
            transporte = UNSET
        elif isinstance(self.transporte, Ecf31Transporte):
            transporte = self.transporte.to_dict()
        else:
            transporte = self.transporte

        otra_moneda: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda, Unset):
            otra_moneda = UNSET
        elif isinstance(self.otra_moneda, Ecf31OtraMoneda):
            otra_moneda = self.otra_moneda.to_dict()
        else:
            otra_moneda = self.otra_moneda


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "version": version,
            "idDoc": id_doc,
            "emisor": emisor,
            "comprador": comprador,
            "totales": totales,
        })
        if informaciones_adicionales is not UNSET:
            field_dict["informacionesAdicionales"] = informaciones_adicionales
        if transporte is not UNSET:
            field_dict["transporte"] = transporte
        if otra_moneda is not UNSET:
            field_dict["otraMoneda"] = otra_moneda

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_31_comprador import Ecf31Comprador
        from ..models.ecf_31_emisor import Ecf31Emisor
        from ..models.ecf_31_id_doc import Ecf31IdDoc
        from ..models.ecf_31_informaciones_adicionales import Ecf31InformacionesAdicionales
        from ..models.ecf_31_otra_moneda import Ecf31OtraMoneda
        from ..models.ecf_31_totales import Ecf31Totales
        from ..models.ecf_31_transporte import Ecf31Transporte
        d = dict(src_dict)
        version = Ecf31VersionType(d.pop("version"))




        id_doc = Ecf31IdDoc.from_dict(d.pop("idDoc"))




        emisor = Ecf31Emisor.from_dict(d.pop("emisor"))




        comprador = Ecf31Comprador.from_dict(d.pop("comprador"))




        totales = Ecf31Totales.from_dict(d.pop("totales"))




        def _parse_informaciones_adicionales(data: object) -> Ecf31InformacionesAdicionales | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                informaciones_adicionales_type_1 = Ecf31InformacionesAdicionales.from_dict(data)



                return informaciones_adicionales_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf31InformacionesAdicionales | None | Unset, data)

        informaciones_adicionales = _parse_informaciones_adicionales(d.pop("informacionesAdicionales", UNSET))


        def _parse_transporte(data: object) -> Ecf31Transporte | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transporte_type_1 = Ecf31Transporte.from_dict(data)



                return transporte_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf31Transporte | None | Unset, data)

        transporte = _parse_transporte(d.pop("transporte", UNSET))


        def _parse_otra_moneda(data: object) -> Ecf31OtraMoneda | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_type_1 = Ecf31OtraMoneda.from_dict(data)



                return otra_moneda_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf31OtraMoneda | None | Unset, data)

        otra_moneda = _parse_otra_moneda(d.pop("otraMoneda", UNSET))


        ecf_31_encabezado = cls(
            version=version,
            id_doc=id_doc,
            emisor=emisor,
            comprador=comprador,
            totales=totales,
            informaciones_adicionales=informaciones_adicionales,
            transporte=transporte,
            otra_moneda=otra_moneda,
        )


        ecf_31_encabezado.additional_properties = d
        return ecf_31_encabezado

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
