from lesson16.dishes import DishFactory, Pizza, Pasta, Sup


class ItalianFood(DishFactory):
    _dish_type = 'Italian Food'

    def __init__(self):
        self.name = 'Italian'
        self._type = ['pasta', 'pizza', 'sup']

    @property
    def type(self):
        return self._type

    def get_order(self, name):
        if name == 'pasta':
            return Pasta()
        elif name == 'pizza':
            return Pizza()
        elif name == 'sup':
            return Sup()
        else:
            print('Unfortunately we don`t have this type of dish')
