"""Ejercicio excepciones. Agregar elemento en una lista
Crea un programa que pida introducir por consola 10 nombres propios de personas.
Los nombres se guardarán en una lista.
Si introducimos un nombre repetido, el programa lanzará una excepción de tipo ValueError, la excepción nos informará del error con el texto “Error. Este nombre ya se ha introducido”, y no se guardará el nombre repetido en la lista.
Imprimir el contenido de la lista por consola."""

def agregadorNombres(limite):
    contador = 0
    listaNombres = []
    while contador < limite:
        try:
            nombre = input("Introduce un nombre: ")
            if nombre in listaNombres:
                raise ValueError("El nombre está repetido.")
            else:
                listaNombres.append(nombre)
                contador += 1
        except ValueError:
            print("Error: este nombre está repetido.")
    return listaNombres

print(agregadorNombres(10))