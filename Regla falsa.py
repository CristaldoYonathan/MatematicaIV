# # Metodo de la Regla Falsa
# # busqueda en intervalo [a,b]
# # Como se debe ingresar la funcion: x**3+4*x**2-10
# # Como se debe ingresar la tolerancia: 0.0001 (en decimal y con punto)

import tkinter as tk
from tkinter import ttk

def regla_falsa(func, a, b, tolerancia):
    fa = func(a)
    fb = func(b)
    iter_count = 0
    error = float('inf')

    result = []

    anterior = 0
    while error > tolerancia:
        c = b - fb * ((a - b) / (fa - fb))
        fc = func(c)

        

        if fc * fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        
        result.append((iter_count+1, f"{a:.6f}", f"{b:.6f}", f"{fa:.6f}", f"{fb:.6f}", f"{c:.6f}"))

        error = abs((c - anterior) / c)
        anterior = c

        iter_count += 1

    return result, c

def solve():
    # Obtener los valores ingresados en la interfaz
    func_str = func_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    tolerancia = float(tol_entry.get())

    # Convertir la función ingresada a una función evaluable en Python
    func = lambda x: eval(func_str)

    # Aplicar el método de la regla falsa
    result, sol = regla_falsa(func, a, b, tolerancia=tolerancia)

    # Mostrar los resultados en la interfaz
    for child in result_table.get_children():
        result_table.delete(child)

    for row in result:
        result_table.insert("", tk.END, values=row)

    sol_label.config(text=f"La aproximación de la solución es: {sol:.6f}")

# Crear la ventana de la interfaz
window = tk.Tk()
window.title("Método de la Regla Falsa")

# Crear los elementos de la interfaz
func_label = tk.Label(window, text="Ingrese la función:")
func_entry = tk.Entry(window)
a_label = tk.Label(window, text="Ingrese el valor de a:")
a_entry = tk.Entry(window)
b_label = tk.Label(window, text="Ingrese el valor de b:")
b_entry = tk.Entry(window)
tol_label = tk.Label(window, text="Ingrese la tolerancia:")
tol_entry = tk.Entry(window)
solve_button = tk.Button(window, text="Resolver", command=solve)
sol_label = tk.Label(window, text="La aproximación de la solución es:")

# Crear la tabla de resultados
result_table = ttk.Treeview(window, columns=("iteration", "a", "b", "fa", "fb", "xn"))
result_table.heading("iteration", text="Iteración")
result_table.heading("a", text="a")
result_table.heading("b", text="b")
result_table.heading("fa", text="f(a)")
result_table.heading("fb", text="f(b)")
result_table.heading("xn", text="xn")

result_table.column("#0", width=0)
result_table.column("iteration", width=100)
result_table.column("a", width=100)
result_table.column("b", width=100)
result_table.column("fa", width=100)
result_table.column("fb", width=100)
result_table.column("xn", width=100)

# Posicionar los elementos en la interfaz
func_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
func_entry.grid(row=0, column=1, padx=10, pady=5)
a_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
a_entry.grid(row=1, column=1, padx=10, pady=5)
b_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
b_entry.grid(row=2, column=1, padx=10, pady=5)
tol_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
tol_entry.grid(row=3, column=1, padx=10, pady=5)
solve_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

result_table.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
sol_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

# Iniciar la ventana
window.mainloop()
