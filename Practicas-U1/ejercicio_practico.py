# creacion de la lista inicial
print("CREACION DE LISTA INICIAL")
estudiantes=["Ana","Carlos","Diana"]
print(estudiantes)
# inserccion de elementos
print("INSERCCION DE ELEMENTOS")
estudiantes.append("Elena")
estudiantes.insert(1,"Beatriz")
print("Lista actualizada: ",estudiantes)
# busqueda y acceso por indice
print("BUSQUEDA Y ACCESO POR INDICE")
print("Estudiante en el indice 0: ",estudiantes[0])
print("Estudiante en el indice 2: ",estudiantes[2])
# metodo index
print("METODO INDEX")
indice=estudiantes.index("Diana")
print("Ddiana se encuentra en el indice: ",indice)
# operaciones de slicing ([inicio:fin:paso])
print("OPERACIONES DE SLICING")
print("Primeros 3 estudiantes: ",estudiantes[:3])
print("Subgrupo del indice 1 al 3 : ",estudiantes[1:4])
print("Ultimos 2 estudiantes: ",estudiantes[-2:])
print("Lista totalmente invertida: ",estudiantes[::-1])