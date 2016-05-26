# -*- coding: utf-8 -*-
"""
Created on Thu May 26 19:23:08 2016

@author: Liberator
"""

def sumkrok2(n):
    i = 1
    suma = 0
    while(i <= n):
        suma = suma + i
        i = i + 2       
    return suma

print(sumkrok2(10))