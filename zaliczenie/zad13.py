# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:46:24 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt
# coś jest źle. Jak zrobić 2**x ?
#a)
x = np.linspace(0, np.pi, 10)
w1 = [2, 1, -2, 0]

y = np.polyval(w1, x)

plt.plot(x, y)
#b)
x = np.linspace(0, np.pi, 100)
w1 = [2, 1, -2, 0]

y = np.polyval(w1, x)

plt.plot(x, y)