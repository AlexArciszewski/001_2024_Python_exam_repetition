# 1. Program ma wykonać kilka operacji na pobranym od użytkownika dowolnym tekście (stringu),  który ma co najmniej siedem znaków.
# Operacje te to:
# ●	wprowadzenie i wyświetlenie na ekranie tego tekstu
# ●	wyświetlenie liczby znaków, które on zawiera
# ●	wyświetlenie pierwszego i ostatniego znaku tego tekstu
# ●	wyświetlenie dowolnych 3 znaków z środka tego tekstu.


def main() -> None:
    while True:
        # funkcja pobiera string od usera i go analizuje
        text = input("Wprowadź dowolny tekst (minimum 7 znaków): ")

        if len(text) <= 7:
            print("The program will now exit")
            break

        else:
            print(text)
            print(f" Total length of a string is: {len(text)}")
            print(text[0], text[-1])

            start = (len(text) - 3) // 2  # 11-3=8 8//2 ->4
            middle = text[start:start + 3]
            print(f"3 letters from the middle are: {middle}")
            break


if __name__ == "__main__":
    main()


