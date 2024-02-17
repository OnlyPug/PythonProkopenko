"""1.Створіть класс з описом будь-якої тварини. Додайте 1 static method"""


class Animal:
    def __init__(self, name, animal_type, color, paws, country, microchip, home):
        self.name = name
        self.animal_type = animal_type
        self.color = color
        self.paws = int(paws)
        self.country = country
        self.microchip = microchip
        self.home = home

    @staticmethod
    def cheak_animals(paws):
        if paws == 2:
            print('I think we add Homo sapiens')

    @staticmethod
    def number_last_type_animal(microchip, animal_type):
        x = microchip + 1
        print(f'Last {animal_type} have #{microchip} for next we need create #{x}')


tiger = Animal('tiger', 'Mammalia', 'yellow', 4, 'Africa', 213213, 'yes')
elephant = Animal('elephant', 'Chordata', 'gray', 4, 'Africa', 1234548, 'no')
anastasiia = Animal('anastasiia', 'human', '-', 2, 'Ukraine', 'no', 'yes')
tiger.number_last_type_animal(tiger.microchip, tiger.animal_type)
anastasiia.cheak_animals(int(anastasiia.paws))
elephant.cheak_animals(int(elephant.paws))

"""2.Створіть класс з описом будь-якої компанії чи організації. Додайте 1 classmethod"""


class Worker:
    def __init__(self, name, age, gender, profession, salary, work_home):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.profession = profession
        self.salary = int(salary)
        self.work_home = bool(work_home)

    @classmethod
    def olds(cls, name, age, gender):
        if age > 70:
            if gender == 'man':
                x = 'him'
            elif gender == 'woman':
                x = 'her'
            else:
                x = 'there'
            print(f'We have {name} and time to give {x} money and vacation in Paris')
        else:
            print('Young and beautiful')


mike = Worker('Mike', 24, 'man', 'developer', 4000, True)
anna = Worker('Anna', 45, 'woman', 'designer', 3500, True)
jimmy = Worker('Jimmy', 75, 'man', 'developer', 8000, False)
mike.olds(mike.name, mike.age, mike.gender)
anna.olds(anna.name, anna.age, anna.gender)
jimmy.olds(jimmy.name, jimmy.age, jimmy.gender)

"""Якщо ви хочете спитати "Анастасія що це за чіпи, що за Паріж" то краще не треба. Це єдине на що була здатна в мене 
фантазія в цей день=)"""
