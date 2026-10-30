import numpy as np

A= np.array([[10, 15],[20, 5]])
B= np.array([[5, 12],[15, 8]])

total_ventas=A+B
precio=50

ingresos=total_ventas*precio
print("MATRICES CON PYTHON NATIVO")
print("Total de productos vendidos: ")
for fila in total_ventas:
    print(fila)

print("Ingreso Total en Pesos: ")
for fila in ingresos:
    print(fila)
    