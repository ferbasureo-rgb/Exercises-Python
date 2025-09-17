

"""www.pildorasinformaticas.es 1
Ejercicio 1:
• Crea un programa que pida introducir una dirección de email por teclado. El programa debe imprimir en consola si la dirección de email es correcta o no en función de si esta tiene el símbolo ‘@’. 
Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email o al final, la dirección también será errónea,"""

emailUsuario=input("Introduce tu email: ")

while emailUsuario.count("@")!=1 or (emailUsuario.startswith("@") or emailUsuario.endswith("@")):
    print("ERROR: Introduzca un email correcto.")
    emailUsuario = input("Introduce tu email: ")

print("Email registrado con éxito")



