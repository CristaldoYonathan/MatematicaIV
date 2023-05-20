import tkinter as tk
from tkinter import messagebox
import sympy as sp
from tkinter import ttk

# Función de punto fijo
def punto_fijo():
    # Obtener los valores ingresados por el usuario
    try:
        x0 = float(entry_x0.get())
        tolerancia = float(entry_tolerancia.get())
        fx_expression = entry_fx.get()
        gx_expression = entry_gx.get()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
        return

    # Convertir las expresiones de las funciones en funciones evaluables
    x = sp.symbols('x')
    try:
        fx = sp.lambdify(x, sp.sympify(fx_expression), 'numpy')
        gx = sp.lambdify(x, sp.sympify(gx_expression), 'numpy')
    except (sp.SympifyError, TypeError):
        messagebox.showerror("Error", "Por favor, ingrese funciones válidas.")
        return

    # Algoritmo de punto fijo
    iteracion = 0
    error = tolerancia + 1

    iteraciones = []  # Lista para almacenar las iteraciones y valores correspondientes

    while error > tolerancia and iteracion < 100:
        x_nuevo = gx(x0)
        error = abs(x_nuevo - x0)

        # Agregar la iteración y los valores correspondientes a la lista
        iteraciones.append((iteracion, x0, error))

        x0 = x_nuevo
        iteracion += 1

    # Mostrar los resultados
    if error <= tolerancia:
        messagebox.showinfo("Resultado", f"El método de punto fijo convergió a la solución:\nx = {x_nuevo}\nNúmero de iteraciones: {iteracion}")
  

    # Mostrar la tabla de iteraciones en la interfaz gráfica
    tabla.delete(*tabla.get_children())
    for i, x, e in iteraciones:
        tabla.insert("", tk.END, values=(i, x, e))

# Crear la ventana principal
window = tk.Tk()
window.title("Método de Punto Fijo")

# Crear campos de entrada para x0, tolerancia, max_iteraciones, fx y gx
label_x0 = tk.Label(window, text="x0:")
label_x0.pack()
entry_x0 = tk.Entry(window)
entry_x0.pack()

label_tolerancia = tk.Label(window, text="Tolerancia:")
label_tolerancia.pack()
entry_tolerancia = tk.Entry(window)
entry_tolerancia.pack()


label_fx = tk.Label(window, text="f(x):")
label_fx.pack()
entry_fx = tk.Entry(window)
entry_fx.pack()

label_gx = tk.Label(window, text="g(x):")
label_gx.pack()
entry_gx = tk.Entry(window)
entry_gx.pack()

# Botón para ejecutar el método
button_calcular = tk.Button(window, text="Calcular", command=punto_fijo)
button_calcular.pack()

# Crear la tabla de iteraciones
tabla = ttk.Treeview(window)
tabla["columns"] = ("Iteración", "x_i", "Error")
tabla.heading("Iteración", text="Iteración")
tabla.heading("x_i", text="x_i")
tabla.heading("Error", text="Error")
tabla.pack(fill="both", expand=True)

# Establecer el ancho de las columnas al contenido
tabla.column("#0", width=0, stretch=tk.NO)  # Ocultar la primera columna
tabla.column("Iteración", width=100, anchor=tk.CENTER, stretch=True)
tabla.column("x_i", width=100, anchor=tk.CENTER, stretch=True)
tabla.column("Error", width=100, anchor=tk.CENTER, stretch=True)

# Ejecutar la aplicación
window.mainloop()
