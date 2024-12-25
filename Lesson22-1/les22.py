#1
import requests
import json
import os
import time

os.makedirs("photos", exist_ok=True)

url = "https://jsonplaceholder.typicode.com/photos"

start_time = time.time()

response = requests.get(url)
photos = response.json()

for photo in photos[:5]:
    photo_url = photo['url']  
    photo_id = photo['id']    

    photo_response = requests.get(photo_url)

    with open(f"photos/photo_{photo_id}.jpg", "wb") as file:
        file.write(photo_response.content)

    print(f"Сохранено: photo_{photo_id}.jpg")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Фотографии успешно загружены. Затраченное время: {elapsed_time:.2f} секунд.")


#2
import aiohttp
import asyncio
import os
import time

os.makedirs("photos", exist_ok=True)

async def download_photo(session, photo):
    photo_url = photo['url']
    photo_id = photo['id']

    async with session.get(photo_url) as response:
        content = await response.read()

        with open(f"photos/photo_{photo_id}.jpg", "wb") as file:
            file.write(content)

        print(f"Сохранено: photo_{photo_id}.jpg")

async def fetch_photos():
    url = "https://jsonplaceholder.typicode.com/photos"

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            photos = await response.json()

            tasks = [download_photo(session, photo) for photo in photos[:5]]
            await asyncio.gather(*tasks)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Фотографии успешно загружены. Затраченное время: {elapsed_time:.2f} секунд.")

asyncio.run(fetch_photos())
