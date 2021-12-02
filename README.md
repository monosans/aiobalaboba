# aiobalaboba

Асинхронная обёртка для [Яндекс Балабоба](https://yandex.ru/lab/yalm).

Синхронная версия [здесь](https://github.com/monosans/balaboba).

## Установка

```sh
python -m pip install aiobalaboba
```

## Примеры использования

### Базовый пример

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

### Варианты стилизации

Функции `balaboba` в качестве аргумента `intro` можно передать желаемый вариант стилизации. Номера всех вариантов стилизации есть в [докстринге](https://github.com/monosans/aiobalaboba/blob/main/aiobalaboba/_balaboba.py#L24). В примере используется 11-й вариант стилизации "Народные мудрости" ([полный код примера](https://github.com/monosans/aiobalaboba/blob/main/examples/style.py)):

```python
response = await balaboba("Привет", intro=11)
```

### Свой экземпляр aiohttp.ClientSession

Функции `balaboba` в качестве аргумента `session` можно передать экземпляр aiohttp.ClientSession ([полный код примера](https://github.com/monosans/aiobalaboba/blob/main/examples/client_session.py)):

```python
async with ClientSession() as session:
    response = await balaboba("Привет", session=session)
```

## Дисклеймер с сайта

Нейросеть не знает, что говорит, и может сказать всякое — если что, не обижайтесь. Распространяя получившиеся тексты, помните об ответственности.

## License / Лицензия

[MIT](https://github.com/monosans/aiobalaboba/blob/main/LICENSE)
