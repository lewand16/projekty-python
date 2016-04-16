# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 08:25:04 2016

@author: Liberator
"""

from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.25, 1.25, 101)
y0 = 0 * x
def f1(x):
    return np.sqrt(np.sin(x) * np.sin(x) + abs(x)) - x**2
    
def f2(x):
    return (x - 1) * (np.exp(2 * x) - (2 * np.exp(x)))
    

plt.plot(x, f1(x), x, f2(x), x, y0)

x1 = fsolve(f1, -1.5)
print(x1)
x1 = fsolve(f1, -0.5)
print(x1)
x1 = fsolve(f1, 1)
print(x1)

x2 = fsolve(f2, 0.6)
print(x2)
x2 = fsolve(f2, 0.9)
print(x2)

def f12(x):
    return f2(x) - f1(x)

x12 = fsolve(f12, 1)
print(x12)
x12 = fsolve(f12, 0.4)
print(x12)
