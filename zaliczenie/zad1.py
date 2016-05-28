# -*- coding: utf-8 -*-
"""
Created on Mon May 23 20:55:07 2016

@author: Liberator
"""
#opor zastepczy trzech opornikow
def oporZast(R1, R2, R3):
    R = (1 / ((1 / R1) + (1 / R2) + (1 / R3)))
    return R

#dane wejsciowe
R1 = 3
R2 = 3
R3 = 3

#wynik
print(oporZast(R1, R2, R3))