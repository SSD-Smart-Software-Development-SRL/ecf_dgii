from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.all_tipo_ecf_types_type_1 import AllTipoECFTypesType1
from ..models.dgii_environment import DGIIEnvironment
from ..models.ecf_estado_type_1 import EcfEstadoType1
from ..models.ecf_progress import EcfProgress
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="EcfResponse")



@_attrs_define
class EcfResponse:
    """ 
        Example:
            {'fileName': 'fileName', 'encf': 'encf', 'codSec': 'codSec', 'rncReceptor': 'rncReceptor', 'dgiiEnvironment':
                'Test', 'secuenciaUtilizada': True, 'messageId': '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'ecfContent':
                'ecfContent', 'tipoEcf': 'FacturaDeCreditoFiscalElectronica', 'fechaEmision': datetime.date(2000, 1, 23),
                'impresionUrl': 'impresionUrl', 'rncEmisor': 'rncEmisor', 'emisorReceptorErrors': 'emisorReceptorErrors',
                'queueName': 'queueName', 'estatus': '', 'includeEcfContent': True, 'fechaFirma': datetime.datetime(2000, 1, 23,
                4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tenantId':
                '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'progress': 'New', 'mensaje': 'mensaje', 'montoTotal':
                0.8008281904610115, 'errors': 'errors', 'timestamp': datetime.datetime(2000, 1, 23, 4, 56, 7,
                tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00'))}

        Attributes:
            message_id (UUID):
            timestamp (datetime.datetime):
            fecha_emision (datetime.date):
            queue_name (str):
            include_ecf_content (bool):
            ecf_content (str):
            tipo_ecf (AllTipoECFTypesType1 | None):
            encf (str):
            rnc_emisor (str):
            rnc_receptor (None | str):
            monto_total (float | str):
            file_name (None | str):
            tenant_id (UUID):
            estatus (EcfEstadoType1 | None):
            cod_sec (None | str):
            fecha_firma (datetime.datetime | None):
            mensaje (None | str):
            errors (None | str):
            progress (EcfProgress):
            emisor_receptor_errors (None | str):
            secuencia_utilizada (bool | None):
            dgii_environment (DGIIEnvironment):
            impresion_url (None | str | Unset):
     """

    message_id: UUID
    timestamp: datetime.datetime
    fecha_emision: datetime.date
    queue_name: str
    include_ecf_content: bool
    ecf_content: str
    tipo_ecf: AllTipoECFTypesType1 | None
    encf: str
    rnc_emisor: str
    rnc_receptor: None | str
    monto_total: float | str
    file_name: None | str
    tenant_id: UUID
    estatus: EcfEstadoType1 | None
    cod_sec: None | str
    fecha_firma: datetime.datetime | None
    mensaje: None | str
    errors: None | str
    progress: EcfProgress
    emisor_receptor_errors: None | str
    secuencia_utilizada: bool | None
    dgii_environment: DGIIEnvironment
    impresion_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message_id = str(self.message_id)

        timestamp = self.timestamp.isoformat()

        fecha_emision = self.fecha_emision.isoformat()

        queue_name = self.queue_name

        include_ecf_content = self.include_ecf_content

        ecf_content = self.ecf_content

        tipo_ecf: None | str
        if isinstance(self.tipo_ecf, AllTipoECFTypesType1):
            tipo_ecf = self.tipo_ecf.value
        else:
            tipo_ecf = self.tipo_ecf

        encf = self.encf

        rnc_emisor = self.rnc_emisor

        rnc_receptor: None | str
        rnc_receptor = self.rnc_receptor

        monto_total: float | str
        monto_total = self.monto_total

        file_name: None | str
        file_name = self.file_name

        tenant_id = str(self.tenant_id)

        estatus: None | str
        if isinstance(self.estatus, EcfEstadoType1):
            estatus = self.estatus.value
        else:
            estatus = self.estatus

        cod_sec: None | str
        cod_sec = self.cod_sec

        fecha_firma: None | str
        if isinstance(self.fecha_firma, datetime.datetime):
            fecha_firma = self.fecha_firma.isoformat()
        else:
            fecha_firma = self.fecha_firma

        mensaje: None | str
        mensaje = self.mensaje

        errors: None | str
        errors = self.errors

        progress = self.progress.value

        emisor_receptor_errors: None | str
        emisor_receptor_errors = self.emisor_receptor_errors

        secuencia_utilizada: bool | None
        secuencia_utilizada = self.secuencia_utilizada

        dgii_environment = self.dgii_environment.value

        impresion_url: None | str | Unset
        if isinstance(self.impresion_url, Unset):
            impresion_url = UNSET
        else:
            impresion_url = self.impresion_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "messageId": message_id,
            "timestamp": timestamp,
            "fechaEmision": fecha_emision,
            "queueName": queue_name,
            "includeEcfContent": include_ecf_content,
            "ecfContent": ecf_content,
            "tipoEcf": tipo_ecf,
            "encf": encf,
            "rncEmisor": rnc_emisor,
            "rncReceptor": rnc_receptor,
            "montoTotal": monto_total,
            "fileName": file_name,
            "tenantId": tenant_id,
            "estatus": estatus,
            "codSec": cod_sec,
            "fechaFirma": fecha_firma,
            "mensaje": mensaje,
            "errors": errors,
            "progress": progress,
            "emisorReceptorErrors": emisor_receptor_errors,
            "secuenciaUtilizada": secuencia_utilizada,
            "dgiiEnvironment": dgii_environment,
        })
        if impresion_url is not UNSET:
            field_dict["impresionUrl"] = impresion_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = UUID(d.pop("messageId"))




        timestamp = isoparse(d.pop("timestamp"))




        fecha_emision = isoparse(d.pop("fechaEmision")).date()




        queue_name = d.pop("queueName")

        include_ecf_content = d.pop("includeEcfContent")

        ecf_content = d.pop("ecfContent")

        def _parse_tipo_ecf(data: object) -> AllTipoECFTypesType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_all_tipo_ecf_types_type_1 = AllTipoECFTypesType1(data)



                return componentsschemas_all_tipo_ecf_types_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AllTipoECFTypesType1 | None, data)

        tipo_ecf = _parse_tipo_ecf(d.pop("tipoEcf"))


        encf = d.pop("encf")

        rnc_emisor = d.pop("rncEmisor")

        def _parse_rnc_receptor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rnc_receptor = _parse_rnc_receptor(d.pop("rncReceptor"))


        def _parse_monto_total(data: object) -> float | str:
            return cast(float | str, data)

        monto_total = _parse_monto_total(d.pop("montoTotal"))


        def _parse_file_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_name = _parse_file_name(d.pop("fileName"))


        tenant_id = UUID(d.pop("tenantId"))




        def _parse_estatus(data: object) -> EcfEstadoType1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_ecf_estado_type_1 = EcfEstadoType1(data)



                return componentsschemas_ecf_estado_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EcfEstadoType1 | None, data)

        estatus = _parse_estatus(d.pop("estatus"))


        def _parse_cod_sec(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cod_sec = _parse_cod_sec(d.pop("codSec"))


        def _parse_fecha_firma(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_firma_type_0 = isoparse(data)



                return fecha_firma_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        fecha_firma = _parse_fecha_firma(d.pop("fechaFirma"))


        def _parse_mensaje(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mensaje = _parse_mensaje(d.pop("mensaje"))


        def _parse_errors(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        errors = _parse_errors(d.pop("errors"))


        progress = EcfProgress(d.pop("progress"))




        def _parse_emisor_receptor_errors(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        emisor_receptor_errors = _parse_emisor_receptor_errors(d.pop("emisorReceptorErrors"))


        def _parse_secuencia_utilizada(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        secuencia_utilizada = _parse_secuencia_utilizada(d.pop("secuenciaUtilizada"))


        dgii_environment = DGIIEnvironment(d.pop("dgiiEnvironment"))




        def _parse_impresion_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        impresion_url = _parse_impresion_url(d.pop("impresionUrl", UNSET))


        ecf_response = cls(
            message_id=message_id,
            timestamp=timestamp,
            fecha_emision=fecha_emision,
            queue_name=queue_name,
            include_ecf_content=include_ecf_content,
            ecf_content=ecf_content,
            tipo_ecf=tipo_ecf,
            encf=encf,
            rnc_emisor=rnc_emisor,
            rnc_receptor=rnc_receptor,
            monto_total=monto_total,
            file_name=file_name,
            tenant_id=tenant_id,
            estatus=estatus,
            cod_sec=cod_sec,
            fecha_firma=fecha_firma,
            mensaje=mensaje,
            errors=errors,
            progress=progress,
            emisor_receptor_errors=emisor_receptor_errors,
            secuencia_utilizada=secuencia_utilizada,
            dgii_environment=dgii_environment,
            impresion_url=impresion_url,
        )


        ecf_response.additional_properties = d
        return ecf_response

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
