# Pytanie 30 - jaką wartość przyjmie poniższe zdanie logiczne?
# Wyjaśnij proces jego ewaluacji i znaczenie poszczególnych słów: is, not, in.

print(1 is not True in [1, 2, 3]) # ->
# (1 is not True) and (True in [1,2,3]) # ->
# (True) and (True) -> True

# różne wyniki dla operatorów "is not" oraz "!=" !
print(1 is not True)
print(1 != True)



# not 2 is 2.0 in [0,2]

# print(not 2 is 2.0)
# print(2.0 in [0,2])
#
# Rozwiązanie:
#
# Powyższe zdanie zostanie przez Pythona przekształcone w: (not 2 is 2.0) and (2.0 in [0,2]).
#
# (2 is 2.0) to False, bo integer nie jest floatem. Słowo not powoduje zamianę tego wyrażenia na True.
#
# (2.0 in [0,2]) to True, bo wartość floata 2.0 równa jest wartości integera 2, a zatem 2.0 znajduje się w liście [0,2].
#
# Mamy więc: True and True czyli True.