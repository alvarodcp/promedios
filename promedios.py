# Solicitud de los datos
nombre_estudiante = input("Digite el nombre del estudiante: ")
nombre_curso = input ("Digite el nombre del curso: ")

#Inicializar la bandera que controla el ciclo
continuar = True

# Ciclo para solicitar la nota
while continuar == True: 
    nota = int(input("Digite la nota obtenida en el curso: "))
    if(nota < 0 or nota > 100):
        print("Dato inválido")
    else:
        continuar = False

# Determinar si el estudiate aprobó o no.
if (nota >= 70):
    mnsj = "El estudiante " + nombre_estudiante + " aprobó el curso con una nota de " + str(nota)
elif (nota >=60) :
    mnsj = "El estudiante " + nombre_estudiante + "debe hacer examen de ampliación del curso " + nombre_curso + " porque obtuvo una nota de " + str(nota)
else:
    mnsj = f"El estudiante {nombre_estudiante} reprobó  el curso con una nota de {nota}"

# Impresión del mensaje
print(mnsj)