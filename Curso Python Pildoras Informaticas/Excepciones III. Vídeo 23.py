def evaluaEdad(edad):

    if edad <0:
        raise ValueError("No se permiten edades negativas")
    elif edad<20:
        return "Menor de edad"
    elif edad<40:
        return "Adulto"
    elif edad<65:
        return "Edad laboral"
    elif edad<100:
        return "Tercera edad"

print(evaluaEdad(80))

import math

def calculaRaiz(numero):

    if numero<0:
        raise ValueError("El número no puede ser negativo.")

    else:
        return math.sqrt(numero)

op1 = int(input("Ingresa un numero: "))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("El programa ha finalizado.")