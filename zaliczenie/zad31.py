# -*- coding: utf-8 -*-
"""
Created on Sat May 28 19:18:24 2016

@author: Liberator
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

#zbuduj wektory zawierajace wspolrzedne czterech punktow na plaszczyznie
x = np.arange(1, 5, 1)
y = 10 * npr.rand(4) - 5

#dopasuj na nich funkcje liniowa polyfit(os x, os y, potega wielomianu)
y1 = np.polyfit(x, y, 1)
prosta = np.poly1d(y1)

#dopasuj na nich funkcje kwadratowa
y2 = np.polyfit(x, y, 2)
kwadratowa = np.poly1d(y2)

#narysuj te funkcje i punkty na wykresie
plt.plot(x, y, 'o')
plt.plot(x, prosta(x))
plt.plot(x, kwadratowa(x))
plt.show()