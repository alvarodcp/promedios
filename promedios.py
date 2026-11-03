# Solicitud de los datos
nombre_estudiante = input("Digite el nombre del estudiante: ")
nombre_curso = input ("Digite el nombre del curso: ")
nota = int(input("Digite la nota obtenida en el curso: "))
mnsj=""
if(nota < 0 or nota > 100):
    print("Dato inválido")
else:
    # Determinar si el estudiate aprobó o no.
    if (nota >= 70):
        mnsj = "El estudiante " + nombre_estudiante + " aprobó el curso con una nota de " + str(nota)
    elif (nota >=60) :
        mnsj = "El estudiante " + nombre_estudiante + "debe hacer examen de ampliación del curso " + nombre_curso + " porque obtuvo una nota de " + nota
    else:
        mnsj = f"El estudiante {nombre_estudiante} reprobó  el curso con una nota de {nota}"

# Impresión del mensaje
print(mnsj)