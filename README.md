# asyncio_url_checker

## Описание
CLI-приложение для проверки доступных HTTP-методов по списку URL.
На создание затрачено 3 часа
## Как использовать
Тестирование:
```bash
poetry run pytest --cov=asyncio_url_checker --cov-report=html
```

Запуск программы:
```bash
poetry run python -m asyncio_url_checker.main https://google.com https://facebook.com
```
