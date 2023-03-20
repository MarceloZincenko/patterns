from Person import Person
from Student import Student
from Teacher import Teacher
from View import View

import sys

class Controller:
    """
    Controller class interacts with Model and View objects
    """
    @staticmethod
    def main(self) -> None:
        Controller().run()
    
    def __init__(self) -> None:
        self._persons = []
        self._view = View()

    @property
    def persons(self) -> None: 
        return self._persons
    
    @persons.setter
    def persons(self, value: list) -> None:
        self._persons = value
        
    def run(self) -> None:
        while True:
            inp = self._view.show_menu()
            if inp == "add student":
                self.add_student(self._view.add_student())
            elif inp == "add teacher":
                self.add_teacher(self._view.add_teacher())
            elif inp == "list people":
                self._view.list_people(self._persons)
            elif inp == "exit":
                break
            else:
                self._view.show_error("Invalid Input!")

    def add_student(self, inp) -> None:
        splits = inp.split(" ")
        try:
            p = Student(splits[0], splits[1], int(splits[2]), int(splits[3]), int(splits[4]))
            self._persons.append(p)
        except Exception:
            self._view.show_error("Unable to parse input!")
            
    def add_teacher(self, inp) -> None:
        splits = inp.split(" ")
        try:
            p = Teacher(splits[0], splits[1], int(splits[2]), splits[3], int(splits[4]))
            self._persons.append(p)
        except Exception:
            self._view.show_error("Unable to parse input!")

# main guard
if __name__ == "__main__":
    Controller.main(sys.argv)