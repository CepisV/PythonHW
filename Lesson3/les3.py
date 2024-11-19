#1
numbers_set = {1, 2, 3, 4, 5, 6, 12, 24}

number_to_remove = int(input("Enter the number you want to remove: "))

numbers_set.discard(number_to_remove)

print("After Removing:", numbers_set)

#2
items_set = {1, 2, 4}

new_items = {'Audi', 'BMW', 'KIA', 'Mersedez', 'Toyota'}

items_set.update(new_items)

print(items_set)

#3
set1 = {96, 2, 1, 59}

set2 = {65, 'Step', 'Academy'}

union_set = set1.union(set2)

print(union_set)

#4
countries = {"France", "Germany", "Italy", "Spain"}

while True:
    print("\n1. Добавить страну")
    print("2. Удалить страну")
    print("3. Поиск стран по символам")
    print("4. Проверка существования страны")
    print("5. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        country_to_add = input("Введите название страны для добавления: ")
        countries.add(country_to_add)
        print("Текущий список стран:", countries)
    
    elif choice == '2':
        country_to_remove = input("Введите название страны для удаления: ")
        countries.discard(country_to_remove)
        print("Текущий список стран:", countries)
    
    elif choice == '3':
        search_query = input("Введите символы для поиска: ")
        found_countries = {country for country in countries if search_query.lower() in country.lower()}
        print("Найденные страны:", found_countries)
    
    elif choice == '4':
        country_to_check = input("Введите название страны для проверки: ")
        if country_to_check in countries:
            print(f"{country_to_check} присутствует в множестве.")
        else:
            print(f"{country_to_check} отсутствует в множестве.")
    
    elif choice == '5':
        print("Выход.")
        break
    
    else:
        print("Неверный выбор. Попробуйте снова.")


#dictionary
#1


#2



