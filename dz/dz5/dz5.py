#1
import math

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

lcm = abs(a * b) // math.gcd(a, b)
print("Наименьшее общее кратное:", lcm)


#for
#2
n = int(input("Введите число n: "))

for i in range(1, n + 1):
    print("".join(str(x) for x in range(1, i + 1)))

#cycle
#2
N = int(input("Введите число N: "))

i = 1
while i * i <= N:
    print(i * i, end=" ")
    i += 1

