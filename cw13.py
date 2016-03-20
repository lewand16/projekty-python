# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 19:24:01 2016

@author: Liberator
"""
# Importowanie bibliotek potrzebnych do działania funkcji i skrocenie ich nazw
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

# a) definiuje zmienna n rowna np. 30
n = 30

# b) oblicza sume liczb naturalnych od 1 do n i wyswietla wynik za pomoca
# polecenia print
print(sum(np.arange(1, (n+1))))

# c) oblicza sume liczb parzystych od 2 do 2n i wyswietla wynik za pomoca
# polecenia print
print(sum(np.arange(2, (2*n)+2, 2)))

# d) oblicza iloczyn kolejnych ulamkow od 1/2 do 1/n i wyswietla wynik
# za pomoca polecenia print
print(np.prod(1 / np.arange(2, n+1)))

# e) oblicza sume kolejnych ulamkow od 1/n^2 do 1/2^2 i wyswietla wynik
# za pomoca polecenia print
print(sum(1 / np.arange(2, n+1)**2))

# f) buduje 2n-elementowa liste x, zawierajaca na przemian liczby generowane
# przez rand i randint
x = []

for l in range(2*n):
    if l % 2 != 0:
        x.append(npr.rand())
    elif l % 2 == 0:
        x.append(npr.randint(n))
print(len(x))
# g) buduje liste y, zawierajaca elementy listy x ustawione w odwrotnej
# kolejnosci
#y = []
##pom = 2*n-1
#for l in range(2*n):
#    y.append(x[len(x)-1-l])
##    pom = pom-1

y = x[:]
y.reverse()

# h) tworzy wykres, zawierajacy punkty wyznaczone przez odpowiednie elementy
# list x i y (niebieskie kropki polaczone czarna linia)
plt.plot(x, y, '-k')
plt.plot(x, y, 'o b')
plt.show()