# Zad 4.
# Jaka jest różnica między kodowaniem UTF-8 a ASCII?
# Jaki byłby rezultat odczytania z pliku polskich liter (np. ą, ę, ć) bez zmiany sposobu formatowania danych?


# Brak możliwości odczytania polskich znakóW.Zapis byłby nieczytelny:




with open("118_zszywka_9_pliki_tekstowe_zadanie_03.txt",'r') as file:
    list_of_text_liners = file.readlines()
    print(list_of_text_liners)
    for line in list_of_text_liners:
        if list_of_text_liners.index(line) % 2 == 0:
            print(line)
# Kto ciÄ™ straciĹ‚. DziĹ› piÄ™knoĹ›Ä‡ twÄ… w caĹ‚ej ozdobie

with open("118_zszywka_9_pliki_tekstowe_zadanie_03.txt", encoding="utf-8") as file:
    list_of_text_liners = file.readlines()
    print(list_of_text_liners)
    for line in list_of_text_liners:
        if list_of_text_liners.index(line) % 2 == 0:
            print(line)

# Kto cię stracił. Dziś piękność twą w całej ozdobie