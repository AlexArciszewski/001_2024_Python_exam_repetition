name = "aleksander"
print(len(name)) #nawias fioletowy to argument w postaci nazwy zmiennej która sprawdzamy
print(name.capitalize()) #obiekt string ma metody np capitalize(pierwsza duza litera). najpierw zmienna a pózniej po kropce
                         #metoda ta metoda nie przyjmuje argumentów wiec jest(0 na koncu)
print(name.upper()) # duże litery w słowie
print(name.lower()) # małe litery
print(name[0])      #pierwsza litera
print(name[-1])     #ostatnia litera
print(name[0:3])    # trzy litery zaczynając od pierwszej na pozycji zero
print(name[1:])     # wszystkie litery zaczynając od drugiej. Po : nie piszemy nic to idzie do konca
print(name[-3:])    # trzy ostatnie

zdanie = " To jest przypomnienie podstaw programowania z roznych kursow jak udemy, yt i inne."
print(zdanie.split(" ")) #rozdzielenie zdania na wyrazy gdzie rozdielającym znakiemjest spacja Tworzy sie lista

#otrzymamy:['', 'To', 'jest', 'przypomnienie', 'podstaw', 'programowania', 'z', 'roznych', 'kursow', 'jak', 'udemy,', 'yt', 'i', 'inne.']

join_string = " " #zrobienie zdania z listy

print(join_string.join(['To', 'jest', 'przypomnienie', 'podstaw', 'programowania', 'z', 'roznych', 'kursow', 'jak', 'udemy,', 'yt', 'i', 'inne.']))

#otrzymamy: To jest przypomnienie podstaw programowania z roznych kursow jak udemy, yt i inne.


print(name.startswith("a")) #true bo name =aleksander i zaczyna się od a
print(name.startswith("A")) # false bo a a nie A
print(name.endswith("r")) #true bo konczy sie na małe r
print(name.endswith("R")) #false bo konczy sie na małe r

print(name.rstrip("r")) #usuneicie z prawej pierwzego r
print(name.lstrip("a")) #usuneicie zlweje pierwszego a
print(name.strip("a"))


name2 = "ealeksandere"
print(name2.strip("e")) #usuniecie skrajnych liter



name3 =" olo "

print(name3.strip()) #usuneicie nadmiernych spacji


first_name = "Aleksander"
last_name  = "Arciszewski"
print(first_name + " " + last_name) #dodanie stringow

#pocja nr 2 #dodanie stringow
print(join_string.join([first_name,last_name]))


james_bond = 7
print(str(james_bond).zfill(3)) #3 ile znakow mammiec nowy string z zerami
#otrzymamy 007

txt = "Example"
print(txt.find("ple")) #4 pozycja to p i jest w Example.
print(txt.find("le")) #5pozycja to l i odniej się zaczyna
string = "anakonda"
print(string.islower()) #True jeśli są same małe litery
print(string.isupper()) #True jeśli są same duże litery
print(string.istitle()) #True jeśli pierwsza jest duża litera a pozostałe małe Jeśli sa dwa wyrazy oba bedą z dużej litery
print(string.isspace()) #True jeśli jest wszystkie znaki to spacja
print(string.isalnum()) #True jeśli jesli znaki sa alfanumeryczne a-z i 0-9 nie alfanumeryczna jest spacja !#%&?
print(string.isalpha()) #True jeśli jesli znaki sa z alfabetu
print(string.isascii()) #True jeśli jesli znaki sa ASCII
print(string.isdecimal()) #True jeśli jesli znaki są cyframi [0-9]
print(string.isdigit()) #True jeśli jesli string to liczba [0-9] ulamki False
print(string.isnumeric()) #True jeśli jesli string to liczba [0-9] to co is digit jednak ulamek da True

# Stringi sa niemutowalen można użyć za to repalce'a

text = "Ala ma kota"
print(text)
text = text.replace("Ala", "Olo")
print(text)


zdanie = " To jest przypomnienie podstaw programowania z roznych kursow jak udemy, yt i inne."
print(zdanie.find("yt"))
#73 znak od 0

print(zdanie.find("ala"))
#-1 bo nie znalazł

print(zdanie.index("yt"))
#73 znak od 0
print(zdanie.find("ala"))
#-1 bo nie znalazł

# odwrócony alfabet
# import string
# upper_case_alphabet = string.ascii_uppercase
# print(upper_case_alphabet)
# print(type(upper_case_alphabet))
# x = "".join(reversed(upper_case_alphabet))
# print(x)
# ZYXWVUTSRQPONMLKJIHGFEDCBA

#https://pythex.org/
greeting = reversed("Hello, World!")
print(greeting)

#replace

s = "Hello$ Python3$"
s1 = s.replace("$", "")
print(s1)
#Output:Hello Python3



# str.replace(old,new,count)
s = "Hello$ Python3$"
s1 = s.replace("$", "" ,1)
print(s1)
#Output:Hello Python3$


#re.sub(pattern, repl, string, count=0, flags=0)

# “Return the string obtained by replacing the leftmost nonoverlapping occurrences of pattern in
# the string by the replacement repl. If the pattern isn’t found, the string is returned unchanged,
# ” according to the Python’s documentation.
#
# If we want to remove specific characters, the replacement string is mentioned as an empty string

s = "Hello$@& Python3$"
import re
s1 = re.sub("[$@&]","",s)
print(s1)
#Output:Hello Python3

# is_alpha

s="Hello$@ Python3&"
s1="".join(c for c in s if c.isalpha())
print (s1)
#Output:HelloPython
# s=”Hello$@ Python3&”
#
# (c for c in s if c.isalpha())
#
# Result: [‘H’, ‘e’, ‘l’, ‘l’, ‘o’, ‘P’, ‘y’, ‘t’, ‘h’, ‘o’, ‘n’]
#
# It’s a generator expression. It returns a generator object containing all alphabets from the string.
#
# s1=””.join(c for c in s if c.isalpha())
#
# ””.join will join all of the elements in the iterable using an empty string.

# Filtrownaie stringa filter

s="Hello$@ Python3&"
f=filter(str.isalpha,s)
s1="".join(f)
print (s1)

# https://builtin.com/software-engineering-perspectives/python-remove-character-from-string
