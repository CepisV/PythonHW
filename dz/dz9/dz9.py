#block1
#1
import datetime

def get_week_number(year, month, day):
    date = datetime.date(year, month, day)
    week_number = date.isocalendar()[1]
    return week_number

year, month, day = 2015, 6, 16
print(get_week_number(year, month, day))

#2
import datetime

def first_monday_of_week(year, week):
    first_day_of_year = datetime.date(year, 1, 1)
    day_of_week = first_day_of_year.weekday()
    days_to_monday = (day_of_week - 0) % 7
    first_monday = first_day_of_year - datetime.timedelta(days=days_to_monday)
    
    delta_weeks = datetime.timedelta(weeks=week - 1)
    monday_of_week = first_monday + delta_weeks
    
    return monday_of_week.strftime('%a %d %B %H:%M:%S %Y')

year, week = 2015, 50
print(first_monday_of_week(year, week))

#block2
#1
import datetime

def get_utc_and_local_time():
    utc_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

    local_time = datetime.datetime.now()

    return utc_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'), local_time.strftime('%Y-%m-%d %H:%M:%S')

utc_time, local_time = get_utc_and_local_time()
print(f"Время по Гринвичу: {utc_time}")
print(f"Местное время: {local_time}")

#block3
#1
import os #для работы с ОС
import shutil #для работы с файлами и каталогами

def move_files():
    current_dir = os.getcwd()
    video_dir = os.path.join(current_dir, 'video')
    sub_dir = os.path.join(current_dir, 'sub')
    watch_me_dir = os.path.join(current_dir, 'watch_me')

    if not os.path.exists(watch_me_dir):
        os.makedirs(watch_me_dir)

    def move_files_from_folder(src_dir):
        for file_name in os.listdir(src_dir):
            file_path = os.path.join(src_dir, file_name)
            if os.path.isfile(file_path):  
                shutil.move(file_path, watch_me_dir)

    move_files_from_folder(video_dir)
    move_files_from_folder(sub_dir)

    print(f"Все файлы перемещены в папку {watch_me_dir}")

move_files()

