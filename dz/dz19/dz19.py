import time
import requests
import asyncio
import aiohttp

URLS = ["https://jsonplaceholder.typicode.com/posts/1"] * 100

def fetch_url(url):
    response = requests.get(url)
    return response.text

#a
def synchronous_execution():
    start_time = time.time()
    for url in URLS:
        fetch_url(url)
    end_time = time.time()
    print(f"Синхронное выполнение заняло {end_time - start_time:.2f} секунд")

async def async_fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

#b
async def asynchronous_execution():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [async_fetch_url(session, url) for url in URLS]
        await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Асинхронное выполнение заняло {end_time - start_time:.2f} секунд")

if __name__ == "__main__":
    print("Запуск синхронного выполнения...")
    synchronous_execution()

    print("\nЗапуск асинхронного выполнения...")
    asyncio.run(asynchronous_execution())
