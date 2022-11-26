from __future__ import annotations

import sys
from random import choice
from typing import Optional, Type

import pytest
from aiohttp import ClientSession

from aiobalaboba import Balaboba

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Literal
else:  # pragma: no cover
    from typing import Literal


@pytest.mark.parametrize("session_type", (None, ClientSession))
@pytest.mark.parametrize("language", ("en", "ru"))
@pytest.mark.parametrize("query", ("Привет", "Hello"))
async def test_balaboba(
    session_type: Optional[Type[ClientSession]],
    language: Literal["en", "ru"],
    query: str,
) -> None:
    try:
        session = ClientSession() if session_type else None
        b = Balaboba(session=session)
        text_types = tuple(await b.get_text_types(language))
        response = await b.balaboba(query, text_type=choice(text_types).number)
    finally:
        if isinstance(session, ClientSession):
            await session.close()
    assert len(response) >= len(query)
    assert query.lower() in response.lower()
