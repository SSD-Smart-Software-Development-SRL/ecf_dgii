from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem_details import ProblemDetails
from ...models.update_certificate_company_request import UpdateCertificateCompanyRequest
from typing import cast



def _get_kwargs(
    rnc: str,
    *,
    body: UpdateCertificateCompanyRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/company/{rnc}/certificate".format(rnc=quote(str(rnc), safe=""),),
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProblemDetails]:
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
    body: UpdateCertificateCompanyRequest,

) -> Response[Any | ProblemDetails]:
    """ 
    Args:
        rnc (str):
        body (UpdateCertificateCompanyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
     """


    kwargs = _get_kwargs(
        rnc=rnc,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCertificateCompanyRequest,

) -> Any | ProblemDetails | None:
    """ 
    Args:
        rnc (str):
        body (UpdateCertificateCompanyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
     """


    return sync_detailed(
        rnc=rnc,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCertificateCompanyRequest,

) -> Response[Any | ProblemDetails]:
    """ 
    Args:
        rnc (str):
        body (UpdateCertificateCompanyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
     """


    kwargs = _get_kwargs(
        rnc=rnc,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateCertificateCompanyRequest,

) -> Any | ProblemDetails | None:
    """ 
    Args:
        rnc (str):
        body (UpdateCertificateCompanyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
     """


    return (await asyncio_detailed(
        rnc=rnc,
client=client,
body=body,

    )).parsed
