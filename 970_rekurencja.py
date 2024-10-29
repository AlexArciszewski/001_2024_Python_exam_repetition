# Pytanie 41 - napisz funkcję, która dla podanego katalgu wypisze znajdujące się w nim pliki.
# Pamiętaj, że katalog może zawierać podkatalogi, do których funkcja również musi zajrzeć.

# os.listdir - zwraca zawartość danego katalogu
# os.path.join - łączy dwa stringi w ścieżkę czytelną dla danego systemu operacyjnego
# os.path.isdir - sprawdza czy pod nadą ściezką znajduje się katalog

#Funkcja będzie wywoływac samą siebie dla okreslonych przypadków.


import os



def wypisz_zaw_kat(sciezka_do_katalogu):
    for element in os.listdir(sciezka_do_katalogu):     #petla for dla każdego elementu ze znalezionych w katalogu os.listdir zwraca wszystkei elementy pod sciezka_do_katalogu
        sciezka_do_elementu = os.path.join(sciezka_do_katalogu, element)    #scieżka do każdego z tych elementów laczy sciezke do katalogu z elementem
        if os.path.isdir(sciezka_do_elementu):  #jak kolejny lement znaleziony bedzie kolejnym katalogiem jak isdir zwórci true
            wypisz_zaw_kat(sciezka_do_elementu) #wtedy funkcja ponownie wywoła samą siebie podając jako argument sciezke do tego elementu
        else:
            print(sciezka_do_elementu)#jak znaleziony element nie bedzie katalgoiem a plikiem to chcemy wypisać ten plik


wypisz_zaw_kat(r"C:\Users\arcis\PycharmProjects\pythonProject25\970_catalog")       #r-rawstring co pomiędzy "" ma być traktowane jak string bez r to \t to element kodu anie kawałek kodu