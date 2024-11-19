#block1
#3
total_sum = 0  

while True:
    n = int(input("Введите целое число (0 для выхода): "))  
    if n == 0: 
        break  
    total_sum += n  

print(total_sum)

#block2 for
#1
start = int(input("Введите первое число (начало диапазона): "))
end = int(input("Введите второе число (конец диапазона): "))

print("Все числа в диапазоне:")
for num in range(start, end + 1):
    print(num, end=' ')
print()  

print("Нечетные числа в диапазоне:")
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=' ')
print()  

print("Четные числа в диапазоне:")
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=' ')
print() 

print("Все числа в диапазоне в порядке убывания:")
for num in range(end, start - 1, -1):
    print(num, end=' ')
print() 

#block3 
#1
n = 5  

for i in range(n):
    for j in range(i + 1):
        print("*", end=' ')
    print()  

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print()    

#2
while True:
    n = int(input("Введите целое число: "))  
    if n < 10:
        continue  
    if n > 100:
        break  
    print(n)  

#3
for num in range(1, 101):  
    divisors = 0  
    
    for i in range(1, num):
        if num % i == 0:  
            divisors += i  

    if divisors == num:
        print(num) 
