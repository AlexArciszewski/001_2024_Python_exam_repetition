# Dla podanego słownika S napisz kod sprawdzający czy liczba 7430 znajduje się wśród kluczy słownika.
#
# Jeśli tak - wypisz True.
#
# Jeśli nie - False.

S = {x:x+1 for x in range(10000) if x%23 == 0}


print(S)
key_list = []
for key in S.keys():
    key_list.append(key)

if 7430 in key_list:
    print(True)
else:
    print(False)


