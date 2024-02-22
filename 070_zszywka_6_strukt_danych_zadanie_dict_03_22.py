# Zad 3.
# Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze). Wartości przypisane do tych kluczy mają być
# równe ilości wystąpień słowa w tekście.
#
# ("Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten "
#  "lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my "
#  "chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more.")


text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."

#tworzenie listy słów i czyszczenie znaków
text2 = text.replace(",","").replace(".", "").replace("-","")
print(text2)
list_of_words = []
list_of_words = text2.split(" ")
print(list_of_words)


#tworzenie listy powtórzeń ktorą zzipuję zórna listą i zrobię słownik
list_of_reps = []
for word in list_of_words:
    counter = list_of_words.count(word)
    list_of_reps.append(counter)
print(list_of_reps)

#tworzenie słownika....
dict_of_words = dict(zip(list_of_words, list_of_reps))
print(dict_of_words)

#tworzenie słownika....
dict2_of_words = {}

for i in range(len(list_of_words)):
    dict2_of_words[list_of_words[i]] = list_of_reps[i]
print(dict2_of_words)





