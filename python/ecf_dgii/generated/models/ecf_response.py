from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.all_tipo_ecf_types import AllTipoECFTypes
from ..models.dgii_environment import DGIIEnvironment
from ..models.ecf_estado_type_1 import EcfEstadoType1
from ..models.ecf_progress import EcfProgress
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acecf_summary_dto import AcecfSummaryDto


T = TypeVar("T", bound="EcfResponse")


@_attrs_define
class EcfResponse:
    """
    Attributes:
        message_id (UUID):
        timestamp (datetime.datetime):
        fecha_emision (datetime.date):
        queue_name (str):
        include_ecf_content (bool):
        ecf_content (str):
        tipo_ecf (AllTipoECFTypes):
        encf (str):
        rnc_emisor (str):
        monto_total (float | str):
        tenant_id (UUID):
        progress (EcfProgress):
        dgii_environment (DGIIEnvironment):
        rnc_receptor (None | str | Unset):
        file_name (None | str | Unset):
        estatus (EcfEstadoType1 | None | Unset):
        cod_sec (None | str | Unset):
        fecha_firma (datetime.datetime | None | Unset):
        mensaje (None | str | Unset):
        errors (None | str | Unset):
        emisor_receptor_errors (None | str | Unset):
        secuencia_utilizada (bool | None | Unset):
        acecfs (list[AcecfSummaryDto] | Unset): ACECFs received from the receptor for this outbound ECF.
        impresion_url (None | str | Unset):
    """

    message_id: UUID
    timestamp: datetime.datetime
    fecha_emision: datetime.date
    queue_name: str
    include_ecf_content: bool
    ecf_content: str
    tipo_ecf: AllTipoECFTypes
    encf: str
    rnc_emisor: str
    monto_total: float | str
    tenant_id: UUID
    progress: EcfProgress
    dgii_environment: DGIIEnvironment
    rnc_receptor: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    estatus: EcfEstadoType1 | None | Unset = UNSET
    cod_sec: None | str | Unset = UNSET
    fecha_firma: datetime.datetime | None | Unset = UNSET
    mensaje: None | str | Unset = UNSET
    errors: None | str | Unset = UNSET
    emisor_receptor_errors: None | str | Unset = UNSET
    secuencia_utilizada: bool | None | Unset = UNSET
    acecfs: list[AcecfSummaryDto] | Unset = UNSET
    impresion_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = str(self.message_id)

        timestamp = self.timestamp.isoformat()

        fecha_emision = self.fecha_emision.isoformat()

        queue_name = self.queue_name

        include_ecf_content = self.include_ecf_content

        ecf_content = self.ecf_content

        tipo_ecf = self.tipo_ecf.value

        encf = self.encf

        rnc_emisor = self.rnc_emisor

        monto_total: float | str
        monto_total = self.monto_total

        tenant_id = str(self.tenant_id)

        progress = self.progress.value

        dgii_environment = self.dgii_environment.value

        rnc_receptor: None | str | Unset
        if isinstance(self.rnc_receptor, Unset):
            rnc_receptor = UNSET
        else:
            rnc_receptor = self.rnc_receptor

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        estatus: None | str | Unset
        if isinstance(self.estatus, Unset):
            estatus = UNSET
        elif isinstance(self.estatus, EcfEstadoType1):
            estatus = self.estatus.value
        else:
            estatus = self.estatus

        cod_sec: None | str | Unset
        if isinstance(self.cod_sec, Unset):
            cod_sec = UNSET
        else:
            cod_sec = self.cod_sec

        fecha_firma: None | str | Unset
        if isinstance(self.fecha_firma, Unset):
            fecha_firma = UNSET
        elif isinstance(self.fecha_firma, datetime.datetime):
            fecha_firma = self.fecha_firma.isoformat()
        else:
            fecha_firma = self.fecha_firma

        mensaje: None | str | Unset
        if isinstance(self.mensaje, Unset):
            mensaje = UNSET
        else:
            mensaje = self.mensaje

        errors: None | str | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        else:
            errors = self.errors

        emisor_receptor_errors: None | str | Unset
        if isinstance(self.emisor_receptor_errors, Unset):
            emisor_receptor_errors = UNSET
        else:
            emisor_receptor_errors = self.emisor_receptor_errors

        secuencia_utilizada: bool | None | Unset
        if isinstance(self.secuencia_utilizada, Unset):
            secuencia_utilizada = UNSET
        else:
            secuencia_utilizada = self.secuencia_utilizada

        acecfs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acecfs, Unset):
            acecfs = []
            for acecfs_item_data in self.acecfs:
                acecfs_item = acecfs_item_data.to_dict()
                acecfs.append(acecfs_item)

        impresion_url: None | str | Unset
        if isinstance(self.impresion_url, Unset):
            impresion_url = UNSET
        else:
            impresion_url = self.impresion_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messageId": message_id,
                "timestamp": timestamp,
                "fechaEmision": fecha_emision,
                "queueName": queue_name,
                "includeEcfContent": include_ecf_content,
                "ecfContent": ecf_content,
                "tipoEcf": tipo_ecf,
                "encf": encf,
                "rncEmisor": rnc_emisor,
                "montoTotal": monto_total,
                "tenantId": tenant_id,
                "progress": progress,
                "dgiiEnvironment": dgii_environment,
            }
        )
        if rnc_receptor is not UNSET:
            field_dict["rncReceptor"] = rnc_receptor
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if estatus is not UNSET:
            field_dict["estatus"] = estatus
        if cod_sec is not UNSET:
            field_dict["codSec"] = cod_sec
        if fecha_firma is not UNSET:
            field_dict["fechaFirma"] = fecha_firma
        if mensaje is not UNSET:
            field_dict["mensaje"] = mensaje
        if errors is not UNSET:
            field_dict["errors"] = errors
        if emisor_receptor_errors is not UNSET:
            field_dict["emisorReceptorErrors"] = emisor_receptor_errors
        if secuencia_utilizada is not UNSET:
            field_dict["secuenciaUtilizada"] = secuencia_utilizada
        if acecfs is not UNSET:
            field_dict["acecfs"] = acecfs
        if impresion_url is not UNSET:
            field_dict["impresionUrl"] = impresion_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acecf_summary_dto import AcecfSummaryDto  # noqa: PLC0415

        d = dict(src_dict)
        message_id = UUID(d.pop("messageId"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        fecha_emision = datetime.date.fromisoformat(d.pop("fechaEmision"))

        queue_name = d.pop("queueName")

        include_ecf_content = d.pop("includeEcfContent")

        ecf_content = d.pop("ecfContent")

        tipo_ecf = AllTipoECFTypes(d.pop("tipoEcf"))

        encf = d.pop("encf")

        rnc_emisor = d.pop("rncEmisor")

        def _parse_monto_total(data: object) -> float | str:
            return cast(float | str, data)

        monto_total = _parse_monto_total(d.pop("montoTotal"))

        tenant_id = UUID(d.pop("tenantId"))

        progress = EcfProgress(d.pop("progress"))

        dgii_environment = DGIIEnvironment(d.pop("dgiiEnvironment"))

        def _parse_rnc_receptor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rnc_receptor = _parse_rnc_receptor(d.pop("rncReceptor", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_estatus(data: object) -> EcfEstadoType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_ecf_estado_type_1 = EcfEstadoType1(data)

                return componentsschemas_ecf_estado_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EcfEstadoType1 | None | Unset, data)

        estatus = _parse_estatus(d.pop("estatus", UNSET))

        def _parse_cod_sec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cod_sec = _parse_cod_sec(d.pop("codSec", UNSET))

        def _parse_fecha_firma(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fecha_firma_type_1 = datetime.datetime.fromisoformat(data)

                return fecha_firma_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        fecha_firma = _parse_fecha_firma(d.pop("fechaFirma", UNSET))

        def _parse_mensaje(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mensaje = _parse_mensaje(d.pop("mensaje", UNSET))

        def _parse_errors(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_emisor_receptor_errors(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        emisor_receptor_errors = _parse_emisor_receptor_errors(d.pop("emisorReceptorErrors", UNSET))

        def _parse_secuencia_utilizada(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        secuencia_utilizada = _parse_secuencia_utilizada(d.pop("secuenciaUtilizada", UNSET))

        _acecfs = d.pop("acecfs", UNSET)
        acecfs: list[AcecfSummaryDto] | Unset = UNSET
        if _acecfs is not UNSET:
            acecfs = []
            for acecfs_item_data in _acecfs:
                acecfs_item = AcecfSummaryDto.from_dict(acecfs_item_data)

                acecfs.append(acecfs_item)

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
            monto_total=monto_total,
            tenant_id=tenant_id,
            progress=progress,
            dgii_environment=dgii_environment,
            rnc_receptor=rnc_receptor,
            file_name=file_name,
            estatus=estatus,
            cod_sec=cod_sec,
            fecha_firma=fecha_firma,
            mensaje=mensaje,
            errors=errors,
            emisor_receptor_errors=emisor_receptor_errors,
            secuencia_utilizada=secuencia_utilizada,
            acecfs=acecfs,
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
