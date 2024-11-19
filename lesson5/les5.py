#4
wallet = {}
currencies = ["$", "€", "¥"]

def deposit(currency, amount):
    if currency in wallet:
        wallet[currency] += amount
    else:
        wallet[currency] = amount
    print(f"{amount} {currency} добавлено. Баланс: {wallet[currency]} {currency}")

def withdraw(currency, amount):
    if wallet.get(currency, 0) >= amount:
        wallet[currency] -= amount
        print(f"{amount} {currency} снято. Баланс: {wallet[currency]} {currency}")
    else:
        print(f"Недостаточно средств для снятия {amount} {currency}. Баланс: {wallet.get(currency, 0)} {currency}")

def check_balance(currency):
    print(f"Баланс: {wallet.get(currency, 0)} {currency}")

def choose_currency():
    print("\nВыберите валюту:")
    for i, currency in enumerate(currencies, start=1):
        print(f"{i} - {currency}")
    choice = int(input("Введите номер валюты: "))
    if 1 <= choice <= len(currencies):
        return currencies[choice - 1]
    else:
        print("Некорректный выбор валюты.")
        return choose_currency()

def main():
    print("*********My purse*********")

    while True:
        print("\nВыберите действие:")
        print("1 - Пополнить баланс")
        print("2 - Снять средства")
        print("3 - Проверить баланс")
        print("4 - Выйти")

        action = input("Введите номер действия: ")
        
        if action == "4":
            print("Выход из программы.")
            break
        elif action in ["1", "2", "3"]:
            currency = choose_currency()
            if action == "1":
                amount = float(input("Введите сумму: "))
                deposit(currency, amount)
            elif action == "2":
                amount = float(input("Введите сумму: "))
                withdraw(currency, amount)
            elif action == "3":
                check_balance(currency)
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 4.")

if __name__ == "__main__":
    main()


#block 2
#1
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

def get_numbers():
    numbers = input("Enter numbers: ").split()
    return int(numbers[0]), int(numbers[1])

base, exponent = get_numbers()
result = power(base, exponent)
print(f"{base} to the {exponent} power is {result}")



#2
def range_sum(a, b):
    if a > b:
        return 0
    return a + range_sum(a + 1, b)

def get_numbers():
    numbers = input("Enter numbers: ").split()
    return int(numbers[0]), int(numbers[1])

a, b = get_numbers()
result = range_sum(a, b)
print(f"Sum from {a} to {b} is {result}")



#fib
def fib(n):
    if n <= 1:
          return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Введите номер числа Фибоначчи: "))
print(f"Число Фибоначчи {n} равно {fib(n)}")
