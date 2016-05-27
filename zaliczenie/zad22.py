# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:25:46 2016

@author: Liberator
"""

def geomsum(r, n):
    suma = 1
    i = 1
    while (i <= n):
        suma = suma + (r**i)
        i= i + 1
    return suma

print(geomsum(1, 10))