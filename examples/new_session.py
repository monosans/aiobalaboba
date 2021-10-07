#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

from aiobalaboba import balaboba


async def main():
    # Используется стандартный вариант стилизации.
    # Для запроса создаётся новый экземпляр aiohttp.ClientSession:
    response = await balaboba("Привет")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
