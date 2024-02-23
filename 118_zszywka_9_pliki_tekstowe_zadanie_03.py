# Zad 3.
# Stwórz plik o nazwie przyklad.txt i umieść w nim następujący tekst:
# Litwo, Ojczyzno moja! ty jesteś jak zdrowie;
# Ile cię trzeba cenić, ten tylko się dowie,
# Kto cię stracił. Dziś piękność twą w całej ozdobie
# Następnie wyświetl z pliku zawartość jego parzystych linii.

#plik:118_zszywka_9_pliki_tekstowe_zadanie_03.txt

with open("118_zszywka_9_pliki_tekstowe_zadanie_03.txt", encoding="utf-8") as file:
    list_of_text_liners = file.readlines()
    print(list_of_text_liners)
    for line in list_of_text_liners:
        if list_of_text_liners.index(line) % 2 == 0:
            print(line)








