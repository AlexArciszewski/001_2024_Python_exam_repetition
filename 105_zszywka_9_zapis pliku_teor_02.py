# “Nauczę się programować wraz z Devs-Mentoring”
# Otwieranie tegot ekstu w programie nr 104_zszywka_9_zapis pliku_01.txt




# Program do prawidłowego działania potrzebuje pętli while (linia 8). Sprawdza ona, czy znak przechowuje jakąś wartość (czy nie doszliśmy do końca pliku). Jeżeli nie, to wyświetlamy znak i następuje automatyczne przejście do następnego. To, ile znaków chcemy przy operacji pobierania danych odczytać, determinuje argument przekazywany do funkcji read() - w naszym przypadku ‘1’ powoduje pobranie pojedynczego następnego znaku.


file = open("104_zszywka_9_zapis pliku_01.txt","r")
# czytamy pierwszy znak
print("pierwszy znak")
element = file.read(1)
print("first elemenet: ", element)   
#pozostałe znaki

print("kolejne znaki")
element = file.read(1)
element = file.read(1)
element = file.read(1)
element = file.read(1)



print("wyswietlenie z uzyciem petli")
while element:
    print(element)
    element = file.read(1) #czyta pozostałem znaki w petli
    
    
# Czytanie linijka po linijce – readline() oraz wszystkich linii od razu 
# - readlines().


# Funkcja readlines() jest przydatna w momencie, gdy chcemy odczytać cały plik za jednym zamachem i pobrane linie tekstu umieścić, np. w liście. 

plik = open("106_zszywka_9_zapis pliku_02.txt", "r")
linie_pliku = plik.readlines()

print(linie_pliku)

plik.close()

# ['Ucze sie programowac.\n', 'Ala ma Kota.\n', 'Kot to Filemon.\n']


# Zapis pliku
# ●	write(tekst)  - zapisuje podany tekst w argumencie w danym pliku
# ●	writelines(lista) - zapisuje tekst z listy w danym pliku

plik = open("C:\Dane\2_programowanie python\1_Repo_Python_for_exam\001_My_Python_programs_2019_2024_repo_01\107_zszywka_9_zapis pliku_02.txt", "w")
plik.write("Do or die")
plik.close()


plik = open("108_zszywka_9_zapis pliku_02.txt", "w")
plik.write("Do or die")
plik.close()




