from abc import ABC, abstractmethod


class DishFactory(ABC):
    _dish_type = ''

    @abstractmethod
    def get_order(self, name):
        pass
