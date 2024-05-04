# Stwórzmy klasę reprezentującą Pojazd z dowolnymi atrybutami. Następnie utwórzmy instancje tej klasy,
# które będą reprezentowały pojazd osobowy i ciężarowy. W ramach klasy Pojazd utwórz metodę opisującą obiekt,
# na rzecz którego została metoda wywołana.



class Pojazd:
    def __init__(self, ilosc_kol_, marka_, kolor_lakieru_):
        self.ilosc_kol = ilosc_kol_
        self.marka = marka_
        self.kolor_lakieru = kolor_lakieru_

    def opisz_pojazd(self):
        print("jesteś w pojeździe który: ")
        print("ma {} kol, jest marki {} i jest koloru {}".format(self.ilosc_kol, self.marka, self.kolor_lakieru))




def main():
    samochod_osobowy = Pojazd(4, "dodge","niebieski")
    samochod_ciezarowy = Pojazd(10,"MAN", "zolty")

    samochod_osobowy.opisz_pojazd()
    samochod_ciezarowy.opisz_pojazd()




if __name__ == "__main__":
    main()





