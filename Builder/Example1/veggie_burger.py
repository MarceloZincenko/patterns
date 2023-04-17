from burger import Burger

class VegBurger(Burger):

    def price(self) -> float:
        return 0.25
    
    def name(self) -> str:
        return "Veg Burger"