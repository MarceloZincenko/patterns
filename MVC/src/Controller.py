from Model import Prices
from View import Printer

class Controller:
    """
    This class represents the Controller Class in the MVC desing pattern.
    Iteracts between model and view.

    """
    def __init__(self, model: Prices, view: Printer) -> None:
        self.model = model
        self.view = view

    def display_prices(self) -> None:
        """
        Display the requested prices
        """
        self.view.print_data((self.model.get_prices_given_ticker()))

if __name__ == "__main__":
    controller = Controller(Prices("AL30"), Printer())
    controller.display_prices()