import random

# TASK 1

"""Задача 1. В змінній min лежить число від 0 до 59, згенероване випадковим чином. Визначте в якій четверті години 
попадає це число (в першій, другій, третій чи четвертій). """

min = random.randint(0, 49)

if min <= 15:
    print('The first half')
elif min <= 30:
    print('The second half')
elif min <= 45:
    print('The third half')
else:
    print('The Fourth half')

# TASK 2
"""В змінній birth_month запишіть номер місяця вашого народження (дані введіть з консолі). В залежності від введених даних виведіть характеристику для відповідної пори року:
Зима - За вікном падав сніг.
Весна - Все довкола розцвітало.
Літо - Діти насолоджувались літніми канікулами.
Осінь - Все довкола загоралось яскравими фарбами."""

birth_month_input = input("Can you please input the number of the month when you were born? ")

if birth_month_input.isdigit():
    birth_month = int(birth_month_input)
    if birth_month in [12, 1, 2]:
        print("Winter - it's a little bit cold outside WHERE IS YOUR HAT!!!")
    elif birth_month in [3, 4, 5]:
        print("Spring - looks I finally see green")
    elif birth_month in [6, 7, 8]:
        print('Summer - WOW, time to take vacation')
    elif birth_month in [9, 10, 11]:
        print("Autumn - I need more coffee, tea and pills")
    else:
        print('Hello Alien !.!')
else:
    print("Invalid input. Please enter a numeric value.")

# TASK 4
"""Число ділиться на 6 тільки в випадку виконання двох умов: остання цифра парна, а сума всіх цифр ділиться на 3.
Рандомним чином згенеруйте будь-яке ціле число і перевірте чи воно ділиться на 6. В випадку позитивного результату
виведіть повідомлення “Число х ділиться на 6” або у випадку негативної “Число х не ділиться на 6” відповідно. ( тут
не хочеться бачити n%6 == 0, основне - знайти суму всіх цифр і перевірити чи вона кратна 3) """

random_number = random.randint(0, 1000)
last_int = int(str(random_number)[-1])
sum_random = sum(map(int, str(random_number)))
division = str(sum_random / 3)
v = division.split('.')

if last_int in [2, 4, 6, 8] and v[1] == '0':
    print(f'Число {random_number} ділиться на 6')
else:
    print(f'Число {random_number} не ділиться на 6')

# TASK 5
'''За введеними координатами з'ясувати, до якої координатної чверті належить точка. ( Координати ввести з консолі,
варто зауважити, що це можуть бути не лише цілі числа. Опрацювати варіант, коли точка- початок координат або лежить
на осі ) Намалюйте блок-схему до даної задачі і прикріпіть зображення до домашнього завдання. '''

x = float(input('Input value for x= '))
y = float(input('Input value for y= '))

if x == 0:
    print("The point lies on the Y-axis")
elif y == 0:
    print("The point lies on the X-axis")
elif x > 0 and y > 0:
    print("The point is in the first coordinate quadrant")
elif x < 0 and y > 0:
    print("The point is in the second coordinate quadrant")
elif x < 0 and y < 0:
    print("The point is in the third coordinate quadrant")
elif x > 0 and y < 0:
    print("The point is in the fourth coordinate quadrant")
elif x == 0 and y == 0:
    print("The point is at the origin")


