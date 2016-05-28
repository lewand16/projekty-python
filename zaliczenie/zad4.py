# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:38:50 2016

@author: Liberator
"""

import numpy.random as npr

#a) liczba rzeczywista z przedzialu (0, 1)
print(npr.rand())

#b) liczba rzeczywista z przedzialu (0, 20)
print(20 * npr.rand())

#c) liczba rzeczywista z przedzialu (20, 50)
print(30 * npr.rand() + 20)

#d) liczba calkowita z przedzialu (0, 10)
print(npr.randint(0, 11))

#e) liczba calkowita z przedzialu (0, 11)
print(npr.randint(0, 12))

#f) liczba calkowita z przedzialu (50, 150)
print(npr.randint(50, 101))