""""Задача 1.Написати програму, для введення та перегляду нотаток. Програма пропонує користувачу вводити ключові слова,
та опрацьовує їх.
Перелік ключових слів:

add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
earliest - виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої
latest - виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
Exit - вихід"""


user_input = []


while True:
    program = input('What do you want to do? ').lower()

    if program == 'add':
        x = input("Input note: ")
        user_input.append(x)
        print(f'You add "{x}" in our list\n\n')
    elif program == 'earliest':
        print('From the earliest to the latest:')
        for note in user_input:
            print(note)
    elif program == 'latest':
        print('From the latest to the earliest:')
        for note in reversed(user_input):
            print(note)
    elif program == 'longest':
        print('From the longest to the shortest:')
        for note in sorted(user_input, key=len, reverse=True):
            print(note)
    elif program == 'shortest':
        print('From the shortest to the longest:')
        for note in sorted(user_input, key=len, reverse=False):
            print(note)
    elif program == 'exit':
        break
    else:
        print('Unknown command. Please try again this is command what you can use'
              '\n-add\n-earliest\n-latest\n-longest\n-shortest')