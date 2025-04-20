# Polimorfizm – karmienie zwierząt
# Stwórz listę z obiektami klas Pies, Kot, Krowa i za pomocą jednej pętli wywołuj daj_glos() na każdym z nich. Przećwicz działanie polimorfizmu.


from abc import ABC, abstractmethod
from typing import List


# Klasa abstrakcyjna
class Zwierze(ABC):
    @abstractmethod
    def daj_glos(self) -> None:
        """Każde zwierzę musi umieć dać głos."""
        pass


# Klasy dziedziczące, muszą zaimplementować daj_glos()
class Pies(Zwierze):
    def daj_glos(self) -> None:
        print("Hau hau!")


class Kot(Zwierze):
    def daj_glos(self) -> None:
        print("Miau!")


class Krowa(Zwierze):
    def daj_glos(self) -> None:
        print("Muuuu!")


# Przykład klasy, która NIE implementuje daj_glos()
# Jeśli odkomentujesz to i spróbujesz utworzyć jej obiekt, dostaniesz TypeError:
#
# class Rybka(Zwierze):
#     pass
#
# rybka = Rybka()  # TypeError: Can't instantiate abstract class Rybka with abstract method daj_glos

def main() -> None:
    zwierzeta: List[Zwierze] = [Pies(), Kot(), Krowa()]

    for zwierze in zwierzeta:
        zwierze.daj_glos()


if __name__ == "__main__":
    main()

# from typing import List
#
# class Animal:
#
#     def say_something(self) -> None:
#         raise NotImplementedError("say something method  must me implemented in inherited classes")
#
# class Dog(Animal):
#     def say_something(self) -> None:
#         print("Woof Woof")
#
# class Cat(Animal):
#     def say_something(self) -> None:
#         print("Miau Miau")
#
# # class FishBob(Animal):
# #     pass
#
#
#
#
# def main() -> None:
#     #animals:list[Animal] = [Dog(), Cat(), FishBob()]
#     animals: list[Animal] = [Dog(), Cat()]
#     for animal in animals:
#         animal.say_something()

