#A
import os
import requests

def download_images_requests(folder, count=10):
    os.makedirs(folder, exist_ok=True)
    for i in range(count):
        try:
            response = requests.get(f"https://picsum.photos/200/300", stream=True)
            if response.status_code == 200:
                with open(f"{folder}/image_{i+1}.jpg", "wb") as file:
                    file.write(response.content)
                print(f"Image {i+1} saved to {folder}")
            else:
                print(f"Failed to download image {i+1}")
        except Exception as e:
            print(f"Error downloading image {i+1}: {e}")

download_images_requests("images_requests")


import aiohttp
import asyncio

async def download_images_aiohttp(base_url, folder, count=10):
    os.makedirs(folder, exist_ok=True)
    async with aiohttp.ClientSession() as session:
        for i in range(count):
            async with session.get(f"{base_url}/?random") as response:
                if response.status == 200:
                    with open(f"{folder}/image_{i+1}.jpg", "wb") as file:
                        file.write(await response.read())
                    print(f"Image {i+1} saved to {folder}")
                else:
                    print(f"Failed to download image {i+1}")

asyncio.run(download_images_aiohttp("https://picsum.photos/200/300", "images_aiohttp"))

#weather
import requests
from bs4 import BeautifulSoup

def get_weather_with_bs4():
    url = "https://yandex.kz/pogoda/astana?lat=51.143964&lon=71.435819"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')

        temperature = soup.find('div', class_='fact__temp').text.strip()
        print(f"Weather in Astana: {temperature}")
    except Exception as e:
        print(f"Failed to fetch the weather: {e}")

get_weather_with_bs4()

