import os
import requests
import aiohttp
import asyncio
import json

BASE_URL = "https://jsonplaceholder.typicode.com/posts"
SAVE_DIR = "json_data"  

os.makedirs(SAVE_DIR, exist_ok=True)

def synchronous_download():
    response = requests.get(BASE_URL)
    response.raise_for_status() 
    json_data = response.json()

    for idx, obj in enumerate(json_data):
        file_name = os.path.join(SAVE_DIR, f"post_{idx + 1}.json")
        with open(file_name, "w") as file:
            json.dump(obj, file, indent=4)
    print(f"Синхронно сохранено {len(json_data)} файлов.")

async def async_download():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as response:
            response.raise_for_status()
            json_data = await response.json()

            for idx, obj in enumerate(json_data):
                file_name = os.path.join(SAVE_DIR, f"post_{idx + 1}.json")
                with open(file_name, "w") as file:
                    json.dump(obj, file, indent=4)
            print(f"Асинхронно сохранено {len(json_data)} файлов.")

if __name__ == "__main__":
    print("Запуск синхронной загрузки...")
    synchronous_download()

    print("\nЗапуск асинхронной загрузки...")
    asyncio.run(async_download())
