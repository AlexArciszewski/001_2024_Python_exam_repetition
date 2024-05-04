# Zad 7.
# Masz do dyspozycji plik przyklad.txt o następującej zawartości:
# Jak czarne ptaki, lecąc lecąc w wyższą nieba nieba stronę,
#  Coraz się zgromadzały. Ledwie słońce zbiegło zbiegło
#  Z południa, już już ich stado pół pół niebios obiegło


already_existed = set()
with open("plik_tekstowy_zad7.txt", 'r', encoding="utf-8") as file:
    array = []
    for line in file:
        for word in line.split():
            if word not in already_existed:
                array.append(word)
                already_existed.add(word)
    print(" ".join(array))