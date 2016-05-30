# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:52:19 2016

@author: Liberator
"""

import numpy as np

#napisz funkcje hipsin argumentu x z definicji sinusa hiperbolicznego(x)
def hipsin(x):
    return ((np.e**x) - (np.e**(-x))) / 2

#dana wejsciowa
x = 5
print(hipsin(x))