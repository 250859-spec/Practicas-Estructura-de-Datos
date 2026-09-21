lista = [29,10,14,100]
n = len(lista) #tamaño total de los elementos
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):   #comparacion e intecambio/va a recorrer todos los indices
        if lista[i]>lista[i+1]:   #se evalua si el n de la izquiera es mayor que
            lista[i],lista[i+1]=lista[i+1],lista[i]    #lista ordenada
            swapped = True
print("Lista ordenada:",lista)            