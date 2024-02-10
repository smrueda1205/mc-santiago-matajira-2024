# -*- coding: utf-8 -*-
"""taller1.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQXnIupN9CY2jCSVG8pvXcWAqoCecDJe
"""

def operacion_conjuntos():

    conjunto1 = set(map(float, input("Ingrese el primer conjunto de números decimales separados por espacios: ").split()))
    conjunto2 = set(map(float, input("Ingrese el segundo conjunto de números decimales separados por espacios: ").split()))
    operacion = input("Ingrese la operación a realizar (union, interseccion, diferencia, diferencia_simetrica): ")
    if operacion == "union":
        resultado = conjunto1.union(conjunto2)
    elif operacion == "interseccion":
        resultado = conjunto1.intersection(conjunto2)
    elif operacion == "diferencia":
        resultado = conjunto1.difference(conjunto2)
    elif operacion == "diferencia_simetrica":
        resultado = conjunto1.symmetric_difference(conjunto2)
    else:
        print("Operacion no encontrada o no valida")
        return
    print("Conjunto Resultante:", resultado)
    print("Cardinalidad:", len(resultado))

operacion_conjuntos()