# -*- coding: utf-8 -*-
"""
Created on Wed May 25 20:25:06 2016

@author: Liberator
"""

import numpy.random as npr

#utworz macierz 4x2 zawierajaca zera i przypisz ja do zmiennej
macierz = npr.randint(1, size = (4, 2))
print(macierz)
print()

#zastap jej drugi wiersz przez 3 i 6
i = 0
for i in range(2):
   macierz[1][i] = macierz[1][i - 1] + 3
   
print(macierz)