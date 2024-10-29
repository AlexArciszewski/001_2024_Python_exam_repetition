# Pytanie 47 - do czego w Pythonie służą funkcje dir() i help().

print(dir())

if __name__ == '__main__':  # blok sprawdzający czy uruchamiamy dany plik bezpośrednio
    pass                    # plik uruchomiony bezpośrednio w atrybucie __name__ ma stringa '__main__'
                            # plik uruchomiony po zaimportowaniu do innego pliku w atrybucie __name__ ma swoją własną nazwę
print("\n and \n")
print(__file__)

# dir(obiekt) - wyświetla listę atrybutów danego obiektu
# help(obiekt.metoda) - wyświetla opis danego atrybutu obiektu
# help() - wpisane w linię komend spowoduje otwarcie interaktywnego menu helpa

#python-quit()  -tryb interaktywny
# >>> dir(list)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> help(list.count)
# Help on method_descriptor:
#
# count(self, value, /)
#     Return number of occurrences of value.

