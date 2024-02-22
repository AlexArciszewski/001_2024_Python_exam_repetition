# Zad6
# Wprowadź jako jeden długi tekst 5 dowolnych kolorów rozdzielonych przecinkami.
# Następnie rozdziel wszystkie kolory na pojedyncze słowa. Wyświetl trzeci wprowadzony kolor.

text = "czerwony, zielony, niebieski, bialy, czarny "
text2 = text.replace(",", "")
print(text2)
text_list = text2.split()
print(text_list[2])