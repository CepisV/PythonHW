#task1
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_point(self):
        return [self.x, self.y]

class PointColor(Point):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color

    def get_color(self):
        return self.color


point = Point(3, 4)
print("Координаты точки:", point.get_point())
print("Расстояние до начала координат:", point.distance_to_origin())

colored_point = PointColor(6, 8, "red")
print("\nКоординаты цветной точки:", colored_point.get_point())
print("Цвет точки:", colored_point.get_color())
print("Расстояние до начала координат:", colored_point.distance_to_origin())

#task2
class Pet:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def show(self):
        print(f"Имя: {self.name}")

    def type(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")


class Dog(Pet):
    def sound(self):
        print("Гав")

    def type(self):
        print("Тип: Собака")


class Cat(Pet):
    def sound(self):
        print("Мяу!")

    def type(self):
        print("Тип: Кошка")


class Parrot(Pet):
    def sound(self):
        print("Чик-чирик!")

    def type(self):
        print("Тип: Попугай")


class Hamster(Pet):
    def sound(self):
        print("Писк!")

    def type(self):
        print("Тип: Хомяк")

dog = Dog("Мухтпр")
cat = Cat("Леся")
parrot = Parrot("Геральт")
hamster = Hamster("Коин")

for pet in [dog, cat, parrot, hamster]:
    pet.show()
    pet.type()
    pet.sound()
    print()


#extraTask
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def start_engine(self):
        print(f"Двигатель автомобиля {self.make} {self.model} запустился.")

    def stop_engine(self):
        print(f"Двигатель автомобиля {self.make} {self.model} остановлен.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, type_of_handlebars):
        super().__init__(make, model)
        self.type_of_handlebars = type_of_handlebars

    def start_engine(self):
        print(f"Двигатель мотоцикла {self.make} {self.model} запустился.")

    def stop_engine(self):
        print(f"Двигатель мотоцикла {self.make} {self.model} остановлен.")


class Truck(Vehicle):
    def __init__(self, make, model, cargo_capacity, number_of_wheels):
        super().__init__(make, model)
        self.cargo_capacity = cargo_capacity
        self.number_of_wheels = number_of_wheels

    def start_engine(self):
        print(f"Двигатель грузовика {self.make} {self.model} запустился.")

    def stop_engine(self):
        print(f"Двигатель грузовика {self.make} {self.model} остановлен.")


class ElectricCar(Car):
    def __init__(self, make, model, number_of_doors, battery_capacity):
        super().__init__(make, model, number_of_doors)
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print(f"Электродвигатель автомобиля {self.make} {self.model} запустился.")

    def stop_engine(self):
        print(f"Электродвигатель автомобиля {self.make} {self.model} остановлен.")


car = Car("Honda", "acord", 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750.", "Standart")
truck = Truck("Volvo", "truckV", 25000, 8)
electric_car = ElectricCar("Tesla", "Model S", 4, 100)

vehicles = [car, motorcycle, truck, electric_car]

for vehicle in vehicles:
    print(f"\n--- {vehicle.make} {vehicle.model} ---")
    vehicle.start_engine()
    vehicle.stop_engine()

print("\nПроверка:")
for vehicle in vehicles:
    if isinstance(vehicle, ElectricCar):
        print(f"{vehicle.make} {vehicle.model} - электромобиль.")
    elif isinstance(vehicle, Truck):
        print(f"{vehicle.make} {vehicle.model} - грузовик.")
    elif isinstance(vehicle, Motorcycle):
        print(f"{vehicle.make} {vehicle.model} - мотоцикл.")
    elif isinstance(vehicle, Car):
        print(f"{vehicle.make} {vehicle.model} - автомобиль.")
