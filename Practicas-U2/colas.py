from collections import deque

# Paso 1: Crear la estructura (Constructor)
cola = deque()

# Paso 2: Encolar 10 elementos (Enqueue)
for i in range(1, 11):
    cola.append(i)

print("Cola inicial:", list(cola))

# Paso 3: Consultar el primer elemento (Front / Peek)
print("Primer elemento de la cola:", cola[0])

# Paso 4: Desencolar 4 elementos (Dequeue)
for i in range(4):
    elemento = cola.popleft()
    print("Elemento eliminado:", elemento)

print("Cola después de desencolar:", list(cola))

# Paso 5: Consultar tamaño y estado vacío (Size y Empty)
print("Cantidad de elementos:", len(cola))
print("¿La cola está vacía?:", len(cola) == 0)

# Paso 6: Vaciar la cola por completo (Extra)
while len(cola) > 0:
    print("Vaciando cola, se elimina:", cola.popleft())

print("Cola final:", list(cola))
print("¿La cola está vacía?:", len(cola) == 0)