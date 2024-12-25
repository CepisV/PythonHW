#task1
class Car:
    def __init__(self, model=None, year=None, manufacturer=None, engine_volume=None, color=None, price=None):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def set_data(self, model, year, manufacturer, engine_volume, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def get_data(self):
        return {
            "Model": self.__model,
            "Year": self.__year,
            "Manufacturer": self.__manufacturer,
            "Engine Volume": self.__engine_volume,
            "Color": self.__color,
            "Price": self.__price
        }

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

car = Car()
car.set_data("Audi RS4", 2021, "Wolkcvagen", 75, "Gray", 4000000)
print(car.get_data())

#task2
class Book:
    def __init__(self, title=None, year=None, publisher=None, genre=None, author=None, price=None):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def set_data(self, title, year, publisher, genre, author, price):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def get_data(self):
        return {
            "Title": self.__title,
            "Year": self.__year,
            "Publisher": self.__publisher,
            "Genre": self.__genre,
            "Author": self.__author,
            "Price": self.__price
        }

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

book = Book()
book.set_data("1984", 1949, "Secker & Warburg", "Dystopian", "George Orwell", 15)
print(book.get_data())

#task3
class Stadium:
    def __init__(self, name=None, opening_date=None, country=None, city=None, capacity=None):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def set_data(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def get_data(self):
        return {
            "Name": self.__name,
            "Opening Date": self.__opening_date,
            "Country": self.__country,
            "City": self.__city,
            "Capacity": self.__capacity
        }

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

stadium = Stadium()
stadium.set_data("Signal Iduna Park", "1971-1974", "Germany", "Dortmund", 81365)
print(stadium.get_data())

#task4
class MainClass:
    def __init__(self, text=""):
        self.__text = text

    def set_text(self, text=None):
        if text:
            self.__text = text
        else:
            self.__text = "Default text"

    def get_text(self):
        return self.__text


class SubClass(MainClass):
    def __init__(self, text="", number=0):
        super().__init__(text)
        self.__number = number

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

main_obj = MainClass("Hello, world!")
print(main_obj.get_text())
main_obj.set_text()
print(main_obj.get_text())

sub_obj = SubClass("Child class text", 42)
print(sub_obj.get_text())
print(sub_obj.get_number())