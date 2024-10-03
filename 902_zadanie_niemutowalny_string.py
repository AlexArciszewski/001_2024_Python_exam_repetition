#Co się stanie po wykonaniu poniższego kodu

# a = 'abcdefgh'
# print(a[1])
# a[1] = 'X'

# Odpowiedź: String nie jest mutowalny więc próba zmiany litery na pozycji 1 spowoduje błąd TypeError?

# error:
# Traceback (most recent call last):
#   File "C:\Users\arcis\PycharmProjects\pythonProject25\902_zadanie_niemutowalny_string.py", line 5, in <module>
#     a[1] = 'X'
#     ~^^^
# TypeError: 'str' object does not support item assignment

# Co innego można zobić...
a = 'abcdefgh'

a_list = list(a)
print(a_list)
a_list[1] = "X"
new_a = ''.join(a_list)
print(new_a)
