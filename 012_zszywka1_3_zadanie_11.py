
# Zad 11.
# Utwórz dwa dowolne stringi o różnych wartościach. Utwórz trzeci napis, który będzie się składał z pierwszej połówki pierwszego
# napisu oraz drugiej połówki drugiego napisu. Skorzystaj z ujemnych indeksów.
# imie1 = “Kacper”
# imie2 = “Lucjan”
# imie3 = “Kacjan”


s1 = "Tomasz"
s2 = "Staszek"
s3 = s1[0:4]+s2[3:]
print(s3)
s4 = s1[:-2]+s2[-4:]
print(s4)
