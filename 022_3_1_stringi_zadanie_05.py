#
# Pobierz od użytkownika dowolny napis zawierający 5 białych znaków (spacji) na początku, a następnie:
# ▪ wyświetl ten napis
# ▪ usuń wiodące białe znaki i wyświetl napis po tej zmianie

def main() -> None:
    while True:
        text = input("Give me the text with the 5 spaces at the beginning: ")
        if text[0:5] == "     ":
            print(text)
            print(text[5:])
            break
        else:
            print("You forgot about the spaces dummy")
            break



if __name__ == "__main__":
    main()