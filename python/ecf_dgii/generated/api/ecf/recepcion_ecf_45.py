from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ecf_45ecf import Ecf45ECF
from ...models.ecf_response import EcfResponse
from ...models.problem_details import ProblemDetails
from typing import cast



def _get_kwargs(
    *,
    body: Ecf45ECF,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ecf/45",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EcfResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = EcfResponse.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = ProblemDetails.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EcfResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Ecf45ECF,

) -> Response[EcfResponse | ProblemDetails]:
    """  Envía el e-CF a la DGII. Reenviar un e-NCF ya recibido devuelve el envío existente si el JSON es
    idéntico, o 409 si es distinto. Excepción: si la DGII rechazó todos los envíos anteriores de ese
    e-NCF sin utilizar la secuencia (secuenciaUtilizada = false), el e-NCF sigue libre y se acepta como
    un envío nuevo (idéntico o corregido) con su propio messageId; los envíos anteriores se conservan
    como historial.

    Args:
        body (Ecf45ECF):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EcfResponse | ProblemDetails]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: Ecf45ECF,

) -> EcfResponse | ProblemDetails | None:
    """  Envía el e-CF a la DGII. Reenviar un e-NCF ya recibido devuelve el envío existente si el JSON es
    idéntico, o 409 si es distinto. Excepción: si la DGII rechazó todos los envíos anteriores de ese
    e-NCF sin utilizar la secuencia (secuenciaUtilizada = false), el e-NCF sigue libre y se acepta como
    un envío nuevo (idéntico o corregido) con su propio messageId; los envíos anteriores se conservan
    como historial.

    Args:
        body (Ecf45ECF):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EcfResponse | ProblemDetails
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: Ecf45ECF,

) -> Response[EcfResponse | ProblemDetails]:
    """  Envía el e-CF a la DGII. Reenviar un e-NCF ya recibido devuelve el envío existente si el JSON es
    idéntico, o 409 si es distinto. Excepción: si la DGII rechazó todos los envíos anteriores de ese
    e-NCF sin utilizar la secuencia (secuenciaUtilizada = false), el e-NCF sigue libre y se acepta como
    un envío nuevo (idéntico o corregido) con su propio messageId; los envíos anteriores se conservan
    como historial.

    Args:
        body (Ecf45ECF):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EcfResponse | ProblemDetails]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: Ecf45ECF,

) -> EcfResponse | ProblemDetails | None:
    """  Envía el e-CF a la DGII. Reenviar un e-NCF ya recibido devuelve el envío existente si el JSON es
    idéntico, o 409 si es distinto. Excepción: si la DGII rechazó todos los envíos anteriores de ese
    e-NCF sin utilizar la secuencia (secuenciaUtilizada = false), el e-NCF sigue libre y se acepta como
    un envío nuevo (idéntico o corregido) con su propio messageId; los envíos anteriores se conservan
    como historial.

    Args:
        body (Ecf45ECF):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EcfResponse | ProblemDetails
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
