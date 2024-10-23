# Pytanie 1:
#
# 1. Co zostanie wypisane w wyniku uruchomienia poniższego kodu?
#
# 2. Co zostanie wypisane jeśli usuniemy linijkę 7, w której znajduje się
#@wypisz_efekt_dzialania


def wypisz_efekt_dzialania(funkcja):
    def funkcja_udekorowana():
        a = funkcja()
        print(a)

    return funkcja_udekorowana


@wypisz_efekt_dzialania
def zwroc_czesc():
    return "cześć"


# Rozwiązanie:
#
# 1. Uruchomienie powyższego kodu spowoduje wypisanie stringa "cześć". Funkcja zwroc_czesc została udekorowana
# dekoratorem, który powoduje wypisanie (przy użyciu print) zwracanej przez funkcję wartości.
#
# 2. Po usunięciu nazwy dekoratora nad definicją funkcji zwroc_czesc nie wypisze się nic. Funkcja zwroc_czesc
# zwraca (przy użyciu return), ale nie drukuje stringa, i bez "pomocy" dekoratora ten string nie zostanie wypisany.
#
#
# Zatem:
#
# 1. "cześć"
#
# 2. nic