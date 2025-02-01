plik = open("plik.txt","r")     #do odczytu ściezka względna dobry jak plik znajduje się w meijscu pliku wykonującego program lub plik uruchamiany z poziomu IDLEco plik skryptowy z rozszerzeniem 414_pandas_zmiana_typu_danych_kol_astype_to_numeric.py
plik2 = open("C:\Users\Admin\plik2.txt","w") #do zapisu scieżka bezwzględna

# Po pracy z plikiem zamykamy do niego dostęp.
# Istnieje bowiem określona maksymalna ilość plików, które możesz otworzyć. 
# Jeżeli przekroczysz tę ilość, może nastąpić crash programu.
# używamy metody close()
plik.close()
plik2.close()
# ASCII i UTF-8. 
#  pliki polskie dekodujemy po UTF-8
plik = open("plik.txt", "r") #dekodowanie ASCII
plik_utf8 =  open("polski_plik.txt", "r", encoding="utf-8") #dekodowanie UTF-8

#przykład
# otwieranie pliku w formacie binarnym b przed drugim parametrem funkcji i zapis listy do pliku....

plik = open("plik_binarny.bin", "wb")

liczby = [1,2,4,5,7]

bin_lista = bytearray(liczby) #bytearray() zwraca postać bajtową danego obiektu tablicowego


plik.write(bin_lista)
plik.close()
#zapis do pliku plik_binarny.bin



rlist = [1, 2, 3, 4, 5]
arr = bytearray(rlist)
print(arr)
# bytearray(b'\x01\x02\x03\x04\x05')


# czytanie pliku tekstowego
# ●	read(ilość_znaków) - czyta określoną ilość znaków z pliku, zaczynając od miejsca, w którym się w danym momencie znajdujemy 
# ●	readline() - czyta litery z pliku zaczynając od pozycji, w której się znajdujemy aż do napotkania znaku końca linii, czyli ‘\n’ (newline)
# ●	readlines() - czyta całą zawartość pliku







