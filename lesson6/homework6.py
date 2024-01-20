import random

# Task 1

"""1.Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх 
у порядку зростання. """


def list_of_numbers(set1, set2):
    third_set = set1.intersection(set2)
    print(sorted(third_set))


a = {55, 3, 7, 0, 1, 88, 124324, 234566, 757345, 6, 7, 8, 345}
b = {345, 1, 8, 9, 757345, 3, 5, 55, 7, 8}
list_of_numbers(a, b)

# Task 2

"""2.Створіть словник із даними про студентів: ключі - імена студентів, значення - бали для кожного. Програма повинна
визначити середній бал і вивести імена студентів, чий бал вище середнього."""

students_points = {'Harry': 89.8, 'Hermione': 100, 'Ron': 75.5, 'Lucius': 99.9, 'Tom': 95, 'Neville': 50}


def average_point_students(dictionary):
    sum_points = sum(dictionary.values())
    averege_point = sum_points / len(dictionary)
    print(f'Cередній бал групи: {round(averege_point, 1)}')
    for students, points in dictionary.items():
        if averege_point <= points:
            print(f'Імена наших студентів в яких вище середнього {students}')


average_point_students(students_points)

"""3.Створіть списки із значеннями для name, surname, location, наприклад name = ['Alex', 'John', 'Simba']. напишіть
програму, яка створює словники з даними випадкових людей на основі ваших списків, роздрукуйте результат. для
випадковості значень скористайтесь модулем random. приклад згенерованого словника:

{'name':'Liza', 'surname':'Djoconda', 'location':'Florence'}"""


def create_random_person():
    name = random.choice(['Anastasiia', 'Anna', 'Oleh', 'Dima', 'Alex', 'Vika'])
    surname = random.choice(['Prokopenko', 'Vinnuk', 'Koladenko', 'Leon', 'People'])
    location = random.choice(['Kyiv', 'NY', 'London', 'Tbilisi', 'Madagascar'])
    dictionary = {'name': name, 'surname': surname, 'location': location}
    print(f'Перший варіант вирішення 3 задачі {dictionary}')


create_random_person()

"""Ще один варіант коли списки знаходяться за функцією"""


def create_random_person2(name, surname, location):
    names = random.choice(name)
    surnames = random.choice(surname)
    locations = random.choice(location)
    dictionary = {'name': names, 'surname': surnames, 'location': locations}
    print(f'Другий варіант вирішення 3 задачі {dictionary}')


name = ['Anastasiia', 'Anna', 'Oleh', 'Dima', 'Alex', 'Vika']
surname = ['Prokopenko', 'Vinnuk', 'Koladenko', 'Leon', 'People']
location = ['Kyiv', 'NY', 'London', 'Tbilisi', 'Madagascar']
create_random_person2(name, surname, location)
