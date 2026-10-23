#el primero en entrar es el primero en salir
# Paso 1: Importar los módulos necesarios-crear cola y retirar elementos del principio
from collections import deque
import time              #simular el tiempo

# Paso 2: Inicializar la cola
cola_turnos = deque()   #deque=permite retirara al primer cliente

# Paso 3: Registrar turnos (Encolar - FIFO)
cola_turnos.append("Cliente 1")
cola_turnos.append("Cliente 2")
cola_turnos.append("Cliente 3")
cola_turnos.append("Cliente 4")
cola_turnos.append("Cliente 5")

# Mostrar los turnos emitidos
print("Turnos emitidos:", list(cola_turnos))

# Paso 4: Procesar la atención (Desencolar)
while len(cola_turnos) > 0:
    cliente = cola_turnos.popleft()   #popleft=elimina el elemneto que esta al principio

    print("\nAtendiendo al:", cliente)

    time.sleep(1)

    print("Atención finalizada:", cliente)
    print("Clientes restantes en la fila:", len(cola_turnos))

print("\nNo hay más clientes. La fila está vacía.")