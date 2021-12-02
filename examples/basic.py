#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

from aiobalaboba import balaboba


async def main() -> None:
    """Базовый пример."""
    response = await balaboba("Привет")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
