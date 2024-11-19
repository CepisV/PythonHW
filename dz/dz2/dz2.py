#1
input_str = input("Введите строку из двух слов: ")
words = input_str.split()  
if len(words) == 2:
    result = f"{words[1]} {words[0]}" 
    print(result)
else:
    print("Пожалуйста, введите строку, состоящую только из двух слов.")

#2   
input_str = input("Введите строку: ")
word_count = input_str.count(" ") + 1  
print("Количество слов:", word_count)

#3
input_str = input("Введите строку с годом 2020: ")
result = input_str.replace("2020", "2021")  
print(result)


#ewe zadaniya
#1
grades = input("Введите список оценок через пробел: ").split()
grades = list(map(int, grades))  

fives = grades.count(5)
fours = grades.count(4)
threes = grades.count(3)
twos = grades.count(2)

print(f"{fives} {fours} {threes} {twos}")

average_grade = sum(grades) / len(grades)
print(average_grade)

#2
grades = input("Введите список оценок через пробел: ")
modified_grades = grades.replace("2", "3")  
print(modified_grades)
