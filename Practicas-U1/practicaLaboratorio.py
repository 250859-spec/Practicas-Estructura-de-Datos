# Practica de Laboratorio
## Registro y Evaluacion de Calificaciones 


def mostrar_encabezado_escuela(): 
    print("Universidad Tecnológica de Xicotepec de Juárez") 
    print("REGISTRO Y EVALUACIÓN DE CALIFICACIONES") 

def obtener_nota_minima_aprobatoria():                         #Función sin parametros
    return 6.0 

def evaluar_rendimiento(nota_final):                           #Funcion con parametros
    if nota_final < 7.0: 
        return "Reprobado" 
    elif nota_final < 9.5: 
        return "Aprobado" 
    else: 
        return "Excelente" 

def calcular_promedio_ponderado(nota_exa, nota_tareas):         #Funcion con parametros
    promedio = (nota_exa * 0.70) + (nota_tareas * 0.30) 
    return round(promedio, 1) 

def generar_boleta(alumno, nota_exa, nota_tareas):              #Funcion con parametros
    nota_final = calcular_promedio_ponderado(nota_exa, nota_tareas) 
    nota_minima = obtener_nota_minima_aprobatoria() 
    estado = evaluar_rendimiento(nota_final) 
    
    print("\n== BOLETA ==") 
    print("Alumno:", alumno) 
    print("Nota Final:", nota_final) 
    print("Estado:", estado) 
    
    if nota_final < nota_minima: 
        print("Tiene que presentar examen extraordinario: Si") 
    else: 
        print("Tiene que presentar examen extraordinario: No") 

# Ejecución del programa
mostrar_encabezado_escuela() 
nombre = input("\nIngrese el nombre del alumno: ") 
examenes = float(input("Ingresa la calificación de exámenes: ")) 
tareas = float(input("Ingresa la calificación de tareas: ")) 

generar_boleta(nombre, examenes, tareas)