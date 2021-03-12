#Se importan las bibliotecas que se consideran necesarias.
import numpy as np
import scipy.integrate as scp
import pandas as pds

def funcion (x,p):
    """
       Evaluar el lado derecho de la EDO
       parámetro y: valor numérico de la variable sobre la que se desarrolla la EDO
       parámetro p: valor numérico de función de la variable y, p(y)
       salida: valor numérico obtenido al evaluar el lado derecho de la EDO de primer orden p'=f(y,p)
    """
    g = 9.81
    m = 0.0289647
    r =8.314462
    t = 293 - x/200
    f = -(m*p*g)/(r*t)
    return f

#Se establecen los puntos de interes donde evaluar la función.
alturas = np.linspace(0, 3000, 31)

#Se calcula la solución de la EDO en los puntos de interés
solucion = scp.solve_ivp(funcion,[0,3000],[101325],method='RK45',t_eval=alturas)

#Los resultados son ordenados en una tabla.
resultados = pds.DataFrame({'Altura (m)':alturas, 'Presión (Pa):' :solucion.y[0]})
print(resultados)
