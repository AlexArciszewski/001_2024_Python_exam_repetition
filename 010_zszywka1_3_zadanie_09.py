
# Zad 9.
# Korzystając z funkcji input(), pobierz dowolny napis od użytkownika.
# Następnie utwórz nowy string z zamienioną pierwszą literą z ostatnią i wyświetl efekt na ekranie, np.
# >Użytkownik wprowadził wyraz “Hello world!”
# > Program wydrukuje na ekranie nowy napis: “dello worlH!”
#
# Podpowiedź:
# Spróbuj wykonać tę operację, działając jedynie na oryginalnym napisie. Czy jest to możliwe?
#string jest niemutowalny....trzeeba slicing
word = input("Pls give me the word: ")
total = len(word) -1
new_first = word[total]
new_last = word[0]
middle = word[1:-1]
print(f"The modified word is {new_first}{middle}{new_last}")
