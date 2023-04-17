from item import Item

class Meal(object):
    def __init__(self) -> None:
        self.items = []
    
    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def get_cost(self) -> float:

        res = 0
        for item in self.items:
            res += item.price()

        return res
    
    def show_items(self) -> None:
   
      for item in self.items:
         print(f"Item : {item.name()} ,Packing: {item.packing().pack()} ,Price: {item.price()}")
      
