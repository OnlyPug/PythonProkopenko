from abc import ABC, abstractmethod

"""Опишіть об'єкти мистецтва для музею. скористайтесь всіма 5 принципами: абстракція, наслідування, поліморфізм,
скриття, інкапсуляція. додайте property, setter. Створіть хоча-б по одному інстансу кожного класу і викличте методи"""


class Museum(ABC):
    def __init__(self, name, type_obj, old):
        self.name = name
        self.type_obj = type_obj
        self.old = old

    @abstractmethod  # абстракція
    def short_description_obg(self):
        pass


class Dishes(Museum):  # наслідування
    def __init__(self, name, old):
        super().__init__(name, 'dishes', old)

    def short_description_obg(self):  # абстракція
        print(f'The {self.name}, a dish type, was used in the {self.type_obj}')

    def introduction(self):
        print('We have Dishes')


class Weapons(Museum):  # наслідування
    def __init__(self, name, old, use_in_war: bool, price):
        super().__init__(name, 'weapon', old)
        self.use_in_war = bool(use_in_war)
        self._price = int(price)  # скриття
        self.__shoots = 'in target'

    @property
    def shoots(self):
        return self.__shoots

    @shoots.setter
    def shoots(self, shoots):
        self.__shoots = shoots


    def short_description_obg(self):  # абстракція
        if self.use_in_war:
            print(f'The {self.name} is a type of weapon that was created in the {self.old} year. This weapon has been '
                  f'extensively used in various wars. ')
        else:
            print(f'The {self.name} is a type of weapon that was created in the {self.old} year.')

    def _create_auсtion(self):
        print(f'The cratet auction for {self.name}')

    def _money(self):
        money = self._price * 100
        print(f'The price for {self.name} is: {money}')

    def __finish_auсtion(self):
        print(f'SOLD')

    def iligal_auction(self):       # інкапсуляція
        self._create_auсtion()
        self._money()
        self.__finish_auсtion()

    def introduction(self):
        print('We have Weapons')


class Tank(Weapons):
    def __init__(self, name, old, use_in_war, speed, price):
        super().__init__(name, 'car', old, use_in_war)
        self.speed = int(speed)
        self.price = int(price)

    def short_description_obg(self):  # абстракція
        if self.use_in_war:
            print(f'The {self.name} is a type of car that was created in the {self.old} year. This tank has been '
                  f'extensively used in various wars. Spead of this tank is {self.speed}.')
        else:
            print(f'The {self.name} is a type of weapon that was created in the {self.old} year. '
                  f'Spead of this car is {self.speed}.')

    def auction(self):
        self.iligal_auction()

    def introduction(self):
        print('We have Tank')


# Інстанс кожного класу
cup = Dishes('cup', 806)
garand = Weapons('Garand', 1929, True, 1600)
car = Tank('T-84', 1975, True, 65, 4500000)

# абстракція
garand.short_description_obg()
cup.short_description_obg()
car.short_description_obg()

# інкапсуляція
garand.iligal_auction()
car.auction()

# поліморфізм
cup.introduction()
garand.introduction()
car.introduction()

#property and setter
print(garand.shoots)
garand.shoots = 'miss target'
print(garand.shoots)
