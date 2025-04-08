# 6. Wprowadź jako jeden długi tekst 5 dowolnych kolorów rozdzielonych przecinkami. Następnie rozdziel
# wszystkie kolory na pojedyncze słowa. Wyświetl trzeci wprowadzony kolor.


def main() -> None:
    text = "czerwony,zielony,niebieski,szary,czarny"
    text_spaced = text.replace(",", " ")
    print(text_spaced)
    text_list = text_spaced.split(" ")
    print(text_list[3])







if __name__ == "__main__":
    main()