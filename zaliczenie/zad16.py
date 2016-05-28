# -*- coding: utf-8 -*-
"""
Created on Thu May 26 17:45:21 2016

@author: Liberator
"""
#P - suma pieniedzy
#r - oprocentowanie w skali roku
#n - lata
#Tn - suma pieniedzy po n latach

#jezeli pewna suma pieniedzy P jest zlozona na koncie bankowym o oprocentowaniu r
#i rocznej kapitalizacji, to koncowa suma pieniedzy po n latacy jest dana przez:
def sumaPieniedzy(P, r, n):
    return P * ((1 + r)**n)

#dane wejsciowe
P = 1000
r = .1
n = 1
Tn = sumaPieniedzy(P, r, n)
print(Tn)