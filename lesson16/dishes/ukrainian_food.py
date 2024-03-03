from lesson16.dishes import DishFactory, Borch, Salo, Varenik


class UkraineFood(DishFactory):
    _dish_type = 'Ukraine Food'

    def __init__(self):
        self.name = 'Ukraine'
        self._type = ['borch', 'salo', 'varenik']

    @property
    def type(self):
        return self._type

    def get_order(self, name):
        if name == 'borch':
            return Borch()
        elif name == 'salo':
            return Salo()
        elif name == 'varenik':
            return Varenik()
        else:
            print('Unfortunately we don`t have this type of dish, but Slava Ukraine')