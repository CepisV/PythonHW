#1 index
def access_array_element(arr, index):
    try:
        print(f"Элемент массива на индексе {index}: {arr[index]}")
    except IndexError:
        print("Ошибка: Индекс выходит за пределы массива!")

arr = [10, 20, 30, 40, 50]
access_array_element(arr, 5) 
access_array_element(arr, 2)  

#2 plus_two
def plus_two(number):
    try:
        result = 2 + number
        print(f"Результат: {result}")
    except TypeError:
        print("Ожидаемый тип данных — число!")

plus_two(5)  
plus_two("hello")  
