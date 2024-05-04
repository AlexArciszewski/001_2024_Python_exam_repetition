class Czlowiek:
    """klasa uogólniony schemat tworzenia obiektów.Jakie konkretnie będą wartości tych właściwości,
    określamy w momencie tworzenia obiektów danych klas pod mainem osoba1, osoba2"""

    # tu niżej jest ciało klasy

    def __init__(self, imie_, plec_, wiek_):#self bo tworzymy metodę init w obebie danej klasy
        """Metoda __init__() to pewnego rodzaju magiczna metoda, która jest zawsze automatycznie uruchamiana przy
        tworzeniu nowych obiektów klasy.konstruuje ona obiekt danej klasy precyzuje jakie wartość pól będzie on
        przechowywał. """
        self.imie = imie_    #●	self w konstruktorze aby tworzyć i skojarzyć określone pole z tworzoną
        self.plec = plec_   #klasą (self.nazwa_pola = wartość) ●	Nadać wartość danemu polu ( self.nazwa_pola = wartość)
        self.wiek = wiek_
#Po drugie, self umożliwia odwoływanie się do pól danej klasy, gdy znajdujemy się wewnątrz niej. Self będziemy
# wykorzystywali za każdym razem, gdy programując funkcjonalność danej klasy,
# będziemy odwoływali się do jej składników (do pól i metod).
def main():

    osoba1 = Czlowiek("Olo", "M", 41)
    osoba2 = Czlowiek("Toma", "M", 40)


    print("imie pierwszej osoby to:", osoba1.imie)
    print("wiek drugiej osoby to:", osoba2.wiek)


if __name__ == "__main__":
    main()