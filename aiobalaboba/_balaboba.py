from __future__ import annotations

import sys
from typing import Any, Dict, List, Optional

from aiohttp import ClientSession

from ._text_type import TextType

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal
else:  # pragma: no cover
    from typing import Literal


class Balaboba:
    """Asynchronous wrapper for Yandex Balaboba."""

    __slots__ = ("session",)

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        """Asynchronous wrapper for Yandex Balaboba.

        Args:
            session: Instance of aiohttp.ClientSession. By default, a
                new instance is created for each request.
        """
        self.session = session

    async def get_text_types(
        self, language: Literal["en", "ru"] = "ru"
    ) -> List[TextType]:
        """Get text types."""
        endpoint = "intros" if language == "ru" else "intros_eng"
        response = await self._get_response(method="GET", endpoint=endpoint)
        return [TextType(*intro) for intro in response["intros"]]

    async def balaboba(self, query: str, *, text_type: int) -> str:
        """Get an answer from Balaboba.

        Args:
            query: Text for Balaboba.
            text_type: Text type number. You can get the list of types using
                the get_text_types method.
        """
        response = await self._get_response(
            method="POST",
            endpoint="text3",
            json={"query": query, "intro": text_type, "filter": 1},
        )
        return "{}{}".format(response["query"], response["text"])

    async def _get_response(
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
