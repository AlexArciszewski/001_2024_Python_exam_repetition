# Zad 14.
# Znajdź przykłady 3 sposobów na szyfrowanie znaków w systemach informatycznych i zapoznaj się z ich działaniem
# (jakie operacje matematyczne przeprowadzają?).
#
#     Szyfrowanie symetryczne:
#
#         Działanie: W tej metodzie używana jest ta sama klucz do zarówno szyfrowania, jak i deszyfrowania danych. Algorytmy
#         szyfrowania symetrycznego są szybkie i efektywne, co sprawia, że są często stosowane do szyfrowania dużych ilości danych.
#
#         Przykład: Algorytmy takie jak AES (Advanced Encryption Standard) są powszechnie używane do szyfrowania danych symetrycznego.
#
#     Szyfrowanie asymetryczne (klucze publiczny/klucz prywatny):
#
#         Działanie: W tej metodzie używane są dwa klucze: klucz publiczny do szyfrowania danych i klucz prywatny do ich deszyfrowania.
#         Klucz publiczny jest udostępniany publicznie, natomiast klucz prywatny jest trzymany w tajemnicy.
#
#         Przykład: Algorytmy takie jak RSA (Rivest-Shamir-Adleman) używają tego podejścia. Dane zaszyfrowane kluczem publicznym mogą
#         być odszyfrowane tylko przy użyciu odpowiadającego im klucza prywatnego.
#
#     Szyfrowanie hasłem (hashowanie):
#
#         Działanie: W tym podejściu nie ma klucza, ale używane jest hasło jako dane wejściowe dla algorytmu haszującego. Hasz jest
#         jednokierunkowy, co oznacza, że nie da się łatwo odwrócić procesu i odzyskać oryginalnych danych.
#
#         Przykład: Algorytmy haszujące, takie jak MD5, SHA-256, czy bcrypt, są powszechnie stosowane do przechowywania haseł użytkowników.
#         Głównym celem jest zapewnienie bezpieczeństwa haseł, nawet gdy dane przechowywane są w przypadku wycieku.
#
# Te trzy metody różnią się podejściem do zarządzania kluczami i zastosowaniami praktycznymi. Szyfrowanie symetryczne jest szybkie
# i efektywne, ale wymaga bezpiecznego udziału klucza. Szyfrowanie asymetryczne umożliwia bezpieczną wymianę kluczy, ale
# jest bardziej zasobożerne. Szyfrowanie hasłem jest używane do zabezpieczania haseł i innych danych wrażliwych w przypadku
# przechowywania ich w systemach informatycznych.