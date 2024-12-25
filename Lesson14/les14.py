#OOP
#3
class Country:
    def __init__(self, name="", continent="", population=0, phone_code="", capital="", cities=None):
        if cities is None:
            cities = []
        self.__name = name
        self.__continent = continent
        self.__population = population
        self.__phone_code = phone_code
        self.__capital = capital
        self.__cities = cities

    def set_name(self, name):
        self.__name = name

    def set_continent(self, continent):
        self.__continent = continent

    def set_population(self, population):
        self.__population = population

    def set_phone_code(self, phone_code):
        self.__phone_code = phone_code

    def set_capital(self, capital):
        self.__capital = capital

    def set_cities(self, cities):
        self.__cities = cities

    def get_name(self):
        return self.__name

    def get_continent(self):
        return self.__continent

    def get_population(self):
        return self.__population

    def get_phone_code(self):
        return self.__phone_code

    def get_capital(self):
        return self.__capital

    def get_cities(self):
        return self.__cities

    def display_info(self):
        print(f"Страна: {self.__name}")
        print(f"Континент: {self.__continent}")
        print(f"Население: {self.__population}")
        print(f"Телефонный код: {self.__phone_code}")
        print(f"Столица: {self.__capital}")
        print(f"Города: {', '.join(self.__cities)}")


if __name__ == "__main__":
    country1 = Country()
    country1.set_name("Чехия")
    country1.set_continent("Европа")
    country1.set_population(10700000)
    country1.set_phone_code("+420")
    country1.set_capital("Прага")
    country1.set_cities(["Прага", "Брно", "Острава", "Пльзень"])

    country1.display_info()

    print("Столица:", country1.get_capital())
    print("Континент:", country1.get_continent())


#block2
class Person:
    def __init__(self, name="", age=0, address=""):
        self.__name = name
        self.__age = age
        self.__address = address

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str) and name.strip(): 
            self.__name = name
        else:
            raise ValueError("Имя должно быть непустой строкой.")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age >= 0:  
            self.__age = age
        else:
            raise ValueError("Возраст должен быть целым неотрицательным числом.")

    def get_address(self):
        return self.__address

    def set_address(self, address):
        if isinstance(address, str):  
            self.__address = address
        else:
            raise ValueError("Адрес должен быть строкой.")

    def display_info(self):
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Адрес: {self.__address}")


if __name__ == "__main__":
    person = Person()
    
    person.set_name("Ян Новак")
    person.set_age(23)
    person.set_address("г. Прага, ул. Карлова, д. 15")
    
    print("Информация о человеке:")
    print("Имя:", person.get_name())
    print("Возраст:", person.get_age())
    print("Адрес:", person.get_address())

    print("\nПолная информация:")
    person.display_info()


#Book
class Book:
    def __init__(self, title, author, year):
        self.__title = title  
        self.__author = author  
        self.__year = year  
        self.__is_checked_out = False 

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_checked_out(self):
        return self.__is_checked_out

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_year(self, year):
        self.__year = year

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            print(f"Книга '{self.__title}' теперь выдана.")
        else:
            print(f"Книга '{self.__title}' уже выдана.")

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            print(f"Книга '{self.__title}' возвращена в библиотеку.")
        else:
            print(f"Книга '{self.__title}' уже в наличии.")

    def toggle_status(self):
        self.__is_checked_out = not self.__is_checked_out
        status = "выдана" if self.__is_checked_out else "в наличии"
        print(f"Книга '{self.__title}' теперь {status}.")

    def display_info(self):
        status = "Выдана" if self.__is_checked_out else "В наличии"
        print(f"Название: {self.__title}")
        print(f"Автор: {self.__author}")
        print(f"Год издания: {self.__year}")
        print(f"Статус: {status}")


if __name__ == "__main__":
    book1 = Book("Триумфальная арка", "Эрих Мария Ремапрк", 1945)

    book1.display_info()
    print("\nПроверяем статус книги:")
    book1.check_out()
    book1.display_info()
    print("\nВозвращаем книгу:")
    book1.return_book()
    book1.display_info()
    print("\nИзменяем статус через toggle_status:")
    book1.toggle_status()
    book1.display_info()


#extra task
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        sum_left_leaves = 0
        if root.left and not root.left.left and not root.left.right:
            sum_left_leaves += root.left.val  #этот момент я не совсем понял. пришлось прибегнуть к помощи интрнета

        sum_left_leaves += self.sumOfLeftLeaves(root.left)
        sum_left_leaves += self.sumOfLeftLeaves(root.right)

        return sum_left_leaves

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    result = solution.sumOfLeftLeaves(root)
    print(f"Сумма левх листьев: {result}")

