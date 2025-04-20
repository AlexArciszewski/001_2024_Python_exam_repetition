#Utwórz klasę Zwierze jako klasę bazową z metodą daj_glos(). Niech klasy Pies, Kot i
# Krowa dziedziczą po niej i implementują tę metodę po swojemu.


from abc import ABC, abstractmethod
from typing import List


# Klasa abstrakcyjna Zwierze
class Zwierze(ABC):
    """Klasa bazowa dla wszystkich zwierząt. Zawiera metodę abstrakcyjną daj_glos,
       którą muszą zaimplementować klasy dziedziczące."""

    @abstractmethod
    def daj_glos(self) -> str:
        """Abstrakcyjna metoda, którą muszą zaimplementować klasy dziedziczące"""
        pass

#klasa pies dziedziczaca po zwierze
class Pies(Zwierze):
    def daj_glos(self) -> str:
        return "Woof Woof"

# Klasa Kot dziedzicząca po Zwierze
class Kot(Zwierze):
    def daj_glos(self) -> str:
        return "Miau miau"

# Klasa Krowa dziedzicząca po Zwierze
class Krowa(Zwierze):
    def daj_glos(self) -> str:
        return "Muuu"


def listing_zwierzeta(zwierzeta:list[Zwierze]) ->None:
    for zwierze in zwierzeta:
        print(f"{zwierze.__class__.__name__}:{zwierze.daj_glos()}")


def main() -> None:
    zwierzeta: List[Zwierze] = [Pies(), Kot(), Krowa()]
    listing_zwierzeta(zwierzeta)





if __name__ == "__main__":
    main()