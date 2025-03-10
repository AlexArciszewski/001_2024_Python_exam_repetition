# Pytanie 35 - do czego w Pythonie służy __init__ ? Czym różni się od __init__.py ?
# Napisz fragment kodu wykorzystujący __init__.
#innit.py musi byc zawarty w folderze aby byl to apkiet a tu mamy konstruktor
class Pies:
    """Tworzenie klasy pies """

    def __init__(self, imie: str, rasa: str) -> None:      # konstruktor klasy pobierający imię i rasę
        self.imie = imie                                    # tworzenie pól klasy i przypisywanie do nich wartości podanych w konstruktorze
        self.rasa = rasa                                    # tworzenie pól klasy i przypisywanie do nich wartości podanych w konstruktorze

maly_pies = Pies("Pikuś", 'ratlerek')    # tworzenie obiektu klasy Pies, z parametrami konstruktora "Pikuś" i 'ratlerek'
duzy_pies = Pies("Killer", 'doberman')   # tworzenie obiektu klasy Pies, z parametrami konstruktora "Killer" i 'doberman'

print(maly_pies.imie, maly_pies.rasa)    # wydrukowanie atrybutów obiektów
print(duzy_pies.imie, duzy_pies.rasa)    # wydrukowanie atrybutów obiektów