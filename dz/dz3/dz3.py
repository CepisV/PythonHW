#3
numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

unique_set = set()

for number, count in counts.items():
    for i in range(1, count + 1):
        unique_set.add(str(number) * i)

print(unique_set)

#dictionary
#2
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

initial_id = id(my_dict)

keys = list(my_dict.keys())

my_dict[keys[0]], my_dict[keys[-1]] = my_dict[keys[-1]], my_dict[keys[0]]

del my_dict[keys[1]]

my_dict["new_key"] = "new_value"

print("Адрес словаря в памяти остался тем же:", id(my_dict) == initial_id)
print("Итоговый словарь:", my_dict)

#3
import pickle

countries_dict = {
    "Russia": "Moscow",
    "France": "Paris",
    "Italy": "Rome",
    "Germany": "Berlin",
    "Spain": "Madrid"
}

while True:
    print("\nВыберите действие:")
    print("1 - Добавить страну и столицу")
    print("2 - Удалить страну")
    print("3 - Найти столицу по названию страны")
    print("4 - Редактировать столицу страны")
    print("5 - Сохранить данные в файл")
    print("6 - Загрузить данные из файла")
    print("7 - Показать текущий словарь")
    print("0 - Выйти из программы")
    
    choice = input("Ваш выбор: ")

    if choice == "1":
        country = input("Введите название страны: ")
        capital = input("Введите название столицы: ")
        countries_dict[country] = capital
        print(f"Добавлено: {country} - {capital}")

    elif choice == "2":
        country = input("Введите название страны для удаления: ")
        if country in countries_dict:
            del countries_dict[country]
            print(f"Удалено: {country}")
        else:
            print(f"Страна {country} не найдена.")

    elif choice == "3":
        country = input("Введите название страны для поиска: ")
        capital = countries_dict.get(country, "Страна не найдена.")
        print(f"Столица {country}: {capital}")

    elif choice == "4":
        country = input("Введите название страны для редактирования: ")
        if country in countries_dict:
            new_capital = input(f"Введите новую столицу для {country}: ")
            countries_dict[country] = new_capital
            print(f"Обновлено: {country} - {new_capital}")
        else:
            print(f"Страна {country} не найдена.")

    elif choice == "5":
        filename = input("Введите название файла для сохранения: ")
        with open(filename, "wb") as file:
            pickle.dump(countries_dict, file)
        print(f"Данные сохранены в файл {filename}")

    elif choice == "6":
        filename = input("Введите название файла для загрузки: ")
        try:
            with open(filename, "rb") as file:
                countries_dict = pickle.load(file)
            print(f"Данные загружены из файла {filename}")
        except FileNotFoundError:
            print("Файл не найден.")
        except pickle.UnpicklingError:
            print("Ошибка при загрузке данных.")

    elif choice == "7":
        print("Текущий словарь стран и столиц:", countries_dict)

    elif choice == "0":
        print("Выход из программы.")
        break

    else:
        print("Некорректный выбор. Пожалуйста, попробуйте снова.")
