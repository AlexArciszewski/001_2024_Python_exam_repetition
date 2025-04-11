# Lista z rachunkami
bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]

# Tworzymy pusty słownik, który będzie przechowywał dane o osobach
rachunek = {}

# Iterujemy przez listę rachunków
for osoba, potrawa, cena in bill_items:
    # Sprawdzamy, czy osoba już istnieje w słowniku
    if osoba not in rachunek:
        rachunek[osoba] = {'potrawy': [], 'cena': 0}

    # Dodajemy potrawę do listy i cenę do sumy
    rachunek[osoba]['potrawy'].append(potrawa)
    rachunek[osoba]['cena'] += cena

# Wyświetlamy wynik
print(rachunek)