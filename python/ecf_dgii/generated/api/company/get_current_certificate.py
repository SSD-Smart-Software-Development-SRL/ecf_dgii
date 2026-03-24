from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.certificate_response import CertificateResponse
from ...models.problem_details import ProblemDetails
from typing import cast



def _get_kwargs(
    rnc: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/company/{rnc}/certificate".format(rnc=quote(str(rnc), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemDetails | list[CertificateResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = CertificateResponse.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProblemDetails | list[CertificateResponse]]:
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

) -> Response[ProblemDetails | list[CertificateResponse]]:
    """ 
    Args:
        rnc (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[CertificateResponse]]
     """


    kwargs = _get_kwargs(
        rnc=rnc,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,

) -> ProblemDetails | list[CertificateResponse] | None:
    """ 
    Args:
        rnc (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[CertificateResponse]
     """


    return sync_detailed(
        rnc=rnc,
client=client,

    ).parsed

async def asyncio_detailed(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ProblemDetails | list[CertificateResponse]]:
    """ 
    Args:
        rnc (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[CertificateResponse]]
     """


    kwargs = _get_kwargs(
        rnc=rnc,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,

) -> ProblemDetails | list[CertificateResponse] | None:
    """ 
    Args:
        rnc (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[CertificateResponse]
     """


    return (await asyncio_detailed(
        rnc=rnc,
client=client,

    )).parsed
