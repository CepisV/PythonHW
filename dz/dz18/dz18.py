import os
import random
import time
from threading import Thread

def write_random_number_to_file(file_name):
    time.sleep(1)  
    random_number = random.randint(1, 1000)
    with open(file_name, "w") as file:
        file.write(str(random_number))

#a
def sequential_execution():
    start_time = time.time()
    for i in range(1, 1001):
        file_name = f"file_{i}.txt"
        write_random_number_to_file(file_name)
    end_time = time.time()
    print(f"Последовательное выполнение заняло {end_time - start_time:.2f} секунд")

#b
def thread_execution():
    threads = []
    start_time = time.time()
    

    for i in range(1, 1001):
        file_name = f"file_{i}.txt"
        thread = Thread(target=write_random_number_to_file, args=(file_name,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f"Многопоточное выполнение заняло {end_time - start_time:.2f} секунд")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    os.chdir("output")
    
    print("Запуск последовательного выполнения...")
    sequential_execution()
    
    print("\nЗапуск многопоточного выполнения...")
    thread_execution()
