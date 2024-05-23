# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FOmktJ7tTZYhUbNRd5QWbHXKxE_AvFq5
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# Datos de la tabla
x = np.array([1, 2, 3, 4, 5, 6, 7])
f_x = np.array([1, 5, 4, 4, -2, 2, 9])

# Interpolación de Lagrange
polinomio_lagrange = lagrange(x, f_x)

# Interpolación con Trazadores Cúbicos
spl = CubicSpline(x, f_x)

# Valor estimado de f(3.55)
x_est = 3.55
f_lagrange = polinomio_lagrange(x_est)
f_spline = spl(x_est)

print(f"Valor estimado de f(3.55) usando Lagrange: {f_lagrange}")
print(f"Valor estimado de f(3.55) usando Trazadores Cúbicos: {f_spline}")

# Graficar
x_graf = np.linspace(min(x), max(x), 100)
f_lagrange_graf = polinomio_lagrange(x_graf)
f_spline_graf = spl(x_graf)

plt.figure(figsize=(10, 6))

# Puntos originales
plt.plot(x, f_x, 'o', label='Puntos originales')

# Polinomio de Lagrange
plt.plot(x_graf, f_lagrange_graf, label='Interpolación de Lagrange')

# Trazadores cúbicos
plt.plot(x_graf, f_spline_graf, label='Trazadores Cúbicos')

# Punto estimado
plt.plot(x_est, f_lagrange, 's', label=f'Lagrange f({x_est}) = {f_lagrange:.2f}')
plt.plot(x_est, f_spline, 's', label=f'Trazadores Cúbicos f({x_est}) = {f_spline:.2f}')

plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación Polinómica y Trazadores Cúbicos')
plt.grid(True)
plt.show()