# Metodo de Biseccion
# busqueda en intervalo [a,b]
import numpy as np

# INGRESO
while True:
    try:
        fx_str = input("Ingrese la función f(x): ")
        fx = lambda x: eval(fx_str)
        fx(0)  # Comprobar que la función es válida
        break
    except:
        print("Error: función inválida. Intente nuevamente.")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
tolera = float(input("Ingrese la tolerancia: "))

# Cabecera de la tabla
print("Iteración |    a    |    b    |    c    |  f(a)   |  f(b)   |  f(c)   |  Tramo")

# PROCEDIMIENTO
tramo = np.abs(b - a)
i = 0
while tramo >= tolera:
    c = (a + b) / 2

    fa = fx(a)
    fb = fx(b)
    fc = fx(c)

    cambia = np.sign(fa) * np.sign(fc)

    if cambia < 0:
        a = a
        b = c

    if cambia > 0:
        a = c
        b = b

    tramo = np.abs(b - a)
    i += 1
    print(
        f"{i}        | {a:.6f} | {b:.6f} | {c:.6f} | {fa:.6f} | {fb:.6f} | {fc:.6f} | {tramo:.6f}"
    )

# SALIDA
print(f"\nLa raíz es: {c:.6f}")


