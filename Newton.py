# # Metodo de Newton-Raphson

# import numpy as np


# # INGRESO
# fx=lambda x: x**3+4*(x**2)-10
# fdx=lambda x: 3*(x**2)+8*x

# x0= 2
# tolera= 0.0001

# # PROCEDIMIENTO
# xi=x0
# tramo=abs(2*tolera)

# iteracion = 0

# print("\nITERACIÓN    |    X_i     |   X_nuevo  |   TRAMO \n")
# while (tramo>=tolera):
#     xnuevo = xi - fx(xi)/fdx(xi)
#     tramo = abs(xnuevo-xi)
#     print(f"iteración {iteracion}  |  {xi:.6f}  |  {xnuevo:.6f}  |  {tramo:.6f}")
#     xi = xnuevo
#     iteracion += 1

    
# # SALIDA
# print("\nEl valor resultante es:",xnuevo,"\n")


import numpy as np
import sympy as sym

# Pedir al usuario que ingrese la función y el punto inicial
fx_str = input("Ingrese la función f(x): ")
x0 = float(input("Ingrese el punto inicial x0: "))

# Convertir la cadena de caracteres de la función en una función lambda
fx = lambda x: eval(fx_str)

# Calcular la derivada simbólica de la función utilizando SymPy
x = sym.Symbol('x')
dfx = sym.diff(fx(x), x)
fdx = sym.lambdify(x, dfx)

tolera = 0.0001

# PROCEDIMIENTO
xi = x0
tramo = abs(2*tolera)

iteracion = 0

print("La derivada de la función es: ", dfx)

print("\nITERACIÓN    |    X_i     |   X_nuevo  |   TRAMO    |    f(X_i)   |   f'(X_i)  \n")
while (tramo >= tolera):
    xnuevo = xi - fx(xi) / fdx(xi)
    tramo = abs(xnuevo - xi)
    print(f"iteración {iteracion}  |  {xi:.6f}  |  {xnuevo:.6f}  |  {tramo:.6f} |  {fx(xi):.6f}  |  {fdx(xi):.6f}")
    xi = xnuevo
    iteracion += 1

# SALIDA
print("\nEl valor resultante es:", xnuevo, "\n")


