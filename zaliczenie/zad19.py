# -*- coding: utf-8 -*-
"""
Created on Thu May 26 18:47:11 2016

@author: Liberator
"""

import numpy as np

#napisz funkcje wektormn, tworzaca wektor liczb calkowitych od m do n niezaleznie od tego,
#ktory z tych parametrow jest wiekszy. Jezeli m = n, to wektor bedzie mial 1 element
def wektormn(m, n):
    if (m < n):
        wektor = np.arange(m, n + 1, 1)
    elif(m > n):
        wektor = np.arange(n, m + 1, 1)
    else:
        wektor = [m]
    return wektor

#dane wejsciowe
m = 1
n = 3
print(wektormn(m, n))