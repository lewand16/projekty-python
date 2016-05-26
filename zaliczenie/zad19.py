# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:47:11 2016

@author: Liberator
"""

import numpy as np

def wektormn(m, n):
    if (m < n):
        wektor = np.arange(m, n, 1)
    elif(m > n):
        wektor = np.arange(n, m, 1)
    else:
        wektor = [m]
    return wektor

print(wektormn(1, 1))