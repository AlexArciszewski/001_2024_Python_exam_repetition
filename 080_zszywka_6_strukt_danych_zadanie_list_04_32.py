# Zad 5.
# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ;  ! ?), a następnie
# korzystając z metod operujących na listach, program powinien:
# • podawać liczbę wyrazów w zdaniu
# • podawać wyrazy, które rozpoczynają się wielką literą, jeśli takie są, jeśli nie, również to zgłosić
# • sprawdzać i podawać, czy lista zawiera: „i”, „w”, „na”, „pod”, „dla”. Jeśli tak, to które są to wyrazy i
# jakie są ich indeksy na liście. Jeśli żaden z poszukiwanych wyrazów w zdaniu nie występuje program również
# powinien o tym informować
# • posortować wyrazy ze zdania alfabetycznie i wydrukować je w zmienionej kolejności.

# some_text = input("Some text pls: ")
some_text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."
some_text = some_text.replace(",","").replace(".", "").replace(":", " ").replace(";", "").replace("!", "").replace("?", "")
print(some_text)
some_text_list = some_text.split(" ")
print(some_text_list)
# • podawać liczbę wyrazów w zdaniu
print(len(some_text_list))

# • podawać wyrazy, które rozpoczynają się wielką literą, jeśli takie są, jeśli nie, również to zgłosić
True_box = []
False_box = []
for word in some_text:
    if word.istitle() == True:
        True_box.append(True)
    else:
        False_box.append(False)
if len(True_box) > 0:
    print("There is a big letter in the text")
else:
    print("There is no a big letter in the text")

# • sprawdzać i podawać, czy lista zawiera: „i”, „w”, „na”, „pod”, „dla”. Jeśli tak, to które są to wyrazy i
# jakie są ich indeksy na liście. Jeśli żaden z poszukiwanych wyrazów w zdaniu nie występuje program również
# powinien o tym informować

searched_words = ["while", "I", "many", "of", "in", "Once"]
print("Searched words are: ")
for searched_word in searched_words:
    print(searched_word)
box_pos = []
for searched_word in searched_words:
     if searched_word in some_text:
        print(searched_word)
        counter = some_text_list.count(searched_word)
        print(f"times showed: {counter}")
        pos = (some_text.find(searched_word))
        print(some_text.find(searched_word))



















