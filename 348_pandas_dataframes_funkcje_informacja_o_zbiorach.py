import pandas as pd
df_4 = pd.read_csv("C:/Dane/2_ML_Projekty/003_programowanie_ML_zadanka_kurs_wprowadzenie/002_iris.csv")
print(df_4)

#     5.1  3.5  1.4  0.2     Iris-setosa
#0    4.9  3.0  1.4  0.2     Iris-setosa
#1    4.7  3.2  1.3  0.2     Iris-setosa
#2    4.6  3.1  1.5  0.2     Iris-setosa
#3    5.0  3.6  1.4  0.2     Iris-setosa
#4    5.4  3.9  1.7  0.4     Iris-setosa
#..   ...  ...  ...  ...             ...
#144  6.7  3.0  5.2  2.3  Iris-virginica
#145  6.3  2.5  5.0  1.9  Iris-virginica
#146  6.5  3.0  5.2  2.0  Iris-virginica
#147  6.2  3.4  5.4  2.3  Iris-virginica
#148  5.9  3.0  5.1  1.8  Iris-virginica
#[149 rows x 5 columns]

print("nagłówek i 5 wierszy")
print(df_4.head())

#  5.1  3.5  1.4  0.2  Iris-setosa
#0  4.9  3.0  1.4  0.2  Iris-setosa
#1  4.7  3.2  1.3  0.2  Iris-setosa
#2  4.6  3.1  1.5  0.2  Iris-setosa
#3  5.0  3.6  1.4  0.2  Iris-setosa
#4  5.4  3.9  1.7  0.4  Iris-setosa


print("zerowy  wiersz")
print(df_4.head(0))

#Empty DataFrame
#Columns: [5.1, 3.5, 1.4, 0.2, Iris-setosa]
#Index: []

print("końcowe 5 wierszy")
print(df_4.tail())

#     5.1  3.5  1.4  0.2     Iris-setosa
#144  6.7  3.0  5.2  2.3  Iris-virginica
#145  6.3  2.5  5.0  1.9  Iris-virginica
#146  6.5  3.0  5.2  2.0  Iris-virginica
#147  6.2  3.4  5.4  2.3  Iris-virginica
#148  5.9  3.0  5.1  1.8  Iris-virginica



print("końcowy wiersz")
print(df_4.tail(1))

#     5.1  3.5  1.4  0.2     Iris-setosa
#148  5.9  3.0  5.1  1.8  Iris-virginica


print("\nmetoda shape ile wierszy ile kolumn\n")
print(df_4.shape)
#(149, 5)

print("\nmetoda info podstawowe dane o zbiorze danych wszystkie kolumny , rekordy not null jak not-null 891 rekordów a w bazie jest 891 rekordów to nie ma pustych nullowych rekordów dobrze\n")
print(df_4.info())


#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 149 entries, 0 to 148
#Data columns (total 5 columns):
# #   Column       Non-Null Count  Dtype
#---  ------       --------------  -----
# 0   5.1          149 non-null    float64
# 1   3.5          149 non-null    float64
# 2   1.4          149 non-null    float64
# 3   0.2          149 non-null    float64
# 4   Iris-setosa  149 non-null    object
#dtypes: float64(4), object(1)
#memory usage: 5.9+ KB
#None

# warto sprawdzić czy te typy danych zgadzają się z naszą logiką…..czy float jest tam gdzie być powinien.... itd
print("\nmetoda info podstawowe dane o zbiorze danych wszystkie kolumny , rekordy not null jak not-null 891 rekordów a w bazie jest 891 rekordów to nie ma pustych nullowych rekordów dobrze\n")
print(df_4.describe())

#              5.1         3.5         1.4         0.2
#count  149.000000  149.000000  149.000000  149.000000
#mean     5.848322    3.051007    3.774497    1.205369
#std      0.828594    0.433499    1.759651    0.761292
#min      4.300000    2.000000    1.000000    0.100000
#25%      5.100000    2.800000    1.600000    0.300000
#50%      5.800000    3.000000    4.400000    1.300000
#75%      6.400000    3.300000    5.100000    1.800000
#max      7.900000    4.400000    6.900000    2.500000
# count ile wartosci bez braku danych, mean średnia wartość, std-odhcylenie standrd, 1,2,3, kwartyl. mediana...

print("\nmetoda columns zwraca nazwy kolumn\n")

print(df_4.columns)

#Index(['5.1', '3.5', '1.4', '0.2', 'Iris-setosa'], dtype='object')



print("\nmetoda isnull() zwracam True gdzie sa braki a tam gdzie zapisane to False\n")

