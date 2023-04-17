from meal_builder import MealBuilder

meal_builder = MealBuilder()
veg_meal = meal_builder.prepare_veg_meal()
veg_meal.show_items()
print("Total Cost: " + str(veg_meal.get_cost()))

meal_builder = MealBuilder()
non_veg_meal = meal_builder.prepare_non_veg_meal()
non_veg_meal.show_items()
print("Total Cost: " + str(non_veg_meal.get_cost()))

