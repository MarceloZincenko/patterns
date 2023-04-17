from cold_drink import ColdDrink

class Pepsi(ColdDrink):

    def price(self) -> float:
        return 35.0
    
    def name(self) -> str:
        return "Pepsi"