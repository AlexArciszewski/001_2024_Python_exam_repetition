# Stwórz klasę Kot, a w niej konstruktor, który będzie pobierał imie i kolor.
# Do zmiennej k przypisz obiekt klasy Kot, daj mu na imię "Mruczek" i dowolny kolor.
# Dalsza część kodu zajmie się wypisaniem imienia obiektu przechowywanego pod zmienną k.




class Cat:
    """Class of the cat object """

    def __init__(self, name: str, color: str) -> None:
        self.name = name
        self.color = color


k = Cat("Mruczek", "black")
print(k.name)
