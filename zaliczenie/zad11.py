# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:18:19 2016

@author: Liberator
"""

import matplotlib.pyplot as plt
import numpy.random as npr
import numpy as np

#napisz skrypt, ktory przypisuje wartosci wspolrzednym x i y kilku punktow
x = np.linspace(0, 10, 31)
y = npr.rand(31)

#zaznacz te punkty na plaszczyznie xy niebieskimi plusami
plt.plot(x, y, '+b')
plt.show()