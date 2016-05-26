# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:03:27 2016

@author: Liberator
"""
import numpy as np

Rz = 2
Rw = 1

V = (4 * np.pi * ((Rz ** 3) - (Rw ** 3))) / 3
print(V)