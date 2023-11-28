import numpy as np
import math
from scipy.spatial import distance

wzorzec_1 = np.array([
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]])

wzorzec_2 = np.array([
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1]])

wzorzec_3 = np.array([
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0]])


test_1 = np.array([
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 1]])

test_2 = np.array([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1]])

test_3 = np.array([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 1]])

def euclidean_distance(a,b):
    return distance.euclidean(a, b)
    
def macierz_do_lista_punktow(macierz):
    lista_punktow = []
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] == 1:
                lista_punktow.append((i, j))
    return lista_punktow

def miara_niepodobienstwa(bitmapa_a, bitmapa_b):
    miara = 0
    for (pay, pax) in bitmapa_a:
        odl_min = math.inf
        for (pby, pbx) in bitmapa_b:
            odl_akt = euclidean_distance((pay, pax), (pby, pbx))
            odl_min = min(odl_min, odl_akt)
        miara += odl_min
    return miara
            
def miara_podobienstwa_obustronnego_euklidesa(bitmapa_a, bitmapa_b):
    return -(miara_niepodobienstwa(bitmapa_a, bitmapa_b) + miara_niepodobienstwa(bitmapa_b, bitmapa_a))

# Konwersja macierzy na listy punktów samych czarnych
bitmapa_wzorzec_1 = macierz_do_lista_punktow(wzorzec_1)
bitmapa_test_1 = macierz_do_lista_punktow(test_1)

bitmapa_wzorzec_2 = macierz_do_lista_punktow(wzorzec_2)
bitmapa_test_2 = macierz_do_lista_punktow(test_2)

bitmapa_wzorzec_3 = macierz_do_lista_punktow(wzorzec_3)
bitmapa_test_3 = macierz_do_lista_punktow(test_3)

#Wzorzec od 1 do 3 i test_1
print(f"Test1\nWynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_1 i test_1: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_1, bitmapa_test_1)}")
print(f"Wynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_2 i test_1: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_2, bitmapa_test_1)}")
print(f"Wynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_3 i test_1: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_3, bitmapa_test_1)}\n")
print(f'Do bitmapy test_1 najbardziej podobna jest bitmapa wzorzec_1\n')
#Wzorzec od 1 do 3 i test_2
print(f"Test2\nWynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_1 i test_2: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_1, bitmapa_test_2)}")
print(f"Wynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_2 i test_2: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_2, bitmapa_test_2)}")
print(f"Wynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_3 i test_2: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_3, bitmapa_test_2)}\n")
print(f'Do bitmapy test_2 najbardziej podobna jest bitmapa wzorzec_3\n')
#Wzorzec od 1 do 3 i test_3
print(f"Test3\nWynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_1 i test_3: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_1, bitmapa_test_3)}")
print(f"Wynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_2 i test_3: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_2, bitmapa_test_3)}")
print(f"Wynik miary podobieństwa obustronnego miedzy dwoma bitmapami wzorzec_3 i test_3: {miara_podobienstwa_obustronnego_euklidesa(bitmapa_wzorzec_3, bitmapa_test_3)}\n")
print(f'Do bitmapy test_3 najbardziej podobna jest bitmapa wzorzec_2')

     