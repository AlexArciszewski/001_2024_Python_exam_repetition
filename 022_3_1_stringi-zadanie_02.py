# 2. Program ma (w zadaniach zastosuj nowy sposób formatowania tekstu f-string):
# ●	zapytać ile kotów ma Ala i pobrać od użytkownika tę liczbę
# ●	wyświetlić na ekranie zdanie:  ‘Dzisiaj Ala znalazła jeszcze 3 koty …’ (zamiast kropek napisz od siebie gdzie je znalazła)
# ●	dodać 3 do wprowadzonej wcześniej liczby
# ●	wyświetlić na ekranie zdanie:  ‘Teraz Ala ma już … kotów’ (w miejsce kropek wpisujecie obliczoną przez program prawidłową liczbę)
# ●	wyświetlić to zdanie tak, aby każde słowo było oddzielone przecinkiem
# ●	wyświetlić to zdanie tak, by każde słowo znajdowało się w osobnej linijce
# ●	sprawdzić, czy wszystkie litery są małe i jeśli nie, to zamienić je na małe (wyświetl  wynik tej zmiany)
# ●	zmień pierwszą literę zdania na wielką i wyświetl zdanie po tej modyfikacji
#

def main() -> None:

    cat_number = int(input("how many cas does Ala have? "))
    print("Today Ala got three more cats at Chinese restaurant")
    print(f"Now Ala has {3 + cat_number} cats")

    some_string = f"Now Ala has {3 + cat_number} cats"
    print(some_string.split(' '))

    for word in some_string.split(' '):
        print(word)

    some_string_lowered = some_string.lower()

    for word in some_string_lowered.split(' '):
        print(word)

    print(some_string_lowered.capitalize())


if __name__ == "__main__":
    main()