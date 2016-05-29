# -*- coding: utf-8 -*-
"""
Created on Sun May 29 21:11:27 2016

@author: Liberator
"""

import numpy as np

#tworzenie tablicy
x = np.arange(0, 10)
print(x)
print()
#pierwsza proba kopiowania
y1 = x
print(y1,'y1 = x')

#zmiana pierwszej komorki pierwszej tablicy dla sprawdzenia
x[0] = 20
print(x)
print(y1,'zmiana x wplynela na y1')
print()
#druga proba kopiowania
x = np.arange(0, 10)
y2 = x[:]
print(y2)
#zmiana pierwszej komorki pierwszej tablicy dla sprawdzenia
x[0] = 21
print(x)
print(y2,'zmiana x wplynela na y2')
print()
#trzecia proba kopiowania
x = np.arange(0, 10)
y3 = []
i = 0
for i in range(len(x)):
    y3 = np.append(y3, x[i])
print(y3)
#zmiana pierwszej komorki pierwszej tablicy dla sprawdzenia
x[0] = 22
print(x)
print(y3,'zmiana x nie wplynela na y3')