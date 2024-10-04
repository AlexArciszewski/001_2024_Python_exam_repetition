"""
Zadanie 1:

Stwórz klasę Pracownik zawierającą następujące atrybuty:

imie (str) - imię pracownika
nazwisko (str) - nazwisko pracownika
stawka (float) - stawka godzinowa pracownika
Klasa powinna mieć również następujące metody:

pracuj() - wyświetl komunikat "Pracuję"
oblicz_wynagrodzenie(godziny: int) -> float - oblicz wynagrodzenie pracownika na podstawie podanych godzin i
stawki godzinowej
Następnie stwórz klasę Programista dziedziczącą po klasie Pracownik. Klasa Programista powinna zawierać dodatkowy
atrybut jezyki (list of str) - lista znanych przez programistę języków programowania.

Klasa Programista powinna również mieć następujące metody:

napisz_kod() - wyświetl komunikat "Piszę kod"
zwieksz_stawke(procent: float) - zwiększ stawkę godzinową programisty o podany procent
"""


class Employee:
    """Class that represents the Employee object"""

    def __init__(self, name: str, surname: str, wage: float) -> None:
        """initialize a new employee with name, surname and wage"""

        self.name = name
        self.surname = surname
        self.wage = wage

    @staticmethod
    def work() -> str:
        """static method wit no argument that prints string: I am working"""
        print("I am working..")

    def salary(self, working_hours: int) -> float:
        """method used to calculate salary by using working hours and wage and connects
         it to Employee name and surname"""
        salary = self.wage * working_hours
        print(f"Salary of {self.name} {self.surname} is", salary)
        return salary


class Programmer(Employee):
    """Class that represents the programmer object inherited after Employee object"""

    def __init__(self, name: str, surname: str, wage: float, coding_language: list[str]) -> None:
        """initialize a new Programmer with name, surname and wage from inherited
         Employee object and adding coding language"""
        super().__init__(name, surname, wage)
        self.coding_language = coding_language

    def write_code(self) -> None:
        """method to show the string I am writing...."""
        print(f"I am writing some code now...")

    def increase_wage(self, percent_given: float) -> float:
        """method to calculate the increase wage of the Programmer"""
        increase_wage = self.wage + self.wage * percent_given/100
        print(f"The total wage of {self.name} {self.surname} is", increase_wage)
        return increase_wage


def main() -> None:
    """Creates ah Employee object and forces it to work"""

    tom = Employee('Tom', 'Smith', 105.4)
    tom.work()
    tom.salary(10)
    ann = Programmer('Ann', 'Smith', 110, coding_language=['Python'])
    ann.write_code()
    ann.increase_wage(100)


if __name__ == "__main__":
    main()






