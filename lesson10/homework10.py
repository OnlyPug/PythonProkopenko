from lesson10.arithmetic_operation import sum_for_numbers as sum_for_two
from lesson10 import sum_for_numbers, divide_for_numbers
import csv
import re

"""1.Реалізуйте бібліотеку з будь-яким функціоналом. Наприклад, створіть функції для арифметичних операцій і
побудуйте каскад імпортів з декількох packagів. Має бути можливість імпортувати деякі функції з пакета, але не всі."""

# Варіант 1 коли сама бібліотека лежить на рівні

print(sum_for_two(4, 5))

# Варіант каскад чи "папка з папкою")))

print(sum_for_numbers(8, 3, 6))
print(divide_for_numbers(80, 4, 9))

"""2. Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів (domains.txt) та повертає їх у
вигляді списку рядків (назви повертати без крапки)."""


def parameter_domains(file):
    with open(file) as domains:
        read = domains.readlines()
        list_domains = []
        for i in read:
            remove_dot = i.replace('.', '')
            remove_symbols = remove_dot.rstrip()
            list_domains.append(remove_symbols)
        return list_domains


print(parameter_domains('domains.txt'))

"""3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з 
нього. Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і записати туди дані"""


def parameter_names(file):
    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['surname'])


parameter_names('names.txt')

"""4. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) і повертає список словників виду {
"date": date} у яких date - це дата з рядка (якщо є), Наприклад [{"date": "1st January 1919"}, {"date": "8th February 
1828"}, ...]"""


def parameter_authors(file):
    pattern = re.compile(r'\d{1,2}[a-z]{2}.\w+.\d{4}')
    date_list = []
    with open(file) as date:
        for line in date:
            result = pattern.findall(line)
            for x in result:
                date_list.append({"date": x})
        print(date_list)


parameter_authors('authours.txt')

"""5.Створіть функцію, яка читає файл csv. Вона приймає назву файлу(str), повертає список рядків(list). Також 
створіть функцію, яка записує в файл данні. Вона приймає назву файлу(str), список рядків(list), які треба записать в 
файл. Нічого не повертає. Тепер за допомогою створених функцій спочатку створіть файл(3 рядків достатньо), 
потім прочитайте той-же файл, записавши рядки в змінну, потім додайте два рядки в змінну, і після цього запишіть ваші 
зміни в інший файл."""

first_text = [['name', 'surname', 'age', 'gender', 'country', 'number'],
              ['Anna', 'Rila', 36, 'm', 'indian', 48454892],
              ['Juju', 'Bubu', 12, 'm', 'asian', 22480000],
              ['Agent', '007', 'none', 'm', 'british', '???007???']]

second_text = [['008', 'Some', 50, 'w', 'german', 84894684],
               ['Anna','Bulka','27','w','ukrainian',68416825]]


def read_file(file):
    with open(file, 'r', newline='') as read_line:
        lines = []
        csv_reader = csv.reader(read_line, delimiter=',')
        for row in csv_reader:
            lines.append(row)
        return lines


def write_file(file, lines):
    with open(file, 'w', newline='') as write_line:
        csv_writer = csv.writer(write_line)
        csv_writer.writerows(lines)


def copy_list_to_new_file(file, old_list, new_list):
    with open(file, 'w',  newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(old_list)
        writer.writerows(new_list)


write_file('task5.csv', first_text)
old_list = (read_file('task5.csv'))
print(old_list)
print(copy_list_to_new_file('copy_with_new.csv', old_list, second_text))
