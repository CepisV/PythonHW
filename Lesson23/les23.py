import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup

#requests
def fetch_with_requests(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"HTML сохранён в файл {file_name} (requests)")
    else:
        print(f"Ошибка при загрузке страницы : {response.status_code}")

#aiohttp
async def fetch_with_aiohttp(url, file_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"HTML сохранён в файл {file_name} (aiohttp)")
            else:
                print(f"Ошибка при загрузке страницы: {response.status}")

def get_first_paragraph(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        paragraph = soup.find('p')  
        if paragraph:
            print("Первый абзац:")
            print(paragraph.text)
        else:
            print("Не удалось найти абзац в HTML.")

url = "https://ru.wikipedia.org/wiki/Python"
requests_file = "python_requests.html"
aiohttp_file = "python_aiohttp.html"

fetch_with_requests(url, requests_file)

asyncio.run(fetch_with_aiohttp(url, aiohttp_file))

get_first_paragraph(requests_file)
