#a
import time

def create_file(filename):
    time.sleep(1)  
    with open(filename, 'w') as file:
        file.write(f"Файл {filename} создан.\n")


#b
import time

def run_sequential():
    start_time = time.time()
    for i in range(100):
        create_file(f"file_{i}.txt")
    end_time = time.time()
    print(f"Последовательное выполнение заняло: {end_time - start_time:.2f} секунд.")

#c
from concurrent.futures import ThreadPoolExecutor

def run_multithreaded():
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=10) as executor: 
        futures = [executor.submit(create_file, f"file_{i}.txt") for i in range(100)]
        
        for future in futures:
            future.result()
    
    end_time = time.time()
    print(f"Многопоточное выполнение заняло: {end_time - start_time:.2f} секунд.")


if __name__ == "__main__":
    print("Запуск последовательного выполнения:")
    run_sequential()

    print("\nЗапуск многопоточного выполнения:")
    run_multithreaded()
