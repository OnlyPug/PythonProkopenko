import random

"""Створіть декоратор, який виводить в консоль ім'я функції, яку було викликано. Наприклад, створіть пару функцій для
арифметичних операцій додавання і множення. При виклику цих функцій має повертатись результат операції і виводиться в
консоль ім'я функції, яку було викликано. """


def name_func(func):
    def inner(*args, **kwargs):
        print(f"Викликано функцію: {func.__name__}")
        print(f'Які аргументи були введені: {args}')  # це я чисто для себе)
        result = func(*args, **kwargs)
        print(f"Твій результат пане: {result}")

    return inner


@name_func
def perfect_sum(*args):
    return sum(args)


@name_func
def perfect_multiplication(*args):
    result = 1
    for num in args:
        result *= num
    return result


perfect_sum(4, 8, 10)
perfect_multiplication(2, 2, 10)

"""Створіть за допомогою list comprehension список, в якому буде 100 елементів, і кожен із яких буде в границях від 1 
до 10(для цього можна скористатись функцією randint із модуля random). Порахуйте кількість кожного елемента і 
виведіть в консоль"""

list_comprehension = [random.randint(1, 10) for item in range(100)]


def count_for_numbers(elements):
    number = 1
    while number <= 10:
        element_counts = elements.count(number)
        print(f"Елемент {number} зустрічається {element_counts} разів")
        number += 1


count_for_numbers(list_comprehension)
