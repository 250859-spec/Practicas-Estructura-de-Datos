historial_navegacion=[]
#OPERACIÓN PARA APILAR (PUSH)
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.com")
print("Historial cargado",historial_navegacion)

#OPERACIÓN CIMA (TOP-PEEK)
pagina_actual=historial_navegacion[-1]
print("Pagina actual en pantalla: ",pagina_actual)

#OPERACIÓN PARA DESAPILAR (POP)
pagina_cerrada=historial_navegacion.pop()
print("Saliendo de: ",pagina_cerrada)
print("Historial despues de presionar 'Atrás'",historial_navegacion)

#OPERACIÓN TAMAÑO (SIZE)
total_paginas=len(historial_navegacion)
print("Páginas guardadas: ",total_paginas)

#OPERACIÓN VACIA (EMPTY)
sin_paginas=len(historial_navegacion)==0
print("¿El historial está vacio?",sin_paginas)
