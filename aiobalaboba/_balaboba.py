from __future__ import annotations

import sys
from typing import Dict, List, Optional, Union

from aiohttp import ClientSession

from ._http import HTTPSession
from ._text_type import TextType

if sys.version_info < (3, 8):  # pragma: <3.8 cover
    from typing_extensions import Literal
else:  # pragma: >=3.8 cover
    from typing import Literal


class Balaboba:
    """Asynchronous wrapper for Yandex Balaboba."""

    __slots__ = ("_session",)

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        """Asynchronous wrapper for Yandex Balaboba."""
        self._session = HTTPSession(session)

    @property
    def session(self) -> Optional[ClientSession]:
        return self._session.session

    @session.setter
    def session(self, session: Optional[ClientSession]) -> None:
        self._session.session = session

    async def get_text_types(
        self, language: Literal["en", "ru"] = "ru"
    ) -> List[TextType]:
        endpoint = "intros" if language == "ru" else "intros_eng"
        response = await self._session.get_response(
            method="GET", endpoint=endpoint, headers=self._get_text_types_headers()
        )
        return [TextType(*intro) for intro in response["intros"]]

    async def balaboba(self, query: str, text_type: Union[TextType, int]) -> str:
        intro = text_type.number if isinstance(text_type, TextType) else text_type
        response = await self._session.get_response(
            method="POST",
            endpoint="text3",
            json={"query": query, "intro": intro, "filter": 1},
            headers=self._get_balaboba_headers(query, intro),
        )
        return "{}{}".format(response["query"], response["text"])

    def _get_text_types_headers(self) -> Dict[str, str]:
        return {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; rv:113.0) Gecko/20100101 Firefox/113.0"
            )
        }

    def _get_balaboba_headers(
        self, query: str, text_type: int  # noqa: ARG002
    ) -> Dict[str, str]:
        return {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; rv:113.0) Gecko/20100101 Firefox/113.0"
            )
        }
