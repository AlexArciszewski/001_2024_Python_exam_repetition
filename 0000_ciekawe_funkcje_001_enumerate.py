# Enumerate zwraca wartość oraz indeks.

# bez enumerate
owoce = ['jabłko', 'banan', 'wiśnia']

for owoc in owoce:
    print(owoc)
# Wynik:
# jabłko
# banan
# wiśnia

# z enumerate
owoce = ['jabłko', 'banan', 'wiśnia']

for indeks, owoc in enumerate(owoce):
    print(f"{indeks}: {owoc}")


# Wynik
# 0: jabłko
# 1: banan
# 2: wiśnia