# Zad 3.
# Zapisz wszystkie wyrazy z poniższego tekstu do słownika (jako klucze).
# Wartości przypisane do tych kluczy mają być równe ilości wystąpień słowa w tekście.

some_text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."

text = some_text.replace(",", "").replace(".", "").replace("-", "")
print(text)
text_list = text.split(" ")
print(text_list)
text_dict = {}
list_of_reps =[]
for word in text_list:
    counter = text_list.count(word)
    list_of_reps.append(counter)
print(list_of_reps)

word_dict = dict(zip(text_list, list_of_reps))
print(word_dict)




# my_list = ['apple', 'banana', 'grapes', 'pear']
# for counter, value in enumerate(my_list):
#     print(counter, value)