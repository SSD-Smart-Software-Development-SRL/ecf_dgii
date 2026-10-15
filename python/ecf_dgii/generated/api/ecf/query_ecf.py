from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ecf_response import EcfResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    rnc: str,
    encf: str,
    *,
    include_ecf_content: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["includeEcfContent"] = include_ecf_content


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ecf/{rnc}/{encf}".format(rnc=quote(str(rnc), safe=""),encf=quote(str(encf), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemDetails | list[EcfResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = EcfResponse.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProblemDetails | list[EcfResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rnc: str,
    encf: str,
    *,
    client: AuthenticatedClient | Client,
    include_ecf_content: bool | Unset = False,

) -> Response[ProblemDetails | list[EcfResponse]]:
    """ 
    Args:
        rnc (str):
        encf (str):
        include_ecf_content (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[EcfResponse]]
     """


    kwargs = _get_kwargs(
        rnc=rnc,
encf=encf,
include_ecf_content=include_ecf_content,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    rnc: str,
    encf: str,
    *,
    client: AuthenticatedClient | Client,
    include_ecf_content: bool | Unset = False,

) -> ProblemDetails | list[EcfResponse] | None:
    """ 
    Args:
        rnc (str):
        encf (str):
        include_ecf_content (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[EcfResponse]
     """


    return sync_detailed(
        rnc=rnc,
encf=encf,
client=client,
include_ecf_content=include_ecf_content,

    ).parsed

async def asyncio_detailed(
    rnc: str,
    encf: str,
    *,
    client: AuthenticatedClient | Client,
    include_ecf_content: bool | Unset = False,

) -> Response[ProblemDetails | list[EcfResponse]]:
    """ 
    Args:
        rnc (str):
        encf (str):
        include_ecf_content (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[EcfResponse]]
     """


    kwargs = _get_kwargs(
        rnc=rnc,
encf=encf,
include_ecf_content=include_ecf_content,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    rnc: str,
    encf: str,
    *,
    client: AuthenticatedClient | Client,
    include_ecf_content: bool | Unset = False,

) -> ProblemDetails | list[EcfResponse] | None:
    """ 
    Args:
        rnc (str):
        encf (str):
        include_ecf_content (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[EcfResponse]
     """


    return (await asyncio_detailed(
        rnc=rnc,
encf=encf,
client=client,
include_ecf_content=include_ecf_content,

    )).parsed
