from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.directorio import Directorio
from ...models.problem_details import ProblemDetails
from typing import cast



def _get_kwargs(
    rnc_path: str,
    *,
    rnc_query: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["RNC"] = rnc_query


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dgii/{rnc_path}/consultadirectorio/obtener-directorio-por-rnc".format(rnc_path=quote(str(rnc_path), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Directorio | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = Directorio.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = ProblemDetails.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Directorio | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rnc_path: str,
    *,
    client: AuthenticatedClient | Client,
    rnc_query: str,

) -> Response[Directorio | ProblemDetails]:
    """ 
    Args:
        rnc_path (str):
        rnc_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Directorio | ProblemDetails]
     """


    kwargs = _get_kwargs(
        rnc_path=rnc_path,
rnc_query=rnc_query,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    rnc_path: str,
    *,
    client: AuthenticatedClient | Client,
    rnc_query: str,

) -> Directorio | ProblemDetails | None:
    """ 
    Args:
        rnc_path (str):
        rnc_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Directorio | ProblemDetails
     """


    return sync_detailed(
        rnc_path=rnc_path,
client=client,
rnc_query=rnc_query,

    ).parsed

async def asyncio_detailed(
    rnc_path: str,
    *,
    client: AuthenticatedClient | Client,
    rnc_query: str,

) -> Response[Directorio | ProblemDetails]:
    """ 
    Args:
        rnc_path (str):
        rnc_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Directorio | ProblemDetails]
     """


    kwargs = _get_kwargs(
        rnc_path=rnc_path,
rnc_query=rnc_query,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    rnc_path: str,
    *,
    client: AuthenticatedClient | Client,
    rnc_query: str,

) -> Directorio | ProblemDetails | None:
    """ 
    Args:
        rnc_path (str):
        rnc_query (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Directorio | ProblemDetails
     """


    return (await asyncio_detailed(
        rnc_path=rnc_path,
client=client,
rnc_query=rnc_query,

    )).parsed
