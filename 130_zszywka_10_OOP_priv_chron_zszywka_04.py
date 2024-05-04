# Stwórzmy klasę reprezentującą Pojazd z dowolnymi atrybutami. Następnie utwórzmy instancje tej klasy,
# które będą reprezentowały pojazd osobowy i ciężarowy. W ramach klasy Pojazd utwórz metodę opisującą obiekt,
# na rzecz którego została metoda wywołana.

#Pola prywatne i chronione:


class Pojazd:
    def __init__(self, ilosc_kol_, marka_, kolor_lakieru_):
        self.__ilosc_kol = ilosc_kol_ #pole prywatne
        self._marka = marka_            #pole chronione
        self.kolor_lakieru = kolor_lakieru_ #pole publiczne

#getter pola prywatnego ilosc kol
    def get_ilosc_kol(self):
        return self.__ilosc_kol

#setter pola __ilosc_kol
    def set_ilosc_kol(self, ilosc_kol_):
        self.__ilosc_kol = ilosc_kol_

#tonie zadziała
    # def opisz_pojazd(self):
    #     print("jesteś w pojeździe który: ")
    #     print("ma {} kol, jest marki {} i jest koloru {}".format(self.ilosc_kol, self.marka, self.kolor_lakieru))

def main():
    samochod_osobowy = Pojazd(4, "dodge","niebieski")
    samochod_ciezarowy = Pojazd(10,"MAN", "zolty")


    # print(samochod_osobowy.__ilosc_kol) #poleprywatne nie może byc poza klasa nie mozna sie odwolac do niego poza klasa
    print(samochod_osobowy.get_ilosc_kol())
    samochod_osobowy.set_ilosc_kol(18) #ok ustawiłem setterem liczbe kół na 18

    print(samochod_osobowy.get_ilosc_kol()) #printem gettera wyświetlam liczbę kół czyli ustawiona setterem 18 :)
    #to nie działa
    # samochod_osobowy.opisz_pojazd()
    # samochod_ciezarowy.opisz_pojazd()




if __name__ == "__main__":
    main()

# Tak jak powiedzieliśmy - odwołanie do pól prywatnych poza klasą jest niemożliwe.
# Aby móc nimi manipulować konieczne jest utworzenie getter’a i setter’a dla danego pola.
# czym się różni pole prywatne (private) od chronionego (protected)?
# Na pewno tym, że do prywatnego nie mamy dostępu poza klasą, ale czy czymś jeszcze?
# Prywatne atrybuty nie są jeszcze bowiem dziedziczone.



