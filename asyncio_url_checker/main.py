import aiohttp
import asyncio
import json
import re
import ssl
import sys

URL_REGEX = re.compile(r'^(https?|ftp)://[^\s/$.?#].[^\s]*$', re.IGNORECASE)


def is_valid_url(url):
    return re.match(URL_REGEX, url) is not None


async def check_urls(urls):
    if not urls:
        return "Необходимо передать хотя бы одну строку."
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD']
    result = {}
    for url in urls:
        if is_valid_url(url):
            result[url] = {}
            async with aiohttp.ClientSession() as session:
                for method in methods:
                    ssl_context = ssl.create_default_context()
                    ssl_context.check_hostname = False
                    ssl_context.verify_mode = ssl.CERT_NONE
                    async with session.request(method, url, ssl=ssl_context) as resp:
                        if resp.status != 405:
                            result[url][method] = resp.status
        else:
            print(f'Строка "{url}" не является ссылкой')
    return json.dumps(result, indent=4, ensure_ascii=False)


async def main():
    urls = sys.argv[1:]
    result = await check_urls(urls)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())