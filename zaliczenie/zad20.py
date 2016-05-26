# -*- coding: utf-8 -*-
"""
Created on Thu May 26 19:04:32 2016

@author: Liberator
"""

import numpy.random as npr
    
def czyParzysta(x):
    if (x % 2 == 0):
        return 'parzysta'
    else:
        return 'nieparzysta'
        
zakres = 100
x = npr.randint(0, zakres)

print(x, czyParzysta(x))