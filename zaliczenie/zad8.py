# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:25:25 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt

#utworz wektor x skladajacy sie z 21 rownoodleglych punktow z zakresu -pi do pi
x = np.linspace(-np.pi, np.pi, 21)

#oblicz y = x^2 - 4x + 3
y = [2, -4, 3]
rozw = np.polyval(y, x)

#sporzadz odpowiedni wykres
plt.plot(x, rozw)
plt.show()
