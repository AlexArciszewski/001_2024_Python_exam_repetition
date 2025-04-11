
some_text = "W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel."


birds = {
    'kos' : 'Turdus merula',
    'wilga' : 'Oriolus oriolus',
    'rudzik' : 'Erithacus rubecula',
    'kukulka' : 'Cuculus canorus',
    'pleszka' : 'Phoenicurus phoenicurus',
    'bogatka' : 'Parus major',
    'drozd' : 'Turdus philomelos',
    'zieba' : 'Fringilla coelebs',
    'dzwoniec' : 'Chloris chloris',
    'szczygiel' : 'Carduelis carduelis',
    'szpak' : 'Sturnus vulgaris',
    'kopciuszek' : 'Phoenicurus ochruros'
    }

print(birds.keys())
print(birds.values())

for key, value in birds.items():
    some_text = some_text.replace(key, key + "(" + value + ")")

print(some_text)