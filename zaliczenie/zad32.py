# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:08:05 2016

@author: Liberator
"""
import numpy as np
import matplotlib.pyplot as plt

#formula opisujaca ewolucje populacji USA
def ewolucjaPopulacji(rok):
    potega = -0.03137 * (rok - 1913.25)
    P = 19727300 / (1 + (np.e**potega))
    return P

#zakres lat miedzy 1790 a 2000, co 10 lat
x = np.arange(1790, 2000, 10)

#wyznaczenie populacji w kazdej dacie
y = ewolucjaPopulacji(x)

#narysowanie wykresu
plt.plot(x, y)
plt.show()
