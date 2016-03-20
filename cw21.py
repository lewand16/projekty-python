# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:28:26 2016

@author: Liberator
"""
import numpy as np
import matplotlib.pyplot as plt

# (a) buduje liste kodujaca wielomian
w1 = [2, 4, 0, 1, 7]

# (b) oblicza wartosc wielomianu w punkcie x = 3
a = 3
b = np.polyval(w1, a)
print(b)
# (c) wyswietla wykres z tego wielomianu z zaznaczonym punktem (3, w(3))

x = np.linspace(-4, 4, 101)
y = np.polyval(w1, x)

plt.plot(x, y, '-b')
plt.plot(a, b, 'ok')