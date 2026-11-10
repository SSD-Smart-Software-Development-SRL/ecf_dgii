from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.tracking_detalle import TrackingDetalle
from ...types import UNSET, Response


def _get_kwargs(
    rnc: str,
    *,
    rnc_emisor: str,
    encf: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["rncEmisor"] = rnc_emisor

    params["encf"] = encf

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dgii/{rnc}/consultatrackids/consulta".format(
            rnc=quote(str(rnc), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | list[TrackingDetalle] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TrackingDetalle.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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

    if response.status_code == 502:
        response_502 = ProblemDetails.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | list[TrackingDetalle]]:
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
    rnc_emisor: str,
    encf: str,
) -> Response[ProblemDetails | list[TrackingDetalle]]:
    """
    Args:
        rnc (str):
        rnc_emisor (str):
        encf (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[TrackingDetalle]]
    """

    kwargs = _get_kwargs(
        rnc=rnc,
        rnc_emisor=rnc_emisor,
        encf=encf,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    rnc_emisor: str,
    encf: str,
) -> ProblemDetails | list[TrackingDetalle] | None:
    """
    Args:
        rnc (str):
        rnc_emisor (str):
        encf (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[TrackingDetalle]
    """

    return sync_detailed(
        rnc=rnc,
        client=client,
        rnc_emisor=rnc_emisor,
        encf=encf,
    ).parsed


async def asyncio_detailed(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    rnc_emisor: str,
    encf: str,
) -> Response[ProblemDetails | list[TrackingDetalle]]:
    """
    Args:
        rnc (str):
        rnc_emisor (str):
        encf (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[TrackingDetalle]]
    """

    kwargs = _get_kwargs(
        rnc=rnc,
        rnc_emisor=rnc_emisor,
        encf=encf,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    rnc_emisor: str,
    encf: str,
) -> ProblemDetails | list[TrackingDetalle] | None:
    """
    Args:
        rnc (str):
        rnc_emisor (str):
        encf (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[TrackingDetalle]
    """

    return (
        await asyncio_detailed(
            rnc=rnc,
            client=client,
            rnc_emisor=rnc_emisor,
            encf=encf,
        )
    ).parsed
