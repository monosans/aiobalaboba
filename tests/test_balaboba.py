from __future__ import annotations

import sys

import pytest
from aiohttp import ClientResponseError, ClientSession

from aiobalaboba import Balaboba

if sys.version_info < (3, 8):  # pragma: <3.8 cover
    from typing_extensions import Literal
else:  # pragma: >=3.8 cover
    from typing import Literal


@pytest.mark.parametrize(("language", "query"), [("en", "Hello"), ("ru", "Привет")])
async def test_balaboba(language: Literal["en", "ru"], query: str) -> None:
    b = Balaboba()
    assert b.session is None
    text_types = await b.get_text_types(language)
    async with ClientSession() as session:
        b.session = session
        assert b.session is session
        try:
            response = await b.balaboba(query, text_type=text_types[0])
        except ClientResponseError as e:  # pragma: no cover
            if e.status != 400:  # noqa: PLR2004
                raise
            return
    assert len(response) >= len(query)
    assert query.lower() in response.lower()
