from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_41_version_type import Ecf41VersionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_41_comprador import Ecf41Comprador
  from ..models.ecf_41_emisor import Ecf41Emisor
  from ..models.ecf_41_id_doc import Ecf41IdDoc
  from ..models.ecf_41_otra_moneda import Ecf41OtraMoneda
  from ..models.ecf_41_totales import Ecf41Totales





T = TypeVar("T", bound="Ecf41Encabezado")



@_attrs_define
class Ecf41Encabezado:
    """ 
        Example:
            {'comprador': {'direccionComprador': 'direccionComprador', 'correoComprador': 'correoComprador',
                'responsablePago': 'responsablePago', 'informacionAdicionalComprador': 'informacionAdicionalComprador',
                'contactoComprador': 'contactoComprador', 'provinciaComprador': '', 'razonSocialComprador':
                'razonSocialComprador', 'municipioComprador': '', 'rncComprador': 'rncComprador', 'codigoInternoComprador':
                'codigoInternoComprador'}, 'idDoc': {'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroCuentaPago': 'numeroCuentaPago',
                'indicadorMontoGravado': '', 'encf': 'encf', 'tipoCuentaPago': '', 'bancoPago': 'bancoPago', 'tipoeCF':
                'FacturaDeCreditoFiscalElectronica', 'tipoPago': '', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'terminoPago': 'terminoPago', 'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'},
                {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}, 'otraMoneda': '', 'version': 'Version1_0',
                'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'}, 'totales': {'montoPeriodo': 5.962133916683182,
                'totalISRPercepcion': None, 'montoGravadoI3': None, 'montoGravadoI2': None, 'montoAvancePago': None,
                'montoGravadoI1': None, 'totalITBIS3': None, 'totalITBIS1': None, 'totalITBIS2': None, 'totalITBISPercepcion':
                None, 'itbiS2': None, 'itbiS1': None, 'itbiS3': None, 'totalITBISRetenido': None, 'totalITBIS': None,
                'saldoAnterior': None, 'totalISRRetencion': None, 'montoExento': None, 'montoGravadoTotal': 1.4658129805029452,
                'valorPagar': None, 'montoTotal': None}}

        Attributes:
            version (Ecf41VersionType):
            id_doc (Ecf41IdDoc):  Example: {'fechaLimitePago': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'numeroCuentaPago': 'numeroCuentaPago',
                'indicadorMontoGravado': '', 'encf': 'encf', 'tipoCuentaPago': '', 'bancoPago': 'bancoPago', 'tipoeCF':
                'FacturaDeCreditoFiscalElectronica', 'tipoPago': '', 'totalPaginas': 6, 'fechaVencimientoSecuencia':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'terminoPago': 'terminoPago', 'tablaFormasPago': [{'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'},
                {'montoPago': 0.8008281904610115, 'formaPago': 'Efectivo'}]}.
            emisor (Ecf41Emisor):  Example: {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'}.
            comprador (Ecf41Comprador):  Example: {'direccionComprador': 'direccionComprador', 'correoComprador':
                'correoComprador', 'responsablePago': 'responsablePago', 'informacionAdicionalComprador':
                'informacionAdicionalComprador', 'contactoComprador': 'contactoComprador', 'provinciaComprador': '',
                'razonSocialComprador': 'razonSocialComprador', 'municipioComprador': '', 'rncComprador': 'rncComprador',
                'codigoInternoComprador': 'codigoInternoComprador'}.
            totales (Ecf41Totales):  Example: {'montoPeriodo': 5.962133916683182, 'totalISRPercepcion': None,
                'montoGravadoI3': None, 'montoGravadoI2': None, 'montoAvancePago': None, 'montoGravadoI1': None, 'totalITBIS3':
                None, 'totalITBIS1': None, 'totalITBIS2': None, 'totalITBISPercepcion': None, 'itbiS2': None, 'itbiS1': None,
                'itbiS3': None, 'totalITBISRetenido': None, 'totalITBIS': None, 'saldoAnterior': None, 'totalISRRetencion':
                None, 'montoExento': None, 'montoGravadoTotal': 1.4658129805029452, 'valorPagar': None, 'montoTotal': None}.
            otra_moneda (Ecf41OtraMoneda | None | Unset):
     """

    version: Ecf41VersionType
    id_doc: Ecf41IdDoc
    emisor: Ecf41Emisor
    comprador: Ecf41Comprador
    totales: Ecf41Totales
    otra_moneda: Ecf41OtraMoneda | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_41_comprador import Ecf41Comprador
        from ..models.ecf_41_emisor import Ecf41Emisor
        from ..models.ecf_41_id_doc import Ecf41IdDoc
        from ..models.ecf_41_otra_moneda import Ecf41OtraMoneda
        from ..models.ecf_41_totales import Ecf41Totales
        version = self.version.value

        id_doc = self.id_doc.to_dict()

        emisor = self.emisor.to_dict()

        comprador = self.comprador.to_dict()

        totales = self.totales.to_dict()

        otra_moneda: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda, Unset):
            otra_moneda = UNSET
        elif isinstance(self.otra_moneda, Ecf41OtraMoneda):
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
        if otra_moneda is not UNSET:
            field_dict["otraMoneda"] = otra_moneda

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_41_comprador import Ecf41Comprador
        from ..models.ecf_41_emisor import Ecf41Emisor
        from ..models.ecf_41_id_doc import Ecf41IdDoc
        from ..models.ecf_41_otra_moneda import Ecf41OtraMoneda
        from ..models.ecf_41_totales import Ecf41Totales
        d = dict(src_dict)
        version = Ecf41VersionType(d.pop("version"))




        id_doc = Ecf41IdDoc.from_dict(d.pop("idDoc"))




        emisor = Ecf41Emisor.from_dict(d.pop("emisor"))




        comprador = Ecf41Comprador.from_dict(d.pop("comprador"))




        totales = Ecf41Totales.from_dict(d.pop("totales"))




        def _parse_otra_moneda(data: object) -> Ecf41OtraMoneda | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_type_1 = Ecf41OtraMoneda.from_dict(data)



                return otra_moneda_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf41OtraMoneda | None | Unset, data)

        otra_moneda = _parse_otra_moneda(d.pop("otraMoneda", UNSET))


        ecf_41_encabezado = cls(
            version=version,
            id_doc=id_doc,
            emisor=emisor,
            comprador=comprador,
            totales=totales,
            otra_moneda=otra_moneda,
        )


        ecf_41_encabezado.additional_properties = d
        return ecf_41_encabezado

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
