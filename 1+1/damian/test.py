import pandas as pd
import matplotlib.pyplot as plt
from lab_1 import wczytaj_dane_iris


plik_probek = "iris.txt"
plik_typy = "iris_type.txt"

plik_probek = "iris.txt"
plik_typy = "iris_type.txt"

data = wczytaj_dane_iris(plik_probek, plik_typy)
print(data)

