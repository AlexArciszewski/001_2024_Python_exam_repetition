# Plikami w formacie JSON. Jest to w rozwinięciu - JavaScript Object Notation - otwarty format zapisu struktur danych. 
# json_data.json:
# {
#   "title" : "This Is What You Came For",
#   "artist" : "Calvin Harris",
#   "length" : "3.41",
#   "released" : "2016.04.29"
# }

# Odczyt:
import json
with open('json_data.json') as json_file:
    data = json.load(json_file)
    print(data)
#otwarcie jsona z użyciem metody json.load(json_file)
# Wynikiem jest słownik który odzwierciedla strukturę danych pliku .json

#Zapis do pliku JSON

# metoda json.dump, która przyjmuje dwa argumenty: data - słownik, który ma być zapisany w formacie JSON oraz outfile, czyli uchwyt do pliku, do którego będziemy zapisywali.
import json

data = {
    'employees':[
        {
         'name':'jan Nowak',
         'spec':'Welder'
         'place': 'Baltic Sea'   
            
        },
        {
         'name':'Jan Matejko',
         'spec':'Painter'
         'place': 'Heaven'    
            
        },
        
        
    ]
}

with open("json_data.json",'w') as outfile:
          json.dump(data, outfile)
          


