from order import Order

class Broker(object):
    def __init__(self) -> None:
        self._orders = []
    
    @property
    def orders(self) -> None:
        return self._orders
    
    def take_order(self, order: Order) -> None:
        self._orders.append(order)

    def place_orders(self) -> None:

        for order in self.orders:
            order.execute()
        
        self._orders = []