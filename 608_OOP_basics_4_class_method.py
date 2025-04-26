# 4. Klasa Pracownik i @classmethod
# Zrób klasę Pracownik, która przechowuje imię, nazwisko i pensję. Dodaj metodę klasową
# z_stringa("Jan,Kowalski,5000"), która utworzy pracownika z jednego stringa.




class Worker:
    """class that represents the worker object"""

    def __init__(self, name:str,last_name: str, wage_usd:float) -> None:
        """initialize a new employee with name, surname and wage"""
        self.name = name
        self.last_name = last_name
        self.wage_usd = wage_usd

    def __str__(self)->str:
        """returns  name, surname and wage after print(john)"""
        return f"{self.name}, {self.last_name}, {self.wage_usd}"

    def show_worker(self)->str:
        """returns  name, surname and wage after print(john.show_worker)"""
        return f"{self.name}, {self.last_name}, {self.wage_usd}"

    @classmethod
    def from_string(cls, name:str, last_name:str, wage_usd:float):

        return cls(name, last_name, wage_usd)


def main() -> None:
    """Creates an Employee object and forces it to work"""
    john = Worker("John", "Doe", 100.5)
    print(john)
    print(john.show_worker())
    jan = Worker.from_string("Jan","Kowalski", 50.5)
    print(jan)

if __name__ == "__main__":
    main()