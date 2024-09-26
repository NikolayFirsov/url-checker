import json
import pytest
from asyncio_url_checker.main import is_valid_url, check_urls


@pytest.mark.parametrize('url,expected', [
    ('https://google.com', True),
    ('not_a_url', False),
    ('ftp://example.com', True),
    ('http://localhost:8000', True),
])
def test_is_valid_url(url, expected):
    assert is_valid_url(url) == expected


@pytest.mark.asyncio
async def test_main():
    urls = ['https://google.com', 'https://facebook.com', 'not_a_url']
    expected = {
        'https://google.com': {
            'GET': 200,
            'HEAD': 200
        },
        'https://facebook.com': {
            'GET': 200,
            'POST': 200,
            'PUT': 200,
            'DELETE': 200,
            'PATCH': 200,
            'OPTIONS': 200,
            'HEAD': 200
        }
    }
    assert await check_urls(urls) == json.dumps(expected, indent=4, ensure_ascii=False)
    urls = []
    assert await check_urls(urls) == "Необходимо передать хотя бы одну строку."
