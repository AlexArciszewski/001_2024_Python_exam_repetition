plik = open("107_zszywka_9_zapis pliku_03.txt", "r")
linie_pliku = plik.readlines()
print(linie_pliku)

plik.close()

# ['Ucze sie programowac.\n', 'Ala ma Kota.\n', 'Kot to Filemon.\n']


# plik:
# Ucze sie programowac.
# Ala ma Kota.
# Kot to Filemon.


# zapis do pliku  tekstowego

plik = open("109_zszywka_9_zapis pliku_04.txt","w")
plik.write("Keep rawhide")
plik.close()

# w 109_zszywka_9_zapis pliku_04.txt zapisoano: Keep rawhide

plik = open("110_zszywka_9_zapis pliku_05.txt","w")
linie = ["Keep rawhide\n", "Keep rawhide\n"]        #\n mamy dzięki temu podział na linie.............
plik.writelines(linie)
plik.close()

# Context manager:

linie = ["Keep rawhide\n", "Keep rawhide\n", "Keep rawhide\n", "Keep rawhide\n", "Keep rawhide\n", "Keep rawhide\n"]   
with open("111_zszywka_9_context_manager_06.txt", "w") as plik:
    plik.writelines(linie)
plik.close()
