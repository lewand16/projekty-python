# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:45:21 2016

@author: Liberator
"""
#P - suma pieniedzy
#r - oprocentowanie w skali roku
#n - lata
#Tn - suma pieniedzy po n latach

def sumaPieniedzy(P, r, n):
    return P * ((1 + r)**n)

Tn = sumaPieniedzy(1000, .1, 1)
print(Tn)