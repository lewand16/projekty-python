# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:12:22 2016

@author: Liberator
"""

import numpy.random as npr

komorka1 = 7
komorka2 = 12

#tworzenie macierzy, najpierw z losowymi wartosciami
macierz = npr.randint(1, size = (2, 4))

j = 0
#podmiana komorek macierzy na zadane wartosci
for j in range(4):
    macierz[0][j] = komorka1
    komorka1 = komorka1 + 1
    macierz[1][j] = komorka2 
    komorka2 = komorka2 - 2

#a) element w pierwszym wierszu i trzeciej kolumnie 
print(macierz[0][2])
print()
j = 0
#b) wszystkie elementy drugiego wiersza (wyswietla sie obok siebie)
for j in range(4):
    print(macierz[1][j], end = ', ') 
print('\n')
   
j = 0
k = 0
#c) pierwsze dwie kolumny
for j in range(2):
    for k in range(2):
        print(macierz[j][k], end = ', ')
    print() 
print()