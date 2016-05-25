# -*- coding: utf-8 -*-
"""
Created on Wed May 25 20:25:06 2016

@author: Liberator
"""

import numpy.random as npr

macierz = npr.randint(1, size = (4, 2))
i = 0
for i in range(2):
   macierz[1][i] = macierz[1][i - 1] + 3
   
print(macierz)