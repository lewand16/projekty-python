# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:46:24 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt

#wykresl funkcje 2^x - (2x - x^2)
#a) uzyj 10 punktow z zakresu
x = np.linspace(0, np.pi, 10)
y = 2**x - ((2 * x) - x**2)

plt.plot(x, y)
plt.show()

#b) uzyj 100 punktow z zakresu
x = np.linspace(0, np.pi, 100)
y = 2**x - ((2 * x) - x**2)

plt.plot(x, y)
plt.show()