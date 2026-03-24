from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_46_version_type import Ecf46VersionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_46_comprador import Ecf46Comprador
  from ..models.ecf_46_emisor import Ecf46Emisor
  from ..models.ecf_46_id_doc import Ecf46IdDoc
  from ..models.ecf_46_informaciones_adicionales import Ecf46InformacionesAdicionales
  from ..models.ecf_46_otra_moneda import Ecf46OtraMoneda
  from ..models.ecf_46_totales import Ecf46Totales
  from ..models.ecf_46_transporte import Ecf46Transporte





T = TypeVar("T", bound="Ecf46Encabezado")



@_attrs_define
class Ecf46Encabezado:
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
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'telefonoAdicional': 'telefonoAdicional',
                'paisComprador': 'paisComprador'}, 'idDoc': {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1,
                23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'bancoPago': 'bancoPago',
                'indicadorEnvioDiferido': '', 'tipoPago': 'Contado', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago':
                0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version': 'Version1_0', 'emisor':
                {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor', 'informacionAdicionalEmisor':
                'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000, 1, 23), 'provincia': '',
                'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor': 'correoEmisor', 'webSite':
                'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'], 'sucursal': 'sucursal',
                'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna': 'numeroFacturaInterna', 'nombreComercial':
                'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta': 'rutaVenta', 'codigoVendedor': 'codigoVendedor'},
                'totales': {'totalITBIS': None, 'montoNoFacturable': 5.962133916683182, 'montoPeriodo': None, 'montoGravadoI3':
                None, 'saldoAnterior': None, 'montoAvancePago': None, 'totalITBIS3': None, 'montoGravadoTotal':
                1.4658129805029452, 'valorPagar': None, 'montoTotal': None, 'itbiS3': None}}

        Attributes:
            version (Ecf46VersionType):
            id_doc (Ecf46IdDoc):  Example: {'tipoIngresos': '01', 'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56,
                7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'bancoPago': 'bancoPago',
                'indicadorEnvioDiferido': '', 'tipoPago': 'Contado', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago':
                0.8008281904610115, 'formaPago': 'Efectivo'}]}.
            emisor (Ecf46Emisor):  Example: {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial', 'zonaVenta': 'zonaVenta', 'rutaVenta':
                'rutaVenta', 'codigoVendedor': 'codigoVendedor'}.
            comprador (Ecf46Comprador):  Example: {'direccionComprador': 'direccionComprador', 'correoComprador':
                'correoComprador', 'fechaOrdenCompra': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'responsablePago': 'responsablePago',
                'provinciaComprador': '', 'razonSocialComprador': 'razonSocialComprador', 'identificadorExtranjero':
                'identificadorExtranjero', 'municipioComprador': '', 'rncComprador': 'rncComprador', 'codigoInternoComprador':
                'codigoInternoComprador', 'direccionEntrega': 'direccionEntrega', 'numeroOrdenCompra': 'numeroOrdenCompra',
                'informacionAdicionalComprador': 'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador',
                'contactoEntrega': 'contactoEntrega', 'fechaEntrega': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'telefonoAdicional': 'telefonoAdicional',
                'paisComprador': 'paisComprador'}.
            totales (Ecf46Totales):  Example: {'totalITBIS': None, 'montoNoFacturable': 5.962133916683182, 'montoPeriodo':
                None, 'montoGravadoI3': None, 'saldoAnterior': None, 'montoAvancePago': None, 'totalITBIS3': None,
                'montoGravadoTotal': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None, 'itbiS3': None}.
            informaciones_adicionales (Ecf46InformacionesAdicionales | None | Unset):
            transporte (Ecf46Transporte | None | Unset):
            otra_moneda (Ecf46OtraMoneda | None | Unset):
     """

    version: Ecf46VersionType
    id_doc: Ecf46IdDoc
    emisor: Ecf46Emisor
    comprador: Ecf46Comprador
    totales: Ecf46Totales
    informaciones_adicionales: Ecf46InformacionesAdicionales | None | Unset = UNSET
    transporte: Ecf46Transporte | None | Unset = UNSET
    otra_moneda: Ecf46OtraMoneda | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_46_comprador import Ecf46Comprador
        from ..models.ecf_46_emisor import Ecf46Emisor
        from ..models.ecf_46_id_doc import Ecf46IdDoc
        from ..models.ecf_46_informaciones_adicionales import Ecf46InformacionesAdicionales
        from ..models.ecf_46_otra_moneda import Ecf46OtraMoneda
        from ..models.ecf_46_totales import Ecf46Totales
        from ..models.ecf_46_transporte import Ecf46Transporte
        version = self.version.value

        id_doc = self.id_doc.to_dict()

        emisor = self.emisor.to_dict()

        comprador = self.comprador.to_dict()

        totales = self.totales.to_dict()

        informaciones_adicionales: dict[str, Any] | None | Unset
        if isinstance(self.informaciones_adicionales, Unset):
            informaciones_adicionales = UNSET
        elif isinstance(self.informaciones_adicionales, Ecf46InformacionesAdicionales):
            informaciones_adicionales = self.informaciones_adicionales.to_dict()
        else:
            informaciones_adicionales = self.informaciones_adicionales

        transporte: dict[str, Any] | None | Unset
        if isinstance(self.transporte, Unset):
            transporte = UNSET
        elif isinstance(self.transporte, Ecf46Transporte):
            transporte = self.transporte.to_dict()
        else:
            transporte = self.transporte

        otra_moneda: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda, Unset):
            otra_moneda = UNSET
        elif isinstance(self.otra_moneda, Ecf46OtraMoneda):
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
        from ..models.ecf_46_comprador import Ecf46Comprador
        from ..models.ecf_46_emisor import Ecf46Emisor
        from ..models.ecf_46_id_doc import Ecf46IdDoc
        from ..models.ecf_46_informaciones_adicionales import Ecf46InformacionesAdicionales
        from ..models.ecf_46_otra_moneda import Ecf46OtraMoneda
        from ..models.ecf_46_totales import Ecf46Totales
        from ..models.ecf_46_transporte import Ecf46Transporte
        d = dict(src_dict)
        version = Ecf46VersionType(d.pop("version"))




        id_doc = Ecf46IdDoc.from_dict(d.pop("idDoc"))




        emisor = Ecf46Emisor.from_dict(d.pop("emisor"))




        comprador = Ecf46Comprador.from_dict(d.pop("comprador"))




        totales = Ecf46Totales.from_dict(d.pop("totales"))




        def _parse_informaciones_adicionales(data: object) -> Ecf46InformacionesAdicionales | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                informaciones_adicionales_type_1 = Ecf46InformacionesAdicionales.from_dict(data)



                return informaciones_adicionales_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf46InformacionesAdicionales | None | Unset, data)

        informaciones_adicionales = _parse_informaciones_adicionales(d.pop("informacionesAdicionales", UNSET))


        def _parse_transporte(data: object) -> Ecf46Transporte | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transporte_type_1 = Ecf46Transporte.from_dict(data)



                return transporte_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf46Transporte | None | Unset, data)

        transporte = _parse_transporte(d.pop("transporte", UNSET))


        def _parse_otra_moneda(data: object) -> Ecf46OtraMoneda | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_type_1 = Ecf46OtraMoneda.from_dict(data)



                return otra_moneda_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf46OtraMoneda | None | Unset, data)

        otra_moneda = _parse_otra_moneda(d.pop("otraMoneda", UNSET))


        ecf_46_encabezado = cls(
            version=version,
            id_doc=id_doc,
            emisor=emisor,
            comprador=comprador,
            totales=totales,
            informaciones_adicionales=informaciones_adicionales,
            transporte=transporte,
            otra_moneda=otra_moneda,
        )


        ecf_46_encabezado.additional_properties = d
        return ecf_46_encabezado

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
