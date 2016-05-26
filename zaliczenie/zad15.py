# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:52:19 2016

@author: Liberator
"""

import numpy as np

def hipsin(x):
    return (np.e**x - np.e**(-2)) / 2

print(hipsin(5))