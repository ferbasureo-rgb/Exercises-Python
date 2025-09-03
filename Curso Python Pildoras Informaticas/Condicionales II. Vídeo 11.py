print("---VERIFICACIÓN DE ACCESO---")

edad_usuario = int(input("Introduzca la edad: "))

def control_acceso(edad):
    if edad>=18:
        acceso="Puede pasar."
    else:
        acceso="No puede pasar."
    return acceso

print(control_acceso(edad_usuario))

print("El programa ha finalizado")

"""EJERCICIOS"""

"""Ejercicio 1:
• Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos."""

print("---NÚMERO MÁS ALTO---")
num1 = int(input("Introduzca primer número: "))
num2 = int(input("Introduzca segundo número: "))

def devuelve_max(x, y):
    if x>y:
        print(x)
    elif x<y:
        print(y)
    else:
        print("Los números son iguales")

print("El número más alto es: ")

devuelve_max(num1, num2)

"""Ejercicio 2:
• Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados en una lista y 
mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado)."""

name = input("Introduzca el nombre: ")
address= input("Introduzca dirección: ")
phone = input("Introduzca el telefono: ")
data_user = [name, address, phone]
print("Los datos personales son: "+data_user[0]+" "+data_user[1]+" "+data_user[2])

"""Ejercicio 3:
• Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos."""
x = int(input("Introduzca número 1: "))
y = int(input("Introduzca número 2: "))
z = int(input("Introduzca número 3: "))

print("La media aritmética es: ", ((x+y+z)/3))
