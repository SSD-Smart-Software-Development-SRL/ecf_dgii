from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.problem_details import ProblemDetails
from ...models.respuesta_consulta_track_id import RespuestaConsultaTrackId
from typing import cast



def _get_kwargs(
    rnc: str,
    *,
    track_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["trackId"] = track_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/dgii/{rnc}/consultaresultado/estado".format(rnc=quote(str(rnc), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemDetails | RespuestaConsultaTrackId | None:
    if response.status_code == 200:
        response_200 = RespuestaConsultaTrackId.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProblemDetails | RespuestaConsultaTrackId]:
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
    track_id: str,

) -> Response[ProblemDetails | RespuestaConsultaTrackId]:
    """ 
    Args:
        rnc (str):
        track_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | RespuestaConsultaTrackId]
     """


    kwargs = _get_kwargs(
        rnc=rnc,
track_id=track_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    track_id: str,

) -> ProblemDetails | RespuestaConsultaTrackId | None:
    """ 
    Args:
        rnc (str):
        track_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | RespuestaConsultaTrackId
     """


    return sync_detailed(
        rnc=rnc,
client=client,
track_id=track_id,

    ).parsed

async def asyncio_detailed(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    track_id: str,

) -> Response[ProblemDetails | RespuestaConsultaTrackId]:
    """ 
    Args:
        rnc (str):
        track_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | RespuestaConsultaTrackId]
     """


    kwargs = _get_kwargs(
        rnc=rnc,
track_id=track_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    rnc: str,
    *,
    client: AuthenticatedClient | Client,
    track_id: str,

) -> ProblemDetails | RespuestaConsultaTrackId | None:
    """ 
    Args:
        rnc (str):
        track_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | RespuestaConsultaTrackId
     """


    return (await asyncio_detailed(
        rnc=rnc,
client=client,
track_id=track_id,

    )).parsed
