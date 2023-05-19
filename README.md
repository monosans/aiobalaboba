# aiobalaboba

[![CI](https://github.com/monosans/aiobalaboba/actions/workflows/ci.yml/badge.svg)](https://github.com/monosans/aiobalaboba/actions/workflows/ci.yml)
[![Downloads](https://static.pepy.tech/badge/aiobalaboba)](https://pepy.tech/project/aiobalaboba)

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
