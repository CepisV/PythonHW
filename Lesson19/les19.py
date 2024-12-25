import time
import threading

def add_with_delay(a, b, results, index):
    time.sleep(1)  
    results[index] = a + b  

def sequential_execution():
    start_time = time.time()
    results = []  
    for _ in range(100):
        results.append(add_with_delay(1, 2, {}, 0))  
    end_time = time.time()
    print(f"Время последовательного выполнения: {end_time - start_time:.2f} секунд")
    return results

def multithreaded_execution():
    start_time = time.time()
    threads = []  
    results = [None] * 100  
    for i in range(100):
        thread = threading.Thread(target=add_with_delay, args=(1, 2, results, i))
        threads.append(thread)  
        thread.start()  

    for thread in threads:
        thread.join()  

    end_time = time.time()
    print(f"Время многопоточного выполнения: {end_time - start_time:.2f} секунд")
    return results

if __name__ == "__main__":
    print("Запуск последовательного выполнения...")
    sequential_results = sequential_execution()

    print("Запуск многопоточного выполнения...")
    multithreaded_results = multithreaded_execution()
