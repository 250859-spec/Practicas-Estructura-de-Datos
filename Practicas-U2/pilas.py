# Paso 1: Crear la estructura
# Constructor
pila = []

# Paso 2: Apilar 10 elementos (Push)
for i in range(1, 11):
    pila.append(f"Plato {i}")

print("Pila inicial:", pila)

# Paso 3: Consultar el plato en la cima (Top)
print("Plato en la cima:", pila[-1])

# Paso 4: Desapilar 4 elementos (Pop)
for i in range(4):
    eliminado = pila.pop()
    print("Plato retirado:", eliminado)

print("Pila después de retirar 4 platos:", pila)

# Paso 5: Consultar tamaño y estado vacío (Size y Empty)
print("Cantidad de platos:", len(pila))
print("¿La pila está vacía?:", len(pila) == 0)

# Paso 6: Vaciar la pila por completo (Extra)
while len(pila) > 0:
    eliminado = pila.pop()
    print("Retirando:", eliminado)

print("Pila final:", pila)
print("¿La pila está vacía?:", len(pila) == 0)