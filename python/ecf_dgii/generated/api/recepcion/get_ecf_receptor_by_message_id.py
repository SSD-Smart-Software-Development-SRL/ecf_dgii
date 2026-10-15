from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ecf_receptor_dto import EcfReceptorDto
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    rnc: str,
    message_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recepcion/{rnc}/{message_id}".format(
            rnc=quote(str(rnc), safe=""),
            message_id=quote(str(message_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EcfReceptorDto | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = EcfReceptorDto.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EcfReceptorDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rnc: str,
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | EcfReceptorDto | ProblemDetails]:
    """
    Args:
        rnc (str):
        message_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EcfReceptorDto | ProblemDetails]
    """

    kwargs = _get_kwargs(
        rnc=rnc,
        message_id=message_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rnc: str,
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | EcfReceptorDto | ProblemDetails | None:
    """
    Args:
        rnc (str):
        message_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EcfReceptorDto | ProblemDetails
    """

    return sync_detailed(
        rnc=rnc,
        message_id=message_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    rnc: str,
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | EcfReceptorDto | ProblemDetails]:
    """
    Args:
        rnc (str):
        message_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EcfReceptorDto | ProblemDetails]
    """

    kwargs = _get_kwargs(
        rnc=rnc,
        message_id=message_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rnc: str,
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | EcfReceptorDto | ProblemDetails | None:
    """
    Args:
        rnc (str):
        message_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EcfReceptorDto | ProblemDetails
    """

    return (
        await asyncio_detailed(
            rnc=rnc,
            message_id=message_id,
            client=client,
        )
    ).parsed
