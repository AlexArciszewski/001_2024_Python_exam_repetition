# Zad 2.
# Napisz program, który wczyta dowolne zdanie podane przez użytkownika.
# Usunie z tego zdania znaki interpunkcyjne (, . : ; ! ?), a następnie:
# korzystając z metod krotek:
# ●	zliczy wszystkie wyrazy w zdaniu
# ●	wydrukuje wszystkie wyrazy ze zdania w jednej linii
# ●	poda jaki jest pierwszy i czwarty wyraz w tym zdaniu
# korzystając z metod zbiorów:
# ●	zliczy unikatowe wyrazy w zdaniu
# ●	wyświetli unikatowe wyrazy ze zdania w jednej linii
# ●	poda jaki jest pierwszy i czwarty wyraz w tym zdaniu, zakładając, że pierwszy wyraz rozpoczyna zbiór.
# ●	sprawdzi, czy elementy: pierwszy i czwarty z ostatnich poleceń podpunktów a i b są takie same czy też nie.




# some_sentence = input("Pls write some sentence: ")

# jebac pis,ko,psl,trzeia droge, kukiza, holownie i konfederacje!
some_sentence = "Dzisiaj było slonecznie póxniej padal snieg"
new_string = ""

to_remove = [",", ".", ":", ";", "!", "?"]

for char in some_sentence:
    if char not in to_remove:
        new_string = new_string + char
print(new_string)
x = new_string.split(" ")


new_string_converted = " ".join(x)
print(new_string_converted)
print(f"dl stringa: {len(new_string_converted)}")




# some_new_string = ''.join([char for char in some_sentence if char not in to_remove])
# print(some_sentence)
#
# znaki_interpunkcyjne = [",", ".", ":", ";", "!", "?"]
# zdanie = 'ala ma, kota'
# zdanie_bez_interpunkcji = ''.join([znak for znak in zdanie if znak not in znaki_interpunkcyjne])
# print(zdanie)





# korzystając z metod krotek:
# ●	zliczy wszystkie wyrazy w zdaniu
# ●	wydrukuje wszystkie wyrazy ze zdania w jednej linii
# ●	poda jaki jest pierwszy i czwarty wyraz w tym zdaniu

# Usuń wszystkie niepotrzebne spacje i przekonwertuj tekst na listę
word_box = new_string.strip().split()


word_tuple = tuple(word_box)
word_count = len(word_tuple)
print(word_count)
print(new_string)


print(word_box[0],  word_box[3])

 # korzystając z metod zbiorów:
# ●	zliczy unikatowe wyrazy w zdaniu
# ●	wyświetli unikatowe wyrazy ze zdania w jednej linii
# ●	poda jaki jest pierwszy i czwarty wyraz w tym zdaniu, zakładając, że pierwszy wyraz rozpoczyna zbiór.
# ●	sprawdzi, czy elementy: pierwszy i czwarty z ostatnich poleceń podpunktów a i b są takie same czy też nie.\

word_set = set()
for el in x:
    word_set.add(el)
# wyświetli unikatowe wyrazy ze zdania w jednej linii
print(word_set)
# ●	zliczy unikatowe wyrazy w zdaniu
print(len(word_set))
# ●	poda jaki jest pierwszy i czwarty wyraz w tym zdaniu, zakładając, że pierwszy wyraz rozpoczyna zbiór.

y = list(word_set)
print(y)
print(y[0], y[3])

if y[0] == y[3]:
    print(True)
else:
    print(False)