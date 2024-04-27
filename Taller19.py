import numpy as np
import matplotlib.pyplot as plt

# Datos de entrada
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([4.3, 6.5, 7.5, 8, 8.5, 8.8, 9, 9.5])

def ecuacion_de_potencias(x, y):
    # Aplicando logaritmos para linealizar la ecuación de potencias
    log_x = np.log(x)
    log_y = np.log(y)
    
    # Aplicando regresión lineal a los datos linealizados
    A = np.vstack([log_x, np.ones(len(log_x))]).T
    m, c = np.linalg.lstsq(A, log_y, rcond=None)[0]
    
    # Calculando los parámetros a y b
    a = np.exp(c)
    b = m
    
    return a, b

def razon_de_crecimiento(x, y):
    # Aplicando logaritmos para linealizar la ecuación de razón de crecimiento
    log_x = np.log(1 + x)
    log_y = np.log(y)
    
    # Aplicando regresión lineal a los datos linealizados
    A = np.vstack([log_x, np.ones(len(log_x))]).T
    m, c = np.linalg.lstsq(A, log_y, rcond=None)[0]
    
    # Calculando los parámetros a, b y c
    a = np.exp(c)
    b = m
    c = 1
    
    return a, b, c

def graficar(x, y, a_potencias, b_potencias, a_crecimiento, b_crecimiento, c_crecimiento):
    # Crear puntos para graficar las curvas ajustadas
    x_values = np.linspace(min(x), max(x), 100)
    y_potencias = a_potencias * (x_values ** b_potencias)
    y_crecimiento = a_crecimiento * (1 + b_crecimiento * x_values) ** c_crecimiento
    
    # Graficar puntos originales y curvas ajustadas
    plt.scatter(x, y, label='Datos Originales')
    plt.plot(x_values, y_potencias, label='Ecuación de Potencias (Mínimos Cuadrados)', linestyle='--')
    plt.plot(x_values, y_crecimiento, label='Razón de Crecimiento (Mínimos Cuadrados)', linestyle='--')
    
    # Linealización por series de Taylor
    taylor = np.polyfit(x, y, 1)
    y_taylor = np.polyval(taylor, x_values)
    plt.plot(x_values, y_taylor, label='Linealización por series de Taylor', linestyle='--')
    
    # Linealización por cambio de variable
    x_cambio_var = np.log(x)
    y_cambio_var = np.log(y)
    cambio_var = np.polyfit(x_cambio_var, y_cambio_var, 1)
    y_cambio_var_fit = np.exp(np.polyval(cambio_var, np.log(x_values)))
    plt.plot(x_values, y_cambio_var_fit, label='Linealización por cambio de variable', linestyle='--')
    
    # Linealización por aproximación numérica
    def aproximacion_num(x, y):
        A = np.vstack([x, np.ones(len(x))]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]
        return m, c
    m_num, c_num = aproximacion_num(x, y)
    y_aprox_num = m_num * x_values + c_num
    plt.plot(x_values, y_aprox_num, label='Linealización por aproximación numérica', linestyle='--')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ajuste de Curvas con Diferentes Métodos de Linealización')
    plt.legend()
    plt.grid(True)
    plt.show()

# Calcular parámetros para cada modelo
a_potencias, b_potencias = ecuacion_de_potencias(x, y)
a_crecimiento, b_crecimiento, c_crecimiento = razon_de_crecimiento(x, y)

# Graficar los resultados
graficar(x, y, a_potencias, b_potencias, a_crecimiento, b_crecimiento, c_crecimiento)
