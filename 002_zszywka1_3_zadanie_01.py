# Zad 1.
# Na podstawie poznanych poleceń, wskaż dowolne, które mogłyby świadczyć o tym,
# że Python jest wysokopoziomowym językiem programowania.

#Python jest uznawany za wysokopoziomowy język programowania, co oznacza, że oferuje abstrakcję od szczegółów sprzętowych i operacji niskiego poziomu, co
# ułatwia programowanie i zwiększa czytelność kodu. Poniżej wymieniam kilka cech i poleceń w Pythonie, które świadczą o jego wysokopoziomowym charakterze:
#Automatyczne zarządzanie pamięcią: Python posiada mechanizm automatycznego zarządzania pamięcią, co oznacza, że programiści nie muszą ręcznie alokować i
# zwalniać pamięci.

#Dynamiczne typowanie: W Pythonie nie trzeba deklarować typów zmiennych, ponieważ są one dynamicznie przypisywane w trakcie wykonywania programu.

#Bogata biblioteka standardowa: Python dostarcza obszerną bibliotekę standardową, co umożliwia korzystanie z gotowych modułów do różnych zastosowań
# bez potrzeby implementacji od zera.

# Prostota i czytelność składni: Składnia Pythona jest przejrzysta i czytelna, co ułatwia zrozumienie kodu nawet dla osób niebędących doświadczonymi programistami.
# Wysokopoziomowe struktury danych: Python dostarcza gotowe, wysokopoziomowe struktury danych takie jak listy, słowniki czy krotki, co pozwala programistom na efektywne operowanie danymi.

# Obsługa wyjątków: Mechanizm obsługi wyjątków w Pythonie ułatwia radzenie sobie z błędami w trakcie wykonywania programu.
#
# Interpretowany: Python jest językiem interpretowanym, co oznacza, że nie wymaga kompilacji przed uruchomieniem programu, co przyspiesza cykl rozwoju.
#
# Przykładowe polecenie:



# Przykład: Obsługa pliku tekstowego w Pythonie
with open('plik.txt', 'r') as file:
    for line in file:
        print(line)

# W powyższym przykładzie open to funkcja wysokopoziomowa, która umożliwia obsługę plików bez konieczności zajmowania się szczegółami operacji
# na poziomie bitów czy bajtów.