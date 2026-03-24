from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ecf_43_version_type import Ecf43VersionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ecf_43_emisor import Ecf43Emisor
  from ..models.ecf_43_id_doc import Ecf43IdDoc
  from ..models.ecf_43_otra_moneda import Ecf43OtraMoneda
  from ..models.ecf_43_totales import Ecf43Totales





T = TypeVar("T", bound="Ecf43Encabezado")



@_attrs_define
class Ecf43Encabezado:
    """ 
        Example:
            {'idDoc': {'encf': 'encf', 'tipoeCF': 'FacturaDeCreditoFiscalElectronica', 'tipoPago': '', 'totalPaginas': 0,
                'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}, 'otraMoneda': '', 'version': 'Version1_0',
                'emisor': {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'}, 'totales': {'montoPeriodo': 5.962133916683182,
                'saldoAnterior': None, 'montoAvancePago': None, 'montoExento': 6.027456183070403, 'valorPagar': None,
                'montoTotal': 1.4658129805029452}}

        Attributes:
            version (Ecf43VersionType):
            id_doc (Ecf43IdDoc):  Example: {'encf': 'encf', 'tipoeCF': 'FacturaDeCreditoFiscalElectronica', 'tipoPago': '',
                'totalPaginas': 0, 'fechaVencimientoSecuencia': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}.
            emisor (Ecf43Emisor):  Example: {'direccionEmisor': 'direccionEmisor', 'razonSocialEmisor': 'razonSocialEmisor',
                'informacionAdicionalEmisor': 'informacionAdicionalEmisor', 'municipio': '', 'fechaEmision': datetime.date(2000,
                1, 23), 'provincia': '', 'actividadEconomica': 'actividadEconomica', 'rncEmisor': 'rncEmisor', 'correoEmisor':
                'correoEmisor', 'webSite': 'webSite', 'tablaTelefonoEmisor': ['tablaTelefonoEmisor', 'tablaTelefonoEmisor'],
                'sucursal': 'sucursal', 'numeroPedidoInterno': 'numeroPedidoInterno', 'numeroFacturaInterna':
                'numeroFacturaInterna', 'nombreComercial': 'nombreComercial'}.
            totales (Ecf43Totales):  Example: {'montoPeriodo': 5.962133916683182, 'saldoAnterior': None, 'montoAvancePago':
                None, 'montoExento': 6.027456183070403, 'valorPagar': None, 'montoTotal': 1.4658129805029452}.
            otra_moneda (Ecf43OtraMoneda | None | Unset):
     """

    version: Ecf43VersionType
    id_doc: Ecf43IdDoc
    emisor: Ecf43Emisor
    totales: Ecf43Totales
    otra_moneda: Ecf43OtraMoneda | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ecf_43_emisor import Ecf43Emisor
        from ..models.ecf_43_id_doc import Ecf43IdDoc
        from ..models.ecf_43_otra_moneda import Ecf43OtraMoneda
        from ..models.ecf_43_totales import Ecf43Totales
        version = self.version.value

        id_doc = self.id_doc.to_dict()

        emisor = self.emisor.to_dict()

        totales = self.totales.to_dict()

        otra_moneda: dict[str, Any] | None | Unset
        if isinstance(self.otra_moneda, Unset):
            otra_moneda = UNSET
        elif isinstance(self.otra_moneda, Ecf43OtraMoneda):
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
        if otra_moneda is not UNSET:
            field_dict["otraMoneda"] = otra_moneda

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ecf_43_emisor import Ecf43Emisor
        from ..models.ecf_43_id_doc import Ecf43IdDoc
        from ..models.ecf_43_otra_moneda import Ecf43OtraMoneda
        from ..models.ecf_43_totales import Ecf43Totales
        d = dict(src_dict)
        version = Ecf43VersionType(d.pop("version"))




        id_doc = Ecf43IdDoc.from_dict(d.pop("idDoc"))




        emisor = Ecf43Emisor.from_dict(d.pop("emisor"))




        totales = Ecf43Totales.from_dict(d.pop("totales"))




        def _parse_otra_moneda(data: object) -> Ecf43OtraMoneda | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                otra_moneda_type_1 = Ecf43OtraMoneda.from_dict(data)



                return otra_moneda_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Ecf43OtraMoneda | None | Unset, data)

        otra_moneda = _parse_otra_moneda(d.pop("otraMoneda", UNSET))


        ecf_43_encabezado = cls(
            version=version,
            id_doc=id_doc,
            emisor=emisor,
            totales=totales,
            otra_moneda=otra_moneda,
        )


        ecf_43_encabezado.additional_properties = d
        return ecf_43_encabezado

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
