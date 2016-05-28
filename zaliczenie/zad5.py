# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:01:06 2016

@author: Liberator
"""
import numpy as np

#punkty stworzone na kilka sposobow do wyboru!

#a) utworz wektor 3 4 5 6
print('a1', np.linspace(3, 6, 4)) #da zawsze zmiennoprzecinkowe, wiec opcja druga
print('a2', np.arange(3, 7, 1))

#b) utworz wektor 1.0000 1.5000 2.0000 2.5000 3.0000
print('b1', np.linspace(1, 3, 5))
print('b2', np.arange(1, 3.5, 0.5))

#c) utworz wektor 5 4 3 2
#metoda 1
print('c1', np.arange(2, 6, 1)[::-1])
#powyższe korzysta z klasy slice[start : stop : krok]
#inaczej trzeba wykorzystać funkcję odwracającą ponizej

#metoda 2. Najpierw tworzymy wektor rosnacy, a potem odwracamy go
s = np.arange(2, 6, 1)
i = 0
k = (len(s) / 2)

for i in range(len(s)):
    if (i < k):
        pom = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = pom
    
print('c2', s)

#metoda 3: tworzymy pusta tablice i wstawiamy liczby we wlasciwej kolejnosci
s2 = []
i = 5
while (i >= 2):
    s2 = np.append(s2, i)
    i = i - 1
    
print('c3', s2)