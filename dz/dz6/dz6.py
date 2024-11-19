#block1
#1
def main():
    n = int(input("Введите длину списка: "))
    nums = list(map(int, input(f"Введите {n} чисел через пробел: ").split()))
    
    if len(nums) != n:
        print("Количество чисел не совпадает с заданной длиной!")
        return

    odd_numbers = [x for x in nums if x % 2 != 0]
    even_numbers = [x for x in nums if x % 2 == 0]
    
    print("Нечетные числа:", *odd_numbers)
    print("Четные числа:", *even_numbers)
    print("YES" if len(even_numbers) >= len(odd_numbers) else "NO")

if __name__ == "__main__":
    main()

#2
def create_matrix():
    """
    Создает вложенный список (матрицу) размером 3x3.
    Возвращает матрицу.
    """
    print("Введите элементы матрицы (построчно):")
    matrix = []
    for i in range(3):
        row = list(map(int, input().split()))
        if len(row) != 3:
            raise ValueError("Каждая строка должна содержать ровно 3 числа.")
        matrix.append(row)
    return matrix

def diagonal_sum(matrix):
  
    return sum(matrix[i][i] for i in range(3))

def main():
    try:
        matrix = create_matrix()
        
        diag_sum = diagonal_sum(matrix)
        
        print("Ваша матрица:")
        for row in matrix:
            print(*row)
        print(f"Сумма главной диагонали: {diag_sum}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

#block
#2
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

n = int(input("Введите число: "))
print(is_power_of_two(n))
