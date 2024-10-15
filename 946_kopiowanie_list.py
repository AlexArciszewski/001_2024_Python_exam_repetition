
A = [1, 2, 3, 4,5]  #obszar w pamieci dla listy A
B = A               #obszar w pamieci B przyjmuje nie listę A a referencję do niej.
C = A[:]            #drugi obszar w pamieci bo to kopia a kopuia zapisuje sie gdzies indziej
# Do lsity C przypisaliśmy zawartośc listy A przeczytaną od poczatku do końca.
# Nie przypisaliśmy referencji a zawartość listy


B[0] = 111          # zmieniamy w liście B element na pozycji 0 ale też zmieniamy go w liscie A bo A=B
print(id(B))
print(id(A))
print(id(C))
# 1988470838976
# 1988470838976
# 1988474152640