# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:05:03 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt

#oblicz pierwiastek z 17
print(np.sqrt(17))

#oblicz 3 do potegi 1.3
print(3**1.3)

#oblicz tangens z pi
print(np.tan(np.pi))

#przedzial wykresu -5 do 5
x = np.linspace(-5, 5, 101)

#funkcja pierwiastek z x
plt.plot(x, np.sqrt(x))
plt.show()

#funkcja 3 do potegi x
plt.plot(x, 3**x)
plt.show()

#funkcja tangens x
plt.plot(x, np.tan(x))
plt.show()