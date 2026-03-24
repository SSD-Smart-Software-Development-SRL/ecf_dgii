from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.detalle_anulacion_request_dto import DetalleAnulacionRequestDto
  from ..models.respuesta_anulacion_rango import RespuestaAnulacionRango





T = TypeVar("T", bound="AnulacionListResponse")



@_attrs_define
class AnulacionListResponse:
    """ 
        Example:
            {'fileName': 'fileName', 'updatedBy': 'updatedBy', 'detalleAnulacion': [{'secuencias': [{'hastaEncf':
                'hastaEncf', 'desdeEncf': 'desdeEncf'}, {'hastaEncf': 'hastaEncf', 'desdeEncf': 'desdeEncf'}],
                'cantidadeNcfAnulados': None, 'tipoEcf': 'ECF31', 'noLinea': [None, None]}, {'secuencias': [{'hastaEncf':
                'hastaEncf', 'desdeEncf': 'desdeEncf'}, {'hastaEncf': 'hastaEncf', 'desdeEncf': 'desdeEncf'}],
                'cantidadeNcfAnulados': None, 'tipoEcf': 'ECF31', 'noLinea': [None, None]}], 'updatedOn':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
                'createdOn': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
                '+00:00')), 'companyRnc': 'companyRnc', 'createdBy': 'createdBy', 'response': '', 'fechaHoraAnulacioneNCF':
                datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'tenantId':
                '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'cantidadeNCFAnulados': 0, 'anulacionId':
                '046b6c7f-0b8a-43b9-b35d-6489e6daee91', 'statusCode': None}

        Attributes:
            anulacion_id (UUID | Unset):
            tenant_id (UUID | Unset):
            company_rnc (str | Unset):
            cantidade_ncf_anulados (int | str | Unset):
            detalle_anulacion (list[DetalleAnulacionRequestDto] | None | Unset):
            response (None | RespuestaAnulacionRango | Unset):
            status_code (int | str | Unset):
            file_name (str | Unset):
            fecha_hora_anulacione_ncf (datetime.datetime | Unset):
            created_on (datetime.datetime | Unset):
            updated_on (datetime.datetime | Unset):
            created_by (str | Unset):
            updated_by (str | Unset):
     """

    anulacion_id: UUID | Unset = UNSET
    tenant_id: UUID | Unset = UNSET
    company_rnc: str | Unset = UNSET
    cantidade_ncf_anulados: int | str | Unset = UNSET
    detalle_anulacion: list[DetalleAnulacionRequestDto] | None | Unset = UNSET
    response: None | RespuestaAnulacionRango | Unset = UNSET
    status_code: int | str | Unset = UNSET
    file_name: str | Unset = UNSET
    fecha_hora_anulacione_ncf: datetime.datetime | Unset = UNSET
    created_on: datetime.datetime | Unset = UNSET
    updated_on: datetime.datetime | Unset = UNSET
    created_by: str | Unset = UNSET
    updated_by: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.detalle_anulacion_request_dto import DetalleAnulacionRequestDto
        from ..models.respuesta_anulacion_rango import RespuestaAnulacionRango
        anulacion_id: str | Unset = UNSET
        if not isinstance(self.anulacion_id, Unset):
            anulacion_id = str(self.anulacion_id)

        tenant_id: str | Unset = UNSET
        if not isinstance(self.tenant_id, Unset):
            tenant_id = str(self.tenant_id)

        company_rnc = self.company_rnc

        cantidade_ncf_anulados: int | str | Unset
        if isinstance(self.cantidade_ncf_anulados, Unset):
            cantidade_ncf_anulados = UNSET
        else:
            cantidade_ncf_anulados = self.cantidade_ncf_anulados

        detalle_anulacion: list[dict[str, Any]] | None | Unset
        if isinstance(self.detalle_anulacion, Unset):
            detalle_anulacion = UNSET
        elif isinstance(self.detalle_anulacion, list):
            detalle_anulacion = []
            for detalle_anulacion_type_0_item_data in self.detalle_anulacion:
                detalle_anulacion_type_0_item = detalle_anulacion_type_0_item_data.to_dict()
                detalle_anulacion.append(detalle_anulacion_type_0_item)


        else:
            detalle_anulacion = self.detalle_anulacion

        response: dict[str, Any] | None | Unset
        if isinstance(self.response, Unset):
            response = UNSET
        elif isinstance(self.response, RespuestaAnulacionRango):
            response = self.response.to_dict()
        else:
            response = self.response

        status_code: int | str | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        file_name = self.file_name

        fecha_hora_anulacione_ncf: str | Unset = UNSET
        if not isinstance(self.fecha_hora_anulacione_ncf, Unset):
            fecha_hora_anulacione_ncf = self.fecha_hora_anulacione_ncf.isoformat()

        created_on: str | Unset = UNSET
        if not isinstance(self.created_on, Unset):
            created_on = self.created_on.isoformat()

        updated_on: str | Unset = UNSET
        if not isinstance(self.updated_on, Unset):
            updated_on = self.updated_on.isoformat()

        created_by = self.created_by

        updated_by = self.updated_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if anulacion_id is not UNSET:
            field_dict["anulacionId"] = anulacion_id
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if company_rnc is not UNSET:
            field_dict["companyRnc"] = company_rnc
        if cantidade_ncf_anulados is not UNSET:
            field_dict["cantidadeNCFAnulados"] = cantidade_ncf_anulados
        if detalle_anulacion is not UNSET:
            field_dict["detalleAnulacion"] = detalle_anulacion
        if response is not UNSET:
            field_dict["response"] = response
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if fecha_hora_anulacione_ncf is not UNSET:
            field_dict["fechaHoraAnulacioneNCF"] = fecha_hora_anulacione_ncf
        if created_on is not UNSET:
            field_dict["createdOn"] = created_on
        if updated_on is not UNSET:
            field_dict["updatedOn"] = updated_on
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.detalle_anulacion_request_dto import DetalleAnulacionRequestDto
        from ..models.respuesta_anulacion_rango import RespuestaAnulacionRango
        d = dict(src_dict)
        _anulacion_id = d.pop("anulacionId", UNSET)
        anulacion_id: UUID | Unset
        if isinstance(_anulacion_id,  Unset):
            anulacion_id = UNSET
        else:
            anulacion_id = UUID(_anulacion_id)




        _tenant_id = d.pop("tenantId", UNSET)
        tenant_id: UUID | Unset
        if isinstance(_tenant_id,  Unset):
            tenant_id = UNSET
        else:
            tenant_id = UUID(_tenant_id)




        company_rnc = d.pop("companyRnc", UNSET)

        def _parse_cantidade_ncf_anulados(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        cantidade_ncf_anulados = _parse_cantidade_ncf_anulados(d.pop("cantidadeNCFAnulados", UNSET))


        def _parse_detalle_anulacion(data: object) -> list[DetalleAnulacionRequestDto] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                detalle_anulacion_type_0 = []
                _detalle_anulacion_type_0 = data
                for detalle_anulacion_type_0_item_data in (_detalle_anulacion_type_0):
                    detalle_anulacion_type_0_item = DetalleAnulacionRequestDto.from_dict(detalle_anulacion_type_0_item_data)



                    detalle_anulacion_type_0.append(detalle_anulacion_type_0_item)

                return detalle_anulacion_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DetalleAnulacionRequestDto] | None | Unset, data)

        detalle_anulacion = _parse_detalle_anulacion(d.pop("detalleAnulacion", UNSET))


        def _parse_response(data: object) -> None | RespuestaAnulacionRango | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_type_1 = RespuestaAnulacionRango.from_dict(data)



                return response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RespuestaAnulacionRango | Unset, data)

        response = _parse_response(d.pop("response", UNSET))


        def _parse_status_code(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        status_code = _parse_status_code(d.pop("statusCode", UNSET))


        file_name = d.pop("fileName", UNSET)

        _fecha_hora_anulacione_ncf = d.pop("fechaHoraAnulacioneNCF", UNSET)
        fecha_hora_anulacione_ncf: datetime.datetime | Unset
        if isinstance(_fecha_hora_anulacione_ncf,  Unset):
            fecha_hora_anulacione_ncf = UNSET
        else:
            fecha_hora_anulacione_ncf = isoparse(_fecha_hora_anulacione_ncf)




        _created_on = d.pop("createdOn", UNSET)
        created_on: datetime.datetime | Unset
        if isinstance(_created_on,  Unset):
            created_on = UNSET
        else:
            created_on = isoparse(_created_on)




        _updated_on = d.pop("updatedOn", UNSET)
        updated_on: datetime.datetime | Unset
        if isinstance(_updated_on,  Unset):
            updated_on = UNSET
        else:
            updated_on = isoparse(_updated_on)




        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        anulacion_list_response = cls(
            anulacion_id=anulacion_id,
            tenant_id=tenant_id,
            company_rnc=company_rnc,
            cantidade_ncf_anulados=cantidade_ncf_anulados,
            detalle_anulacion=detalle_anulacion,
            response=response,
            status_code=status_code,
            file_name=file_name,
            fecha_hora_anulacione_ncf=fecha_hora_anulacione_ncf,
            created_on=created_on,
            updated_on=updated_on,
            created_by=created_by,
            updated_by=updated_by,
        )


        anulacion_list_response.additional_properties = d
        return anulacion_list_response

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
