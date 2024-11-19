#task1
# Ввод строки
s = input("Введите строку: ")

# 1
print("Третий символ строки:", s[2])

# 2
print("Предпоследний символ строки:", s[-2])

# 3
print("Первые пять символов строки:", s[:5])

# 4
print("Вся строка, кроме последних двух символов:", s[:-2])

# 5
print("Все символы с четными индексами:", s[::2])

# 6
print("Все символы с нечетными индексами:", s[1::2])

# 7
print("Все символы в обратном порядке:", s[::-1])

# 8
print("Все символы через один в обратном порядке:", s[::-2])

# 9
print("Длина строки:", len(s))

#task2
# 3
numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))

total_sum = sum(numbers)

print("Сумма всех элементов списка:", total_sum)

# 4
numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))

positive_count = sum(1 for x in numbers if x > 0)
negative_count = sum(1 for x in numbers if x < 0)

print("Количество положительных чисел:", positive_count)
print("Количество отрицательных чисел:", negative_count)

#5
numbers = list(map(int, input("Введите элементы списка через пробел: ").split()))

even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]

print("Четные числа:", even_numbers)
print("Нечетные числа:", odd_numbers)

#task2
#1
A, B = input("Введите загаданное Петей и предложенное Васей числа через пробел: ").split()

bulls = sum(1 for i in range(4) if A[i] == B[i])

cows = 0
remaining_A = []
remaining_B = []

for i in range(4):
    if A[i] != B[i]:
        remaining_A.append(A[i])
        remaining_B.append(B[i])


for digit in remaining_B:
    if digit in remaining_A:
        cows += 1
        remaining_A.remove(digit)  

print(bulls, cows)

#2
students = input("Введите список фамилий через пробел: ").split()

expelled_student = input("Введите фамилию отчисленного студента: ")

if expelled_student in students:
    students.remove(expelled_student)

print(" ".join(students))


