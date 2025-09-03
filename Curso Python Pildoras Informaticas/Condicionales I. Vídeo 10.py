print("---PROGRAMA DE INSTALACIÓN DE EVALUACIÓN DE NOTAS DE ALUMNOS---")
nota_alumno=input("Introduzca la calificación: ")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))
