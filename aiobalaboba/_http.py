from __future__ import annotations

from typing import Any, Dict, Optional

from aiohttp import ClientSession


class HTTPSession:
    __slots__ = ("session",)

    def __init__(self, session: Optional[ClientSession]) -> None:
        self.session = session

    async def get_response(
        self,
        *,
        method: str,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        if isinstance(self.session, ClientSession) and not self.session.closed:
            return await self._fetch(
                method=method,
                endpoint=endpoint,
                json=json,
                session=self.session,
            )
        async with ClientSession() as session:
            return await self._fetch(
                method=method, endpoint=endpoint, json=json, session=session
            )

    async def _fetch(
        self,
        *,
        method: str,
        endpoint: str,
        json: Optional[Dict[str, Any]],
        session: ClientSession,
    ) -> Any:
        async with session.request(
            method,
            f"https://yandex.ru/lab/api/yalm/{endpoint}",
            json=json,
            raise_for_status=True,
        ) as response:
            return await response.json()
