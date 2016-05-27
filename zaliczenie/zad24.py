# -*- coding: utf-8 -*-
"""
Created on Fri May 27 20:08:40 2016

@author: Liberator
"""

import numpy as np
import numpy.random as npr

wektor = npr.randint(-10, 10, 5)

print(wektor)

#a) odejmij 3 od kazdego elementu
def odejmij_3(wek):
    i = 0    
    for i in range(len(wek)):
        wek[i] = wek[i] - 3
    return wek
    
print('Wektor po odjeciu 3 od kazdego elementu:', odejmij_3(wektor))

#b) oblicz ile elementow jest dodatnich
def ileDodatnich(wek):
    i = 0
    licznik = 0
    for i in range(len(wek)):
        if (wek[i] >= 0):
            licznik = licznik + 1
    return licznik
    
print('Dodatnich liczb jest:', ileDodatnich(wektor))

#c) oblicz modul kazdego elementu
def modul(wek):
    i = 0
    for i in range(len(wek)):
        if (wek[i] < 0):
            wek[i] = wek[i] * (-1)
    return wek
    
print('Moduly elementow wektora:', modul(wektor))

#d) znajdz element maksymalny
def elementMax(wek):
    i = 0
    maks = -99
    for i in range(len(wek)):
        if (wek[i] > maks):
            maks = wek[i]
    return maks
    
print('Element maksymalny:', elementMax(wektor))