# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:25:25 2016

@author: Liberator
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 21)

y = [2, -4, 3]
rozw = np.polyval(y, x)

plt.plot(x, rozw)
plt.show()
