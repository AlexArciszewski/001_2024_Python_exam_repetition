# 4. Klasa Pracownik i @classmethod
# Zrób klasę Pracownik, która przechowuje imię, nazwisko i pensję. Dodaj metodę klasową
# z_stringa("Jan,Kowalski,5000"), która utworzy pracownika z jednego stringa.
#Dodaj do klasy Pracownik metody __str__() i __repr__(), które będą zwracały czytelny
#opis pracownika (do printa i do debugowania).



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
    def from_string(cls, data:str):
        name, last_name, wage = data.split(",")
        return cls(name, last_name, float(wage.strip()))

    @staticmethod
    def is_pesel_correct(pesel:str) -> bool:
        if pesel.isdigit() and len(pesel) == 11:
            return True
        else:
            return False

    def __str__(self) -> str:
        #return string  when alling worker class obj
        return f"The new worker is {self.name}"


    def __repr__(self) -> str:
        # return string  when alling worker class obj
        return f"The new worker is {self.name}, {self.last_name}"


def main() -> None:
    """Creates an Employee object and forces it to work"""
    john = Worker("John", "Doe", 100.5)
    print(john) # tu tez nastepuje zamiana
    print(john.show_worker())
    jan = Worker.from_string("Jan, Kowalski, 50.5")
    print(jan) #str i repr go zasapily
    print(jan.is_pesel_correct("89111570821"))
    print(str(john))
    print(repr(john))


if __name__ == "__main__":
    main()