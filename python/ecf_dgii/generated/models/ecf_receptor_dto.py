from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.all_tipo_ecf_types import AllTipoECFTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acecf_summary_dto import AcecfSummaryDto


T = TypeVar("T", bound="EcfReceptorDto")


@_attrs_define
class EcfReceptorDto:
    """
    Attributes:
        ecf_receptor_id (UUID | Unset):
        tenant_id (UUID | Unset):
        company_rnc (str | Unset):
        encf (str | Unset):
        rnc_emisor (str | Unset):
        rnc_receptor (str | Unset):
        tipo_ecf (AllTipoECFTypes | Unset):
        monto_total (float | str | Unset):
        fecha_emision (datetime.date | Unset):
        file_name (str | Unset):
        raw_json_data (str | Unset):
        created_on (datetime.datetime | Unset):
        fecha_firma (datetime.datetime | None | Unset):
        cod_sec (None | str | Unset):
        estado (int | None | str | Unset): Estado from the generated ARECF (ECFRecibido / ECFNoRecibido).
        progress (int | str | Unset): EcfReceptionRequest.Progress — Pending / Processing / Completed / Error.
        ambiente (str | Unset): DGII environment serving this tenant ("Test"/"Certification"/"Production").
        url_impresion (None | str | Unset): DGII consulta-timbre URL with QR query string.
        acecfs (list[AcecfSummaryDto] | Unset):
    """

    ecf_receptor_id: UUID | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    company_rnc: str | Unset = UNSET
    encf: str | Unset = UNSET
    rnc_emisor: str | Unset = UNSET
    rnc_receptor: str | Unset = UNSET
    tipo_ecf: AllTipoECFTypes | Unset = UNSET
    monto_total: float | str | Unset = UNSET
    fecha_emision: datetime.date | Unset = UNSET
    file_name: str | Unset = UNSET
    raw_json_data: str | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    fecha_firma: datetime.datetime | None | Unset = UNSET
    cod_sec: None | str | Unset = UNSET
    estado: int | None | str | Unset = UNSET
    progress: int | str | Unset = UNSET
    ambiente: str | Unset = UNSET
    url_impresion: None | str | Unset = UNSET
    acecfs: list[AcecfSummaryDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ecf_receptor_id: str | Unset = UNSET
        if not isinstance(self.ecf_receptor_id, Unset):
            ecf_receptor_id = str(self.ecf_receptor_id)

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)

        company_rnc = self.company_rnc

        encf = self.encf

        rnc_emisor = self.rnc_emisor

        rnc_receptor = self.rnc_receptor

        tipo_ecf: str | Unset = UNSET
        if not isinstance(self.tipo_ecf, Unset):
            tipo_ecf = self.tipo_ecf.value

        monto_total: float | str | Unset
        if isinstance(self.monto_total, Unset):
            monto_total = UNSET
        else:
            monto_total = self.monto_total

        fecha_emision: str | Unset = UNSET
        if not isinstance(self.fecha_emision, Unset):
            fecha_emision = self.fecha_emision.isoformat()

        file_name = self.file_name

        raw_json_data = self.raw_json_data

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        fecha_firma: None | str | Unset
        if isinstance(self.fecha_firma, Unset):
            fecha_firma = UNSET
        elif isinstance(self.fecha_firma, datetime.datetime):
            fecha_firma = self.fecha_firma.isoformat()
        else:
            fecha_firma = self.fecha_firma

        cod_sec: None | str | Unset
        if isinstance(self.cod_sec, Unset):
            cod_sec = UNSET
        else:
            cod_sec = self.cod_sec

        estado: int | None | str | Unset
        if isinstance(self.estado, Unset):
            estado = UNSET
        else:
            estado = self.estado

        progress: int | str | Unset
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

        ambiente = self.ambiente

        url_impresion: None | str | Unset
        if isinstance(self.url_impresion, Unset):
            url_impresion = UNSET
        else:
            url_impresion = self.url_impresion

        acecfs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acecfs, Unset):
            acecfs = []
            for acecfs_item_data in self.acecfs:
                acecfs_item = acecfs_item_data.to_dict()
                acecfs.append(acecfs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ecf_receptor_id is not UNSET:
            field_dict["ecfReceptorId"] = ecf_receptor_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if company_rnc is not UNSET:
            field_dict["companyRnc"] = company_rnc
        if encf is not UNSET:
            field_dict["encf"] = encf
        if rnc_emisor is not UNSET:
            field_dict["rncEmisor"] = rnc_emisor
        if rnc_receptor is not UNSET:
            field_dict["rncReceptor"] = rnc_receptor
        if tipo_ecf is not UNSET:
            field_dict["tipoEcf"] = tipo_ecf
        if monto_total is not UNSET:
            field_dict["montoTotal"] = monto_total
        if fecha_emision is not UNSET:
            field_dict["fechaEmision"] = fecha_emision
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if raw_json_data is not UNSET:
            field_dict["rawJsonData"] = raw_json_data
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if fecha_firma is not UNSET:
            field_dict["fechaFirma"] = fecha_firma
        if cod_sec is not UNSET:
            field_dict["codSec"] = cod_sec
        if estado is not UNSET:
            field_dict["estado"] = estado
        if progress is not UNSET:
            field_dict["progress"] = progress
        if ambiente is not UNSET:
            field_dict["ambiente"] = ambiente
        if url_impresion is not UNSET:
            field_dict["urlImpresion"] = url_impresion
        if acecfs is not UNSET:
            field_dict["acecfs"] = acecfs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acecf_summary_dto import AcecfSummaryDto

        d = dict(src_dict)
        _ecf_receptor_id = d.pop("ecfReceptorId", UNSET)
        ecf_receptor_id: UUID | Unset
        if isinstance(_ecf_receptor_id, Unset):
            ecf_receptor_id = UNSET
        else:
            ecf_receptor_id = UUID(_ecf_receptor_id)

        _tenant_id = d.pop("tenantId", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)

        company_rnc = d.pop("companyRnc", UNSET)

        encf = d.pop("encf", UNSET)

        rnc_emisor = d.pop("rncEmisor", UNSET)

        rnc_receptor = d.pop("rncReceptor", UNSET)

        _tipo_ecf = d.pop("tipoEcf", UNSET)
        tipo_ecf: AllTipoECFTypes | Unset
        if isinstance(_tipo_ecf, Unset):
            tipo_ecf = UNSET
        else:
            tipo_ecf = AllTipoECFTypes(_tipo_ecf)

        def _parse_monto_total(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        monto_total = _parse_monto_total(d.pop("montoTotal", UNSET))

        _fecha_emision = d.pop("fechaEmision", UNSET)
        fecha_emision: datetime.date | Unset
        if isinstance(_fecha_emision, Unset):
            fecha_emision = UNSET
        else:
            fecha_emision = datetime.date.fromisoformat(_fecha_emision)

        file_name = d.pop("fileName", UNSET)

        raw_json_data = d.pop("rawJsonData", UNSET)

        _created_on = d.pop("createdOn", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on, Unset):
            created_on = UNSET
        else:
            created_on = datetime.datetime.fromisoformat(_created_on)

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

        def _parse_cod_sec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cod_sec = _parse_cod_sec(d.pop("codSec", UNSET))

        def _parse_estado(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        estado = _parse_estado(d.pop("estado", UNSET))

        def _parse_progress(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        progress = _parse_progress(d.pop("progress", UNSET))

        ambiente = d.pop("ambiente", UNSET)

        def _parse_url_impresion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_impresion = _parse_url_impresion(d.pop("urlImpresion", UNSET))

        _acecfs = d.pop("acecfs", UNSET)
        acecfs: list[AcecfSummaryDto] | Unset = UNSET
        if _acecfs is not UNSET:
            acecfs = []
            for acecfs_item_data in _acecfs:
                acecfs_item = AcecfSummaryDto.from_dict(acecfs_item_data)

                acecfs.append(acecfs_item)

        ecf_receptor_dto = cls(
            ecf_receptor_id=ecf_receptor_id,
            tenant_id=tenant_id,
            company_rnc=company_rnc,
            encf=encf,
            rnc_emisor=rnc_emisor,
            rnc_receptor=rnc_receptor,
            tipo_ecf=tipo_ecf,
            monto_total=monto_total,
            fecha_emision=fecha_emision,
            file_name=file_name,
            raw_json_data=raw_json_data,
            created_on=created_on,
            fecha_firma=fecha_firma,
            cod_sec=cod_sec,
            estado=estado,
            progress=progress,
            ambiente=ambiente,
            url_impresion=url_impresion,
            acecfs=acecfs,
        )

        ecf_receptor_dto.additional_properties = d
        return ecf_receptor_dto

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
