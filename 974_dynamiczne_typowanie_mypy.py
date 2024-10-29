# Pytanie 45 - co to znaczy, że Python językiem dynamicznie typowanym?

a = 5            # tu zmienna a jest typu int
print(type(a))
a = "pięć"       # tu zmienna a jest typu str
print(type(a))
a = [1,2,3]      # a tu zmienna a jest typu List
print(type(a))

from typing import List   # aby używać type hints należy zainstalować i zaimportować bibliotekę typing

def przeliteruj(word: str) -> List[str]:  # definicja funkcji, która pobiera argument typu string i zwraca listę stringów
    return 5

print(przeliteruj(1))

# mypy - program, który pozwala analizować kod Pythona pod kątem poprawności przy założeniu statycznego typowania
# aby go użyć należy w konsoli wpisać: mypy nazwa_pliku_ktory_chcemy_przeanalizoac.py
from typing import List

def show_letters(word_given: str) -> List[str]:
    """Function that returns letter of the word_given"""

    return list(word_given)

print(show_letters("Alamakota"))

# (venv) PS C:\Users\arcis\PycharmProjects\pythonProject25> mypy 974_dynamiczne_typowanie_mypy.py
# 974_dynamiczne_typowanie_mypy.py:5: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
# 974_dynamiczne_typowanie_mypy.py:7: error: Incompatible types in assignment (expression has type "list[int]", variable has type "int")  [assignment]
# 974_dynamiczne_typowanie_mypy.py:13: error: Incompatible return value type (got "int", expected "list[str]")  [return-value]
# 974_dynamiczne_typowanie_mypy.py:15: error: Argument 1 to "przeliteruj" has incompatible type "int"; expected "str"  [arg-type]
# Found 4 errors in 1 file (checked 1 source file)
