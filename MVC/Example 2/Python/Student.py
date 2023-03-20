from Person import Person

class Student(Person):
    """
    Student class inherit Person
    """
    def __init__(self, last_name: str, first_name: str, age: int, student_id: int, grade_level: int) -> None:
        super().__init__(last_name, first_name, age)
        self._student_id = student_id
        self._grade_level = grade_level

    @property
    def student_id(self) -> int:
        """
        student_id getter
        """
        return self._student_id
    
    @property
    def grade_level(self) -> int:
        """
        grade_level getter
        """
        return self._grade_level
    
    def happy_birthday(self) -> None:
        """
        adds one to age of person and grade level
        """
        self._age += 1
        self._grade_level += 1

    
    def __str__(self) -> str:
        """
        returns ""first_name last_name: age (student_id - grade_level)""
        """
        return f"{self._first_name} {self._last_name}: {self._age} ({self._student_id} - {self._grade_level})"
