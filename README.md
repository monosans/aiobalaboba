# aiobalaboba

[![CI](https://github.com/monosans/aiobalaboba/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/aiobalaboba/actions/workflows/ci.yml?query=event%3Apush+branch%3Amain)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/aiobalaboba/main.svg)](https://results.pre-commit.ci/latest/github/monosans/aiobalaboba/main)
[![Coverage](https://img.shields.io/codecov/c/github/monosans/aiobalaboba/main?logo=codecov)](https://codecov.io/gh/monosans/aiobalaboba)
[![PyPI Downloads](https://img.shields.io/pypi/dm/aiobalaboba?logo=pypi)](https://pypi.org/project/aiobalaboba/)

Asynchronous wrapper for [Yandex Balaboba](https://yandex.com/lab/yalm-en) ([Яндекс Балабоба](https://yandex.ru/lab/yalm)).

Synchronous version [here](https://github.com/monosans/balaboba).

## Disclaimer

The neural network doesn’t really know what it’s saying, so it can say absolutely anything. Don’t get offended if it says something that hurts your feelings. When sharing the texts, make sure they’re not offensive or violate the law.

## Installation

```bash
python -m pip install -U aiobalaboba
```

## Usage example

```python
import asyncio

from aiobalaboba import Balaboba


async def main():
    bb = Balaboba()
    text_types = await bb.get_text_types(language="en")
    response = await bb.balaboba("Hello", text_type=text_types[0])
    print(response)

asyncio.run(main())
```

## License

[MIT](https://github.com/monosans/aiobalaboba/blob/main/LICENSE)
