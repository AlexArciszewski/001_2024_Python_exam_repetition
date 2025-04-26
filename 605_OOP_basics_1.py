# 1. Klasa Samochod
#
# Napisz klasę Samochod z atrybutami: marka, model, rok.
# Dodaj metodę opisz(), która wypisze te dane w jednym zdaniu.

class Car:
    """Class that represents the Car object"""

    def __init__(self, make:str, model:str, year:int) -> None:
        """initialize a new car with make model, year"""
        self.make = make
        self.model = model
        self.year = year

    def describe(self) -> str:
        """method used to describe the car object"""
        return f"The car is: {self.make}, {self.model}, {self.year}"


def main() -> None:
    """Creates car object and demonstrates how it works"""
    ford = Car("Ford", "Taurus SHO", 1995)
    print(ford.describe())


if __name__ == "__main__":
    main()