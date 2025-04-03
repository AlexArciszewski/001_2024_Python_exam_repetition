import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


path = r"C:\Dane\26_SQL\3_database\3_db_cars_csv_2\vehicles.csv"
# df = pd.read_csv(path)
# print(df.head())
# df.info()

#Chunki danych
# chunk_size = 1000  # Wiersze na raz
# for chunk in pd.read_csv(path, chunksize=chunk_size):
#     print(chunk.head())
# print(chunk.info())

df = pd.read_csv(path)

# Konwertuje manufacturer na string i uzupełnienie braków
df["manufacturer"] = df["manufacturer"].astype(str).fillna("No Data")

# Sprawdzenie unikalnych wartości
print(df["manufacturer"].unique())

# Liczenie wystąpień i rysowanie wykresu
manufacturer_counts = df["manufacturer"].value_counts()

#zliczam fordy
ford_cars = df["manufacturer"].value_counts().get("ford",0)
print(ford_cars)
print(f"There are {ford_cars} ford cars")

#nowe plutno na wykres 10/5
plt.figure(figsize=(10, 5))
#Lista kategorii na osi X (np. nazwy producentów aut),Y Liczby odpowiadające każdej kategorii (np. liczba samochodów danej marki).
plt.bar(manufacturer_counts.index, manufacturer_counts.values)
plt.xlabel("manufacturer")
plt.ylabel("Number ")
plt.title("Number of cars per Manufacturer")
#rotacja nazw aby sie zmeisciły na wykresie
plt.xticks(rotation=45)

plt.show()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 880 entries, 426000 to 426879
# Data columns (total 26 columns):
#  #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   id            880 non-null    int64  
#  1   url           880 non-null    object 
#  2   region        880 non-null    object 
#  3   region_url    880 non-null    object 
#  4   price         880 non-null    int64  
#  5   year          880 non-null    int64  
#  6   manufacturer  837 non-null    object 
#  7   model         863 non-null    object 
#  8   condition     616 non-null    object 
#  9   cylinders     521 non-null    object 
#  10  fuel          879 non-null    object 
#  11  odometer      880 non-null    int64  
#  12  title_status  880 non-null    object 
#  13  transmission  877 non-null    object 
#  14  VIN           568 non-null    object 
#  15  drive         600 non-null    object 
#  16  size          239 non-null    object 
#  17  type          657 non-null    object 
#  18  paint_color   628 non-null    object 
#  19  image_url     880 non-null    object 
#  20  description   880 non-null    object 
#  21  county        0 non-null      float64
#  22  state         880 non-null    object 
#  23  lat           876 non-null    float64
#  24  long          876 non-null    float64
#  25  posting_date  880 non-null    object 
# dtypes: float64(3), int64(4), object(19)
# memory usage: 178.9+ KB
# None

