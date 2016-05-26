# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:56:16 2016

@author: Liberator
"""

import numpy as np

def trzeciBok(b, c, alpha):
    a = np.sqrt(b**2 + c**2 - 2 * b * c * np.cos(alpha))
    return a

b = 2
c = 2
alpha = 30 * np.pi / 180   #zamiana stopni na radiany

print(trzeciBok(b, c, alpha))