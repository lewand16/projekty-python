# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:51:39 2016

@author: Liberator
"""

import numpy as np
import math as m

#przyblizona wartosc funkcji silnia moze byc otrzymana za pomoca formuly Stirlinga:
def silnia(n):
    return np.sqrt(2 * np.pi * n) * ((n / np.e)**n)

#dana wejsciowa
n = 11
print('silnia z', n, 'z funkcji Stirlinga =', silnia(n))
print('silnia z', n, 'z wbudowanej funkcji =', m.factorial(n))
