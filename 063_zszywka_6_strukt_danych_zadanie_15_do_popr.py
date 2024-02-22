# Zad 15
# Stwórz słownik przechowujący 5 dowolnych nr PESEL jako klucze i do każdego z nich przypisz cechy osób o
# podanym PESELu w formie kolejnego słownika (cechy te to: kolor_oczu, imie, nazwisko, wiek),
# czyli możliwa by była operacja:
# ●	Za pomocą pętli for dodaj do każdej wartości w słowniku (która jest kolejnym słownikiem) nowy klucz (imię_matki) oraz nadaj odpowiednie wartości
# ●	Usuń z słownika osoby, których pesel kończy się na znak ‘1’.
# ●	Wydrukuj zawartość słownika w przyjaznej formie (w komunikacie mają nie wyświetlać się klamry {})


slownik = {
    '12345678901': {'imie': 'Jan', 'nazwisko': 'Kowalski', 'data_urodzenia': '1980-01-01'},
    '23456789012': {'imie': 'Anna', 'nazwisko': 'Nowak', 'data_urodzenia': '1990-02-02'},
    '34567890123': {'imie': 'Piotr', 'nazwisko': 'Wiśniewski', 'data_urodzenia': '1985-03-03'},
}
#usuniecie peseli z nr1
for key in slownik.keys():
    print(key)
pesel_box = []
for key in slownik:
    if key[-1] == "1":
        pesel_box.append(key)
        print(pesel_box)
for pesel in pesel_box:
    if pesel in slownik:
        slownik.pop(pesel)
print(slownik)


for key in slownik:
    print(key)
    print(slownik[key])
for pesel in slownik:
    print(f'pesel: {pesel}')
    for attribute in slownik[pesel]:
        print(f'{slownik[pesel][attribute]}')










