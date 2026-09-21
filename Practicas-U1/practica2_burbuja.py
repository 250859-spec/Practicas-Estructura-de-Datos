lista = [5,2,6,3,4,8,9,10,7,1,8,6,4,9,10]
n = len(lista) 
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):   
        if lista[i]>lista[i+1]:  
            lista[i],lista[i+1]=lista[i+1],lista[i]  
            swapped = True
print("Orden Ascendente:",lista)            