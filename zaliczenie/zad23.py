# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:39:05 2016

@author: Liberator
"""
import numpy.random as npr
import numpy as np

n = 4
m = 4
macierz = npr.randint(10,size=(n, m))

print(macierz)
#wbudowana funkcja liczaca srednia
print(np.mean(macierz))

#stworzona funkcja liczaca srednia
def sredniaMacierzy(n, m, mac):
    wiersz = 0
    kolumna = 0
    srednia = 0
    for wiersz in range(n):
        for kolumna in range(m):
            srednia = srednia + mac[wiersz][kolumna]
    return srednia / (n * m)
    
print(sredniaMacierzy(n, m, macierz))