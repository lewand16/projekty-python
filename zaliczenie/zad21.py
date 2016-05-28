# -*- coding: utf-8 -*-
"""
Created on Thu May 26 19:23:08 2016

@author: Liberator
"""

#napisz funkcje sumkrok2, ktora oblicza sume liczb od 1 do n z krokiem 2,
#gdzie n jest argumentem funkcji
def sumkrok2(n):
    i = 1
    suma = 0
    while(i <= n):
        suma = suma + i
        i = i + 2       
    return suma
    
#dana wejsciowa
n = 10
print(sumkrok2(n))