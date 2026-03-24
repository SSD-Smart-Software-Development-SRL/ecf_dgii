from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_32_version_type import Ecf32VersionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_32_comprador import Ecf32Comprador
  from ..models.ecf_32_emisor import Ecf32Emisor
  from ..models.ecf_32_id_doc import Ecf32IdDoc
  from ..models.ecf_32_informaciones_adicionales import Ecf32InformacionesAdicionales
  from ..models.ecf_32_otra_moneda import Ecf32OtraMoneda
  from ..models.ecf_32_totales import Ecf32Totales
  from ..models.ecf_32_transporte import Ecf32Transporte





T = TypeVar("T", bound="Ecf32Encabezado")



@_attrs_define
class Ecf32Encabezado:
    """ 
        Example:
            {'transporte': '', 'informacionesAdicionales': '', 'comprador': {'direccionComprador': 'direccionComprador',
                'correoComprador': 'correoComprador', 'fechaOrdenCompra': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'responsablePago': 'responsablePago',
                'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador', 'identificadorExtranjero':
                'identificadorExtranjero', 'municipioComprador': '', 'rncComprador': 'rncComprador', 'codigoInternoComprador':
                'codigoInternoComprador', 'direccionEntrega': 'direccionEntrega', 'numeroOrdenCompra': 'numeroOrdenCompra',
                'informacionAdicionalComprador': 'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador',
                'contactoEntrega': 'contactoEntrega', 'fechaEntrega': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'telefonoAdicional': 'telefonoAdicional'}, 'idDoc':
                {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'indicadorMontoGravado': '', 'bancoPago':
                'bancoPago', 'indicadorEnvioDiferido': '', 'tipoPago': 'Contado', 'totalPaginas': 6,
                'indicadorServicioTodoIncluido': '', 'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago':
                'Efectivo'}, {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version':
                'Version1_0', 'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta':
                'rutaVenta', 'codigoVendedor': 'codigoVendedor'}, 'totales': {'montoPeriodo': None, 'montoGravadoI3': None,
                'montoGravadoI2': None, 'montoAvancePago': None, 'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1':
                None, 'totalITBIS2': None, 'itbiS2': None, 'montoImpuestoAdicional': 5.962133916683182, 'itbiS1': None,
                'itbiS3': None, 'totalITBIS': None, 'montoNoFacturable': 2.3021358869347655, 'impuestosAdicionales':
                [{'tipoImpuesto': '001', 'montoImpuestoSelectivoConsumoAdvalorem': None, 'tasaImpuestoAdicional':
                5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None, 'otrosImpuestosAdicionales': None},
                {'tipoImpuesto': '001', 'montoImpuestoSelectivoConsumoAdvalorem': None, 'tasaImpuestoAdicional':
                5.637376656633329, 'montoImpuestoSelectivoConsumoEspecifico': None, 'otrosImpuestosAdicionales': None}],
                'saldoAnterior': None, 'montoExento': None, 'montoGravadoTotal': 1.4658129805029452, 'valorPagar': None,
                'montoTotal': None}}

        Attributes:
            version (Ecf32VersionType):
            id_doc (Ecf32IdDoc):  Example: {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56,
                7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'indicadorMontoGravado': '', 'bancoPago':
                'bancoPago', 'indicadorEnvioDiferido': '', 'tipoPago': 'Contado', 'totalPaginas': 6,
                'indicadorServicioTodoIncluido': '', 'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago':
                'Efectivo'}, {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}.
            emisor (Ecf32Emisor):  Example: {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta':
                'rutaVenta', 'codigoVendedor': 'codigoVendedor'}.
            comprador (Ecf32Comprador):  Example: {'direccionComprador': 'direccionComprador', 'correoComprador':
                'correoComprador', 'fechaOrdenCompra': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'responsablePago': 'responsablePago',
                'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador', 'identificadorExtranjero':
                'identificadorExtranjero', 'municipioComprador': '', 'rncComprador': 'rncComprador', 'codigoInternoComprador':
                'codigoInternoComprador', 'direccionEntrega': 'direccionEntrega', 'numeroOrdenCompra': 'numeroOrdenCompra',
                'informacionAdicionalComprador': 'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador',
                'contactoEntrega': 'contactoEntrega', 'fechaEntrega': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'telefonoAdicional': 'telefonoAdicional'}.
            totales (Ecf32Totales):  Example: {'montoPeriodo': None, 'montoGravadoI3': None, 'montoGravadoI2': None,
                'montoAvancePago': None, 'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1': None, 'totalITBIS2': None,
                'itbiS2': None, 'montoImpuestoAdicional': 5.962133916683182, 'itbiS1': None, 'itbiS3': None, 'totalITBIS': None,
                'montoNoFacturable': 2.3021358869347655, 'impuestosAdicionales': [{'tipoImpuesto': '001',
                'montoImpuestoSelectivoConsumoAdvalorem': None, 'tasaImpuestoAdicional': 5.637376656633329,
                'montoImpuestoSelectivoConsumoEspecifico': None, 'otrosImpuestosAdicionales': None}, {'tipoImpuesto': '001',
                'montoImpuestoSelectivoConsumoAdvalorem': None, 'tasaImpuestoAdicional': 5.637376656633329,
                'montoImpuestoSelectivoConsumoEspecifico': None, 'otrosImpuestosAdicionales': None}], 'saldoAnterior': None,
                'montoExento': None, 'montoGravadoTotal': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None}.
            informaciones_adicionales (Ecf32InformacionesAdicionales | None | Unset):
            transporte (Ecf32Transporte | None | Unset):
            otra_moneda (Ecf32OtraMoneda | None | Unset):
     """

    version: Ecf32VersionType
    id_doc: Ecf32IdDoc
    emisor: Ecf32Emisor
    comprador: Ecf32Comprador
    totales: Ecf32Totales
    informaciones_adicionales: Ecf32InformacionesAdicionales | None | Unset = UNSET
    transporte: Ecf32Transporte | None | Unset = UNSET
    otra_moneda: Ecf32OtraMoneda | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_32_comprador import Ecf32Comprador
        from ..models.ecf_32_emisor import Ecf32Emisor
        from ..models.ecf_32_id_doc import Ecf32IdDoc
        from ..models.ecf_32_informaciones_adicionales import Ecf32InformacionesAdicionales
        from ..models.ecf_32_otra_moneda import Ecf32OtraMoneda
        from ..models.ecf_32_totales import Ecf32Totales
        from ..models.ecf_32_transporte import Ecf32Transporte
        version = self.version.value

        id_doc = self.id_doc.to_dict()

        emisor = self.emisor.to_dict()

        comprador = self.comprador.to_dict()

        totales = self.totales.to_dict()

        informaciones_adicionales: dict[str, Any] | None | Unset
        if isinstance(self.informaciones_adicionales, Unset):
            informaciones_adicionales = UNSET
        elif isinstance(self.informaciones_adicionales, Ecf32InformacionesAdicionales):
            informaciones_adicionales = self.informaciones_adicionales.to_dict()
        else:
            informaciones_adicionales = self.informaciones_adicionales

        transporte: dict[str, Any] | None | Unset
        if isinstance(self.transporte, Unset):
            transporte = UNSET
        elif isinstance(self.transporte, Ecf32Transporte):
            transporte = self.transporte.to_dict()
        else:
            transporte = self.transporte

        otra_moneda: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda, Unset):
            otra_moneda = UNSET
        elif isinstance(self.otra_moneda, Ecf32OtraMoneda):
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
        from ..models.ecf_32_comprador import Ecf32Comprador
        from ..models.ecf_32_emisor import Ecf32Emisor
        from ..models.ecf_32_id_doc import Ecf32IdDoc
        from ..models.ecf_32_informaciones_adicionales import Ecf32InformacionesAdicionales
        from ..models.ecf_32_otra_moneda import Ecf32OtraMoneda
        from ..models.ecf_32_totales import Ecf32Totales
        from ..models.ecf_32_transporte import Ecf32Transporte
        d = dict(src_dict)
        version = Ecf32VersionType(d.pop("version"))




        id_doc = Ecf32IdDoc.from_dict(d.pop("idDoc"))




        emisor = Ecf32Emisor.from_dict(d.pop("emisor"))




        comprador = Ecf32Comprador.from_dict(d.pop("comprador"))




        totales = Ecf32Totales.from_dict(d.pop("totales"))




        def _parse_informaciones_adicionales(data: object) -> Ecf32InformacionesAdicionales | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                informaciones_adicionales_type_1 = Ecf32InformacionesAdicionales.from_dict(data)



                return informaciones_adicionales_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf32InformacionesAdicionales | None | Unset, data)

        informaciones_adicionales = _parse_informaciones_adicionales(d.pop("informacionesAdicionales", UNSET))


        def _parse_transporte(data: object) -> Ecf32Transporte | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transporte_type_1 = Ecf32Transporte.from_dict(data)



                return transporte_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf32Transporte | None | Unset, data)

        transporte = _parse_transporte(d.pop("transporte", UNSET))


        def _parse_otra_moneda(data: object) -> Ecf32OtraMoneda | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_type_1 = Ecf32OtraMoneda.from_dict(data)



                return otra_moneda_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf32OtraMoneda | None | Unset, data)

        otra_moneda = _parse_otra_moneda(d.pop("otraMoneda", UNSET))


        ecf_32_encabezado = cls(
            version=version,
            id_doc=id_doc,
            emisor=emisor,
            comprador=comprador,
            totales=totales,
            informaciones_adicionales=informaciones_adicionales,
            transporte=transporte,
            otra_moneda=otra_moneda,
        )


        ecf_32_encabezado.additional_properties = d
        return ecf_32_encabezado

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
