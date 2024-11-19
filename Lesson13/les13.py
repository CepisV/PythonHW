#block1
#ex1
def main():
    try:
        first_value = input("Первое значение: ")
        second_value = input("Второе значение: ")
        
        try:
            first_number = float(first_value)
            second_number = float(second_value)
            result = first_number + second_number
        except ValueError:
            result = first_value + second_value
        
        print("Результат:", result)
    
    except Exception as e:
        print("Произошла ошибка:", e)

if __name__ == "__main__":
    main()

#2
def main():
    try:
        user_input = input("Введите трехзначное число: ")
        
        if not user_input.isdigit() or len(user_input) != 3:
            raise ValueError("Ошибка: Введите корректное трехзначное число.")
        
        digits = [int(d) for d in user_input]  
        digit_sum = sum(digits)  
        
        digit_product = 1
        for d in digits:
            if d == 0:
                raise ZeroDivisionError("Ошибка: Нельзя делить на 0.")
            digit_product *= d
        
        print(f"Сумма цифр: {digit_sum}")
        print(f"Произведение цифр: {digit_product}")
    
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError as zde:
        print(zde)
    except Exception as e:
        print("Произошла неизвестная ошибка:", e)

if __name__ == "__main__":
    main()

#block2
#1
def avg(a, b):
    try:
        a = float(a)
        b = float(b)
        
        if a < 0 or b < 0:
            raise ValueError("Ошибка: одно или оба значения отрицательные.")
        
        return (a * b) ** 0.5
    
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
    except TypeError as te:
        print(f"Ошибка типа: {te}")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")

print(avg(4, 9))    
print(avg(-4, 9))   
print(avg("a", 9))  

#block3
#1
class NameTooLongError(Exception):
    pass

def check_name(name):
    if len(name) > 4:
        raise NameTooLongError(f"Имя слишком длинное: {name}")
    print(f"Имя '{name}' прошло проверку.")

try:
    check_name("Влад")   
    check_name("Владислав")  
except NameTooLongError as e:
    print(f"Ошибка: {e}")

#ExtraTask
def remove_duplicates(nums):
    if not nums:  
        return 0

    k = 1  

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:  
            nums[k] = nums[i]       
            k += 1

    return k

nums = [5, 5, 4, 4, 3, 2, 2, 1]
expectedNums = [5, 4, 3, 2, 1]

k = remove_duplicates(nums)

assert k == len(expectedNums), "Количество уникальных элементов неверно"
for i in range(k):
    assert nums[i] == expectedNums[i], f"Элемент nums[{i}] некорректен"

print("Все тесты пройдены!")
print(f"Массив после удаления дубликатов: {nums[:k]}")
print(f"Количество уникальных элементов: {k}")
