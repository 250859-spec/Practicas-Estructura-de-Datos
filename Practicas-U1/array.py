# Crear un array (lista) de frutas
frutas = ["manzana", "pera", "uva","banana"]

# Acceder al primer elemento
print(frutas[0])  # Muestra: manzana

# Modificar el segundo elemento
frutas[1] = "naraja"
print(frutas)     # Muestra: ['manzana', 'naraja', 'uva']

# Agregar un elemento al final
frutas.append("sandía")
print(len(frutas)) # Muestra la cantidad de elementos: 4

frutas.remove("banana")
print(frutas)