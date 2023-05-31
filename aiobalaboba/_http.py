from __future__ import annotations

from typing import Any, Mapping, Optional

from aiohttp import ClientResponse, ClientSession


class HTTPSession:
    __slots__ = ("session",)

    def __init__(self, session: Optional[ClientSession]) -> None:
        self.session = session

    async def get_response(
        self,
        *,
        method: str,
        endpoint: str,
        json: Any = None,
        headers: Mapping[str, str],
    ) -> Any:
        if isinstance(self.session, ClientSession) and not self.session.closed:
            response = await self._fetch(
                method=method,
                endpoint=endpoint,
                json=json,
                headers=headers,
                session=self.session,
            )
        else:
            async with ClientSession() as session:
                response = await self._fetch(
                    method=method,
                    endpoint=endpoint,
                    json=json,
                    headers=headers,
                    session=session,
                )
        return await response.json()

    async def _fetch(
        self,
        *,
        method: str,
        endpoint: str,
        json: Any,
        headers: Mapping[str, str],
        session: ClientSession,
    ) -> ClientResponse:
        async with session.request(
            method,
            f"https://yandex.ru/lab/api/yalm/{endpoint}",
            json=json,
            headers=headers,
            raise_for_status=True,
        ) as response:
            await response.read()
        return response
