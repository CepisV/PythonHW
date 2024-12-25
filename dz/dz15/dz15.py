#task1
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return 2 * math.pi * self.radius > 2 * math.pi * other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return 2 * math.pi * self.radius < 2 * math.pi * other.radius
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return 2 * math.pi * self.radius >= 2 * math.pi * other.radius
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return 2 * math.pi * self.radius <= 2 * math.pi * other.radius
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
        return self

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
        return self

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
        return self

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius -= value
        return self

    def __str__(self):
        return f"Circle(radius={self.radius})"
    
circle1 = Circle(5)
circle2 = Circle(7)

print(circle1 == circle2)  
print(circle1 < circle2)   

print(circle1 > circle2)   

circle1 += 2
print(circle1)

#task2
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complex(real_part, imag_part)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real**2 + other.imag**2
            real_part = (self.real * other.real + self.imag * other.imag) / denominator
            imag_part = (self.imag * other.real - self.real * other.imag) / denominator
            return Complex(real_part, imag_part)
        return NotImplemented

    def __str__(self):
        return f"{self.real} + {self.imag}i"

complex1 = Complex(2, 3)
complex2 = Complex(1, 4)

print(complex1 + complex2) 
print(complex1 - complex2) 
print(complex1 * complex2) 
print(complex1 / complex2) 

#task3
class Airplane:
    def __init__(self, model, passengers):
        self.model = model
        self.passengers = passengers

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model
        return NotImplemented

    def __add__(self, passengers):
        if isinstance(passengers, int):
            self.passengers += passengers
        return self

    def __sub__(self, passengers):
        if isinstance(passengers, int):
            self.passengers -= passengers
        return self

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers > other.passengers
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.passengers < other.passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.passengers >= other.passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.passengers <= other.passengers
        return NotImplemented

    def __str__(self):
        return f"Airplane(model={self.model}, passengers={self.passengers})"

airplane1 = Airplane("Boeing 747", 400)
airplane2 = Airplane("Airbus A380", 500)

print(airplane1 == airplane2) 
print(airplane1 + 50) 
print(airplane1 < airplane2)

#task4
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Flat):
            return self.area != other.area
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __str__(self):
        return f"Flat(area={self.area}, price={self.price})"

flat1 = Flat(50, 100000)
flat2 = Flat(50, 120000)

print(flat1 == flat2)  
print(flat1 != flat2) 
print(flat1 < flat2)

#extraTask
class Roman:
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    def __init__(self, value):
        self.value = value

    @staticmethod
    def to_roman(value):
        result = ''
        for numeral in sorted(Roman.roman_numerals.keys(), reverse=True):
            while value >= numeral:
                result += Roman.roman_numerals[numeral]
                value -= numeral
        return result

    @staticmethod
    def from_roman(roman):
        value = 0
        index = 0
        for numeral in sorted(Roman.roman_numerals.keys(), reverse=True):
            while roman[index:index+len(Roman.roman_numerals[numeral])] == Roman.roman_numerals[numeral]:
                value += numeral
                index += len(Roman.roman_numerals[numeral])
        return value

number = 1995
roman_number = Roman.to_roman(number)
print(f"{number} in Roman is {roman_number}")

roman_str = "MCMXCV"
integer_value = Roman.from_roman(roman_str)
print(f"{roman_str} is {integer_value}")
