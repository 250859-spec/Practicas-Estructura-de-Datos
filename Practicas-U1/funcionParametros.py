def calcular_promedio(nota1, nota2):                   #definir funcion
    promedio = (nota1 + nota2) / 2                     #dos datos para calcular
    return promedio                                    #devolver el resultado
resultado = calcular_promedio(8, 10)
print(f"El promedio es: {resultado}")                  #imprimir resultado


#FUNCION 2

def presentar_persona(nombre, ciudad):                 #definir funcion do parametros
    print(f"Hola {nombre}, eres de {ciudad}.")

presentar_persona("Paola", "Puebla")
