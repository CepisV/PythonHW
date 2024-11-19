#block1
#zad3
from datetime import datetime

input_string = "1 января 2014 14:43"

input_format = "%d %B %Y %H:%M"

date_time_obj = datetime.strptime(input_string, input_format)

output_format = "%Y-%d-%m %H:%M:%S"
output_string = date_time_obj.strftime(output_format)

print(output_string)

#zad4
from datetime import datetime

current_time = datetime.now()

formatted_time = current_time.strftime("%H:%M:%S.%f")

print(formatted_time)


#block2
#zad3
from datetime import date, timedelta

start_year = 2015
end_year = 2016

monday_count = 0

for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        first_day = date(year, month, 1)
        if first_day.weekday() == 0:  
            monday_count += 1

print(f"Число понедельников, выпадающих на 1-е число месяца: {monday_count}")

#zad4
import time

message = "Это строка выводится с задержкой"

for _ in range(5):
    print(message)
    time.sleep(3)  

#zad5
from datetime import datetime, timedelta

current_date = datetime.now()

date_before = current_date - timedelta(days=30)

date_after = current_date + timedelta(days=30)

print(f"Текущая дата: {current_date.strftime('%Y-%m-%d')}")
print(f"Дата за 30 дней до: {date_before.strftime('%Y-%m-%d')}")
print(f"Дата через 30 дней: {date_after.strftime('%Y-%m-%d')}")
    
#block3
#zad1
input_file_path = "input.txt"  
output_file_path = "output.txt"  

with open(input_file_path, "r", encoding="utf-8") as infile, open(output_file_path, "w", encoding="utf-8") as outfile:
    for line in infile:
        words = line.split()
        long_words = [word for word in words if len(word) >= 7]
        if long_words:
            outfile.write(" ".join(long_words) + "\n")

print(f"Слова длиной не менее 7 букв записаны в файл: {output_file_path}")

#block4
#zad1
import os
import shutil

extensions = ["mp3", "flac", "oga"]

current_directory = os.getcwd()

for ext in extensions:
    folder_path = os.path.join(current_directory, ext)
    os.makedirs(folder_path, exist_ok=True)  

for file_name in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, file_name)):
        file_extension = file_name.split('.')[-1].lower()
        if file_extension in extensions:
            destination_folder = os.path.join(current_directory, file_extension)
            shutil.move(os.path.join(current_directory, file_name), destination_folder)

print("Файлы распределены по папкам в зависимости от их расширений.")

