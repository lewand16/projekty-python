# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:26:07 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 101, 5)
print(x)

y = np.exp(-x**2)
print(y)

plt.plot(x, y)