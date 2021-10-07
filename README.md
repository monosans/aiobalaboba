# aiobalaboba

Асинхронный модуль для взаимодействия с [Яндекс Балабоба](https://yandex.ru/lab/yalm).

Синхронная версия [здесь](https://github.com/monosans/balaboba).

## Установка

```sh
python -m pip install aiobalaboba
```

Или просто скопируйте [код](https://github.com/monosans/aiobalaboba/blob/main/aiobalaboba/__init__.py) себе.

## Примеры использования

### Базовый пример

Используется стандартный вариант стилизации, для запроса создаётся новый экземпляр aiohttp.ClientSession:

```python
import asyncio

from aiobalaboba import balaboba


async def main():
    response = await balaboba("Привет")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
```

Вывод: `Привет! Я рад тебя видеть на моём канале. Здесь ты сможешь встретить много интересных аниме, музыки, видео, и многого другого.`

### Продвинутый пример

Используется 11-ый вариант стилизации "Народные мудрости", для запроса используется существующий экземпляр aiohttp.ClientSession:

```python
import asyncio

from aiobalaboba import balaboba
from aiohttp import ClientSession


async def main():
    async with ClientSession() as session:
        response = await balaboba("Привет", intro=11, session=session)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
```

## Дисклеймер с сайта

Нейросеть не знает, что говорит, и может сказать всякое — если что, не обижайтесь. Распространяя получившиеся тексты, помните об ответственности.

## License / Лицензия

[MIT](LICENSE)
