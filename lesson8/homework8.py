import re

"""1. Напишіть програму яка перевіряє чи стрічка містить лише великі і малі літери, числа та нижнє підкреслення."""


def cheak_letters_and_numbers(user):
    patern = re.compile('\w+')
    result = patern.findall(user)
    print(result)


cheak_letters_and_numbers("GSDGSDgw534gf№g_")

"""
2)Напишіть програму, що видаляє область дужок в стрічці
["example (.com)", "github (.com)", "stackoverflow (.com)"] ->
example
github
stackoverflow"""

list_with_world = ["example (.com)", "github (.com)", "stackoverflow (.com)"]


def delete_com(table):
    pattern = re.compile('\(.com\)$')
    for i in table:
        result = pattern.sub('', i)
        print(result.rstrip())


delete_com(list_with_world)

'''Напишіть програму, що. вставляє пробіл перед великою літерою'''


def spase_for_letters(text):
    pattern = re.compile(r'([a-z])([A-Z])')
    result = pattern.sub(r'\1 \2', text)
    print(result)


spase_for_letters('AdsfVfsdfsdfFvcvsf')
