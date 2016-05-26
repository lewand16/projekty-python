# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:44:13 2016

@author: Liberator
"""

import numpy as np
import numpy.random as npr

macierz = npr.rand(3, 5)
print(macierz)

macierz = np.delete(macierz, 2, 0)
print(macierz)