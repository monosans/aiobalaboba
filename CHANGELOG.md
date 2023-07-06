# Changelog

[Semantic Versioning](https://semver.org/)

## [3.0.3] - 2023-07-06

- Add documentation.

## [3.0.2] - 2023-06-10

- Update User-Agent header.

## [3.0.1] - 2023-05-31

- Added headers to requests to avoid triggering Yandex WAF. Fixes 400 Bad Request error.

## [3.0.0] - 2022-11-26

- The `intros` method has been renamed to `get_text_types` and now it returns a list instead of a generator. The `balaboba` method parameter has been renamed accordingly from `intro` to `text_type`.
- The `text_type` parameter can now accept both an int and an object from the list returned by the `get_text_types` method.
- Add `py.typed` file.

## [2.0.0] - 2022-09-11

- Raise the minimum required version of Python from 3.6 to 3.7.
- Completely rewrite the library interface.
- Add the ability to get a list of all text types, or as they are called in the Balaboba API - "intros" (in both English and Russian).
- Translate everything from Russian into English.
- Add unit tests.
- Other minor improvements.