print(df_4.isnull())

#       5.1    3.5    1.4    0.2  Iris-setosa
#0    False  False  False  False        False
#1    False  False  False  False        False
#2    False  False  False  False        False
#3    False  False  False  False        False
#4    False  False  False  False        False
#..     ...    ...    ...    ...          ...
#144  False  False  False  False        False
#145  False  False  False  False        False
#146  False  False  False  False        False
#147  False  False  False  False        False
#148  False  False  False  False        False

print("\nmetoda isna() braki w rekordach tam gdzie brak True\n")

print(df_4.isna())

#       5.1    3.5    1.4    0.2  Iris-setosa
#0    False  False  False  False        False
#1    False  False  False  False        False
#2    False  False  False  False        False
#3    False  False  False  False        False
#4    False  False  False  False        False
#..     ...    ...    ...    ...          ...
#144  False  False  False  False        False
#145  False  False  False  False        False
#146  False  False  False  False        False
#147  False  False  False  False        False
#148  False  False  False  False        False

#[149 rows x 5 columns]



print("\nmetoda dropna() usuniecie brakow danych\n")

df_5 =df_4.dropna(how='all')
print(df_5)

#nie ma braków
#     5.1  3.5  1.4  0.2     Iris-setosa
#0    4.9  3.0  1.4  0.2     Iris-setosa
#1    4.7  3.2  1.3  0.2     Iris-setosa
#2    4.6  3.1  1.5  0.2     Iris-setosa
#3    5.0  3.6  1.4  0.2     Iris-setosa
#4    5.4  3.9  1.7  0.4     Iris-setosa
#..   ...  ...  ...  ...             ...
#144  6.7  3.0  5.2  2.3  Iris-virginica
#145  6.3  2.5  5.0  1.9  Iris-virginica
#146  6.5  3.0  5.2  2.0  Iris-virginica
#147  6.2  3.4  5.4  2.3  Iris-virginica
#148  5.9  3.0  5.1  1.8  Iris-virginica


print("\nmetoda dropna() usuniecie brakow danych\n")

df_5 =df_4.dropna(how='any')
print(df_5)

#metoda dropna() usuniecie brakow danych

#     5.1  3.5  1.4  0.2     Iris-setosa
#0    4.9  3.0  1.4  0.2     Iris-setosa
#1    4.7  3.2  1.3  0.2     Iris-setosa
#2    4.6  3.1  1.5  0.2     Iris-setosa
#3    5.0  3.6  1.4  0.2     Iris-setosa
#4    5.4  3.9  1.7  0.4     Iris-setosa
#..   ...  ...  ...  ...             ...
#144  6.7  3.0  5.2  2.3  Iris-virginica
#145  6.3  2.5  5.0  1.9  Iris-virginica
#146  6.5  3.0  5.2  2.0  Iris-virginica
#147  6.2  3.4  5.4  2.3  Iris-virginica
#148  5.9  3.0  5.1  1.8  Iris-virginica

#[149 rows x 5 columns]

print("\nmetoda isna(0.sum() czyszczenie bazy z brakow\n")
# Korzystajac z argumentu any usuwamy znaczną cześc informacji trzeba uważać
# dropna nie jest najlepszą opcją!!!
df6 = df_4.isna().sum()
print(df6)


print("\nmetoda duplicated() czyszczenie bazy z brakow\n")

print(df_4.duplicated())


#0      False
#1      False
#2      False
#3      False
#4      False
##       ...
#144    False
#145    False
#146    False
#147    False
#148    False
#Length: 149, dtype: bool
#nie ma zduplikowanych rekordów

#sprawdzamy sumowaniem
print(df_4.duplicated().sum())
#sumowanie zduplikowanych rekordów mamy 3


print("\nmetoda drop_duplicates() usuwanie duplikatoww\n")
df_8=df_4.drop_duplicates()
print(df_8)
print(df_8.shape)
#usuwamy duplikaty
#     5.1  3.5  1.4  0.2     Iris-setosa
#0    4.9  3.0  1.4  0.2     Iris-setosa
#1    4.7  3.2  1.3  0.2     Iris-setosa
#2    4.6  3.1  1.5  0.2     Iris-setosa
#3    5.0  3.6  1.4  0.2     Iris-setosa
#4    5.4  3.9  1.7  0.4     Iris-setosa
#..   ...  ...  ...  ...             ...
#144  6.7  3.0  5.2  2.3  Iris-virginica
#145  6.3  2.5  5.0  1.9  Iris-virginica
#146  6.5  3.0  5.2  2.0  Iris-virginica
#147  6.2  3.4  5.4  2.3  Iris-virginica
#148  5.9  3.0  5.1  1.8  Iris-virginica
#
#[146 rows x 5 columns]
#(146, 5)

