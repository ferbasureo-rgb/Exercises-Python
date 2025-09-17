def evaluarAlumno(nota):
    valoración = ""
    if 10 > nota > 0:
        if 0<nota<5:
            valoración = "Suspenso"
            return valoración
        elif nota<7:
            valoración = "Aprobado"
            return valoración
        elif nota<9:
            valoración = "Notable"
            return valoración
        else:
            valoración = "Sobresaliente"
            return valoración
    else:
        return "Introducir una calificación del 0 al 10."

print(evaluarAlumno(9.4))