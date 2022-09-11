# aiobalaboba

[![CI](https://github.com/monosans/aiobalaboba/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/monosans/aiobalaboba/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/monosans/aiobalaboba/main.svg)](https://results.pre-commit.ci/latest/github/monosans/aiobalaboba/main)
[![codecov](https://codecov.io/gh/monosans/aiobalaboba/branch/main/graph/badge.svg)](https://codecov.io/gh/monosans/aiobalaboba)

Asynchronous wrapper for [Yandex Balaboba](https://yandex.com/lab/yalm-en) ([Яндекс Балабоба](https://yandex.ru/lab/yalm)).

Synchronous version [here](https://github.com/monosans/balaboba).

## Disclaimer

The neural network doesn’t really know what it’s saying, so it can say absolutely anything. Don’t get offended if it says something that hurts your feelings. When sharing the texts, make sure they’re not offensive or violate the law.

## Installation

```bash
python -m pip install aiobalaboba
```

## Usage example

```python
import asyncio

from aiobalaboba import Balaboba


async def main():
    bb = Balaboba()

    # Get text types
    intros = await bb.intros(language="en")

    # Get the first text type
    intro = next(intros)

    # Print Balaboba's response to the "Hello" query
    response = await bb.balaboba("Hello", intro=intro.number)
    print(response)

asyncio.run(main())
```

## License

[MIT](https://github.com/monosans/aiobalaboba/blob/main/LICENSE)
