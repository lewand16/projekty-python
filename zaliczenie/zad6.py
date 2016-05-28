# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:12:22 2016

@author: Liberator
"""

import numpy.random as npr

komorka1 = 7
komorka2 = 12

#tworzenie macierzy, najpierw z losowymi wartosciami od 0 do 1-1
macierz = npr.randint(1, size = (2, 4))

j = 0
#podmiana komorek macierzy na zadane wartosci
for j in range(4):
    #wstaw w pierwszym wierszu 7 8 9 10
    macierz[0][j] = komorka1
    komorka1 = komorka1 + 1
    #wstaw w drugim wierszu 12 10 8 6
    macierz[1][j] = komorka2 
    komorka2 = komorka2 - 2

#a) wyswietl element w pierwszym wierszu i trzeciej kolumnie 
print(macierz[0][2])
print()
j = 0
#b) wyswietl wszystkie elementy drugiego wiersza (wyswietla sie obok siebie)
for j in range(4):
    print(macierz[1][j], end = ', ') #liczby wyswietla sie obok siebie po przecinku zamiast jedna pod druga
print('\n')
   
j = 0
k = 0
#c) pierwsze dwie kolumny
for j in range(2):
    for k in range(2):
        print(macierz[j][k], end = ', ')
    print() 
print()