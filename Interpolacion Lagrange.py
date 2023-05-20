# Iterpolacion de Lagrange

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import math as mp

# INGRESO, Datos de prueba
#xi = ([0, math.pi/6, math.pi/3, math.pi])
#fi = ([0, 1/2, math.sqrt(3)/2, 1])
xi = ([1,3,6])
fi = ([5,2,9])

#PROCEDIMIENTO
n = len(xi)
x = sym.Symbol('x')
polinomio = 0
for i in range(0,n,1):
      numerador = 1
      denominador = 1
      for j in range(0,n,1):
            if (i!=j):
                  numerador = numerador*(x-xi[j])
                  denominador = denominador*(xi[i]-xi[j])
            termino = (numerador/denominador)*fi[i]
      polinomio = polinomio + termino 

#SALIDA
polisimple = sym.expand(polinomio)
px = sym.lambdify(x, polinomio)
print('polinomio')
print(polinomio)
print('polisimple:')
print(polisimple)

#GRAFICA 
# vectoreas para graficas
muestras = 51
a = np.min(xi)
b = np.max(xi)
p_xi = np.linspace(a,b,muestras)
pfi = px(p_xi)

plt.plot(xi,fi,'o')
plt.plot(p_xi,pfi)
plt.show()

