# Importación de bibliotecas
import numpy as np
import pandas as pds


# Definición de funciones

def F(y, p):
    """
    Evaluar el lado derecho de la EDO
    parámetro y: valor numérico de la variable sobre la que se desarrolla la EDO
    parámetro p: valor numérico de función de la variable y, p(y)
    salida: valor numérico obtenido al evaluar el lado derecho de la EDO de primer orden p'=f(y,p)
    """

    m = 0.0289647               # masa molar del aire en kg/mol
    r = 8.314462                # constante del gas ideal en J/molK
    t = 293.0 - y / 200.0       # temperatura del aire en función de la altura (y) en K
    g = 9.8                     # aceleración de la gravedad en m/s^2
    f = -(m * p * g) / (r * t)
    return f


def RK4(f, p0, y0, yf, h):
    """
    Realiza el cálculo de los valores de p utilizando el método numérico Runge Kutta de cuarto orden
    parámetro f: función que corresponde al lado derecho de la EDO
    parámetro p0: valor de p(y) en y = y0, condición inicial
    parámetro y0: extremo inferior del intervalo de valores de y
    parámetro yf: extremo superior del intervalo de valores de y
    parámetro h: espaciamiento entre los valores de y
    salidas: arreglo con los valores de y de interés, arreglo con los valores de p obtenidos con RK4
    """

    # Se calcula el número de puntos de interés en el intervalo
    n = int((yf - y0) / h + 1)

    # Se crea un arreglo con los valores y de interés
    arregloY = np.linspace(y0, yf, n)

    # Se inicializa un arreglo para los valores p(y) a aproximar
    arregloP = np.zeros(n)
    # Se establece la condición inicial
    arregloP[0] = p0

    # Se define el método de cálculo RK4
    for i in range(0, n - 1):
        k1 = h * f(arregloY[i], arregloP[i])
        k2 = h * f(arregloY[i] + h / 2, arregloP[i] + k1 / 2)
        k3 = h * f(arregloY[i] + h / 2, arregloP[i] + k2 / 2)
        k4 = h * f(arregloY[i] + h, arregloP[i] + k3)
        arregloP[i + 1] = arregloP[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return arregloY, arregloP


def main():
    # Se definen los parámetros de RK4
    y0 = 0.0
    yf = 3000.0
    h = 100
    p0 = 101325.0

    # Se calculan los valores aproximados de p(y) con RK4
    y, p = RK4(F, p0, y0, yf, h)

    # Se presentan los resultados obtenidos
    resultados = pds.DataFrame({'Altura (m)':y, 'Presión (Pa)':p})
    print(resultados)


if __name__ == '__main__':
    main()
