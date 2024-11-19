#1
#2
a1, b1, c1 = map(int, input("Введите три целых числа a, b и c через пробел: ").split())
a2, b2, c2 = map(int, input("Введите три целых числа a, b и c через пробел: ").split())

print((a1 + b1) > c1)
print((a2 + b2) > c2)


#3
a1 = int(input("Введите число a: "))
a2 = int(input("Введите число a: "))

print(a1 % 2 == 0)
print(a2 % 2 == 0)


#block2 
#2
n = int(input("Введите целое число n: "))

if n > 0:
    n += 1  
elif n < 0:
    n -= 2  
else:
    n = 10  

print(n)

#block2
#3
n = int(input("Введите целое число: "))

if (-15 < n <= 12) or (14 < n < 17) or (n >= 19):
    print(True)  
else:
    print(False)  

#5
n = int(input("Введите количество программистов: "))

ending = "программистов"  

if n % 10 == 1:
    if n % 100 != 11:
        ending = "программист"  
elif 2 <= n % 10 <= 4:
    if not (12 <= n % 100 <= 14):
        ending = "программиста"  

print(f"{n} {ending}")


