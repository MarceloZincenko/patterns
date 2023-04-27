class Stock:
    def __init__(self, name: str, quantity: int) -> None:
        self._name = name
        self._quantity = quantity

    @property
    def name(self) -> str:
        return self._name
   
    @property
    def quantity(self) -> int:
        return self._quantity
    
    def buy(self) -> None:
        print(f"Stock [Name: {self._name}, quantity: {self._quantity} bought]")
    
    def sell(self) -> None:
        print(f"Stock [Name: {self._name}, quantity: {self._quantity} sold]")