# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:51:39 2016

@author: Liberator
"""

import numpy as np

def silnia(n):
    return np.sqrt(2 * np.pi * n) * ((n / np.e)**n)

n = 3
print(silnia(n))
