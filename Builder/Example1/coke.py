from cold_drink import ColdDrink

class Coke(ColdDrink):

    def price(self) -> float:
        return 24.0
    
    def name(self) -> str:
        return "Coke"