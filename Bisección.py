# # Metodo de Biseccion
# # busqueda en intervalo [a,b]

# import numpy as np

# # INGRESO
# fx = lambda x: x**3+4*(x**2)-10
# a = 1
# b = 2
# tolera = 0.0001

# # PROCEDIMIENTO 
# tramo = np.abs(b-a)
# while (tramo>=tolera):    
#     c = (a+b)/2
    
#     fa = fx(a)
#     fb = fx(b)
#     fc = fx(c)

#     cambia = np.sign(fa)*np.sign(fc)
#     print(cambia)

#     if cambia<0:
#         a = a
#         b = c

#     if cambia>0:
#         a = c
#         b = b

#     tramo = np.abs(b-a)
#     print(c)

# #SALIDA
# print(c)


# import numpy as np

# # INGRESO
# fx_str = input("Ingrese la función f(x): ")
# a = float(input("Ingrese el valor de a: "))
# b = float(input("Ingrese el valor de b: "))
# tolera = float(input("Ingrese la tolerancia: "))

# # Convertir la cadena de caracteres de la función en una función lambda
# fx = lambda x: eval(fx_str)

# # PROCEDIMIENTO 
# tramo = np.abs(b-a)
# iteracion = 0

# print("\nITERACIÓN |     a     |     b     |     c     |  f(a)   |  f(b)   |  f(c)   |  TRAMO\n")
# while (tramo>=tolera):    
#     c = (a+b)/2
    
#     fa = fx(a)
#     fb = fx(b)
#     fc = fx(c)

#     cambia = np.sign(fa)*np.sign(fc)

#     print(f"   {iteracion}    |  {a:.6f} |  {b:.6f} |  {c:.6f} | {fa:.6f} | {fb:.6f} | {fc:.6f} | {tramo:.6f}")
    
#     if cambia<0:
#         a = a
#         b = c

#     if cambia>0:
#         a = c
#         b = b

#     tramo = np.abs(b-a)
#     iteracion += 1

# #SALIDA
# print("\nEl valor resultante es:", c)

import numpy as np

# INGRESO
while True:
    try:
        fx_str = input("Ingrese la función f(x): ")
        fx = lambda x: eval(fx_str)
        fx(0) # Comprobar que la función es válida
        break
    except:
        print("Error: función inválida. Intente nuevamente.")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
tolera = float(input("Ingrese la tolerancia: "))

# PROCEDIMIENTO 
tramo = np.abs(b-a)
while (tramo>=tolera):    
    c = (a+b)/2
    
    fa = fx(a)
    fb = fx(b)
    fc = fx(c)

    cambia = np.sign(fa)*np.sign(fc)

    if cambia<0:
        a = a
        b = c

    if cambia>0:
        a = c
        b = b

    tramo = np.abs(b-a)
    print(f"{i}    | {a:.6f} | {b:.6f} | {c:.6f} | {fa:.6f} | {fb:.6f} | {fc:.6f} | {tramo:.6f}")

# SALIDA
print(f"\nLa raíz es: {c:.6f}")

