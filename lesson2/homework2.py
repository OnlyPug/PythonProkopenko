import math

# Task 1
""" Task 1.1 Запишіть програму, в яку спочатку запишіть в 1 змінну ваше ім'я, в 2 ваше прізвище, а потім виводить на
екран повідомлення з вашими особистими даними.Тут використайте конкатенацію, тобто об'єднайте стрічки. """

first_name = 'Anastasiia'
second_name = 'Prokopenko'
result = first_name + ' ' + second_name
print(result)

""" Task 1.2 Виведіть результат в нижньому, верхнього регістрах з капіталізацією перших букв кожного слова."""
print(result.lower())
print(result.upper())
print(result.title())

"""Task 1.3 Змініть значення своєї змінної, яку ви створили на кроці 1 , додавши до свого імені декілька пробілів на 
початку та вкінці. Прослідкуйте щоб \t \n зустрічались хоча б один раз. Виведіть нове значення. Видаліть пропуски і 
збережіть новий результат. """

first_name = '       \t    Anastasiia               '
second_name = '         Prokopenko  \n          '
result_before_srtip = first_name + ' ' + second_name
print(result_before_srtip)
result_after_strip = first_name.strip() + ' ' + second_name.strip()
print(result_after_strip)

# Task 2

"""Task 2 Створіть програму для обчислення довжини кола та площі круга за введеним радіусом. (Використати функцію pi 
модуля math) Радіус задайте в змінній. Вивести отримані результати, використовуючи f-string """

radius = 5
form_for_circumference = 2 * math.pi * radius
form_for_area = math.pi * radius**2

print(form_for_circumference)
print(form_for_area)
print(f'Дякую Вам велике за те що я згадувала що таке радіус=)')
print(f'Отож результут:\nДовжина кола - {form_for_circumference};\nПлоща круга - {form_for_area}')

# Task 3
"""1)Створіть змінну що містить поточний курс долара
2)Створіть нову змінну що конвертує 1000 гривень в долар
3)Заокругліть отримане значення до двох знаків після коми
4)Виведіть результат за допомогою форматування (“Поточний курс складає: значення”)"""

dollar_exchange_rate = 37.94
hrn = 1000
conversion_to_hrn = hrn / dollar_exchange_rate
print('Поточний курс складає: ' + str(round(conversion_to_hrn, 2)))
