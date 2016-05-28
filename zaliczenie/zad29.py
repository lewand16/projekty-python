# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:27:46 2016

@author: Liberator
"""
import numpy as np
import matplotlib.pyplot as plt

#oblicz wartosc wielomianu 3x^3 + 4x^2 + 2x
wielomian = [3, 4, 2, 0]

#dla:
x1 = 6
x2 = 8

#obliczenie wartosci wielomianow w punktach x1 i x2
w1 = np.polyval(wielomian, x1)
w2 = np.polyval(wielomian, x2)

#tworzenie osi x w zakresie szukanych punktow
x = np.linspace(0, 10, 101)

#wyliczenie wielomianu dla calej osi x
y = np.polyval(wielomian, x)

plt.plot(x, y, '-b')
plt.plot(x1, w1, 'ok')
plt.plot(x2, w2, 'ok')
plt.show()