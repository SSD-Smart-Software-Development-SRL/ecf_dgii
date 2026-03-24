from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.paginated_api_result_of_company_response import PaginatedApiResultOfCompanyResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    rncs: list[str] | Unset = UNSET,
    names: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_rncs: list[str] | Unset = UNSET
    if not isinstance(rncs, Unset):
        json_rncs = rncs


    params["Rncs"] = json_rncs

    json_names: list[str] | Unset = UNSET
    if not isinstance(names, Unset):
        json_names = names


    params["Names"] = json_names

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
        "url": "/company",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedApiResultOfCompanyResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = PaginatedApiResultOfCompanyResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PaginatedApiResultOfCompanyResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    rncs: list[str] | Unset = UNSET,
    names: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> Response[PaginatedApiResultOfCompanyResponse | ProblemDetails]:
    """ 
    Args:
        rncs (list[str] | Unset):
        names (list[str] | Unset):
        page (int | str | Unset):
        limit (int | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfCompanyResponse | ProblemDetails]
     """


    kwargs = _get_kwargs(
        rncs=rncs,
names=names,
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
    rncs: list[str] | Unset = UNSET,
    names: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> PaginatedApiResultOfCompanyResponse | ProblemDetails | None:
    """ 
    Args:
        rncs (list[str] | Unset):
        names (list[str] | Unset):
        page (int | str | Unset):
        limit (int | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfCompanyResponse | ProblemDetails
     """


    return sync_detailed(
        client=client,
rncs=rncs,
names=names,
page=page,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    rncs: list[str] | Unset = UNSET,
    names: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> Response[PaginatedApiResultOfCompanyResponse | ProblemDetails]:
    """ 
    Args:
        rncs (list[str] | Unset):
        names (list[str] | Unset):
        page (int | str | Unset):
        limit (int | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfCompanyResponse | ProblemDetails]
     """


    kwargs = _get_kwargs(
        rncs=rncs,
names=names,
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
    rncs: list[str] | Unset = UNSET,
    names: list[str] | Unset = UNSET,
    page: int | str | Unset = UNSET,
    limit: int | str | Unset = UNSET,

) -> PaginatedApiResultOfCompanyResponse | ProblemDetails | None:
    """ 
    Args:
        rncs (list[str] | Unset):
        names (list[str] | Unset):
        page (int | str | Unset):
        limit (int | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfCompanyResponse | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
rncs=rncs,
names=names,
page=page,
limit=limit,

    )).parsed
