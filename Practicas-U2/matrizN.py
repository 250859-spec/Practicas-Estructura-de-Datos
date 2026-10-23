#CREACIÓN D EMATRIZ DE 3X3
matriz=[
    [10,20,30],
    [40,50,60,],
    [70,80,90]
]
#ACCESO A ELEMENTOS MATRIZ (FILA)(COLUMNA)
print(matriz[1][2]) #imprimiria fila indice 1, columna indice 2
#MODIFICAR UN ELEMENTO
matriz[0][0]=100
#RECORRER LA MATRIZ
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()