import numpy as np
import pandas as pds



alturas = np.linspace(0, 3000, 31)
y = np.zeros(len(alturas))

def funcion (y):
    g = 9.81
    m = 0.0289647
    r = 8.314462
    P0 = 101325
    p = P0 * np.exp(((m*g*200)/r)*np.log((y-58600)/(-58600)))
    return p

for i in range (0,len(alturas)):
    y[i] = funcion(alturas[i])

resultados = pds.DataFrame({'Altura (m)':alturas, 'Presión (Pa):' :y})
print(resultados)