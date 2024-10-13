#  Pytanie 16 - wypisz podaną listę imion przed każdym dodając kolejny numer.
# # Zacznij numerowanie od 1.
#
# imiona = ['Adam', 'Stanisław', 'Maria', 'Zofia', 'Mikołaj']

names = ['Adam', 'Stanisław', 'Maria', 'Zofia', 'Mikołaj']


for number, name in enumerate(names):
    print(number, name)
# 0 Adam
# 1 Stanisław
# 2 Maria
# 3 Zofia
# 4 Mikołaj
# lista krotek
print(list(enumerate(names)))
# [(0, 'Adam'), (1, 'Stanisław'), (2, 'Maria'), (3, 'Zofia'), (4, 'Mikołaj')]
print(list(enumerate(names, start=1)))
# [(1, 'Adam'), (2, 'Stanisław'), (3, 'Maria'), (4, 'Zofia'), (5, 'Mikołaj')]


# Opcja nr2

def enumerate(names, start=1):
    n = start
    for elem in names:
        yield n, elem
        n += 1
print(list(enumerate(names)))
[(1, 'Adam'), (2, 'Stanisław'), (3, 'Maria'), (4, 'Zofia'), (5, 'Mikołaj')]


# Pętla
num = 1
for name in names:
    print(num, name)
    num += 1

# 1 Adam
# 2 Stanisław
# 3 Maria
# 4 Zofia
# 5 Mikołaj