import csv
import datetime as dt

"""1.Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів. Приймає на вхід будь-яку дату та
час (datetime), а також значення днів(int), і знак(True або False, які репрезентують + і -). Повертає datetime. В цій
задачі скористайтесь datetime.timedelta"""


def sum_subtraction_days(date, days=20, add=True):
    if add:
        return date + dt.timedelta(days=days)
    else:
        return date - dt.timedelta(days=days)


user_date = dt.datetime(2000, 8, 20, 15, 24)
print(sum_subtraction_days(user_date, 8, add=False))

"""2.Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні), вираховуючі різницю між 
наданим значенням і значенням datetime.now(). Приймає дату та час(datetime), повертає три значення: 
datetime.timedelta, datetime.timestamp прожитого життя і строкове значення часу народження в форматі (рік(останні два 
числа, день, місяць, години, хвилини,секунди, am/pm в 12 годинному форматі). Виведіть результат в консоль"""


def how_old_are_you(date):
    date_now = dt.datetime.now()
    date_live = date_now - date
    date_timestamp = date_now.timestamp() - date.timestamp()
    time_format = '%y-%d-%m %I:%M:%S %p'
    date_format = date.strftime(time_format)
    return date_live, date_timestamp, date_format


user_date = dt.datetime(1997, 8, 29, 5, 24)
print(how_old_are_you(user_date))

"""3.Створіть обробку одного будь-якого exception, який не використався як приклад на занятті, додайте обробку решти 
ексепшенів за допомогою Exception. Виведіть результат в консоль"""


def problems_with_file(file):
    try:
        with open(file, 'r') as read_line:
            lines = []
            csv_reader = csv.reader(read_line, delimiter=',')
            for row in csv_reader:
                lines.append(row)
            return lines
    except FileNotFoundError:
        print('Something went wrong with your file')
    except Exception as e:
        print('Something went wrong!!!')
    finally:
        print('Please, re-check name and location of your file')


problems_with_file('not_exsiting_file.txt')
problems_with_file(12354)

'''Трішки мене перше задання занесло не туди куди потрібно, спочатку сама собі задачу ускладнила і вже вона не 
відпускала мене бо дуже хотіла її вирішити. Залишу її тут бо надто багато ізвилен мого мозку загинули тут ахаха'''


def sum_subtraction_days_task3():
    date = input('Введіть дату в такому форматі DD-MM-YYYY: ')
    try:
        user_date = dt.datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Неправильний формат дати.")
        return None
    days_str = input("Введіть кількість днів: ")
    try:
        days = int(days_str)
    except ValueError:
        print("Здається ви ввели не число")
        return None
    sign_str = input("Введіть + або - для додавання чи віднімання: ")
    if sign_str not in ('+', '-'):
        print("Ну + чи - і все!!! Тепер все заново запускай")
    if sign_str == '+':
        return user_date + dt.timedelta(days=days)
    else:
        return user_date - dt.timedelta(days=days)


print(sum_subtraction_days_task3())
