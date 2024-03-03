from lesson16.dishes.ukrainian_food import UkraineFood
from lesson16.dishes.italian_food import ItalianFood


class OrderFood():

    @staticmethod
    def get_factory(food_type):
        if food_type == 'Ukraine Food':
            return UkraineFood()
        if food_type == 'Italian Food':
            return ItalianFood()


order_food = OrderFood.get_factory('Ukraine Food')
dish = order_food.get_order('salo')
print(dish)
order_food1 = OrderFood.get_factory('Italian Food')
dish1 = order_food1.get_order('sup')
print(dish1)
