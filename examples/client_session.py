#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

from aiobalaboba import balaboba
from aiohttp import ClientSession


async def main() -> None:
    """Используется существующий экземпляр aiohttp.ClientSession."""
    async with ClientSession() as session:
        response = await balaboba("Привет", session=session)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
