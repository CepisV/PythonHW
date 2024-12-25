import time
import requests
from multiprocessing import Pool


def download_image(i):
    url = "https://www.areal-hotel.ru/upload/uf/976/i3u9dqqzy164yh4wtvzvij69be23z2vi.jpg"
    save_path = f"image_{i}.jpg"
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    num_images = 100

    start_time = time.time()

    with Pool() as pool:
        pool.map(download_image, range(num_images))

    end_time = time.time()
    print(f"Мультипроцессорная загрузка завершена за {end_time - start_time:.2f} секунд")
