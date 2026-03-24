from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_47_version_type import Ecf47VersionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_47_comprador import Ecf47Comprador
  from ..models.ecf_47_emisor import Ecf47Emisor
  from ..models.ecf_47_id_doc import Ecf47IdDoc
  from ..models.ecf_47_otra_moneda import Ecf47OtraMoneda
  from ..models.ecf_47_totales import Ecf47Totales
  from ..models.ecf_47_transporte import Ecf47Transporte





T = TypeVar("T", bound="Ecf47Encabezado")



@_attrs_define
class Ecf47Encabezado:
    """ 
        Example:
            {'transporte': '', 'comprador': '', 'idDoc': {'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'bancoPago': 'bancoPago', 'tipoPago': '',
                'totalPaginas': 6, 'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tablaFormasPago': [{'montoPago':
                0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]},
                'otraMoneda': '', 'version': 'Version1_0', 'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor':
                'razonSocialEmisor', 'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '',
                'fechaEmision': datetime.date(2000, 1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica',
                'rncEmisor': 'rncEmisor', 'correoEmisor': 'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor':
                ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'], 'sucursal': 'sucursal', 'numeroPedidoInterno':
                'numeroPedidoInterno', 'numeroFacturaInterna': 'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'},
                'totales': {'montoPeriodo': 5.962133916683182, 'saldoAnterior': None, 'montoAvancePago': None,
                'totalISRRetencion': None, 'montoExento': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None}}

        Attributes:
            version (Ecf47VersionType):
            id_doc (Ecf47IdDoc):  Example: {'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'encf': 'encf', 'fechaHasta':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'tipoCuentaPago': '', 'fechaDesde': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tipoeCF': 'FacturaDeCreditoFiscalElectronica',
                'terminoPago': 'terminoPago', 'numeroCuentaPago': 'numeroCuentaPago', 'bancoPago': 'bancoPago', 'tipoPago': '',
                'totalPaginas': 6, 'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tablaFormasPago': [{'montoPago':
                0.8008281904610115, 'formaPago': 'Efectivo'}, {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}.
            emisor (Ecf47Emisor):  Example: {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'}.
            totales (Ecf47Totales):  Example: {'montoPeriodo': 5.962133916683182, 'saldoAnterior': None, 'montoAvancePago':
                None, 'totalISRRetencion': None, 'montoExento': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None}.
            comprador (Ecf47Comprador | None | Unset):
            transporte (Ecf47Transporte | None | Unset):
            otra_moneda (Ecf47OtraMoneda | None | Unset):
     """

    version: Ecf47VersionType
    id_doc: Ecf47IdDoc
    emisor: Ecf47Emisor
    totales: Ecf47Totales
    comprador: Ecf47Comprador | None | Unset = UNSET
    transporte: Ecf47Transporte | None | Unset = UNSET
    otra_moneda: Ecf47OtraMoneda | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_47_comprador import Ecf47Comprador
        from ..models.ecf_47_emisor import Ecf47Emisor
        from ..models.ecf_47_id_doc import Ecf47IdDoc
        from ..models.ecf_47_otra_moneda import Ecf47OtraMoneda
        from ..models.ecf_47_totales import Ecf47Totales
        from ..models.ecf_47_transporte import Ecf47Transporte
        version = self.version.value

        id_doc = self.id_doc.to_dict()

        emisor = self.emisor.to_dict()

        totales = self.totales.to_dict()

        comprador: dict[str, Any] | None | Unset
        if isinstance(self.comprador, Unset):
            comprador = UNSET
        elif isinstance(self.comprador, Ecf47Comprador):
            comprador = self.comprador.to_dict()
        else:
            comprador = self.comprador

        transporte: dict[str, Any] | None | Unset
        if isinstance(self.transporte, Unset):
            transporte = UNSET
        elif isinstance(self.transporte, Ecf47Transporte):
            transporte = self.transporte.to_dict()
        else:
            transporte = self.transporte

        otra_moneda: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda, Unset):
            otra_moneda = UNSET
        elif isinstance(self.otra_moneda, Ecf47OtraMoneda):
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
        if transporte is not UNSET:
            field_dict["transporte"] = transporte
        if otra_moneda is not UNSET:
            field_dict["otraMoneda"] = otra_moneda

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_47_comprador import Ecf47Comprador
        from ..models.ecf_47_emisor import Ecf47Emisor
        from ..models.ecf_47_id_doc import Ecf47IdDoc
        from ..models.ecf_47_otra_moneda import Ecf47OtraMoneda
        from ..models.ecf_47_totales import Ecf47Totales
        from ..models.ecf_47_transporte import Ecf47Transporte
        d = dict(src_dict)
        version = Ecf47VersionType(d.pop("version"))




        id_doc = Ecf47IdDoc.from_dict(d.pop("idDoc"))




        emisor = Ecf47Emisor.from_dict(d.pop("emisor"))




        totales = Ecf47Totales.from_dict(d.pop("totales"))




        def _parse_comprador(data: object) -> Ecf47Comprador | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                comprador_type_1 = Ecf47Comprador.from_dict(data)



                return comprador_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf47Comprador | None | Unset, data)

        comprador = _parse_comprador(d.pop("comprador", UNSET))


        def _parse_transporte(data: object) -> Ecf47Transporte | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transporte_type_1 = Ecf47Transporte.from_dict(data)



                return transporte_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf47Transporte | None | Unset, data)

        transporte = _parse_transporte(d.pop("transporte", UNSET))


        def _parse_otra_moneda(data: object) -> Ecf47OtraMoneda | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_type_1 = Ecf47OtraMoneda.from_dict(data)



                return otra_moneda_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf47OtraMoneda | None | Unset, data)

        otra_moneda = _parse_otra_moneda(d.pop("otraMoneda", UNSET))


        ecf_47_encabezado = cls(
            version=version,
            id_doc=id_doc,
            emisor=emisor,
            totales=totales,
            comprador=comprador,
            transporte=transporte,
            otra_moneda=otra_moneda,
        )


        ecf_47_encabezado.additional_properties = d
        return ecf_47_encabezado

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
