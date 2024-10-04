class Pojazd:

    def __init__(self, ilosc_kol_, kolor_lakieru_):
        self.ilosc_kol = ilosc_kol_
        self.kolor_lakieru = kolor_lakieru_

    def jedz(self):
        print("jade na {} kolach.".format(self.ilosc_kol))


    def metoda_bezargumentowa(self):
        pass

    def metodazjednym_argumentem(self, jeden_argument):
        pass



def main():
    audi = Pojazd(4,"biale")
    audi.jedz()



if __name__ == "__main__":
    main()