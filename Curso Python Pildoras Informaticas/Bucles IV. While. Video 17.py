i=1
while i<=10:
    print(f"Ejecución de {i}")
    i += 1

edad = int(input("Introduzca la edad :"))

while edad<5 or edad>100:
    print("La edad no es correcta")
    edad = int(input("Introduzca la edad :"))

print("Gracias.")

"""Ejercicio 1:
• Crea un programa que pida números infinitamente. Los números introducidos deben ser cada vez mayores El programa finalizará cuando se introduce un número menor que el anterior."""

numero = int(input("Introduce numero: "))
num = float("-inf")
while numero>num:
    num = numero
    numero = int(input("Introduce numero: "))

print("El programa ha finalizado")

print("Solución Ejercicio 1:")

num1 = int(input("Introduce numero: "))
num2 = int(input(f"Introduce numero mayor que {num1}: "))

while num2 > num1:
    num1 = num2
    num2 = int(input(f"Introduce numero mayor que {num1}: "))

print(f"{num2} es menor que {num1}")

"""Ejercicio 2: 
Crea un programa que pida números positivos indefinidamente. El programa termina cuando se introduce un número negativo. Finalmente el programa muestra la suma de todos los números introducidos"""

num1 = int(input("Introduce numero positivo: "))
acumulador = 0
while num1>0:
    acumulador = acumulador + num1
    num1 = int(input("Introduce numero positivo: "))

print(f"La suma de todos los números introducidos es igual a {acumulador}")