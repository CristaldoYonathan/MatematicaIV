import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo
x = np.array([5, 6, 9, 11])
y = np.array([12, 13, 14, 16])

# Valor a interpolar
x_interp = 10

# Encontrar los índices de los puntos adyacentes
idx = np.searchsorted(x, x_interp)
idx_left = idx - 1
idx_right = idx

# Calcular las diferencias en x y y
dx = x[idx_right] - x[idx_left]
dy = y[idx_right] - y[idx_left]

# Calcular la pendiente
m = dy / dx

# Calcular el valor interpolado
y_interp = y[idx_left] + m * (x_interp - x[idx_left])

# Crear los puntos para la gráfica
x_plot = np.array([x[idx_left], x[idx_right]])
y_plot = np.array([y[idx_left], y[idx_right]])

print(f'El valor interpolado en x={x_interp} es y={y_interp}')

# Graficar los datos y la interpolación lineal
plt.plot(x, y, 'ro', label='Datos')
plt.plot(x_plot, y_plot, 'b-', label='Interpolación Lineal')
plt.plot(x_interp, y_interp, 'go', label=f'Interpolación en x={x_interp}, y={y_interp}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Lineal')
plt.legend()
plt.grid(True)
plt.show()


