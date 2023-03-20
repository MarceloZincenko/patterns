class Printer(object):
    """
    This class represents the View Class in the MVC desing pattern.
    It only will print model data.
    """
    def __init__(self) -> None:
        pass

    @classmethod
    def print_data(self, data: list) -> None:
        """
        Print list data
        """
        for item in data:
            print(f"The prices are {item}")

if __name__ == "__main__":
    Printer.print_data([1,2,3,4])