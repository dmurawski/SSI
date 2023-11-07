import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np


def k_means(dane, v, iters):
    # 1. Wybierz losowo m różnych próbek i uznaj je jako środki grup (V)
    centra = random.sample(dane, v)
    
    #wykres przed wykonaniem algorytmu
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    data_wykres = np.array(dane)
    axes[0].scatter(data_wykres[:, 0], data_wykres[:, 1], label='Dane', c='blue')
    centers_f = np.array(centra)
    axes[0].scatter(centers_f[:, 0], centers_f[:, 1], label='Środki grup', c='red', marker='X',s=100)
    axes[0].legend()
    axes[0].set_title('Dane przed k-means')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')

    for i in range(iters):
        # Inicjalizacja listy grup
        grupy = []
        for element in range(v):
            grupy.append([])

        # 2.1. Pętla po wszystkich M próbkach, s to indeks aktualnej próbki
        for s in range(len(dane)):
            sample = dane[s]

            # Inicjalizacja listy odległości dla danej próbki
            distances = []

            # 2.1.1. Wylicz odległości między próbką s a każdym środkiem grupy (V)
            for center in centra:
                distance = np.linalg.norm(np.array(sample) - np.array(center))
                distances.append(distance)

            # 2.1.2. Wyznacz us równy indeksowi najbliższego środka grupy dla s-tej próbki
            us = np.argmin(distances)

            # Dodaj próbkę do odpowiedniej grupy
            grupy[us].append(sample)

        # 2.2. Pętla po wszystkich m grupach, j to indeks aktualnej grupy
        for j in range(v):
            # 2.2.2. Jeśli zbiór Xgr jest pusty, pomiń wykonanie dalszej części tej pętli
            if len(grupy[j]) == 0:
                continue

            # 2.2.3. Pętla po wszystkich atrybutach, i to index poszczególnego atrybutu
            for i in range(len(dane[0])):
                # 2.2.3.1 Wartość i-tego atrybutu grupy j-tej to średnia wartość atrybutu i-tego wszystkich próbek Xgr
                grupa_wartosc = [sample[i] for sample in grupy[j]]
                centra[j][i] = np.mean(grupa_wartosc)

    #wykres po wykonaniu algorytmu
    for j in range(v):
        grupa = np.array(grupy[j])
        axes[1].scatter(grupa[:, 0], grupa[:, 1], label=f'Grupa {j + 1}')

    center_array = np.array(centra)
    axes[1].scatter(center_array[:, 0], center_array[:, 1], marker='X', color='red', label='Centra grup',s=100)
    axes[1].legend()
    axes[1].set_title(f'Wyniki k-means po {iters} iteracji')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')
    plt.show()

    return centra, grupy

if __name__ == "__main__":
    data = pd.read_csv("spirala.txt", delim_whitespace=True,header=None)
    data_type = pd.read_csv("spirala_type.txt", delim_whitespace=True,header=None)
    data_values = data.values.tolist()
    v = 3
    iters = 100
    centers, grupy = k_means(data_values, v, iters)
    