# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:44:13 2016

@author: Liberator
"""

import numpy as np
import numpy.random as npr

#utworz macierz 3x5 losowych liczb rzeczywistych
macierz = npr.rand(3, 5)
print(macierz)

#usun jej 3 wiersz
macierz = np.delete(macierz, 2, 0) #tablica, wiersz liczony od 0, kolumna
print(macierz)