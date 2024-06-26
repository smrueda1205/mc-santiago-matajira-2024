# -*- coding: utf-8 -*-
"""Taller15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ANpSrbA24SCfBtGQVKqXNekSOnldIKJH
"""

import copy

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print("|", b[i])
    print()

def intercambiarFilas(a, b, fila1, fila2):
    a[fila1], a[fila2] = a[fila2], a[fila1]
    b[fila1], b[fila2] = b[fila2], b[fila1]

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)

    n = len(b)
    imprimirSistema(a, b, "Matriz inicial")
    for i in range(n):
        pivote = a[i][i]

        # Manejar división por cero
        if pivote == 0:
            # Buscar una fila con un elemento diferente de cero en la misma columna
            fila_con_elemento_no_cero = None
            for k in range(i + 1, n):
                if a[k][i] != 0:
                    fila_con_elemento_no_cero = k
                    break

            # Si se encuentra una fila válida, intercambiar filas
            if fila_con_elemento_no_cero is not None:
                intercambiarFilas(a, b, i, fila_con_elemento_no_cero)
                pivote = a[i][i]
            else:
                print("Error: no se puede resolver el sistema de ecuaciones debido a la división por cero.")
                return None

        # Dividir por el pivote
        for j in range(n):
            a[i][j] /= pivote
        b[i] /= pivote
        imprimirSistema(a, b, "División")

        # Reducción
        for k in range(n):
            if i != k:
                # Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
        imprimirSistema(a, b, "Reducción")

    return b

a = [[2, 2, 0], [3, 3, 4], [4, 0, 1]]
b = [10, 23, 30]
x = gaussJordan(a, b)

if x is not None:
    print("Respuesta:")
    for i in range(len(x)):
        print("x" + str(i+1), "=", x[i])

    # Pruebas
    print("\nPruebas:")
    for i in range(len(b)):
        valorAux = b[i]
        for j in range(len(b)):
            valorAux -= a[i][j] * x[j]
        print("Test", i + 1, "=", valorAux)