# 10. Licznik instancji
# Dodaj do klasy Pracownik zmienną klasową, która będzie zliczać ile obiektów Pracownik zostało
# utworzonych. Wyświetl ją metodą klasową.

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

Dodajemy __Str__ w klasie Employee
"""


class Employee:
    """Class that represents the Employee object"""

    instance_count: int = 0  # Zmienna klasowa zliczająca instancje

    def __init__(self, name: str, surname: str, wage: float) -> None:
        """initialize a new employee with name, surname and wage"""
        self.name = name
        self.surname = surname
        self.wage = wage
        Employee.instance_count += 1  # Zwiększamy licznik za każdym razem, gdy tworzony jest nowy obiekt

    # def __str__(self) -> str:
    #     return (f"My name is {self.name} {self.surname} and my wage is {self.wage}."
    #             f"You can see this thx to this awesome __str__ method It replaces the tom object"
    #             f"when you try to print him in main.")


    def __repr__(self) -> str:
        return (f"My name is {self.name} {self.surname} {self.wage}. Now you can se only this awesome__repr__ method"
                f"because it's goes above __str__ method if you unmark str method the __str__ method appears you can "
                f"still use repr method by printing tom with repr")


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

    @classmethod
    def creating_new_guy(cls, name: str, surname: str, wage: float) -> "Employee":
        """Class method to create a new employee"""
        return cls(name, surname, wage)


    #Dodajemy metodę klasową get_instance_count(), która zwróci liczbę instancji klasy.
    @classmethod
    def get_instance_count(cls) -> int:
        """Class method to get the current instance count"""
        return cls.instance_count


class Programmer(Employee):
    """Class that represents the programmer object inherited after Employee object"""

    def __init__(self, name: str, surname: str, wage: float, coding_language: list[str]) -> None:
        """initialize a new Programmer with name, surname and wage from inherited
         Employee object and adding coding language"""
        super().__init__(name, surname, wage)
        self.coding_language = coding_language

    def write_code(self) -> None:
        """method to show the string I am writing...."""
        print(f"My name is {self.name} I am writing some code now...")

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
    print(ann.write_code())
    ann.increase_wage(100)
    print(tom)
    # print(repr(tom))
    jake = Employee.creating_new_guy('Jake', 'Smith', 105.4)
    print(jake)
    jake.work()

    # Sprawdzamy licznik instancji
    print(f"Total number of Employee instances: {Employee.get_instance_count()}")


if __name__ == "__main__":
    main()


# Zmiany w kodzie:
#
#     Dodajemy zmienną klasową instance_count, która będzie zliczać liczbę utworzonych instancji klasy Employee.
#
#     W konstruktorze klasy Employee zwiększamy wartość tej zmiennej przy każdym tworzeniu nowej instancji.
#
#     Dodajemy metodę klasową get_instance_count(), która zwróci liczbę instancji klasy.
#
#     Sprawdzamy licznik instancji
#     print(f"Total number of Employee instances: {Employee.get_instance_count()}")



