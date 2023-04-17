from meal import Meal
from veggie_burger import VegBurger
from coke import Coke
from chicken_burger import ChickenBurger
from pepsi import Pepsi

class MealBuilder(object):
    def prepare_veg_meal(self) -> Meal:
        meal = Meal()
        meal.add_item(VegBurger())
        meal.add_item(Coke())
        return meal
    
    def prepare_non_veg_meal(self) -> Meal:
        meal = Meal()
        meal.add_item(ChickenBurger())
        meal.add_item(Pepsi())
        return meal