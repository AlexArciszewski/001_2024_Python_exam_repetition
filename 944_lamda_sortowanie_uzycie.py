# Pytanie 23 - czym jest lambda?
# Napisz przykładowy kod wykorzystujący lambdę.
# Funkcja anonimowa krótka stosowana jako argument od innej funkcji które pobierają inną funkcję
# lambda argument : wyrażenie
# lambda x:x+2

L = [('Anna', 82), ('Robert', 33), ('Artur', 40), ('Feliks', 56)]
# W poniższej linijce funkcja sorted pobiera sekwencję danych do posortowania i klucz, po którym będzie sortować.
# Sekwencją jest lista L, a kluczem lambda, która dla kolejnego elementu listy L (czyli tupli)
# zwraca drugi element danej tupli.
L_posortowana = sorted(L, key = lambda x:x[1])
#sortujemy w liscie L za pomoca funkcji lambda gdzie kluczem jest x[1] wyrazenia
# czyli drugi element paryw  tupli sortujemy po wieku
print(L_posortowana)



numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

numbers = [1, 2, 3, 4, 5]
numbers_increased_by_five = list(map(lambda x: x+5, numbers))
print(numbers_increased_by_five)

# zip bez funkcji
paired = list(zip(numbers, numbers_increased_by_five))
print(paired)