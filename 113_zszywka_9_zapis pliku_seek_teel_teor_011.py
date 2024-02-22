# Z pomocą przychodzą funkcje seek() oraz tell():
# ●	Funkcja seek()  - pozwala przemieścić wskaźnik na określoną zawartość pliku (na sprecyzowany numer litery w tekście).
# ●	Funkcja tell() - zwraca nam numer litery z tekstu, informując nas, w którym dokładnie miejscu znajduje się wskaźnik.
# z pliku: 114_zszywka_9-sseek_tell_012.txt

with open("114_zszywka_9-sseek_tell_012.txt", encoding="utf-8") as plik:
    print(plik.readline())  #Yeah, yeah, yeah yeah
    print(plik.readline())      #Don Omar, J Doe, Reek da Villan, Bus a Bus
    print(plik.tell())  #67 znaków poprzedniego wiersza wliczając \n
    print(plik.readline())  #Come on, come on
    plik.seek(67)       #wskaźnik ustawiam na drugą linię znak nr 67
    plik.readline()     #Come on, come on