# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1U_lbAyiGS-VQqqhubRythxfmz9CBptMe
"""

import numpy as np
from scipy.stats import pearsonr

# Datos
x1 = np.array([1, 1, 2, 3, 1, 2, 3, 3])
x2 = np.array([0, 1, 1, 2, 2, 3, 3, 1])
y = np.array([0.6, 2, 0.1, 0.3, 2.2, 2.3, 0.8, -1])

# Construyendo la matriz de diseño
X = np.column_stack((np.ones_like(x1), x1, x2))

# Ajuste lineal
coefficients, _, _, _ = np.linalg.lstsq(X, y, rcond=None)

# Coeficientes del modelo
intercept, slope_x1, slope_x2 = coefficients

# Coeficiente de correlación (r)
r, _ = pearsonr(y, np.dot(X, coefficients))

print("Coeficientes del modelo:")
print("Intercepto:", intercept)
print("Pendiente para x1:", slope_x1)
print("Pendiente para x2:", slope_x2)

print("\nCoeficiente de correlación (r):", r)