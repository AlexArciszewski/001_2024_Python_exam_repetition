# Pytanie 4 - jakiej struktury danych użyłbyś do zamodelowania
# szafki, która ma 3 szuflady, a w każdej z nich 3 przegródki?
# Stwórz taki model i umieść stringa "długopis"
# w środkowej przegródce środkowej szuflady.


szafka = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

szafka[1][1] = 'długopis'

print(szafka)
# wynik [['', '', ''], ['', 'długopis', ''], ['', '', '']]



# Opcja nr2

for i, szuflada in enumerate(szafka):
    print(f"Szuflada {i+1}: {szuflada}")










