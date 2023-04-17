from burger import Burger

class ChickenBurger(Burger):

    def price(self) -> float:
        return 25.0
    
    def name(self) -> str:
        return "Chicken Burger"