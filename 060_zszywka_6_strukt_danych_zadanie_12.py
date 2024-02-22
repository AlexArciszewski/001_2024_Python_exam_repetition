# Zad 12.
# Wydrukuj alfabet w porządku naturalnym, czyli od ‘a’ do ‘z’ a następnie odwróconym,
# pisanym wielkimi literami, czyli od ‘Z’ do ‘A’.
#
# Podpowiedź:
# Skorzystaj z kodów ASCII i konwersji na typ chr.


import string

lower_case_alphabet = string.ascii_lowercase
print(lower_case_alphabet)
upper_case_alphabet = string.ascii_uppercase
print(upper_case_alphabet)
print(type(upper_case_alphabet))
x = "".join(reversed(upper_case_alphabet))
print(x)
