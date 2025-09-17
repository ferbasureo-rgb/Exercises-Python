def devuelve_ciudades(*ciudades): #Cuando ponemos un * delante del argumento, le estamos diciendo a python que vamos a darle una tupla con elementos indeterminados.
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudades_devueltas = devuelve_ciudades("Málaga", "Sevilla", "Milán", "Florencia","Santander")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

def devuelve_ciudades(*ciudades): #Cuando ponemos un * delante del argumento, le estamos diciendo a python que vamos a darle una tupla con elementos indeterminados.
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas = devuelve_ciudades("Málaga", "Sevilla", "Milán", "Florencia","Santander")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))




