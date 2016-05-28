# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:30:05 2016

@author: Liberator
"""

import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt

#wygeneruj losowo liczbe calkowita n
n = npr.randint(20)
print('Wylosowana liczba:', n)

#zbuduj wektor liczb calkowitych od 1 do n z krokiem 2.
wektor = np.arange(1, n + 1, 2.)
print('Otrzymany wektor', wektor)

#podnies kazdy element tego wektora do kwadratu
wektor2 = wektor**2
print('Elementy wektora do kwadratu', wektor2)

# co to znaczy wykresl kwadraty? Usun czy narysuj? :)
# przyjmuje, ze chodzi o narysowanie ;]
plt.plot(wektor, wektor2)
plt.show()