#
# Zad 1.
# Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?), następnie:
# ●	korzystając z metod operujących na listach, podaj wyrazy ze zdania w odwrotnej kolejności.


# some_sentence = input("Pls write some sentence: ")
some_sentence = "W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel? "
some_sentence = some_sentence.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace(",", "").replace("!", "").replace("?", "")
print(f"The text is now: {some_sentence}")
list_some_sentence = some_sentence.split(" ")
#Sort metoda na starej lsicie
print("sort")
print(list_some_sentence)
list_some_sentence.sort(reverse=True)
print(list_some_sentence)

#Sorted tworzy nową listę
print("sorted")
y = sorted(list_some_sentence, reverse=True)
print(y)