#paso 1: crear la estructura
#construtor
pila=[]
 for i in range(1,11):   #paso 2: apilar 10 elementos(push)
    pila.append(f"Plato {i}")
print("Pila inicial: ",pila)
#paso 3: consultar el plato en la cima(top)
print("Plato en la cima: ",pila[-1])
#paso 4: despailar 4 elementos(pop)
for i in range(4):
    eliminado=pila.pop()
    print("Plato retirado: ",eliminado)
print("Pila después de retirar 4 platos: ",pila)
#paso 5: consultar tamaño y estado vacío(size y empty)
print("Cantidad de platos: ",len(pila))
print("¿La pila está vacía?: ",len(pila)==0)
#paso 6: vaciar la pila por completo(extra)
while len(pila)>0:
    eliminado=pila.pop()
    print("Retirando: ",eliminado)

print("Pila final: ",pila)
print("¿La pila está vacía?: ",len(pila)==0)
