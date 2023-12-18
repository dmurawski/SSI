import numpy as np
import matplotlib.pyplot as plt
import random


def funkcja_przystostowania(x):
    if np.all((0 <= x) & (x <= 100)):
        return np.sin(x/10)*np.sin(x/200)
    else:
        print("x musi być z przedziału [0; 100]")

def algorytm_1_1(rozrzut, wsp_przyrostu, l_iteracji, zakres_zmiennosci):
    x = random.uniform(0, zakres_zmiennosci)
    y = funkcja_przystostowania(x)

    x_wykres = [x]
    y_wykres = [y]

    for i in range(l_iteracji):
        xp = x + random.uniform(-rozrzut, rozrzut)

        while xp < 0 or xp > zakres_zmiennosci:
            xp = x + random.uniform(-rozrzut, rozrzut)

        yp = funkcja_przystostowania(xp)

        if yp >= y:
            x = xp
            y = yp
            rozrzut *= wsp_przyrostu
        else:
            x = xp
            y = yp
            rozrzut /= wsp_przyrostu

        x_wykres.append(x)
        y_wykres.append(y)
    

        print(f"Iteracja {i + 1}: x = {x}, y = {y}, rozrzut = {rozrzut}")

    x_range = np.linspace(0, zakres_zmiennosci, 100)
    y_range = funkcja_przystostowania(x_range)
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_range, label='Funkcja przystosowania')
    plt.scatter(x_wykres, y_wykres, marker='.', color='red', label='Punkty iteracji')
    plt.scatter(x_wykres[-1], y_wykres[-1], marker='.', color='yellow', label='Ostatni punkt iteracji',linewidths=10)
    plt.legend()
    plt.show()

algorytm_1_1(10, 1.1, 100, 100)
