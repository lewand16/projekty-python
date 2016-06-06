# -*- coding: utf-8 -*-
"""
Created on Sat May 28 19:18:24 2016

@author: Liberator
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

#zbuduj wektory zawierajace wspolrzedne czterech punktow na plaszczyznie
x = np.arange(1, 61, 15)
y = 10 * npr.rand(4) - 5

#dopasuj na nich funkcje liniowa polyfit(os x, os y, potega wielomianu)
xg = np.arange(1, 61, 1)
p1 = np.polyfit(x, y, 1)
prosta = np.polyval(p1, xg)

#dopasuj na nich funkcje kwadratowa
p2 = np.polyfit(x, y, 2)
kwadratowa = np.polyval(p2, xg)

#narysuj te funkcje i punkty na wykresie
plt.plot(x, y, 'o')
plt.plot(xg, prosta)
plt.plot(xg, kwadratowa)
plt.show()