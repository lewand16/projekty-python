# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:05:03 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt

print(np.sqrt(17))

print(3**1.3)

print(np.tan(np.pi))


x = np.linspace(-5, 5, 101)

plt.plot(x, np.sqrt(x))
plt.show()

plt.plot(x, 3**x)
plt.show()

plt.plot(x, np.tan(x))
plt.show()