# Método de la secante
# la función se debe cargar de la siguiente manerax**2-3*x-4
# x_a debe ser menor que x_b

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def secant(fun, x_a, x_b, tolerance):
    # El método de la secante
    n = 0
    x_n = x_b
    table = []
    while True:
        # Cálculo de la secante
        anterior = x_n
        x_n = x_a - fun(x_a)*(x_b - x_a)/(fun(x_b) - fun(x_a))
        error = abs((x_n - anterior) / x_n)
        f_a = fun(x_a)
        f_b = fun(x_b)
        
        # Agregar los valores a la tabla
        table.append((n, x_n, x_a, x_b, error, f_a, f_b))

        if fun(x_n) == 0 or error < tolerance:
            return x_n, table

        # if fun(x_a) * fun(x_n) < 0:
        #     x_b = x_n
        # else:
        #     x_a = x_n
        x_a = x_b
        x_b = x_n

        n += 1
        if n > 100:
            messagebox.showinfo("Error", "No se ha convergido después de 100 iteraciones")
            return None, table

    return x_n, table

def calculate():
    f_input = f_entry.get()
    x_a = float(x_a_entry.get())
    x_b = float(x_b_entry.get())
    tolerance = float(tolerance_entry.get())

    try:
        f = lambda x: eval(f_input)
        result, table = secant(f, x_a, x_b, tolerance)
        if result is not None:
            result_label.configure(text="El resultado es: {}".format(result))
            create_table(table)
    except Exception as e:
        messagebox.showinfo("Error", str(e))

def create_table(table):
    table_frame = ttk.Frame(window)
    table_frame.pack(pady=10)

    headers = ["n", "x_n", "x_a", "x_b", "Error", "f(x_a)", "f(x_b)"]

    for i, header in enumerate(headers):
        header_label = ttk.Label(table_frame, text=header, font="bold")
        header_label.grid(row=0, column=i, padx=5, pady=5)

    for i, row in enumerate(table):
        for j, value in enumerate(row):
            value_label = ttk.Label(table_frame, text=value)
            value_label.grid(row=i+1, column=j, padx=5, pady=5)

# Configuración de la ventana
window = tk.Tk()
window.title("Método de la Secante")
window.geometry("400x300")

# Etiqueta y campo de entrada para la función f(x)
f_label = tk.Label(window, text="Función f(x):")
f_label.pack()
f_entry = tk.Entry(window, width=30)
f_entry.pack()

# Etiqueta y campo de entrada para x_a
x_a_label = tk.Label(window, text="Valor de x_a:")
x_a_label.pack()
x_a_entry = tk.Entry(window, width=30)
x_a_entry.pack()

# Etiqueta y campo de entrada para x_b
x_b_label = tk.Label(window, text="Valor de x_b:")
x_b_label.pack()
x_b_entry = tk.Entry(window, width=30)
x_b_entry.pack()

# Etiqueta y campo de entrada para la tolerancia
tolerance_label = tk.Label(window, text="Tolerancia:")
tolerance_label.pack()
tolerance_entry = tk.Entry(window, width=30)
tolerance_entry.pack()

# Botón para calcular
calculate_button = tk.Button(window, text="Calcular", command=calculate)
calculate_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(window, text="")
result_label.pack()

# Iniciar el bucle de la ventana
window.mainloop()
