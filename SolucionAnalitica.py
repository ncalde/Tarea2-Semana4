#Se importan las bibliotecas que se consideran necesarias.
import numpy as np
import pandas as pds

#Se establecen los puntos de interes donde evaluar la función.
alturas = np.linspace(0, 3000, 31)

#Se crea un arreglo para almacenar los resultados analíticos
y = np.zeros(len(alturas))

def funcion (y):
    """
           Se define la solución analítica previamenten calculada
    """
    g = 9.81
    m = 0.0289647
    r = 8.314462
    P0 = 101325
    p = P0 * np.exp(((m*g*200)/r)*np.log((y-58600)/(-58600)))
    return p

#Se calcula la presión atmosférica en las alturas deseadas
for i in range (0,len(alturas)):
    y[i] = funcion(alturas[i])

#Los resultados se presentan en forma tabular
resultados = pds.DataFrame({'Altura (m)':alturas, 'Presión (Pa):' :y})
print(resultados)