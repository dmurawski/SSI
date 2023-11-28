import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
import pandas as pd

def wykres_czysc(name):
    name.cla()


def wykres_punkty_rysuj(x, y, size):
    plt.scatter(x, y, s=size)


def wykres_linie_rysuj(x, y):
    plt.plot(x, y)


def zadanie3():
    #kółko
    figure, axes = plt.subplots()
    cc = plt.Circle((0.5, 0.5), 0.4, fill=False, color='r', linewidth=3)
    axes.set_aspect(1)
    axes.add_patch(cc)
    #kropki
    x = np.array([0.3, 0.7, 0.5])
    y = np.array([0.65, 0.65, 0.50])
    plt.scatter(x, y, s=100, marker="D")
    #krzywa
    axes.add_patch(Arc((0.5, 0.5), 0.5, 0.5,
                     theta1=205, theta2=335, edgecolor='y', linewidth=5))
    plt.grid()
    plt.show()

def zadanie4():
    data = pd.read_csv('iris', delimiter='\t',header=None)
    print(data.head(10))
#     df = pd.DataFrame(data,columns=['sepal_length_in_cm', 'sepal_width_in_cm',
# 'petal_length_in_cm','petal_width_in_cm	','class'])
    print(data.head(10))
    print(data.query(data.columns[4]==2))

if __name__ == '__main__':
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])

    #plt.plot(xpoints, ypoints)
    #plt.show()
    #wykres_czysc(plt)
   #plt.show()
    wykres_linie_rysuj([0, 0], [0, 250])
    zadanie3()
   # wykres_punkty_rysuj([1,2,3,4,5],[2,3,4,5,6],20)
   #plt.show()
    zadanie4()