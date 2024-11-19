#
#zad2
salary = float(input("Введите зарплату за месяц: "))
credit_payment = float(input("Введите сумму месячного платежа по кредиту: "))
utility_debt = float(input("Введите задолженность за коммунальные услуги: "))

remaining_amount = salary - credit_payment - utility_debt

print("Сумма, которая останется после всех выплат:", remaining_amount)

#3
d1 = float(input("Введите длину первой диагонали ромба: "))
d2 = float(input("Введите длину второй диагонали ромба: "))

area = (d1 * d2) / 2

print("Площадь ромба:", area)

#2
#zad2
R = float(input("Введите радиус: "))

pi = 3.14

L = 2 * pi * R

S = pi * R ** 2

print(f"L = {L:.2f}")
print(f"S = {S:.2f}")

#5
x = int(input("Введите целое число x: "))

y = 3 * x**2 - 6 * x - 7

print("Значение y:", y)

#6
x = int(input("Введите целое число x: "))

y = 4 * (x - 3) - 7 * (x - 3) + 2

print("Значение y:", y)
