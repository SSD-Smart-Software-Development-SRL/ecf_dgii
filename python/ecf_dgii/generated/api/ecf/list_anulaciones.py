from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ecf_type import ECFType
from ...models.paginated_api_result_of_anulacion_list_response import PaginatedApiResultOfAnulacionListResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    *,
    tipo_ecf: list[ECFType] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    fecha_desde: datetime.datetime | Unset = UNSET,
    fecha_hasta: datetime.datetime | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_tipo_ecf: list[str] | Unset = UNSET
    if not isinstance(tipo_ecf, Unset):
        json_tipo_ecf = []
        for tipo_ecf_item_data in tipo_ecf:
            tipo_ecf_item = tipo_ecf_item_data.value
            json_tipo_ecf.append(tipo_ecf_item)


    params["TipoEcf"] = json_tipo_ecf

    json_rncs: list[str] | Unset = UNSET
    if not isinstance(rncs, Unset):
        json_rncs = rncs


    params["Rncs"] = json_rncs

    json_fecha_desde: str | Unset = UNSET
    if not isinstance(fecha_desde, Unset):
        json_fecha_desde = fecha_desde.isoformat()
    params["FechaDesde"] = json_fecha_desde

    json_fecha_hasta: str | Unset = UNSET
    if not isinstance(fecha_hasta, Unset):
        json_fecha_hasta = fecha_hasta.isoformat()
    params["FechaHasta"] = json_fecha_hasta

    json_page: int | str | Unset
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["Page"] = json_page

    json_limit: int | str | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["Limit"] = json_limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ecf/anulaciones",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedApiResultOfAnulacionListResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PaginatedApiResultOfAnulacionListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedApiResultOfAnulacionListResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    tipo_ecf: list[ECFType] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    fecha_desde: datetime.datetime | Unset = UNSET,
    fecha_hasta: datetime.datetime | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> Response[PaginatedApiResultOfAnulacionListResponse | ProblemDetails]:
    """ 
    Args:
        tipo_ecf (list[ECFType] | Unset):
        rncs (list[str] | Unset):
        fecha_desde (datetime.datetime | Unset):
        fecha_hasta (datetime.datetime | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfAnulacionListResponse | ProblemDetails]
     """


    kwargs = _get_kwargs(
        tipo_ecf=tipo_ecf,
rncs=rncs,
fecha_desde=fecha_desde,
fecha_hasta=fecha_hasta,
page=page,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    tipo_ecf: list[ECFType] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    fecha_desde: datetime.datetime | Unset = UNSET,
    fecha_hasta: datetime.datetime | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> PaginatedApiResultOfAnulacionListResponse | ProblemDetails | None:
    """ 
    Args:
        tipo_ecf (list[ECFType] | Unset):
        rncs (list[str] | Unset):
        fecha_desde (datetime.datetime | Unset):
        fecha_hasta (datetime.datetime | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfAnulacionListResponse | ProblemDetails
     """


    return sync_detailed(
        client=client,
tipo_ecf=tipo_ecf,
rncs=rncs,
fecha_desde=fecha_desde,
fecha_hasta=fecha_hasta,
page=page,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    tipo_ecf: list[ECFType] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    fecha_desde: datetime.datetime | Unset = UNSET,
    fecha_hasta: datetime.datetime | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> Response[PaginatedApiResultOfAnulacionListResponse | ProblemDetails]:
    """ 
    Args:
        tipo_ecf (list[ECFType] | Unset):
        rncs (list[str] | Unset):
        fecha_desde (datetime.datetime | Unset):
        fecha_hasta (datetime.datetime | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfAnulacionListResponse | ProblemDetails]
     """


    kwargs = _get_kwargs(
        tipo_ecf=tipo_ecf,
rncs=rncs,
fecha_desde=fecha_desde,
fecha_hasta=fecha_hasta,
page=page,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    tipo_ecf: list[ECFType] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    fecha_desde: datetime.datetime | Unset = UNSET,
    fecha_hasta: datetime.datetime | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> PaginatedApiResultOfAnulacionListResponse | ProblemDetails | None:
    """ 
    Args:
        tipo_ecf (list[ECFType] | Unset):
        rncs (list[str] | Unset):
        fecha_desde (datetime.datetime | Unset):
        fecha_hasta (datetime.datetime | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfAnulacionListResponse | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
tipo_ecf=tipo_ecf,
rncs=rncs,
fecha_desde=fecha_desde,
fecha_hasta=fecha_hasta,
page=page,
limit=limit,

    )).parsed
