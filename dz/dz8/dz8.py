#1
def generate_cubes(lst):
    return {x: x**3 for x in lst if x % 2 != 0}

lst = [1, 2, 3, 4, 5, 6, 7]
result = generate_cubes(lst)
print(result)

#2
def generate_even_numbers(lst):
    return {x for x in lst if x % 2 == 0}

lst = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
result = generate_even_numbers(lst)
print(result)

#3
def generate_multiples_of_10():
    return [i * 10 for i in range(10)]

result = generate_multiples_of_10()
print(result)

#4
def divisible_by_seven(n):
    for i in range(n + 1):
        if i % 7 == 0:
            yield i

n = 50
result = list(divisible_by_seven(n))
print(result)

