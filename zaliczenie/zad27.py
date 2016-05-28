# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:38:19 2016

@author: Liberator
"""
import numpy.linalg as npl

#rozwaz uklad rownan:
#        4x1 - x2 + 3x4 = 10
# -2x1 + 3x2 + x3 - 5x4 = -3
#    x1 + x2 - x3 + 2x4 = 2
#       3x1 + 2x2 - 4x3 = 4
macierz = [[4, -1, 0, 3], [-2, 3, 1, -5], [1, 1, -1, 2], [3, 2, -4, 0]]

wektor = [10, -3, 2, 4]

wynik = npl.solve(macierz, wektor)

#wynik jest tablica, wiec kazda kolejna wartosc jest kolejnym x
print(' x1 =', wynik[0], '\n', 'x2 =', wynik[1], '\n', 'x3 =', wynik[2], '\n', 'x4 =', wynik[3])