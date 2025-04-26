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

class EV(Car):


    def __init__(self, make:str, model:str, year:int, range_km:int) -> None:
        """initialize a new EV obj with make, model and range from inherited
                 car  object and adding range"""
        super().__init__(make,model,year)
        self.range_km = range_km

    def describe(self) -> str:
        """method used to describe the electric car object"""
        return f"The car is: {self.make}, {self.model}, {self.year}, {self.range_km}"





def main() -> None:
    """Creates car object and demonstrates how it works"""
    ford = Car("Ford", "Taurus SHO", 1995)
    print(ford.describe())
    tesla_s = EV("Tesla", "S Model", 2025, 300)
    print(tesla_s.describe())

if __name__ == "__main__":
    main()