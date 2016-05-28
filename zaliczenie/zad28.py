# -*- coding: utf-8 -*-
"""
Created on Sat May 28 14:38:22 2016

@author: Liberator
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#tworzenie wektora x w zakresie od -3 do 3
x = np.linspace(-3, 3, 101)
#tworzenie wektora y = 0, by znalezc przyblizone pierwiastki
y0 = 0 * x

#zadana funkcja
def f(x):
    return (3 * (x**2)) - (2 * x) - 5

#rysowanie funkcji i obu wektorow 
plt.plot(x, f(x), x, y0)
plt.show()

#wyswietlenie pierwiastkow
#moze tez byc np. x1 zamiast x1[0], ale wtedy wyswietli wynik w nawiasach [ ]
x1 = fsolve(f, -0.9)
print('Pierwsze miejsce zerowe =', x1[0])
x2 = fsolve(f, 1.5)
print('Drugie miejsce zerowe =', x2[0])