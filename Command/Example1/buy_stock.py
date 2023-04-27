from stock import Stock
from order import Order

class BuyStock(Order):
    
    def __init__(self, stock: Stock) -> None:
        self._stock = stock

    @property
    def stock(self) -> None:
        return self._stock
    
    @stock.setter
    def buy_stock(self, stock: Stock) -> None:
        self._stock = stock
        
    def execute(self) -> None:
        self._stock.buy()