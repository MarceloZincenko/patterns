import sys

class View:
    """
    View class handles the user view
    """ 
    def show_menu(self) -> str:
        """
        User menu
        """
        print("Please enter one of the following options:")
        print("  add student")
        print("  add teacher")
        print("  list people")
        print("  exit")
        try:
            inp = sys.stdin.readline()
            return inp.strip()
        except Exception:
            return ""
        
    def add_student(self) -> str:
        """
        Add student 
        """
        print("Please enter the following items for the new student, all on the same line")
        print("LastName FirstName Age StudentID GradeLevel")
        try:
            inp = sys.stdin.readline()
            return inp.strip()
        except Exception:
            return ""
        
    def add_teacher(self) -> str:
        """
        Add teacher 
        """
        print("Please enter the following items for the new teacher, all on the same line")
        print("LastName FirstName Age Classroom Salary")
        try:
            inp = sys.stdin.readline()
            return inp.strip()
        except Exception:
            return ""
        
    def list_people(self, persons: list) -> None:
        """
        List all the peoples
        """
        i = 1
        for p in persons:
            print(f"{i}) {p}")
            i += 1
            
            
    def show_error(self, error) -> None:
        """
        Display errors
        """
        print(f"Error: {error}")