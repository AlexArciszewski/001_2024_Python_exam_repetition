# Pytanie 28 - jaki błąd popełniono w poniższym kodzie?
# Co zrobić aby go uniknąć?
# Stworz moduł kserokopiarka zawierający funkcję, która podany string wydrukuje dwa razy
# Użyj tej funkcji w kodzie poniżej

# from drukarka import wydrukuj_imie
#
# def wydrukuj_imie(imie):
#     print(imie)


# # Kod poprawiony
# from drukarka import wydrukuj_imie as wydrukuj_imie_z_drukarki
# # z modułu drukarka zaimportuj funkcję wydrukuj_imię i nadaj jej alias wydrukuj_mnie_z_drukarki
# from kserokopiarka import zrob_ksero
# # z modułu kserokopiarka zaimportuj funkcję zrob_ksero
#
# def wydrukuj_imie(imie):
#     print(imie)
#
# wydrukuj_imie("Marta")
# wydrukuj_imie_z_drukarki("Marta")
# zrob_ksero("Witaj świecie!")


print("A")
import drukarka_953


drukarka_953.print_name("ADA")


print("B")
import importlib

# Zastąp '953_drukarka' nazwą swojego modułu
drukarka2 = importlib.import_module('953_drukarka2')

# Teraz możesz używać funkcji lub klas z modułu
drukarka2.print_name2("Janek")


print("C")

from drukarka_953 import print_name as func

func("Cezary")



