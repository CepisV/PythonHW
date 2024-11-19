#block1
#1
from datetime import datetime

add_15 = lambda x: x + 15
print("Задание 1:", add_15(10))  

multiply = lambda x, y: x * y
print("Задание 2:", multiply(12, 4))  

numbers = [78, 2, 13, 46, 5, 61, 74, 81, 94, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Задание 3:")
print("Список целых чисел:", numbers)
print("Список четных чисел:", even_numbers)  
print("Список нечетных чисел:", odd_numbers)  

current_datetime = datetime.now()
print("Задание 4:")
print("Текущая дата и время:", current_datetime)  
print("Год:", current_datetime.year)
print("Месяц:", current_datetime.month)
print("День:", current_datetime.day)
print("Время:", current_datetime.time())

#3
numbers = [147, 241, 39, 5, 778, 18, 0, 10]

even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
odd_count = len(list(filter(lambda x: x % 2 != 0, numbers)))

print("Список целых чисел:", numbers)
print("Количество четных чисел:", even_count)  
print("Количество нечетных чисел:", odd_count)  

#block2
#1
import numpy as np
import random

array = np.random.randint(0, 101, (10, 10))

min_value = np.min(array)
max_value = np.max(array)

print("Массив 10x10 со случайными значениями:")
print(array)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)

#5
from datetime import datetime, timedelta

year = 2022
month = 8

start_date = datetime(year, month, 1)
days_in_month = 31  

print("Все даты для августа 2022 года:")
for day in range(days_in_month):
    date = start_date + timedelta(days=day)
    print(date.strftime("%Y-%m-%d"))
