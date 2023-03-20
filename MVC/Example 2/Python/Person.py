class Person(object):
    """
    The Person class 
    """    
    def __init__(self, last_name: str, first_name: str, age: int) -> None:
        """
        Person class initialization
        """
        self._last_name = last_name
        self._first_name =  first_name
        self._age =  age
    
    @property
    def last_name(self) -> str:
        """
        last_name getter
        """
        return self._last_name
    
    @property
    def first_name(self) -> str:
        """
        first_name getter
        """
        return self._first_name
    
    @property
    def age(self) -> int:
        """
        age getter
        """
        return self._age

    def happy_birthday(self) -> None:
        """
        adds one to the age of Person instance
        """
        self._age += 1
    
    def __str__(self) -> str:
        """
        returns "first_name last_name: age"
        """
        return f"{self._first_name} {self._last_name}: {self._age}"