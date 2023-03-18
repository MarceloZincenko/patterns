import csv

class Prices(object):
    """
    This class represents the Model Class in the MVC desing pattern.
    The model will have all the functions related to fetching prices from a csv file.
    """

    def __init__(self, ticker: str = None) -> None:
        assert isinstance(ticker, str),"ticker must be a string"  
        self._ticker = ticker #private variable
    
    @property
    def ticker(self) -> str:
        return self._ticker

    @ticker.setter
    def ticker(self, ticker: str) -> None:
        assert isinstance(ticker, str),"ticker must be a string"  
        self._ticker = ticker

    def print_ticker(self) -> None:
        print(f"The ticker is: {self.ticker}")

    @classmethod
    def get_all_prices(self,csvFilePath: str = "./data/prices.csv") -> list:
        """ 
        Get all prices from the csv and return a dictionary
        """
        result = []
        #read csv file
        with open(csvFilePath, 'r', encoding='utf-8') as csvf: 
            csvReader = csv.DictReader(csvf) 

            #convert each csv row into python dict
            for row in csvReader: 
                #add this python dict to json array
                result.append(row)
        
        return result

    def get_prices_given_ticker(self) -> list:
        """
        Get all prices given a ticker
        """
        result = []
        list_of_prices = self.get_all_prices()
        for item in list_of_prices:
            if item["ticker"] == self._ticker:
                result.append(item)
    
        return result
    
if __name__ == "__main__":
    # example = Prices(123)
    print(Prices.get_all_prices())
    example = Prices("AL30")
    print(example.get_prices_given_ticker())