# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:26:07 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt

#utworz wektor o wartosciach od 0 do 100 z krokiem co 5
x = np.arange(0, 101, 5)
print(x)

#utworz wektor y, ktory zawiera wartosci exp(-x^2)
y = np.exp(-x**2)
print(y)

#wykresl te punkty uzywajac funkcji plot
plt.plot(x, y)
plt.show()