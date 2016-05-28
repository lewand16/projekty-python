# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:25:46 2016

@author: Liberator
"""

#napisz funkcje geomsum, ktora pobiera wartosci r oraz n i oblicza sume szeregu geometrycznego
# 1 + r + r^2 + r^3 + r^4 + ... + r^n
def geomsum(r, n):
    suma = 1
    i = 1
    while (i <= n):
        suma = suma + (r**i)
        i= i + 1
    return suma

#dane wejsciowe
r = 1
n = 10
print(geomsum(r, n))