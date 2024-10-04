# Pytanie 7 - które z poniższych słowników zostały utworzone niepoprawnie?

A = {1: 1, 2: 4, 3: 9}
B = {'imie': 'Anna', 'nazwisko': 'Kowalska'}
C = {[4, 5]: [16, 25]}  #lista nie może być kluczem bo jest mutowalna
D = {(4, 5): [16, 25]}  # typla może być kluczem bo jest niemutowalna
# E = {{1:2}: 'jeden_dwa'}  dict nie może być kluczem bo jest mutowalny