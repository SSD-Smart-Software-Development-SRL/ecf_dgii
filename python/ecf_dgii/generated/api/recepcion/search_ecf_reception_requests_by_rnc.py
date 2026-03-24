from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_api_result_of_ecf_reception_request_dto import PaginatedApiResultOfEcfReceptionRequestDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    rnc: str,
    *,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_message_ids: list[str] | Unset = UNSET
    if not isinstance(message_ids, Unset):
        json_message_ids = []
        for message_ids_item_data in message_ids:
            message_ids_item = str(message_ids_item_data)
            json_message_ids.append(message_ids_item)


    params["MessageIds"] = json_message_ids

    json_encfs: list[str] | Unset = UNSET
    if not isinstance(encfs, Unset):
        json_encfs = encfs


    params["Encfs"] = json_encfs

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
        "url": "/recepcion/{rnc}/ecf".format(rnc=quote(str(rnc), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PaginatedApiResultOfEcfReceptionRequestDto.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]:
    """ 
    Args:
        rnc (str):
        message_ids (list[UUID] | Unset):
        encfs (list[str] | Unset):
        page (int | str | Unset):
        limit (int | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        rnc=rnc,
message_ids=message_ids,
encfs=encfs,
page=page,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails | None:
    """ 
    Args:
        rnc (str):
        message_ids (list[UUID] | Unset):
        encfs (list[str] | Unset):
        page (int | str | Unset):
        limit (int | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails
     """


    return sync_detailed(
        rnc=rnc,
client=client,
message_ids=message_ids,
encfs=encfs,
page=page,
limit=limit,

    ).parsed

async def asyncio_detailed(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]:
    """ 
    Args:
        rnc (str):
        message_ids (list[UUID] | Unset):
        encfs (list[str] | Unset):
        page (int | str | Unset):
        limit (int | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]
     """


    kwargs = _get_kwargs(
        rnc=rnc,
message_ids=message_ids,
encfs=encfs,
page=page,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails | None:
    """ 
    Args:
        rnc (str):
        message_ids (list[UUID] | Unset):
        encfs (list[str] | Unset):
        page (int | str | Unset):
        limit (int | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails
     """


    return (await asyncio_detailed(
        rnc=rnc,
client=client,
message_ids=message_ids,
encfs=encfs,
page=page,
limit=limit,

    )).parsed
