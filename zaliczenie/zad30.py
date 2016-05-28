# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:45:41 2016

@author: Liberator
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

#zbuduj wektor x zawierajacy liczby calkowite od 1 do 20
x = np.arange(1, 21, 1)

#zbuduj wektor y zawierajacy liczby losowe z zakresu -2 do 2
y = 4 * npr.rand(20) - 2

#dopasuj linie prosta do tych danych
y1 = np.polyfit(x, y, 1)
p = np.poly1d(y1)  #splaszczenie otrzymanego wielomianu

#narysuj dane i te linie na jednym wykresie
plt.plot(x, p(x))
plt.plot(x, y, 'o')
plt.show()
