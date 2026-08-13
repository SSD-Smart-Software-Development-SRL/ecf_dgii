from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_api_result_of_ecf_reception_request_dto import PaginatedApiResultOfEcfReceptionRequestDto
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    rnc_emisors: list[str] | Unset = UNSET,
    tipos_ecfs: list[int | str] | Unset = UNSET,
    progresses: list[int | str] | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,
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

    json_rncs: list[str] | Unset = UNSET
    if not isinstance(rncs, Unset):
        json_rncs = rncs

    params["Rncs"] = json_rncs

    json_rnc_emisors: list[str] | Unset = UNSET
    if not isinstance(rnc_emisors, Unset):
        json_rnc_emisors = rnc_emisors

    params["RncEmisors"] = json_rnc_emisors

    json_tipos_ecfs: list[int | str] | Unset = UNSET
    if not isinstance(tipos_ecfs, Unset):
        json_tipos_ecfs = []
        for tipos_ecfs_item_data in tipos_ecfs:
            tipos_ecfs_item: int | str
            tipos_ecfs_item = tipos_ecfs_item_data
            json_tipos_ecfs.append(tipos_ecfs_item)

    params["TiposEcfs"] = json_tipos_ecfs

    json_progresses: list[int | str] | Unset = UNSET
    if not isinstance(progresses, Unset):
        json_progresses = []
        for progresses_item_data in progresses:
            progresses_item: int | str
            progresses_item = progresses_item_data
            json_progresses.append(progresses_item)

    params["Progresses"] = json_progresses

    params["FromDate"] = from_date

    params["ToDate"] = to_date

    json_amount_from: float | str | Unset
    if isinstance(amount_from, Unset):
        json_amount_from = UNSET
    else:
        json_amount_from = amount_from
    params["AmountFrom"] = json_amount_from

    json_amount_to: float | str | Unset
    if isinstance(amount_to, Unset):
        json_amount_to = UNSET
    else:
        json_amount_to = amount_to
    params["AmountTo"] = json_amount_to

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
        "url": "/recepcion",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails | None:
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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    rnc_emisors: list[str] | Unset = UNSET,
    tipos_ecfs: list[int | str] | Unset = UNSET,
    progresses: list[int | str] | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,
) -> Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]:
    """
    Args:
        message_ids (list[UUID] | Unset):
        encfs (list[str] | Unset):
        rncs (list[str] | Unset):
        rnc_emisors (list[str] | Unset):
        tipos_ecfs (list[int | str] | Unset):
        progresses (list[int | str] | Unset):
        from_date (str | Unset):
        to_date (str | Unset):
        amount_from (float | str | Unset):
        amount_to (float | str | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]
    """

    kwargs = _get_kwargs(
        message_ids=message_ids,
        encfs=encfs,
        rncs=rncs,
        rnc_emisors=rnc_emisors,
        tipos_ecfs=tipos_ecfs,
        progresses=progresses,
        from_date=from_date,
        to_date=to_date,
        amount_from=amount_from,
        amount_to=amount_to,
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
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    rnc_emisors: list[str] | Unset = UNSET,
    tipos_ecfs: list[int | str] | Unset = UNSET,
    progresses: list[int | str] | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,
) -> PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails | None:
    """
    Args:
        message_ids (list[UUID] | Unset):
        encfs (list[str] | Unset):
        rncs (list[str] | Unset):
        rnc_emisors (list[str] | Unset):
        tipos_ecfs (list[int | str] | Unset):
        progresses (list[int | str] | Unset):
        from_date (str | Unset):
        to_date (str | Unset):
        amount_from (float | str | Unset):
        amount_to (float | str | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails
    """

    return sync_detailed(
        client=client,
        message_ids=message_ids,
        encfs=encfs,
        rncs=rncs,
        rnc_emisors=rnc_emisors,
        tipos_ecfs=tipos_ecfs,
        progresses=progresses,
        from_date=from_date,
        to_date=to_date,
        amount_from=amount_from,
        amount_to=amount_to,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    rnc_emisors: list[str] | Unset = UNSET,
    tipos_ecfs: list[int | str] | Unset = UNSET,
    progresses: list[int | str] | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,
) -> Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]:
    """
    Args:
        message_ids (list[UUID] | Unset):
        encfs (list[str] | Unset):
        rncs (list[str] | Unset):
        rnc_emisors (list[str] | Unset):
        tipos_ecfs (list[int | str] | Unset):
        progresses (list[int | str] | Unset):
        from_date (str | Unset):
        to_date (str | Unset):
        amount_from (float | str | Unset):
        amount_to (float | str | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails]
    """

    kwargs = _get_kwargs(
        message_ids=message_ids,
        encfs=encfs,
        rncs=rncs,
        rnc_emisors=rnc_emisors,
        tipos_ecfs=tipos_ecfs,
        progresses=progresses,
        from_date=from_date,
        to_date=to_date,
        amount_from=amount_from,
        amount_to=amount_to,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    message_ids: list[UUID] | Unset = UNSET,
    encfs: list[str] | Unset = UNSET,
    rncs: list[str] | Unset = UNSET,
    rnc_emisors: list[str] | Unset = UNSET,
    tipos_ecfs: list[int | str] | Unset = UNSET,
    progresses: list[int | str] | Unset = UNSET,
    from_date: str | Unset = UNSET,
    to_date: str | Unset = UNSET,
    amount_from: float | str | Unset = UNSET,
    amount_to: float | str | Unset = UNSET,
    page: int | str | Unset = 1,
    limit: int | str | Unset = 25,
) -> PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails | None:
    """
    Args:
        message_ids (list[UUID] | Unset):
        encfs (list[str] | Unset):
        rncs (list[str] | Unset):
        rnc_emisors (list[str] | Unset):
        tipos_ecfs (list[int | str] | Unset):
        progresses (list[int | str] | Unset):
        from_date (str | Unset):
        to_date (str | Unset):
        amount_from (float | str | Unset):
        amount_to (float | str | Unset):
        page (int | str | Unset):  Default: 1.
        limit (int | str | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedApiResultOfEcfReceptionRequestDto | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            message_ids=message_ids,
            encfs=encfs,
            rncs=rncs,
            rnc_emisors=rnc_emisors,
            tipos_ecfs=tipos_ecfs,
            progresses=progresses,
            from_date=from_date,
            to_date=to_date,
            amount_from=amount_from,
            amount_to=amount_to,
            page=page,
            limit=limit,
        )
    ).parsed
