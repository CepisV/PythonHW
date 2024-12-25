#task1
class Number:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value + other)
        else:
            raise TypeError("Операнд должен быть объектом числом")

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value - other)
        else:
            raise TypeError("Операнд должен быть объектом числом")

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value * other)
        else:
            raise TypeError("Операнд должен быть объектом числом")

    def __truediv__(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                raise ZeroDivisionError("Деление на ноль недопустимо")
            return Number(self.value / other.value)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль недопустимо")
            return Number(self.value / other)
        else:
            raise TypeError("Операнд должен быть объектом числом")

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Number({self.value})"
    
num1 = Number(16)
num2 = Number(2)

print(num1 + num2) 
print(num1 - num2)  
print(num1 * num2)  
print(num1 / num2)

#task3
class Library:
    def __init__(self, name, address, book_count=0):
        self.name = name
        self.address = address
        self.book_count = book_count

    def __str__(self):
        return f"Библиотека '{self.name}' по адресу {self.address}. Количество книг: {self.book_count}"

    def __add__(self, value):
        if isinstance(value, int) and value >= 0:
            return Library(self.name, self.address, self.book_count + value)
        else:
            raise ValueError("К количеству книг можно добавлять только положительные числа")

    def __sub__(self, value):
        if isinstance(value, int) and value >= 0:
            if self.book_count - value < 0:
                raise ValueError("Количество книг не может быть отрицательным")
            return Library(self.name, self.address, self.book_count - value)
        else:
            raise ValueError("Из количества книг можно вычитать только положительные числа")

    def __iadd__(self, value):
        if isinstance(value, int) and value >= 0:
            self.book_count += value
            return self
        else:
            raise ValueError("К количеству книг можно добавлять только положительные числа")

    def __isub__(self, value):
        if isinstance(value, int) and value >= 0:
            if self.book_count - value < 0:
                raise ValueError("Количество книг не может быть отрицательным")
            self.book_count -= value
            return self
        else:
            raise ValueError("Из количества книг можно вычитать только положительные числа")

    def __lt__(self, other):
        if isinstance(other, Library):
            return self.book_count < other.book_count
        raise TypeError("Сравнивать можно только с объектами класса Library")

    def __gt__(self, other):
        if isinstance(other, Library):
            return self.book_count > other.book_count
        raise TypeError("Сравнивать можно только с объектами класса Library")

    def __le__(self, other):
        if isinstance(other, Library):
            return self.book_count <= other.book_count
        raise TypeError("Сравнивать можно только с объектами класса Library")

    def __ge__(self, other):
        if isinstance(other, Library):
            return self.book_count >= other.book_count
        raise TypeError("Сравнивать можно только с объектами класса Library")

library1 = Library("Национальная академическая библиотека", "ул. Достык, 11", 2000000)
library2 = Library("Центральная городская библиотека", "ул. Бейбитшилик, 26", 150000)

print(library1)  
print(library2) 

library1 += 100
print(library1)  

library2 -= 500
print(library2)  

print(library1 > library2)  
print(library1 < library2)   
print(library1 <= library2)  
print(library2 <= library1)

#task4
from datetime import date

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.date = date(year, month, day) 

    def __sub__(self, other):
        if isinstance(other, Date):
            delta = self.date - other.date
            return delta.days
        return NotImplemented

    def __add__(self, days):
        if isinstance(days, int):
            new_date = self.date + timedelta(days=days)
            return Date(new_date.day, new_date.month, new_date.year)
        return NotImplemented

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

from datetime import timedelta

date1 = Date(1, 1, 2024)
date2 = Date(15, 1, 2024)

days_diff = date2 - date1
print(f"Разница между датами: {days_diff} дней")  

new_date = date1 + 10
print(f"Новая дата после увеличения на 10 дней: {new_date}")  


#block2
#task1
import math

class Cylinder:
    def __init__(self, dia=1, h=1):
        super().__setattr__('dia', dia)
        super().__setattr__('h', h)
        super().__setattr__('area', self.make_area(dia, h))  

    def make_area(self, dia, h):      
        return math.pi * dia * h

    def __setattr__(self, key, value):
        if key == 'dia' or key == 'h':
            super().__setattr__(key, value)
            super().__setattr__('area', self.make_area(self.dia, self.h))
        elif key == 'area':
            raise AttributeError("Свойство 'area' нельзя изменять")
        else:
            super().__setattr__(key, value)

    def __str__(self):
        return f"Цилиндр: диаметр = {self.dia}, высота = {self.h}, площадь = {self.area:.2f}"

a = Cylinder(2, 6)

print(a)

#task3
import math

class MathOperations:
    @staticmethod
    def max_of_four(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min_of_four(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average_of_four(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Факториал только для положительгых чисел.")
        return math.factorial(n)

print("Максимум :", MathOperations.max_of_four(3, 5, 6, 7))
print("Минимум :", MathOperations.min_of_four(3, 5, 6, 7))
print("Среднее арифметическое :", MathOperations.average_of_four(3, 5, 6, 7))
print("Факториал 5:", MathOperations.factorial(5))
