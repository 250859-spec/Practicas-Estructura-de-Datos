from collections import deque
import time
cola_reproduccion=deque()
cola_reproduccion.append("1.Californica")
cola_reproduccion.append("2.Chicas del siglo 21")
cola_reproduccion.append("2.Como Animales")
#MOSTRAR LAS CANCIONES EN ESPERA
print("Canciones en espera: ")
for cancion in cola_reproduccion:
    print("_",cancion)
    print("Iiciando reproducción")
    #El reproductor procesa la cola cancion por cancion (desencolar)
    while cola_reproduccion:
        cancion_actual=cola_reproduccion.popleft()
        print(f"Sonando ahora: {cancion_actual}")
        time.sleep(1) #simula la duracion del tema
        print(f"Finalizó: {cancion_actual}")
        #Muestra cuantas canciones quedan en la cola
        print(f"Quedan {len(cola_reproduccion)} canciones en la cola")
        print("La cola de reproduccion ha terminado.")