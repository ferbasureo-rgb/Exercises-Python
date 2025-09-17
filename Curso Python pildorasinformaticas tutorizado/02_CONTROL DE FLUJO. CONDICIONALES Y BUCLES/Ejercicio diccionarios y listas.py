"""Ejercicio: crear un diccionario donde:
1. Te pida un país como clave.
2. Te pida un valor como ciudad de ese país
3. Si el país ya se ha introducido como clave, se añaden valores a esa clave como lista.
4. Para salir del bucle, presionar "salir" .

Ejemplo:
{"España": ["Madrid", "Barcelona", "Valencia"], "Colombia": ["Bogotá", "Medellín", "Poapayán"], "México": ["DF", "Juárez"]}"""

dictprueba={"España": ["Madrid", "Barcelona", "Valencia"], "Colombia": ["Bogotá", "Medellín", "Poapayán"], "México": ["DF", "Juárez"]}

diccionario={}
while True:
    pais = input("Introduce el país: ")
    if pais == "salir":
        break
    ciudad = input("Introduce ciudad: ")
    if pais not in diccionario:
        diccionario[pais] = []
        diccionario[pais].append(ciudad)
    else:
        diccionario[pais].append(ciudad)
print(diccionario)

"--- SOLUCIÓN ---"
paises = {}
pais = input("Introduce el país: ")
while pais != "salir":
    ciudad = input("Introduce ciudad: ") #Introduce el valor que queremos
    lista_ciudades = paises.setdefault(pais, [ciudad]) #Si "pais" no existe, lo crea con [ciudad] como valor. Si existe, devuelve la lista de ciudades que ya tenía. Se guarda el valor asociado a esa clave.
    if lista_ciudades != [ciudad]:
        paises[pais].append(ciudad)
    pais = input("Introduce el país: ")

print(paises)


