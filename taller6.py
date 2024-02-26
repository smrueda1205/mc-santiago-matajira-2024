import math

def calcular_coseno_aproximado(x, epsilon_s):
    
    resultado_aproximado = 1.0
    termino_actual = 1.0
    iteracion = 1

    while True:
        termino_actual *= -x**2 / ((2 * iteracion) * (2 * iteracion - 1))
        resultado_aproximado += termino_actual
        iteracion += 1

        
        error_absoluto = abs(math.cos(x) - resultado_aproximado)
        error_relativo = error_absoluto / abs(math.cos(x)) * 100

        
        if error_relativo < epsilon_s:
            break

    return resultado_aproximado, error_relativo, iteracion


x = float(input("Ingrese el valor en radianes: "))
epsilon_s = float(input("Ingrese el criterio de error esperado (epsilon_s): "))


resultado, error_relativo, iteraciones = calcular_coseno_aproximado(x, epsilon_s)


print(f"Valor estimado: {resultado}")
print(f"Error aproximado relativo porcentual: {error_relativo:.8f}%")
print(f"Número de iteraciones realizadas: {iteraciones}")
