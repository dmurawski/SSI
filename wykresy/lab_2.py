import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
import pandas as pd
#from lab_1 import DataLoader

def wykres_czysc():
    plt.cla()

def wykres_punkty_rysuj(x, y, size):
    plt.scatter(x, y, s=size)

def wykres_linia_rysuj(xpoints,ypoints):
   plt.plot(xpoints, ypoints)

def zadanie3():
    fig, axes = plt.subplots()

    cc = plt.Circle((0.5, 0.5), 0.4, fill=False, color='r', linewidth=3)
    axes.set_aspect(1)
    axes.add_patch(cc)

    x = np.array([0.3, 0.7, 0.5])
    y = np.array([0.65, 0.65, 0.45])
    plt.scatter(x, y, s=100)

    axes.add_patch(Arc((0.5, 0.5), 0.5, 0.5, theta1=215, theta2=325, edgecolor='y', linewidth=5))
    plt.show()

def zadanie4(data):
    klasa1 = data[data[4] == 1]
    klasa2 = data[data[4] == 2]
    klasa3 = data[data[4] == 3]

    # Tworzenie wykresu z 4 przestrzeniami
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    # Na pierwszej przestrzeni osią x są wartości atrybutu 3-go próbek, a osią y są wartości atrybutu 4-tego (licząc od 1, nie od 0)
    axs[0, 0].scatter(klasa1[2], klasa1[3], label='Setosa', c='red', marker='o')
    axs[0, 0].scatter(klasa2[2], klasa2[3], label='Versicolour', c='blue', marker='o')
    axs[0, 0].scatter(klasa3[2], klasa3[3], label='Virginica', c='green', marker='o')
    axs[0, 0].set_xlabel('petal_length_in_cm')
    axs[0, 0].set_ylabel('petal_width_in_cm')
    axs[0, 0].legend(loc='upper right')
    # # Na drugiej przestrzeni osią x są wartości atrybutu 2-go próbek, a osią y są wartości atrybutu 4-go. 
    axs[0, 1].scatter(klasa1[1], klasa1[3], label='Setosa', c='red', marker='o')
    axs[0, 1].scatter(klasa2[1], klasa2[3], label='Versicolour', c='blue', marker='o')
    axs[0, 1].scatter(klasa3[1], klasa3[3], label='Virginica', c='green', marker='o')
    axs[0, 1].set_xlabel('sepal_width_in_cm')
    axs[0, 1].set_ylabel('petal_width_in_cm')
    axs[0, 1].legend(loc='upper right')
    # # Na trzeciej przestrzeni osią x są wartości atrybutu 1-go próbek, a osią y są wartości atrybutu 4-go.
    axs[1, 0].scatter(klasa1[0], klasa1[3], label='Setosa', c='red', marker='o')
    axs[1, 0].scatter(klasa2[0], klasa2[3], label='Versicolour', c='blue', marker='o')
    axs[1, 0].scatter(klasa3[0], klasa3[3], label='Virginica', c='green', marker='o') 
    axs[1, 0].set_xlabel('sepal_length_in_cm')
    axs[1, 0].set_ylabel('petal_width_in_cm')
    axs[1, 0].legend(loc='upper right')
    # #Na czwartej przestrzeni osią x są wartości atrybutu 2-go próbek, a osią y są wartości atrybutu 3-go. 
    axs[1, 1].scatter(klasa1[1], klasa1[2], label='Setosa', c='red', marker='o')
    axs[1, 1].scatter(klasa2[1], klasa2[2], label='Versicolour', c='blue', marker='o')
    axs[1, 1].scatter(klasa3[1], klasa3[2], label='Virginica', c='green', marker='o')
    axs[1, 1].set_xlabel('sepal_width_in_cm')
    axs[1, 1].set_ylabel('petal_length_in_cm')
    axs[1, 1].legend(loc='upper right')

    axs[0, 0].set_title('Atrybut 3 vs. Atrybut 4')
    axs[0, 1].set_title('Atrybut 2 vs. Atrybut 4')
    axs[1, 0].set_title('Atrybut 1 vs. Atrybut 4')
    axs[1, 1].set_title('Atrybut 2 vs. Atrybut 3')

    
    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    wykres_linia_rysuj(xpoints,ypoints)
    plt.show()
    wykres_czysc()
    zadanie3()
    data = pd.read_csv("iris", delim_whitespace=True,header=None)
    zadanie4(data)

   