#nie ma juz pwoielonych rekordów



#     5.1  3.5  1.4  0.2     Iris-setosa



print("""\nsortowanie po zmiennej fare  czyli po danych z kolumny fare rosnąco. Wynik się nie zapisuje...jeśli  nie jest
 przypisany do nowego argumenty tu sie zapisał bo mamy df5 ale ostawiając df4 by się nie zapisało.\n""")
print(df_8.head())
df5 = df_8.sort_values(by='5.1')
print(df5)
#roznoąco

#   5.1  3.5  1.4  0.2  Iris-setosa
#0  4.9  3.0  1.4  0.2  Iris-setosa
#1  4.7  3.2  1.3  0.2  Iris-setosa
#2  4.6  3.1  1.5  0.2  Iris-setosa
#3  5.0  3.6  1.4  0.2  Iris-setosa
#4  5.4  3.9  1.7  0.4  Iris-setosa
#     5.1  3.5  1.4  0.2     Iris-setosa
#12   4.3  3.0  1.1  0.1     Iris-setosa
#7    4.4  2.9  1.4  0.2     Iris-setosa
#41   4.4  3.2  1.3  0.2     Iris-setosa
#37   4.4  3.0  1.3  0.2     Iris-setosa
#40   4.5  2.3  1.3  0.3     Iris-setosa
#..   ...  ...  ...  ...             ...
#117  7.7  2.6  6.9  2.3  Iris-virginica
#121  7.7  2.8  6.7  2.0  Iris-virginica
#116  7.7  3.8  6.7  2.2  Iris-virginica
#134  7.7  3.0  6.1  2.3  Iris-virginica
#130  7.9  3.8  6.4  2.0  Iris-virginica


print("""\nsortowanie po zmiennej fare  czyli po danych z kolumny fare rosnąco. Wynik się nie zapisuje...jeśli  nie jest
 przypisany do nowego argumenty tu sie zapisał bo mamy df5 ale ostawiając df4 by się nie zapisało.\n""")
print(df_8.head())
df5 = df_8.sort_values(by='5.1')
print(df5)

print("""\nsortowanie malejące\n""")

print(df_8.head())
df6 = df_8.sort_values(by='5.1', ascending=False)
print(df6)

#   5.1  3.5  1.4  0.2  Iris-setosa
#0  4.9  3.0  1.4  0.2  Iris-setosa
#1  4.7  3.2  1.3  0.2  Iris-setosa
#2  4.6  3.1  1.5  0.2  Iris-setosa
#3  5.0  3.6  1.4  0.2  Iris-setosa
#4  5.4  3.9  1.7  0.4  Iris-setosa
#     5.1  3.5  1.4  0.2     Iris-setosa
#130  7.9  3.8  6.4  2.0  Iris-virginica
#121  7.7  2.8  6.7  2.0  Iris-virginica
#116  7.7  3.8  6.7  2.2  Iris-virginica
#117  7.7  2.6  6.9  2.3  Iris-virginica
#134  7.7  3.0  6.1  2.3  Iris-virginica
#..   ...  ...  ...  ...             ...
#40   4.5  2.3  1.3  0.3     Iris-setosa
#41   4.4  3.2  1.3  0.2     Iris-setosa
#7    4.4  2.9  1.4  0.2     Iris-setosa
#37   4.4  3.0  1.3  0.2     Iris-setosa
#12   4.3  3.0  1.1  0.1     Iris-setosa

#[146 rows x 5 columns]
# z automatu ascending ustawione jest na True. jak zmienimy mamy sortowanie malejące



print("""\n unikalne wartosci zmiennej ilosciowej value_counts()\n""")
print(df_8.head())
df5 = df_8['Iris-setosa'].value_counts()
print(df5)

#Iris-setosa ->nazwa kolumny po kotorej zliczamy
#Iris-versicolor    50
#Iris-virginica     49
#Iris-setosa        47
#Name: count, dtype: int64


print("""\n unikalne wartosci zmiennej ilosciowej value_counts(normalize=True) udzial procentowy\n""")
print(df_8.head())
df5 = df_8['Iris-setosa'].value_counts(normalize=True)
print(df5)

#Iris-setosa
#Iris-versicolor    0.342466
#Iris-virginica     0.335616
#Iris-setosa        0.321918
#Name: proportion, dtype: float64












