import math

def calculadoraRaizCuadrada(numero):
    if numero < 0:
        raise ValueError ("El número no puede ser negativo.")
    else:
        return math.sqrt(numero)

numUsuario = int(input("Introduce un numero: "))

try:
    print(calculadoraRaizCuadrada(numUsuario))
except ValueError as ErrorNumeroNegativo:
    print("Error de número negativo.")


print("El programa puede continuar.")