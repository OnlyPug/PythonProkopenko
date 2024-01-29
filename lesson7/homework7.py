"""Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда. """

a = [4, 66, 44423, 3453.5, 34534.5, 2, 345, 'A', 'B', 5345, 'hard func lambda']
b = [234, 'Anastasiia', 'WOW', 66, 44423, 'hard func lambda', 345345, ]

x = list(filter(lambda x: x in a, b))

print(x)

"""Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда"""

hate_lamdba = lambda x: x.replace('.', '', 1).isdigit() or x.startswith('-') and x.replace('-', '', 1).isdigit() and x.count('.') == 1

result = hate_lamdba(input('Please input numbers:  '))

if result:
    print('In your string I see numbers')
else:
    print("-______- In your string I don't see numbers")

"""Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда."""

cool_lists = [['banana', 'cake', 'short'], ['ar', 'br', 'yo'], ['import']]

max_list = max(cool_lists, key=lambda x: len(x))
min_list = min(cool_lists, key=lambda x: len(x))

print(max_list)
print(min_list)

# Скажу чесно, якби не інернет то не було б цього тут рішення. І то мені здається що все одно це якось 'не правильно"
