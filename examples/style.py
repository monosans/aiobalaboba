#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

from aiobalaboba import balaboba


async def main() -> None:
    """Используется 11-й вариант стилизации "Народные мудрости"."""
    response = await balaboba("Привет", intro=11)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
