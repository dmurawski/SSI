import pandas as pd

class DataLoader:
    def __init__(self, plik_probki, plik_atrybuty):
        self.plik_probki = plik_probki
        self.plik_atrybuty = plik_atrybuty
        self.dane_probek = None
        self.informacje_atrybuty = None

    def wczytaj_dane(self):
        self.informacje_atrybuty = pd.read_csv(self.plik_atrybuty, delim_whitespace=True,header=None)
        col_name=self.column_name(0)
        self.dane_probek = pd.read_csv(self.plik_probki, delim_whitespace=True,header=None,names=col_name)

    def print_dane(self):
        return self.dane_probek

    def print_dane_type(self):
        return self.informacje_atrybuty

    def column_name(self,x):
        return self.informacje_atrybuty.iloc[:, x]

    def dane_tablica(self,x,y):
        return self.dane_probek.iloc[x,y]

# Przykład użycia klasy
data = DataLoader("iris", "iris_type")
data.wczytaj_dane()
print(data.print_dane())
print(data.dane_tablica(0,0))