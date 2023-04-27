from stock import Stock
from broker import Broker
from buy_stock import BuyStock
from sell_stock import SellStock

x = Stock("X",1000)
appl = Stock("APPL",100)
msft = Stock("MSFT",10)

sell_appl = SellStock(appl)
sell_msft = SellStock(msft)
buy_x = BuyStock(x)

broker = Broker()
broker.take_order(sell_appl)
broker.take_order(sell_msft)
broker.take_order(buy_x)

broker.place_orders()
