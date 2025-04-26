from typing import List

class Employee:
    """ Representation of Employee object."""


    def __init__(self, name: str, last_name: str, wage:float) -> None:
        """Initialize a new employee with name, last_name and wage."""
        self.name: str = name
        self.last_name: str = last_name
        self.wage: float = wage





def main() -> None:
    ala: Employee = Employee('Ala', 'Makota', 150.5)







if __name__ == "__main__":
    main()
