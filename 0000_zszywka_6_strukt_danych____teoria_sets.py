# print(set(A))
#jak na liscie chce miec unikalne wartosci czyli bez zduplikowanych. korzystamy z funkcji set

# print(A&B) #czyli wspólne elementy
# print(A|B)#wszystkie el unikalne bez powtórzeń tych samych
# print(A - B) #te co w A po odjęciu tych co w B
# print(B -A)   #te co w B po odjęciu tych co w A
# print(A^B)  #alternatywa wykluczajaca od wszystkich to co wspolne
# #A.discard(1)-usuniecie pierwszej wartości tzn 2 od zera
# #A.remove(24)-error jak nie ma tej wartosći
# print(A.issubset(B))             #czy jeden zbiór-A jest podzbiorem-B 2 zbioru

#zbior SET: nie moze miec zduplikowanych danych
names_set ={"Celina", "Dorota", "Adam", "Barbara", "Ewa", "Karol", "Dorota"}
print(names_set)
names_set =set() #pusty set
names_set.add("Tomasz") #dodanie do set/zbioru
names_set.add("Adam")
names_set.add("Barbara")
names_set.add("Ewa")
print(names_set)
names_set.remove("Adam")#element ktory nie istnieje wywoła błąd
print(names_set)
names_set.discard("Ewa")#element ktory nie istnieje nie wywoła bledu
print(names_set) #nie ma wyswietlania imion z setu nawiasami wkadratowymi jak w liscie
for names in names_set:
    print(names)            #różna kolejność wyświetlania
"""
s ={ j for j in range(10)}
print(s)    
"""
print('next')
set = {names for names in names_set}
print(set)
print(names_set)
names_tuple =()
names_set.add(names_tuple) #można dodac niemutowalne obiekty jak tuple do seta ale listy nie!
print(names_set)

names_set2 = {"Pawel", "Michal", "Robert", "Teodor"}
print(names_set2)
names_set3 =names_set.union(names_set2) #tworzymy nowy set stare zostają
print(names_set3)
print("set comprehension")
s2 ={names5 for names5 in names_set3}
print(s2)
print("z set do listy")
list404 =[]
for name in names_set3:  #z set do listy
    print(name)
    list404.append(name)
print(list404)
names_set4 =names_set2
print("checkpoint")
print(names_set4)
print(names_set2)
print(names_set3)
names_set4.update(names_set3)
print(names_set4)

names_set5 = names_set4.difference(names_set2) #z setu4 usuwamy to co pokrywa sie z set2
print("wynik to: ", names_set5) #pusty set to wynik

names_set6 = names_set4.intersection(names_set2) # część wspolne dwoch setow i z tego nowy set6
print(names_set6)

names_set7 = names_set4.symmetric_difference(names_set2) # elementy spoza czesci wspolnej 2 setow trafiaja do set7
print(names_set7) #odp pusty set

print("set cleaning")

names_set3.clear()
print(names_set3)

#adding list to set
print(names_set4)
names_list505 = ["Celina", "Dorota","Adam", "Barbara", "Ewa","Karol"]
names_list505.extend(names_set4)
print(names_list505)  #dodanie el.set do listy.


some_set = {1, 2, 3}

# dodawanie el.
some_set.add(4)
print(some_set)
# {1, 2, 3, 4}

#  usuwanie elementu który jest liczbą 1
#  usuwanie elementu ktorego nie ma w zbiorze da błąd
some_set.remove(1)
print(some_set)
# {2, 3, 4}

# usuwanie elementu ktorego nie ma w zbiorze: NONE
print(some_set.discard(30))


some_set.update({20})
print(some_set)

# OPERACJE NA SETACH
# 1. łączenie zbiorów
# A.union(B)
#
# 2.czesc wspolna
# A.intersection(B)
#
# 3.Różnica
# A-B or A.difference(B)
#
# 4.Symetryczna rożnica to co jest w A ale nie należy do B i to co jest w B ale nie należy do A
# A ^ B
# A.symmetric_difference(B)

#wyświetl konkretny element zbioru:
# Nie iteruje się i nie ma slicingu trzeba zmienic set na listę i wyświetlić el listy:
word_set ={}
y = list(word_set)
print(y)
print(y[0], y[3])
#ostatni element
moj_zbior = {'a', 'b', 'c'}

for element in moj_zbior:
    ostatni = element

print(ostatni)

#pierwszy

moj_zbior = {'jabłko', 'banan', 'gruszka'}
pierwszy = next(iter(moj_zbior))
print(pierwszy)