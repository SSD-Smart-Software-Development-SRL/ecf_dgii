from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.all_tipo_ecf_types import AllTipoECFTypes
from ...models.ecf_estado_type_1 import EcfEstadoType1
from ...models.ecf_progress import EcfProgress
from ...models.paginated_api_result_of_ecf_response import PaginatedApiResultOfEcfResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    *,
    encfs: list[str] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    tipos_ecfs: list[AllTipoECFTypes] | Unset = UNSET,
    include_ecf_content: bool | Unset = False,
    from_fecha_emision: datetime.datetime | Unset = UNSET,
    to_fecha_emision: datetime.datetime | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    progresses: list[EcfProgress] | Unset = UNSET,
    dgii_estados: list[EcfEstadoType1 | None] | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_encfs: list[str] | Unset = UNSET
    if not isinstance(encfs, Unset):
        json_encfs = encfs


    params["Encfs"] = json_encfs

    json_ids: list[str] | Unset = UNSET
    if not isinstance(ids, Unset):
        json_ids = []
        for ids_item_data in ids:
            ids_item = str(ids_item_data)
            json_ids.append(ids_item)


    params["Ids"] = json_ids

    json_tipos_ecfs: list[str] | Unset = UNSET
    if not isinstance(tipos_ecfs, Unset):
        json_tipos_ecfs = []
        for tipos_ecfs_item_data in tipos_ecfs:
            tipos_ecfs_item = tipos_ecfs_item_data.value
            json_tipos_ecfs.append(tipos_ecfs_item)


    params["TiposEcfs"] = json_tipos_ecfs

    params["IncludeEcfContent"] = include_ecf_content

    json_from_fecha_emision: str | Unset = UNSET
    if not isinstance(from_fecha_emision, Unset):
        json_from_fecha_emision = from_fecha_emision.isoformat()
    params["FromFechaEmision"] = json_from_fecha_emision

    json_to_fecha_emision: str | Unset = UNSET
    if not isinstance(to_fecha_emision, Unset):
        json_to_fecha_emision = to_fecha_emision.isoformat()
    params["ToFechaEmision"] = json_to_fecha_emision

    json_amount_from: float | str | Unset
    if isinstance(amount_from, Unset):
        json_amount_from = UNSET
    else:
        json_amount_from = amount_from
    params["AmountFrom"] = json_amount_from

    json_amount_to: float | str | Unset
    if isinstance(amount_to, Unset):
        json_amount_to = UNSET
    else:
        json_amount_to = amount_to
    params["AmountTo"] = json_amount_to

    json_progresses: list[str] | Unset = UNSET
    if not isinstance(progresses, Unset):
        json_progresses = []
        for progresses_item_data in progresses:
            progresses_item = progresses_item_data.value
            json_progresses.append(progresses_item)


    params["Progresses"] = json_progresses

    json_dgii_estados: list[None | str] | Unset = UNSET
    if not isinstance(dgii_estados, Unset):
        json_dgii_estados = []
        for dgii_estados_item_data in dgii_estados:
            dgii_estados_item: None | str
            if isinstance(dgii_estados_item_data, EcfEstadoType1):
                dgii_estados_item = dgii_estados_item_data.value
            else:
                dgii_estados_item = dgii_estados_item_data
            json_dgii_estados.append(dgii_estados_item)


    params["DgiiEstados"] = json_dgii_estados

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
        "url": "/ecf",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedApiResultOfEcfResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PaginatedApiResultOfEcfResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = ProblemDetails.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedApiResultOfEcfResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    encfs: list[str] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    tipos_ecfs: list[AllTipoECFTypes] | Unset = UNSET,
    include_ecf_content: bool | Unset = False,
    from_fecha_emision: datetime.datetime | Unset = UNSET,
    to_fecha_emision: datetime.datetime | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    progresses: list[EcfProgress] | Unset = UNSET,
    dgii_estados: list[EcfEstadoType1 | None] | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> Response[PaginatedApiResultOfEcfResponse | ProblemDetails]:
    """ 
    Args:
        encfs (list[str] | Unset):
        ids (list[UUID] | Unset):
        tipos_ecfs (list[AllTipoECFTypes] | Unset):
        include_ecf_content (bool | Unset):  Default: False.
        from_fecha_emision (datetime.datetime | Unset):
        to_fecha_emision (datetime.datetime | Unset):
        amount_from (float | str | Unset):
        amount_to (float | str | Unset):
        progresses (list[EcfProgress] | Unset):
        dgii_estados (list[EcfEstadoType1 | None] | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfEcfResponse | ProblemDetails]
     """


    kwargs = _get_kwargs(
        encfs=encfs,
ids=ids,
tipos_ecfs=tipos_ecfs,
include_ecf_content=include_ecf_content,
from_fecha_emision=from_fecha_emision,
to_fecha_emision=to_fecha_emision,
amount_from=amount_from,
amount_to=amount_to,
progresses=progresses,
dgii_estados=dgii_estados,
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
    encfs: list[str] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    tipos_ecfs: list[AllTipoECFTypes] | Unset = UNSET,
    include_ecf_content: bool | Unset = False,
    from_fecha_emision: datetime.datetime | Unset = UNSET,
    to_fecha_emision: datetime.datetime | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    progresses: list[EcfProgress] | Unset = UNSET,
    dgii_estados: list[EcfEstadoType1 | None] | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> PaginatedApiResultOfEcfResponse | ProblemDetails | None:
    """ 
    Args:
        encfs (list[str] | Unset):
        ids (list[UUID] | Unset):
        tipos_ecfs (list[AllTipoECFTypes] | Unset):
        include_ecf_content (bool | Unset):  Default: False.
        from_fecha_emision (datetime.datetime | Unset):
        to_fecha_emision (datetime.datetime | Unset):
        amount_from (float | str | Unset):
        amount_to (float | str | Unset):
        progresses (list[EcfProgress] | Unset):
        dgii_estados (list[EcfEstadoType1 | None] | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfEcfResponse | ProblemDetails
     """


    return sync_detailed(
        client=client,
encfs=encfs,
ids=ids,
tipos_ecfs=tipos_ecfs,
include_ecf_content=include_ecf_content,
from_fecha_emision=from_fecha_emision,
to_fecha_emision=to_fecha_emision,
amount_from=amount_from,
amount_to=amount_to,
progresses=progresses,
dgii_estados=dgii_estados,
page=page,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    encfs: list[str] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    tipos_ecfs: list[AllTipoECFTypes] | Unset = UNSET,
    include_ecf_content: bool | Unset = False,
    from_fecha_emision: datetime.datetime | Unset = UNSET,
    to_fecha_emision: datetime.datetime | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    progresses: list[EcfProgress] | Unset = UNSET,
    dgii_estados: list[EcfEstadoType1 | None] | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> Response[PaginatedApiResultOfEcfResponse | ProblemDetails]:
    """ 
    Args:
        encfs (list[str] | Unset):
        ids (list[UUID] | Unset):
        tipos_ecfs (list[AllTipoECFTypes] | Unset):
        include_ecf_content (bool | Unset):  Default: False.
        from_fecha_emision (datetime.datetime | Unset):
        to_fecha_emision (datetime.datetime | Unset):
        amount_from (float | str | Unset):
        amount_to (float | str | Unset):
        progresses (list[EcfProgress] | Unset):
        dgii_estados (list[EcfEstadoType1 | None] | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfEcfResponse | ProblemDetails]
     """


    kwargs = _get_kwargs(
        encfs=encfs,
ids=ids,
tipos_ecfs=tipos_ecfs,
include_ecf_content=include_ecf_content,
from_fecha_emision=from_fecha_emision,
to_fecha_emision=to_fecha_emision,
amount_from=amount_from,
amount_to=amount_to,
progresses=progresses,
dgii_estados=dgii_estados,
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
    encfs: list[str] | Unset = UNSET,
    ids: list[UUID] | Unset = UNSET,
    tipos_ecfs: list[AllTipoECFTypes] | Unset = UNSET,
    include_ecf_content: bool | Unset = False,
    from_fecha_emision: datetime.datetime | Unset = UNSET,
    to_fecha_emision: datetime.datetime | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    progresses: list[EcfProgress] | Unset = UNSET,
    dgii_estados: list[EcfEstadoType1 | None] | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,

) -> PaginatedApiResultOfEcfResponse | ProblemDetails | None:
    """ 
    Args:
        encfs (list[str] | Unset):
        ids (list[UUID] | Unset):
        tipos_ecfs (list[AllTipoECFTypes] | Unset):
        include_ecf_content (bool | Unset):  Default: False.
        from_fecha_emision (datetime.datetime | Unset):
        to_fecha_emision (datetime.datetime | Unset):
        amount_from (float | str | Unset):
        amount_to (float | str | Unset):
        progresses (list[EcfProgress] | Unset):
        dgii_estados (list[EcfEstadoType1 | None] | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfEcfResponse | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
encfs=encfs,
ids=ids,
tipos_ecfs=tipos_ecfs,
include_ecf_content=include_ecf_content,
from_fecha_emision=from_fecha_emision,
to_fecha_emision=to_fecha_emision,
amount_from=amount_from,
amount_to=amount_to,
progresses=progresses,
dgii_estados=dgii_estados,
page=page,
limit=limit,

    )).parsed
