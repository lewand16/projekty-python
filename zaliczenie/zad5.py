# -*- coding: utf-8 -*-
"""
Created on Mon May 23 22:01:06 2016

@author: Liberator
"""
import numpy as np

print(np.linspace(3, 6, 4)) #da zawsze zmiennoprzecinkowe
print(np.arange(3, 7, 1))

print(np.linspace(1, 3, 5))
print(np.arange(1, 3.5, 0.5))

print(np.arange(2, 6, 1)[::-1])
#powyższe korzysta z klasy slice[start : stop : krok]
#inaczej trzeba wykorzystać funkcję odwracającą

s = np.arange(2, 6, 1)
i = 0
k = (len(s) / 2)

for i in range(len(s)):
    if (i < k):
        pom = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = pom
    
print(s)