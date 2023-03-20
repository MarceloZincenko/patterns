from Person import Person

class Teacher(Person):
    """
    Teacher class inherit Person
    """    
    def __init__(self, last_name: str, first_name: str, age: int, classroom: str, salary: int) -> None:
        super().__init__(last_name, first_name, age)
        self._classroom = classroom
        self._salary = salary
        
    @property
    def classroom(self) -> str:
        """
        classroom getter
        """
        return self._classroom
    
    @property
    def salary(self) -> int:
        """
        salary getter
        """
        return self._salary

    def happy_birthday(self) -> None:
        """
        adds one to the age of Person and 1000 to salary
        """
        self._age += 1
        self._salary += 1000
        
    def __str__(self):
        """
        return "first_name last_name: age (classroom - $salary)"
        """
        return f"{self._first_name} {self._last_name}: {self._age} ({self._classroom} - {self._salary})"