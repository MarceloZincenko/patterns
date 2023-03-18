from Model import Prices
from View import Printer
from Controller import Controller

class App(object):
    """
    App class: MVC is implemented
    """

    def __init__(self) -> None:
        pass

    def run(self) -> None:
        """
        Run the MVC App
        """
        while True:
            ticker = input("Enter ticker, or 'quit': ")
            if ticker == 'quit':
                break
            # create a model
            model = Prices(ticker)

            # create a view and place it on the root window
            view = Printer()

            # create a controller
            controller = Controller(model, view)

            # set the controller to view
            controller.display_prices()

if __name__ == '__main__':
    app = App()
    app.run()