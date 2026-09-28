def mostrar_mensaje():                     #definir funcion ()= no necesita parametros
    mensaje = "Buenos dias ESTRELLITAS, la tierra les dice HOLA!!"   #variable mensaje, se define el texto
    return mensaje                         #devoolver el mensaje
resultado = mostrar_mensaje()              #se ejecuta la funcion
print(resultado)



#FUNCION 2  
def mostrar_datos():          #definir funcion ()=sin paraemtros
    nombre = "Elena"           #definimos datos
    edad = 28
    print(f"Nombre: {nombre}, Edad: {edad}")               #mostrar datos

mostrar_datos() #se ejecuta la funcion
