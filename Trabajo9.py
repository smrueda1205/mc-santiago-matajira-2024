# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Pf4c5qOgDFhBZAEl0UmmgHfQuTipJQA
"""

import math

def calcular_seno_aproximado(x, epsilon_s):

    resultado_aproximado = 0.0
    iteracion = 0
    termino_actual = x
    epsilon_a = float('inf')

    while abs(epsilon_a) >= epsilon_s:

        resultado_aproximado += termino_actual


        iteracion += 1
        termino_actual *= -1 * x**2 / ((2 * iteracion) * (2 * iteracion + 1))


        epsilon_a = (termino_actual / resultado_aproximado) * 100

    return resultado_aproximado, epsilon_a, iteracion


x_radianes = float(input("Ingrese el valor en radianes: "))


epsilon_esperado = float(input("Ingrese el criterio de error esperado (epsilon_s): "))


resultado, error_relativo, iteraciones = calcular_seno_aproximado(x_radianes, epsilon_esperado)


print(f"Seno({x_radianes}) aproximado: {resultado}")
print(f"Error relativo porcentual: {error_relativo}%")
print(f"Número de iteraciones realizadas: {iteraciones}")