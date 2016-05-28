# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:03:27 2016

@author: Liberator
"""
import numpy as np

#oblicz objetosc wydrazonej kuli, gdzie Rz jest promieniem zewnetrznym, Rw - wewnetrznym
def objWydrKuli(Rz, Rw):
    V = (4 * np.pi * ((Rz ** 3) - (Rw ** 3))) / 3
    return V
    
#dane wejsciowe    
Rz = 2
Rw = 1
print(objWydrKuli(Rz, Rw))