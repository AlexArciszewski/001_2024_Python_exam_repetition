# Posortuj podaną listę stringów jako kryterium sortowania przyjmując ostatnią literę każdego stringa.

S = ['Anna', 'Robert', 'Artur', 'Feliks']
list_sorted = sorted(S, key = lambda x:x[-1])
print(list_sorted)