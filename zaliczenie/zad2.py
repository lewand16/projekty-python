# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:02:15 2016

@author: Liberator
"""

#funkcja przeliczajaca stopnie fahrenheita na celsjusza
def ctemp(fahr):
    ctemp = (fahr - 32) * 5 / 9
    return ctemp

#temperatura w fahrenheit
ftemp = 60

#wynik
print(ctemp(ftemp))