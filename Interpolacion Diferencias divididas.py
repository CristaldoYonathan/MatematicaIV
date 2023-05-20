# Polinomio interpolación
# Diferencias Diferencias Divididas
# Tarea: Verificar tamaño de vectores,
#        verificar puntos equidistantes en x
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# INGRESO , Datos de prueba
xi = np.array([1, 3, 4, 8])
fi = np.array([2, 3, 2, 10])

# PROCEDIMIENTO

# Tabla de Diferencias Divididas
titulo = ['i','xi','fi']
n = len(xi)
ki = np.arange(0,n,1)
tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
tabla = np.transpose(tabla)
# diferencias finitas vacia
dfinita = np.zeros(shape=(n,n),dtype=float)
tabla = np.concatenate((tabla,dfinita), axis=1)
# Calcula tabla, inicia en columna 3
[n,m] = np.shape(tabla)
diagonal = n-1
j = 3
while (j < m):
    # Añade título para cada columna
    titulo.append('df'+str(j-2))
    # cada fila de columna
    paso = j-2
    i = 0
    while (i < diagonal):
        numerador = tabla[i+1,j-1]-tabla[i,j-1]
        denominador = xi[i+paso] - xi[i]
        tabla[i,j] = numerador/denominador
        i = i+1
    diagonal = diagonal - 1
    j = j+1

# POLINOMIO con diferencias divididas
# caso: puntos equidistantes en eje x
h = xi[1] - xi[0]
dfinita = tabla[0,3:]
n = len(dfinita)

# expresión del polinomio con Sympy
x = sym.Symbol('x')
polinomio = fi[0]
for j in range(1,n,1):
    factor = dfinita[j-1]
    termino = 1
    for k in range(0,j,1):
        termino = termino*(x-xi[k])
    polinomio = polinomio + termino*factor

# simplifica multiplicando entre (x-xi)
polisimple = polinomio.expand()

# polinomio para evaluacion numérica
px = sym.lambdify(x,polisimple)

# Puntos para la gráfica
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

# SALIDA
np.set_printoptions(precision=3)
print('Tabla Diferencia Finita')
print([titulo])
print(tabla)
print('dfinita: ')
print(dfinita)
print('polinomio: ')
print(polinomio)
print('polinomio simplificado: ' )
print(polisimple)

# Gráfica
plt.plot(xi,fi,'o', label = 'Puntos')
##for i in range(0,n,1):
##    plt.axvline(xi[i],ls='--', color='yellow')
plt.plot(pxi,pfi, label = 'Polinomio')

plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación polinómica')
plt.show()
