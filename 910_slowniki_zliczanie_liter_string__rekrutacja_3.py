# Pytanie 9 - dla danego stringa x stwórz słownik
# przechowujący informację ile razy dana litera wystąpiła w stringu

x = "myszydokazujągdykotanieczują"

letter_counter = {}

for letter in x:
    if letter.isalpha():        #spradzam czy alfanumeryczne
        if letter in letter_counter:
            letter_counter[letter] += 1
            # słownik-letter counter[klucz-litera] += wartość =1
        else:
            letter_counter[letter] = 1

print(letter_counter)
# {'m': 1, 'y': 3, 's': 1, 'z': 3, 'd': 2, 'o': 2, 'k': 2, 'a': 2, 'u': 2, 'j': 2, 'ą': 2, 'g': 1, 't': 1, 'n': 1, 'i': 1, 'e': 1, 'c': 1}

# Opcja numer dwa z collections

from collections import Counter

x = "myszydokazujągdykotanieczują"
letter_counter = Counter(c for c in x if c.isalpha())

for letter, count in letter_counter.items():
    print(f"{letter}:{count}")
# m:1
# y:3
# s:1
# z:3
# d:2
# o:2
# k:2
# a:2
# u:2
# j:2
# ą:2
# g:1
# t:1
# n:1
# i:1
# e:1
# c:1


x = "myszydokazujągdykotanieczują"

letter_dict = {}

for letter in x:
    if letter not in letter_dict.keys():
        letter_dict[letter] = 1
    else:
        letter_dict[letter] += 1
print(letter_dict)
# {'m': 1, 'y': 3, 's': 1, 'z': 3, 'd': 2, 'o': 2, 'k': 2, 'a': 2, 'u': 2, 'j': 2, 'ą': 2, 'g': 1, 't': 1, 'n': 1, 'i': 1, 'e': 1, 'c': 1}
