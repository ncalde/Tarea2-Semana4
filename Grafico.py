from RK4 import F, RK4
import scipy.integrate as scp
import matplotlib.pyplot as plt
from SolucionAnalitica import funcion

def main():
    # Se definen los parámetros
    y0 = 0.0
    yf = 3000.0
    h = 100
    p0 = 101325.0

    # Se calculan las soluciones con RK4, RK45
    arregloY, arregloPRK4 = RK4(F, p0, y0, yf, h)
    solucionRK45 = scp.solve_ivp(F, [y0, yf], [p0], method='RK45', t_eval=arregloY)
    arregloPRK45 = solucionRK45.y[0]

    # Se calculan las soluciones reales
    pReal = funcion(arregloY)

    # Se grafican los resultados
    fig = plt.figure()
    plt.plot(arregloY, pReal, 'g-', linewidth=0.8, label='Valor verdadero')
    plt.plot(arregloY, arregloPRK4, 'b1', label='Valor aproximado RK4')
    plt.plot(arregloY, arregloPRK45, 'r2', label='Valor aproximado RK45')
    plt.xlabel("Altura (m)")
    plt.ylabel("Presión atmosférica (Pa)")
    plt.grid(True)
    plt.title("Presión atmosférica en función de la altura sobre el nivel del mar")
    plt.legend(loc='upper right')
    plt.tight_layout()
    fig.savefig("Grafico_EDO")


if __name__ == '__main__':
    main()
