for i in range(5):
    print(f"valor de la variable: {i}")

""" Ejercicio 1:
• Crea un programa que muestre los números impares del 1 al 100. Los números deberán aparecer una al lado del otro sin salto de línea."""

for i in range(100):
    if i % 2 == 1:
        print(i, end=" ")

"""Ejercicio 2:
• Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco.
 Si la contraseña es correcta, el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña errónea”"""
print("---Ejercicio 2---")
password = input("Introduce contraseña: ")
if len(password) < 8 or " " in password:
    print("Contraseña incorrecta.")
else:
    print("Contraseña correcta ")

"""Ejercicio 3:
• Crea un programa que evalúe si una dirección de correo electrónico es válida o no en función de si tiene “@” o “.” 
Hay que tener en cuenta que la dirección se considera correcta si solo tiene una “@” y si tiene uno o más “.”"""

miEmail = input("Introduce tu email: ")
arroba = 0
punto = 0

for i in range(len(miEmail)):
    if miEmail[i]=="@":
        arroba += 1
    if miEmail[i]==".":
        punto += 1
if arroba != 1 and punto == 0:
    print("Email incorrecto")
else:
    print("Email acorrecto")

contra = "hola"
print(contra[0])