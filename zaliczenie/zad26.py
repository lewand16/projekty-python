# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:55:11 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

#zbuduj wektor x zawierajacy liczby calkowite od 1 do 10
x = np.arange(1, 11, 1)

#trzeba robić kopię! Nie wolno użyć np. y = x[:], bo wtedy zmieniając oryginał zmieniamy też kopię!
def kopia(wektorStary, wektorNowy):
    i = 0    
    for i in range(len(wektorStary)):
        wektorNowy = np.append(wektorNowy, wektorStary[i])
    return wektorNowy

#zbuduj wektor y rowny x  
y = []
y = kopia(x, y)

#narysuj te linie prosta
plt.plot(x, y)
plt.show()

#generator szumow :)
def szumy(wektor):
    i = 0
    for i in range(len(wektor)):
        wektor[i] = wektor[i] + (npr.randint(-25, high=25) / 100)
    return wektor

#dodaj szum do danych budujac wektor y2, przechowujacy wartosci y-0.25<y<y+0.25
y2 = []
y2 = kopia(y, y2)
y2 = szumy(y2)
print(x, '\n', y, '\n', y2)

#narysuj prosta i te punkty
plt.plot(x, y, '-b', x, y2, 'o')
plt.show()