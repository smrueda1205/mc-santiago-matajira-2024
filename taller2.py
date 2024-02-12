# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gtpXNL84pNYl0MH1KWIpKD-RO7ChPEt0
"""

def solicitar_conjunto(mensaje):
    elementos = input(f"Ingrese los elementos del conjunto {mensaje} separados por espacios: ")
    return set(elementos.split())
def main():
    U = solicitar_conjunto("universal U")
    A = solicitar_conjunto("A")

    if A.issubset(U):

        operacion1 = U.union(A).intersection(A)
        operacion2 = U.intersection(A).symmetric_difference(A)
        operacion3 = U.difference(A).symmetric_difference(A)


        print("\n(U⋃A)⋂A:", operacion1)
        print("(U⋂A) ⨁A:", operacion2)
        print("(U − A)⨁A:", operacion3)
    else:
        print("Error: A no es subconjunto de U.")

if __name__ == "__main__":
    main()