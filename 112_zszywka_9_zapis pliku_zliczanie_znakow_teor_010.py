# Napisz funkcję, która zliczy wszystkie wyrazy w pliku. 

# Podpowiedź:
# W celu podzielenia odczytanej linii na pojedyncze wyrazy, skorzystaj z funkcji split() (patrz Szkolenie 3.1).
# Tworze plik:111_zszywka_9_context_manager_06.txt
#w pliku:
# Keep rawhide
# Keep rawhide
# Keep rawhide
# Keep rawhide
# Keep rawhide
# Keep rawhide


def zlicz_slowa():
    ile_slow = 0
    with open("111_zszywka_9_context_manager_06.txt", "r") as plik:
        for linia in plik.readlines():      #ile linii w pliku dla lini w liniach 
            slowa = linia.split()            #slowa to linie split()
            ile_slow = ile_slow + len(slowa) #l slow to 0+ len od listy slowa
    
    return ile_slow


def main():
    print(f"mamy {zlicz_slowa()}")
    
if __name__ =="__main__":
    main()















